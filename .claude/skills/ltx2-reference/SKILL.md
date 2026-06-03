---
name: ltx2-reference
description: Lightricks LTX-2 / LTX-2.3 视频生成模型官方文档的本地副本。当 Claude 需要为 LTX 系列模型（LTX-2、LTX-2.3、LTX-Video 等）撰写、改写、审查、调试 prompt，或被问到任何关于 LTX 工作原理、Pipeline 选择、CFG/STG 参数、分辨率/帧数约束、enhance_prompt 用法、最佳实践、能力边界、能做什么不能做什么的问题时，调用此 skill。覆盖文生视频 T2V、图生视频 I2V、视频生视频 V2V、关键帧插值、音频到视频 A2V、Retake 重新生成、LipDub 口型同步等全部官方 pipeline。任何涉及"LTX"/"LTX-2"/"LTX-2.3"/"LTX-Video"/"LTXV"/"Lightricks"的查询都应优先查阅本 skill，而不是依赖训练数据中的记忆。本 skill 是被动参考材料，不主动生成具体题材的视频 prompt，只提供权威原则；用户要生成具体场景视频 prompt 时，配合具体场景 skill（如 ltx23-i2v-prompt、ltx23-f2f-prompt、ltx-t2v-prompt 等）使用。
---

# LTX-2 / LTX-2.3 Reference（官方文档本地副本）

> **来源说明（Source Attribution）**
>
> 本 skill 是 Lightricks 官方文档的本地副本集合，**正文一字不改**，仅在每个文件开头加来源标注。便于 Claude 在写 LTX 相关 prompt 或回答 LTX 相关问题时调用查证。
>
> **与 flux2-reference skill 的关键差异**：BFL 提供了现成的 `flux-best-practices` skill 可以 `git clone` 直接照搬。**Lightricks 没有发布对应的官方 skill**——他们的官方知识分散在 GitHub README、ltx.io blog、HuggingFace model card 中。本 skill 是我们手工整理的副本，**未经 Lightricks 官方认可**，仅作为参考材料使用。
>
> **总体来源**：
> - GitHub repo：https://github.com/Lightricks/LTX-2
> - 官方 blog：https://ltx.io/model/model-blog/prompting-guide-for-ltx-2（备用 URL：https://ltx.video/blog/how-to-prompt-for-ltx-2）
> - HuggingFace：https://huggingface.co/Lightricks/LTX-2.3
> - 官方文档站：https://docs.ltx.video
>
> **抓取日期**：2026-05-18
> **抓取方法**：`git clone --depth 1` + `web_fetch`（详见 references/_sources.md）
>
> **使用原则**：把本 skill 视为只读参考材料。**如有疑议，以 https://docs.ltx.video 的最新版本为准**。如果 Claude 的训练记忆与本 skill 内容冲突，**永远以本 skill 为准**——本 skill 是从官方源直接抓取的真实文档。

---

## 覆盖版本

本 skill 覆盖 **LTX-2** 和 **LTX-2.3**（当前最新版本，HuggingFace 上 2026-05-12 左右更新）。Lightricks 官方将 LTX-2 的 prompting blog 同时作为 LTX-2.3 的官方指南，意味着 prompting 原则在两个版本之间通用。

**不覆盖**的版本：旧版 `Lightricks/LTX-Video`（0.9.x 系列，13B 之前的版本）。这些版本是上一代模型，prompt 风格和参数有差异。如需查询旧版，请查阅 https://github.com/Lightricks/LTX-Video。

---

## Quick Reference（速查）

### Prompt 写作核心原则（来自官方 README + Blog）

1. **单一连续段落，自然语言流**——不要用 keyword 堆砌，不要用 bullet points
2. **现在时态**——`walks` 不是 `walked`，`the camera pushes in` 不是 `push the camera in`
3. **物理线索而非情绪标签**——`Her jaw tightens` 不是 `She feels sad`
4. **4 到 8 个描述性句子**——官方推荐长度
5. **保持在 200 词以内**（官方 README 明确建议）
6. **从主要动作开始**，按时间顺序展开
7. **像电影摄影师那样思考**——shot list 而非情绪描述
8. **对话用引号**——`"Hello"`，必要时标注语言/口音

### 必须包含的 6 个要素

1. **Establish the shot**（建立镜头）—— cinematography terms + scale
2. **Set the scene**（设置场景）—— lighting + color palette + textures + atmosphere
3. **Describe the action**（描述动作）—— natural sequence from beginning to end
4. **Define your character(s)**（定义角色）—— age + hairstyle + clothing + 通过物理线索表达情绪
5. **Identify camera movement(s)**（指定运镜）—— 包括运动结束后的画面状态
6. **Describe the audio**（描述音频）—— ambient + music + dialogue（在引号内）

