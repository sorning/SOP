# ComfyUI Cloud API MCP Server

A zero-dependency, pure Python implementation of the Model Context Protocol (MCP) server for running ComfyUI workflows on both serverless cloud providers (like Fal.ai) and direct ComfyUI HTTP endpoints.

## Features
- **Zero Dependencies**: Implements JSON-RPC 2.0 stdio framing in pure Python (requires Python 3.8+). No need to run `pip install`!
- **Fal.ai Cloud Support**: Integrates with Fal.ai's serverless ComfyUI execution queue (`https://queue.fal.run`).
- **Direct Server Support**: Connects to any local or remote ComfyUI instance's `/prompt` HTTP API (e.g. RunPod, Vast.ai, or local).
- **Auto polling**: Polls status automatically and returns execution outputs.

## Available Tools

1. **`run_fal_comfyui`**: Run a ComfyUI workflow JSON on Fal.ai serverless Cloud API.
   - Arguments:
     - `workflow`: Dict (required) - ComfyUI API JSON format.
     - `fal_api_key`: String (optional) - Overrides `FAL_KEY` / `FAL_API_KEY` environment variables.
2. **`run_comfyui_direct`**: Run a ComfyUI workflow JSON on a direct local or remote ComfyUI HTTP API server.
   - Arguments:
     - `workflow`: Dict (required) - ComfyUI API JSON format.
     - `comfyui_url`: String (optional) - Default: `http://localhost:8188`
3. **`get_comfyui_server_info`**: Fetch system info, loaded models, and device specs from a direct ComfyUI server.
   - Arguments:
     - `comfyui_url`: String (optional) - Default: `http://localhost:8188`

## Installation & Configuration

To integrate this MCP server with your AI Agent clients (like Antigravity, Cursor, Windsurf, or Claude Desktop), add it to your global or project-level `mcp_config.json` (or `mcp_settings.json`).

### Option A: Running via Docker (Recommended for Cloud ComfyUI)
Since you are using ComfyUI Cloud, Docker is the cleanest way to run the MCP server without needing to clone local files.

1. **Build the Docker Image**:
   Navigate to the directory and run:
   ```bash
   docker build -t comfyui-mcp .
   ```

2. **Configure Client**:
   Add this to your `mcp_config.json` under `mcpServers`:
   ```json
   {
     "mcpServers": {
       "comfyui-mcp": {
         "command": "docker",
         "args": [
           "run",
           "-i",
           "--rm",
           "-e",
           "FAL_API_KEY",
           "-e",
           "FAL_KEY",
           "comfyui-mcp"
         ]
       }
     }
   }
   ```

### Option B: Running via Local Python
Merge this block into your `~/.gemini/antigravity/mcp_config.json`:

```json
{
  "mcpServers": {
    "comfyui-mcp": {
      "command": "python3",
      "args": [
        "/Users/willingwind/Documents/Antigravity/Claude/AutoAIVideo/.agent/mcp_servers/comfyui-mcp/server.py"
      ],
      "env": {
        "FAL_API_KEY": "YOUR_FAL_API_KEY_HERE"
      }
    }
  }
}
```

### Option C: Cursor / Windsurf Configuration
Add it to `.vscode/mcp.json` or your global user settings:

```json
{
  "mcp": {
    "servers": {
      "comfyui-mcp": {
        "command": "python3",
        "args": [
          "/Users/willingwind/Documents/Antigravity/Claude/AutoAIVideo/.agent/mcp_servers/comfyui-mcp/server.py"
        ],
        "env": {
          "FAL_API_KEY": "YOUR_FAL_API_KEY_HERE"
        }
      }
    }
  }
}
```

## How to Export Workflow in API Format
1. Open ComfyUI Web UI.
2. Go to **Settings** (gear icon) and enable **"Enable Dev mode"**.
3. You will see a new button: **"Save (API Format)"**.
4. Click it to export the JSON file. Use this JSON in the `workflow` argument.
