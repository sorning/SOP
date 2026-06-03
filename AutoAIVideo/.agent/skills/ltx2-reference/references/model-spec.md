# LTX-2.3 Model Specifications — 硬性技术约束

> **来源**：https://huggingface.co/Lightricks/LTX-2.3（model card README）
> **抓取日期**：2026-05-18
> **正文一字不改照搬**——以下为原 model card 中关于资源限制和注意事项的官方文字

---

## Resolution and Frame Count Constraints（硬性约束，违反会被自动 padding）

> LTX-2.3 support in the Diffusers Python library is coming soon!
>
> Width & height settings must be divisible by 32.
>
> Frame count must be divisible by 8 + 1.
>
> In case the resolution or number of frames are not divisible by 32 or 8 + 1, the input should be padded with -1 and then cropped to the desired resolution and number of frames.

**关键约束**：
- 宽 / 高必须能被 **32** 整除（例如 1024×576、1216×704）
- 帧数必须是 **8n+1**（例如 9、17、25、33、…、121、…、257 等）
- 不符合则自动 padding/cropping

## Limitations（官方声明的局限）

> For tips on writing effective prompts, please visit our Prompting guide
>
> This model is not intended or able to provide factual information. As a statistical model this checkpoint might amplify existing societal biases. The model may fail to generate videos that matches the prompts perfectly. Prompt following is heavily influenced by the prompting-style.

**翻译要点**：
- 模型不擅长产出事实性信息
- 可能放大训练数据中的社会偏见
- 不一定能完美匹配 prompt——**prompt 风格本身对生成质量影响巨大**（这是为什么本 skill 的 prompting-guide-blog.md 如此重要）

## LoRA / 微调

> The base (dev) model is fully trainable. It's extremely easy to reproduce the LoRAs and IC-LoRAs we publish with the model by following the instructions on the LTX-2 Trainer Readme. Training for motion, style or likeness (sound+appearance) can take less than an hour in many settings.

- dev 版本可完全训练
- LoRA 训练 motion / style / likeness 可在 1 小时内完成
- IC-LoRA 用于 video-to-video 控制

---

## 与 LTX-Video（老版本）的对比

旧版 `Lightricks/LTX-Video`（0.9.x）的硬性约束相似但略有差异：

> The model works on resolutions that are divisible by 32 and number of frames that are divisible by 8 + 1 (e.g. 257).
>
> In case the resolution or number of frames are not divisible by 32 or 8 + 1, the input will be padded with -1 and then cropped to the desired resolution and number of frames.
>
> The model works best on resolutions under 720 x 1280 and number of frames below 257

老版本明确声明 **"works best under 720×1280 and frames below 257"**——LTX-2.3 model card 中没有重复这条声明，可能意味着 2.3 已突破此限制或仍适用，建议以 ltx-pipelines/README.md 的 pipeline 默认参数为准。

---

## 不来自 model card 的旁证

以下信息来源于 GitHub README 主文档，与 model card 互相印证：

- **默认推荐分辨率**：1216×704 @ 30 FPS（这是 LTX-Video 13B 的默认值，LTX-2.3 沿用类似默认）
- **建议 prompt 长度**：< 200 words（来自主 README "Prompting for LTX-2" 章节）
- **CFG 默认值**：3.0（video），7.0（audio）（来自 pipelines-claude-md.md）
- **STG 默认值**：`stg_scale=1.0`，LTX-2.3 用 block [28]，LTX-2 用 block [29]（来自 pipelines-claude-md.md）
