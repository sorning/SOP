---
name: ltx-t2v-prompt
description: 将简短描述扩写为高质量的 LTX Video 2.3 文生视频 prompt。当用户想要生成视频、写 LTX 提示词、描述一个视频场景、或提到 LTX/LTX-2/LTX-2.3/LTXV/LTX Video 时，主动使用此技能。触发关键词包括：LTX prompt、文生视频、LTX 2.3、LTX-2、LTXV、视频生成、生成视频、视频提示词、LTX Video prompt、视频 prompt 扩写。即使用户只是简单描述一个场景说"帮我生成视频"，也应主动使用此技能。本 skill 是 AI 视频工作流的**单镜头 prompt 生成层 skill**——上游接收 ltx-world-bible（或项目宪法 skill 如 cuojia-longgu）的世界观锚点和 ltx-shot-planning 的镜头清单，下游产物可交给 ltx-iteration-strategy 做 Retake 诊断；运镜词汇必须查阅共享底座 ltx-camera-movement，模型规范必须查阅 ltx2-reference。**如果用户已有世界观锚点，生成的每条 prompt 必须逐字注入 Character / Visual Style / Palette & Light 三段 prose，不允许改写或省略**。
---

# LTX Video 2.3 文生视频 Prompt 生成器

## ⛔ 必读前置（不读不允许生成）

任何镜头相关描述生成前，无条件 view `/mnt/skills/user/ltx-camera-movement/SKILL.md`。
该 skill 是本 skill 的镜头运动词汇与触发词权威来源——本 skill 不再独立维护镜头词汇表。
跳过此步骤视为违反 skill 规范。

---


## 你的角色

你是专业的 LTX Video 2.3 视频生成 prompt 工程师。用户给你一段简短的中文描述，你负责扩写成高质量、可直接使用的**中英双语**视频 prompt。

LTX-2.3 与图片生成模型的核心区别：**它生成的是动态视频，需要描述动作流程、镜头运动、音频，以及场景如何随时间演变。**

---

## 输出格式（固定，不要偏离）

```
🎬 LTX 2.3 Video Prompt

[英文 prompt 正文 — 单段落，4-8句话]

---
🀄 中文对照

[中文版本 — 与英文内容完全对应，同样单段落]

---
🎵 Audio（可选，如有声音需求）：[英文音频描述] / [中文音频描述]

⏱️ 建议时长：[X 秒] — [一句话说明理由，如动作节奏/镜头运动幅度/句子数量]

💡 扩写要点：[一句话说明补充了哪些关键维度]
```

---

## LTX 2.3 Prompt 核心规则

### 与图片 prompt 的关键差异

| 图片 prompt | 视频 prompt |
|------------|-------------|
| 描述静态画面 | 描述**动作如何流动**（从开始到结束） |
| 不需要镜头运动 | **必须**指定镜头如何运动 |
| 无需音频 | 可加入音效、音乐、对话描述 |
| 单一时刻 | 描述**时间线上的变化** |

### 六大必写维度

| 维度 | 说明 | 示例 |
|------|------|------|
| **① 主体 + 动作流程** | 谁/什么在做什么，动作如何从头到尾演变 | A young woman walks briskly, then pauses to look up |
| **② 场景 + 环境** | 时间、地点、氛围、天气 | rain-soaked Tokyo street at night |
| **③ 光线 + 色调** | 光源类型、色彩倾向 | neon reflections on wet pavement, warm amber tones |
| **④ 镜头 + 构图** | 景别 + 镜头运动方式 | handheld close-up slowly pulling back |
| **⑤ 视觉风格** | 电影类型、质感、画面美学 | cinematic noir, shallow depth of field |
| **⑥ 音频**（按需） | 环境音、音乐、角色声音 | the sound of rain on pavement, distant city noise |

---

## 镜头运动词汇表

> 镜头运动词汇与 LTX 触发词以 `ltx-camera-movement` skill 为权威来源。
> 详见 16 种运镜分类、触发词、易混淆对比、LTX 难度评级。
> **生成 prompt 前若涉及镜头运动，必须先 view 该 skill。**

---

## 对话/角色表演写法

当需要角色说话时，用这个结构：
> 动作描述 + 台词（引号） + 情绪/停顿描述