### LTX-2 不擅长的事

- 复杂物理 / 非线性运动（跳跃、杂耍——但跳舞 OK）
- 文字 / Logo / 招牌 / 品牌名（无法稳定生成可读文字）
- 内在情绪状态描述（`sad` / `confused`）——必须改用可见的物理线索
- 多角色 / 多动作 / 高复杂度场景
- 矛盾光照（如 "暖夕阳 + 冷荧光" 同时存在）
- 过度复杂的 prompt（动作 / 角色 / 指令越多，遗漏越多）

### 硬性技术约束（LTX-2.3）

- 宽 / 高必须被 **32** 整除
- 帧数必须是 **8n+1**（如 121、257）
- 推荐分辨率：1216 × 704 @ 30 FPS（默认）
- 不符合自动 padding/cropping

### Pipeline 选择速查（来自 ltx-pipelines）

| 用途 | 推荐 Pipeline |
|------|--------------|
| 文 / 图生视频，生产质量 | `TI2VidTwoStagesPipeline` |
| 文 / 图生视频，最高质量 | `TI2VidTwoStagesHQPipeline` |
| 文 / 图生视频，快速原型 | `TI2VidOneStagePipeline` |
| 最快推理 | `DistilledPipeline` |
| 视频生视频 / 控制生成 | `ICLoraPipeline` |
| 关键帧插值（首帧+尾帧） | `KeyframeInterpolationPipeline` |
| 音频驱动视频 | `A2VidPipelineTwoStage` |
| 已有视频重绘部分时段 | `RetakePipeline` |
| HDR 输出 | `HDRICLoraPipeline` |
| 换嘴型 / 重新配音 | `LipDubPipeline` |

### 默认参数（来自 pipelines-claude-md）

- **CFG**：3.0（视频），7.0（音频）
- **STG**：scale 1.0，block [28]（LTX-2.3）/ [29]（LTX-2）
- **Modality guidance**：3.0
- **Steps**：30（LTX-2.3）/ 40（LTX-2）/ 15（HQ）/ 8（Distilled，固定）

---

## Rules Reference（详细文档）

阅读各 rules 文件以查阅完整官方内容：

- [references/_sources.md](references/_sources.md) - **所有来源清单和抓取方法（学术诚实）**
- [references/prompting-guide-blog.md](references/prompting-guide-blog.md) - **官方 blog 完整 prompting 指南 + 11 个示范 prompt（最重要）**
- [references/prompting-guide-official-readme.md](references/prompting-guide-official-readme.md) - GitHub README 的 prompting 章节（简洁版 + Optimization Tips）
- [references/pipelines-overview.md](references/pipelines-overview.md) - ltx-pipelines 完整技术文档（497 行）
- [references/pipelines-claude-md.md](references/pipelines-claude-md.md) - **Lightricks 专为 Claude 编写的 ltx-pipelines 架构文档**
- [references/model-spec.md](references/model-spec.md) - LTX-2.3 硬性技术约束（分辨率 / 帧数 / 局限性）

---

## 与你现有 skill 的协作关系

本 skill 是**被动参考材料**，不主动生成具体 prompt。

| 你的场景 skill | 调用本 skill 的方式 |
|--------------|------------------|
| `ltx-t2v-prompt`（文生视频 prompt 扩写） | Claude 写 prompt 时查询本 skill 的 prompting-guide-blog 和 model-spec |
| `ltx23-i2v-prompt`（图生视频 prompt） | 同上 + 查询 pipelines-overview 关于 image conditioning 的说明 |
| `ltx23-f2f-prompt`（首尾帧 prompt） | 同上 + 查询 pipelines-claude-md 关于 KeyframeInterpolationPipeline 的说明 |

---

## Example Prompt（来自官方 blog）

> A warm, intimate cinematic performance inside a cozy, wood-paneled bar, lit with soft amber practical lights and shallow depth of field that creates glowing bokeh in the background. The shot opens in a medium close-up on a young female singer in her 20s with short brown hair and bangs, singing into a microphone while strumming an acoustic guitar, her eyes closed and posture relaxed. The camera slowly arcs left around her, keeping her face and mic in sharp focus as two male band members playing guitars remain softly blurred behind her. Warm light wraps around her face and hair as framed photos and wooden walls drift past in the background. Ambient live music fills the space, led by her clear vocals over gentle acoustic strumming.

约 110 词，5 句话，单段落，现在时态，包含镜头 / 角色 / 服装 / 灯光 / 音频 / 摄影机运动——这是官方推荐的典范结构。完整 11 个示范见 `references/prompting-guide-blog.md`。
