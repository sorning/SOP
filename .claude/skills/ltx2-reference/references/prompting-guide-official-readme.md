# LTX-2 GitHub README — Prompting 章节官方原文

> **来源**：https://github.com/Lightricks/LTX-2 主 README（master 分支，2026-05-18 抓取）
> **正文一字不改照搬**

---

## ⚡ Optimization Tips

* **Use DistilledPipeline** - Fastest inference with only 8 predefined sigmas (8 steps stage 1, 4 steps stage 2)
* **Enable FP8 quantization** - Enables lower memory footprint: `--quantization fp8-cast` (CLI) or `quantization=QuantizationPolicy.fp8_cast()` (Python). Fp8-cast should be used with bf16 checkpoints, it shall downcast them on the fly. For Hopper GPUs with TensorRT-LLM, use `--quantization fp8-scaled-mm` for FP8 scaled matrix multiplication. Fp8-scaled-mm should be used with fp8 checkpoints.
* **Install attention optimizations** - Use xFormers (`uv sync --extra xformers`) or [Flash Attention 3](https://github.com/Dao-AILab/flash-attention) for Hopper GPUs
* **Use gradient estimation** - Reduce inference steps from 40 to 20-30 while maintaining quality (see [pipeline documentation](packages/ltx-pipelines/README.md#denoising-loop-optimization))
* **Skip memory cleanup** - If you have sufficient VRAM, disable automatic memory cleanup between stages for faster processing
* **Choose single-stage pipeline** - Use `TI2VidOneStagePipeline` for faster generation when high resolution isn't required

## ✍️ Prompting for LTX-2

When writing prompts, focus on detailed, chronological descriptions of actions and scenes. Include specific movements, appearances, camera angles, and environmental details - all in a single flowing paragraph. Start directly with the action, and keep descriptions literal and precise. Think like a cinematographer describing a shot list. Keep within 200 words. For best results, build your prompts using this structure:

- Start with main action in a single sentence
- Add specific details about movements and gestures
- Describe character/object appearances precisely
- Include background and environment details
- Specify camera angles and movements
- Describe lighting and colors
- Note any changes or sudden events

For additional guidance on writing a prompt please refer to <https://ltx.video/blog/how-to-prompt-for-ltx-2>

### Automatic Prompt Enhancement

LTX-2 pipelines support automatic prompt enhancement via an `enhance_prompt` parameter.

## 🔌 ComfyUI Integration

To use our model with ComfyUI, please follow the instructions at <https://github.com/Lightricks/ComfyUI-LTXVideo/>.