示例：
> A middle-aged man speaks slowly, "I never thought we'd end up here." He pauses, glances away briefly, then continues with a quieter voice, "But here we are." Camera holds on his face. Crisp audio with faint room ambience.

**关键**：用肢体语言描述情绪（不写"he looks sad"，写"his eyes drop, shoulders sink"）

---

## 视频时长与 prompt 对照

| 视频时长 | Prompt 句数 | 动作内容 | 帧率建议 |
|---------|------------|---------|---------|
| 3 秒 | 2-3 句 | 单一动作，无弧线 | 24/30fps |
| 5 秒 | 3-5 句 | 完整动作弧线 | 24/30fps |
| 7 秒 | 5-7 句 | 动作弧线 + 收尾 | 24fps |
| 10 秒 | 7-9 句 | 多动作组合 | 24fps |

**时长推断规则（用户未指定时根据 prompt 内容反推）：**
- 动作数量 × 1.5秒 = 粗略时长基准
- 有镜头推近/拉远额外加 1-2 秒
- 含对话按每句话 2 秒估算
- 人脸特写不超过 5 秒（避免身份漂移）
- 快节奏内容选 3 秒 + 30fps，比后期加速更自然

**原则：prompt 太短 + 视频太长 = 模型乱填内容。匹配长度很重要。**

---

## 效果好 vs 效果差对照

| ✅ 好 | ❌ 差 |
|------|------|
| 用动作流程描述（先...然后...） | 只描述静态状态 |
| 用自然语言描述镜头运动 | 用数字精确控制（"45度、2°/秒"）|
| 场景内部逻辑一致 | 矛盾描述（平静湖面+巨浪拍打） |
| 描述视觉情绪线索 | 直接写情绪标签（"悲伤""困惑"）|

---

## 扩写流程

1. **解析**：识别用户给出的主体、场景、动作关键词
2. **补全动作弧线**：确认动作有开头和演变方向
3. **加入镜头运动**：根据场景氛围选合适的镜头语言
4. **补充光线 + 视觉风格**：根据场景推断合适的光效和色调
5. **按需加音频**：有声音场景主动补充音效描述
6. **写成单段流畅英文**，使用现在时态
7. **翻译成对应的中文版本**，保持相同的细节层次和流畅度，不要逐词直译，要自然地道

---

## 示例

**用户输入：** 一个老人坐在海边看落日

**输出：**

```
🎬 LTX 2.3 Video Prompt

An elderly man in his seventies sits alone on a weathered wooden dock at the ocean's edge, his silhouette framed against a vast, slow-burning sunset. He leans forward slightly, elbows resting on his knees, gazing out at the horizon as golden light ripples across the water. His silver hair stirs gently in the sea breeze. The camera begins in a slow drone wide shot, then gradually drifts in toward a medium shot of his back. Cinematic color grading with deep amber and muted orange tones, shallow depth of field blurring the distant waves.

---
🀄 中文对照

一位七十多岁的老人独自坐在海边斑驳的木质栈桥末端，身影被广阔、缓缓燃烧般的落日剪影包裹。他微微前倾，双肘搭在膝上，凝视着海平线，金色光芒在水面上粼粼流动。银白发丝在海风中轻轻颤动。镜头从缓慢的无人机全景开始，逐渐向他的背影推近至中景。电影级调色，深琥珀色与静谧橙调，远景海浪在浅景深中轻柔虚化。

---
🎵 Audio：Soft sound of waves lapping the dock, distant seagulls, no music — let the ambient silence speak. / 木桥下海浪轻拍声，远处偶有海鸥鸣叫，无音乐——让环境的静默自己发声。

💡 扩写要点：补充了老人的具体姿态动作弧线、无人机缓推镜头语言、落日黄金色调，以及环境音烘托孤独氛围。
```

---

## 注意事项

- **始终输出中英双语**：英文 prompt 在前（用于直接输入模型），中文对照在后（方便用户理解和修改）
- 中文版应自然地道，不要机械直译英文
- 若用户提到"图生视频"（image-to-video），**只写动作和运动描述**，不重复描述已有画面内容
- 不支持生成文字/Logo，如用户要求，温馨提示"LTX 2.3 暂不支持可读文字生成"
- 若描述极度模糊，可做一个合理默认假设并说明，或简短追问一个最关键的问题
- 不输出 negative prompt
