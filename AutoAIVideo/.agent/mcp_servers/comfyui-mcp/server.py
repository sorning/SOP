import sys
import json
import asyncio
import urllib.request
import urllib.parse
import urllib.error
import os
import time

# Helper function to print logs to stderr
def log(message):
    sys.stderr.write(f"[ComfyUI-MCP] {message}\n")
    sys.stderr.flush()

# Direct ComfyUI API Execution
def http_post(url, data, headers=None):
    if headers is None:
        headers = {}
    headers.setdefault("Content-Type", "application/json")
    req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as res:
            return json.loads(res.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        log(f"HTTP Error: {e.code} - {e.read().decode('utf-8', errors='ignore')}")
        raise
    except Exception as e:
        log(f"Error making POST request to {url}: {e}")
        raise

def http_get(url, headers=None):
    if headers is None:
        headers = {}
    req = urllib.request.Request(url, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(req) as res:
            return json.loads(res.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        log(f"HTTP Error: {e.code} - {e.read().decode('utf-8', errors='ignore')}")
        raise
    except Exception as e:
        log(f"Error making GET request to {url}: {e}")
        raise

async def run_fal_comfyui_api(workflow, fal_api_key=None):
    key = fal_api_key or os.environ.get("FAL_KEY") or os.environ.get("FAL_API_KEY")
    if not key:
        raise ValueError("Fal.ai API key is missing. Set FAL_KEY/FAL_API_KEY environment variable or pass fal_api_key.")

    log("Submitting workflow to Fal.ai ComfyUI queue...")
    headers = {
        "Authorization": f"Key {key}",
        "Content-Type": "application/json"
    }
    
    # Submit request to queue
    queue_url = "https://queue.fal.run/fal-ai/comfyui"
    payload = {
        "load_generator": True,
        "comfyjson": workflow
    }
    
    response = http_post(queue_url, payload, headers)
    request_id = response.get("request_id")
    if not request_id:
        raise RuntimeError(f"Failed to get request_id from Fal.ai response: {response}")
    
    log(f"Request ID: {request_id}. Polling status...")
    status_url = f"https://queue.fal.run/fal-ai/comfyui/requests/{request_id}/status"
    
    # Poll status
    while True:
        status_res = http_get(status_url, headers)
        status = status_res.get("status")
        log(f"Current status: {status}")
        
        if status == "COMPLETED":
            break
        elif status in ["FAILED", "CANCELLED"]:
            raise RuntimeError(f"Fal.ai execution ended with status: {status}. Details: {status_res}")
        
        await asyncio.sleep(2)
        
    # Get final results
    result_url = f"https://queue.fal.run/fal-ai/comfyui/requests/{request_id}"
    results = http_get(result_url, headers)
    return results

async def run_comfyui_direct_api(workflow, comfyui_url="http://localhost:8188"):
    log(f"Submitting workflow to ComfyUI server at {comfyui_url}...")
    prompt_url = f"{comfyui_url.rstrip('/')}/prompt"
    
    # ComfyUI prompt endpoint expects {"prompt": workflow}
    payload = {"prompt": workflow}
    response = http_post(prompt_url, payload)
    
    prompt_id = response.get("prompt_id")
    if not prompt_id:
        raise RuntimeError(f"Failed to get prompt_id from ComfyUI response: {response}")
        
    log(f"Prompt ID: {prompt_id}. Waiting for completion...")
    history_url = f"{comfyui_url.rstrip('/')}/history/{prompt_id}"
    
    # Poll history
    while True:
        try:
            history_res = http_get(history_url)
            # If the prompt ID is in history, it means it is completed
            if prompt_id in history_res:
                log("Workflow execution completed!")
                return history_res[prompt_id]
        except urllib.error.HTTPError as e:
            if e.code != 404:  # Ignore 404 while waiting
                raise
        except Exception as e:
            log(f"Warning during polling: {e}")
            
        await asyncio.sleep(2)

# Tool Definitions
async def call_tool(name, arguments):
    if name == "run_fal_comfyui":
        workflow = arguments.get("workflow")
        fal_api_key = arguments.get("fal_api_key")
        if not workflow:
            return {"content": [{"type": "text", "text": "Error: 'workflow' is a required argument."}], "isError": True}
        try:
            res = await run_fal_comfyui_api(workflow, fal_api_key)
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
        except Exception as e:
            return {"content": [{"type": "text", "text": f"Error executing Fal.ai workflow: {str(e)}"}], "isError": True}
            
    elif name == "run_comfyui_direct":
        workflow = arguments.get("workflow")
        comfyui_url = arguments.get("comfyui_url", "http://localhost:8188")
        if not workflow:
            return {"content": [{"type": "text", "text": "Error: 'workflow' is a required argument."}], "isError": True}
        try:
            res = await run_comfyui_direct_api(workflow, comfyui_url)
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
        except Exception as e:
            return {"content": [{"type": "text", "text": f"Error executing direct ComfyUI workflow: {str(e)}"}], "isError": True}
            
    elif name == "get_comfyui_server_info":
        comfyui_url = arguments.get("comfyui_url", "http://localhost:8188")
        try:
            system_url = f"{comfyui_url.rstrip('/')}/system_info"
            res = http_get(system_url)
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
        except Exception as e:
            return {"content": [{"type": "text", "text": f"Error fetching server info: {str(e)}"}], "isError": True}
            
    else:
        return {"content": [{"type": "text", "text": f"Unknown tool: {name}"}], "isError": True}

# JSON-RPC 2.0 stdio handling
async def rpc_loop():
    loop = asyncio.get_event_loop()
    reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(reader)
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)
    
    log("Server started and listening on stdin...")
    
    while True:
        line = await reader.readline()
        if not line:
            break
            
        try:
            request = json.loads(line.decode("utf-8").strip())
        except Exception as e:
            log(f"Invalid JSON received: {e}")
            continue
            
        method = request.get("method")
        req_id = request.get("id")
        
        # Initialize
        if method == "initialize":
            response = {
                "jsonrpc": "2.0",
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {
                        "tools": {}
                    },
                    "serverInfo": {
                        "name": "comfyui-mcp",
                        "version": "1.0.0"
                    }
                },
                "id": req_id
            }
            sys.stdout.write(json.dumps(response) + "\n")
            sys.stdout.flush()
            
        # Tools List
        elif method == "tools/list":
            response = {
                "jsonrpc": "2.0",
                "result": {
                    "tools": [
                        {
                            "name": "run_fal_comfyui",
                            "description": "Run a ComfyUI workflow on Fal.ai serverless Cloud API.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "workflow": {
                                        "type": "object",
                                        "description": "The ComfyUI workflow JSON (API format)."
                                    },
                                    "fal_api_key": {
                                        "type": "string",
                                        "description": "Optional Fal.ai API Key. If not set, reads from FAL_KEY or FAL_API_KEY env variables."
                                    }
                                },
                                "required": ["workflow"]
                            }
                        },
                        {
                            "name": "run_comfyui_direct",
                            "description": "Run a ComfyUI workflow on a direct local or remote ComfyUI HTTP API server.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "workflow": {
                                        "type": "object",
                                        "description": "The ComfyUI workflow JSON (API format)."
                                    },
                                    "comfyui_url": {
                                        "type": "string",
                                        "description": "Optional ComfyUI API endpoint. Default: http://localhost:8188"
                                    }
                                },
                                "required": ["workflow"]
                            }
                        },
                        {
                            "name": "get_comfyui_server_info",
                            "description": "Get system information, loaded models, and device specs from a direct ComfyUI server.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "comfyui_url": {
                                        "type": "string",
                                        "description": "Optional ComfyUI API endpoint. Default: http://localhost:8188"
                                    }
                                }
                            }
                        }
                    ]
                },
                "id": req_id
            }
            sys.stdout.write(json.dumps(response) + "\n")
            sys.stdout.flush()
            
        # Tool Call
        elif method == "tools/call":
            params = request.get("params", {})
            name = params.get("name")
            arguments = params.get("arguments", {})
            
            log(f"Calling tool '{name}' with arguments: {arguments}")
            
            # Execute tool call asynchronously
            res = await call_tool(name, arguments)
            
            response = {
                "jsonrpc": "2.0",
                "result": res,
                "id": req_id
            }
            sys.stdout.write(json.dumps(response) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    try:
        asyncio.run(rpc_loop())
    except KeyboardInterrupt:
        pass
