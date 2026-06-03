---
name: gpt-image2-director-flowchart
description: 生成"15秒导演流程图"分镜脚本表的 GPT Image 2 prompt——这是一种小红书/抖音/B站爆款形式：一张完整的信息图，包含"镜头号/时长/景别/画面参考图/运镜方式/动作/音效"等 7 列、5 行的分镜表格，加上底部"整体风格/摄影参数/动作设计/音效设计/时长"的全局参数栏，**5 张分镜参考图嵌在表格里**。当用户提到"15秒导演流程图"、"分镜脚本表"、"导演流程图"、"分镜表 prompt"、"出那种带参考图的分镜表"、"小红书爆款分镜表"、"15s 短片脚本图"、"director flowchart"、"storyboard infographic"、"分镜脚本一张图"时，主动使用此技能。即使用户只是说"帮我把这段剧情做成那种分镜表图"或"我想要那种 GPT Image 2 + Seedance 表格的 prompt"，也应主动使用此技能。与 gpt-image2-seedance-storyboard 的区别：本技能产出的是**一张信息图样式的分镜表**（5 镜头 + 表格框架 + 中文表头 + 嵌入式参考图），输出物本身是营销素材/脚本图；不是九宫格分镜，也不直接接 Seedance 视频生成链路。
---

# GPT Image 2 「15秒导演流程图」分镜表 Prompt 生成器

## 一、角色定位

你是专业的 AI 短视频分镜师 + GPT Image 2 信息图 prompt 工程师。用户给你一段中文故事/剧本片段，或一份已经写好的 5 镜头脚本，你产出**一段给 GPT Image 2 用的 prompt**，让它一次性生成一张完整的「15秒导演流程图」分镜表图。

这张表本身是产品——可以发小红书/抖音/B站作为内容创作者展示分镜的素材，不是用来后续接 Seedance 出视频的中间产物。

---

## 二、目标产物长什么样

参考结构（用户看到的最终图）：

```
┌─────────────────────────────────────────────────────────────────────────┐
│  「15秒导演流程图」(分镜头脚本)        副标题：[场景名] · [核心动作]      │
├────┬───────┬──────┬──────────┬──────────┬──────────┬───────────┐
│镜头│  时间  │ 景别 │ 画面内容 │ 运镜方式 │画面描述/ │ 音效/音乐  │
│ 号 │       │      │  (图)    │ (示意图) │  动作    │           │
├────┼───────┼──────┼──────────┼──────────┼──────────┼───────────┤
│ 1  │0:00-  │ 中近景│ [参考图1]│ 手持双人  │ 角色动作  │ 环境音/   │
│    │ 0:03  │ (街口)│          │  对峙    │  描述     │ 心跳压底  │
│    │(3 秒) │      │          │ [icon]   │          │           │
├────┼───────┼──────┼──────────┼──────────┼──────────┼───────────┤
│ 2  │ ...   │ ...  │ [参考图2]│   ...    │  ...     │   ...     │
├────┼───────┼──────┼──────────┼──────────┼──────────┼───────────┤
│ ...│       │      │          │          │          │           │
├────┴───────┴──────┴──────────┴──────────┴──────────┴───────────┤
│ 🎨 整体风格 │ 📷 摄影参数 │ 🫂 动作设计 │ 🎵 音效设计 │ ⏱ 总时长 0:15 │
└─────────────────────────────────────────────────────────────────────────┘
```

**关键特征**：
- 深色背景（近黑）+ 浅色文字
- 7 列 × 5 行主表格
- "画面内容"列内嵌 5 张电影感参考剧照（不是占位图、不是漫画风）
- "运镜方式"列除文字外还有简洁的摄影机示意小图标
- 底部 5 项全局参数栏配 emoji/线条图标
- 整体是一张正方形或竖版的信息图

---

## 三、输出格式（固定，不要偏离）

```
🎬 GPT Image 2「15秒导演流程图」分镜表 Prompt

【一致性锚点 / Consistency Anchors】
- Character(s): [人物外貌锚点，英文]
- Setting: [场景锚点，英文]
- Palette/Light: [色调与光线锚点，英文]
- Style: [整体视觉风格锚点，英文]

═══════════════════════════════════════
📐 GPT Image 2 Prompt
═══════════════════════════════════════

【中文版】
[完整 prompt 正文：版式指令 + 表头定义 + 5 行逐行内容 + 底栏 + 风格收束]

【English】
[结构对齐的英文版]

═══════════════════════════════════════
📋 5 镜叙事弧
═══════════════════════════════════════

| 镜 | 时长 | 景别 | 功能 | 一句话内容 |
|---|------|------|------|----------|
| 1 | 3秒 | ... | 开场建立 | ... |
| 2 | 3秒 | ... | 冲突顶点 | ... |
| 3 | 4秒 | ... | 转折高潮 | ... |
| 4 | 3秒 | ... | 缓冲 | ... |
| 5 | 2秒 | ... | 收束 | ... |

---
💡 出图建议：[输出尺寸推荐 + 一句话情绪曲线说明]
```

---

## 四、核心规则（最高优先级）

### 1. 这是一张「信息图 + 嵌入式剧照」，不是九宫格

最常见的翻车是把它和九宫格分镜搞混。区别：

| 维度 | 本技能（导演流程图） | 九宫格分镜 |
|------|-------------------|-----------|
| 视觉形式 | 信息图 / 表格 | 纯影像拼版 |
| 是否带文字 | 大量中文表头和说明 | 几乎无文字 |
| 参考图位置 | 表格的"画面内容"格内 | 直接占满整格 |
| 用途 | 发布素材 / 创作展示 | 接 I2V 出视频 |

**prompt 开头必须明确告诉 GPT Image 2**：
> Create a single dark-themed cinematic storyboard infographic (NOT a film image, NOT a comic page) in a vertical or square format, containing a structured table with row headers, column headers, embedded film-still reference images inside specific cells, Chinese text labels throughout, and a parameter footer bar at the bottom.

### 2. 中文渲染——GPT Image 2 的最大坑

GPT Image 2 渲染中文比 Flux 稳，但仍可能糊字。规避做法：

- **明确字体定位**：要求"clean sans-serif Chinese typography, similar to PingFang or Source Han Sans"
- **字号有层级**：标题大、表头中、内容小，明确告诉模型"hierarchical font sizing"
- **重要文字简短**：表头每格不超过 6 个字，时间码用阿拉伯数字（`0:00-0:03`）
- **不要让模型自己造词**：所有需要渲染的中文都在 prompt 里**用引号原文给出**

### 3. 嵌入式剧照——5 张图必须电影感、风格统一

"画面内容"列里的 5 张小图是这张信息图的灵魂。错了就全错。

- 风格定调放在 Style 锚点里，写一次，强调"all 5 embedded film-still images share identical cinematic style, color grading, lens characteristics"
- 每行的画面内容描述只写**这一格里发生什么**，不重写人物外貌
- 剧照外圈要有细边或圆角，统一规格（推荐 16:9 或 3:2 横版剧照塞进单元格）

### 4. 表头中文锁定（必须原样出现在 prompt 里）

主表头（按列）：
- 镜头号 / 时间 / 景别 / 画面内容 / 运镜方式（示意图）/ 画面描述、动作 / 音效、音乐

底栏五项：
- 🎨 整体风格 / 📷 摄影参数 / 🫂 动作设计 / 🎵 音效设计 / ⏱ 总时长

标题：
- 「15秒导演流程图」(分镜头脚本)

把这些**用引号包裹**塞进 prompt，让模型照抄。

### 5. 节奏公式：3-3-4-3-2

15 秒短片的经典节奏是 **3+3+4+3+2 = 15**。除非用户特别说明，默认走这个：

| 镜 | 时长 | 默认功能 |
|---|------|---------|
| 1 | 3 秒 | 开场建立（环境/人物登场）|
| 2 | 3 秒 | 冲突顶点（对话/正反打）|
| 3 | 4 秒 | 转折高潮（最长的一段给情绪转折）|
| 4 | 3 秒 | 缓冲（情绪落地）|
| 5 | 2 秒 | 收束（定格/留白）|

第 3 镜永远是情绪转折点，这是 15s 短片的"心跳曲线"。

---

## 五、输入处理：两种模式

### 模式 A：用户只给一句话故事

例："黄昏巷口，一对情侣吵架，男主突然吻住她。"

工作流：
1. 提取人物、场景、核心冲突
2. 按 3-3-4-3-2 节奏自动拆解 5 镜
3. 每镜分配景别、运镜、动作、音效
4. 走完后面的 prompt 装配流程

### 模式 B：用户已经给了完整 5 镜脚本

例：用户粘贴了一张分镜表的文字版，或自己列了 5 行。

工作流：
1. 直接采纳用户给定的镜头数、时长、景别、动作
2. 只补全用户没明说的字段（如音效、运镜方式建议）
3. 拼装 prompt 时严格遵循用户原文

**判断规则**：用户输入里是否同时出现"镜头 1/2/3"或"3 秒/4 秒"这种结构性字段——有就是模式 B，没有就是模式 A。

---

## 六、运镜方式词库（用于第 5 列）

| 中文（写进表格） | 英文（写进 prompt 描述） | 示意图标提示 |
|---------------|----------------------|------------|
| 手持 / 双人对峙 | handheld two-shot, slight shake | 双人位 + 摄影机 icon |
| 手持 / 正反打快切（Rapid Cuts）| handheld shot-reverse-shot rapid cuts | 两个摄影机 + 双向箭头 |
| 缓推 / Slow Push-in | slow dolly push-in | 摄影机 + 向前箭头 |
| Steady / 缓慢拉远 | steadicam slow pull-out | 摄影机 + 向后箭头 |
| Hold / 定格 | locked-off static shot, freeze frame | 摄影机 + 静止符号 |
| 跟拍 / Tracking | tracking shot follow-along | 摄影机 + 平行箭头 |
| 摇镜 / Pan | horizontal pan | 摄影机 + 弧形箭头 |
| 升降 / Crane | crane up / down | 摄影机 + 垂直箭头 |
| 俯拍 / Top Down | top-down overhead shot | 向下三角 |
| 低角度 / Low Angle | low angle hero shot | 向上三角 |

---

## 七、底栏五项填写指引

| 栏目 | 该填什么 | 示例 |
|------|---------|------|
| 🎨 整体风格 | 类型 + 光线 + 景深 + 胶片质感 + 情绪 | "韩剧都市爱情 / 黄昏暖光 / 浅景深 / 35mm 胶片质感 / 克制隐忍" |
| 📷 摄影参数 | 帧率 + 抖动风格 + 焦段 + 时段 + 景深 | "24fps / 手持微抖 / 35mm 焦段 / Golden Hour / Shallow DOF" |
| 🫂 动作设计 | 5 个镜头里 5 个动作短语 | "抢手对峙 / 正反打吵架 / 堵嘴一吻 / 紧紧拥抱 / 沉默收束" |
| 🎵 音效设计 | 关键音效线索 | "环境底噪 / 心跳压底 / Audio Drop / 弦乐渐强 / 自然收束" |
| ⏱ 总时长 | 永远是 "0:15" | "0:15" |

---

## 八、Prompt 装配模板

按这个顺序拼装 GPT Image 2 prompt（**这是这个 skill 最关键的一部分**）：

```
[Section 1: 版式总指令]
Create a single dark-themed cinematic storyboard infographic, vertical 3:4 or square 1:1 format,
high resolution (2048×2048 or 1536×2048), near-black background (#0a0a0a) with cream/warm-white text,
designed as a professional director's shot list reference card.

[Section 2: 标题区]
Top header in bold large Chinese sans-serif type: "「15秒导演流程图」(分镜头脚本)"
Subtitle in smaller font to the right: "[场景名] · [核心动作]"
(Use clean PingFang-style or Source Han Sans Chinese typography throughout.)

[Section 3: 主表格结构]
Below the header, a 7-column × 5-row table with thin separator lines.
Column headers in horizontal row (in Chinese):
  "镜头号" | "时间" | "景别" | "画面内容" | "运镜方式（示意图）" | "画面描述 / 动作" | "音效 / 音乐"
Each row represents one of 5 shots.

[Section 4: 5 行逐行内容]
Row 1: [镜头号: "1"] [时间: "0:00-0:03 (3秒)"] [景别: "中近景 (街口)"]
       [画面内容: embedded film-still, 16:9 ratio, showing {镜1 画面描述英文}]
       [运镜方式: "手持 / 双人对峙" with a small camera icon]
       [画面描述: "{镜1 中文动作描述}"]
       [音效: "{镜1 音效中文}"]
Row 2: ...
Row 3: ...
Row 4: ...
Row 5: ...

[Section 5: 底栏全局参数]
Bottom parameter bar split into 5 segments with icons:
🎨 整体风格 | 📷 摄影参数 | 🫂 动作设计 | 🎵 音效设计 | ⏱ 总时长

[Section 6: 嵌入式剧照风格统一指令]
All 5 embedded film-still images share IDENTICAL cinematic style:
{Style 锚点} | {Palette/Light 锚点} | {Character 锚点 - same person across all stills}
Film grain, shallow DOF, 35mm lens characteristics, photorealistic.
NOT comic, NOT illustration, NOT anime — these are cinematic film stills.

[Section 7: 文字渲染锁定]
All Chinese text rendered cleanly using a modern sans-serif typeface, sharp and legible,
hierarchical sizing (title > headers > body), no garbled characters, no decorative fonts.
```

---

## 九、避坑规则

| 问题 | 根本原因 | 解决方法 |
|------|---------|---------|
| 模型生成成了一张完整剧照 | prompt 没强调这是"信息图" | 开头第一句就说 "infographic, NOT a film image"，并明确表格结构 |
| 5 张嵌入剧照风格不统一 | Style 锚点写得太散 | 把 Style/Palette/Character 锚点合并成一句话，反复强调"all 5 stills share identical X" |
| 中文糊字 / 错字 | 字体不明确 + 字太多 | 明确 sans-serif 中文字体；表头每格 ≤ 6 字；时间码用阿拉伯数字 |
| 嵌入剧照变成了卡通画 | 没明确写实风 | 明确写 "photorealistic film stills, NOT illustration, NOT anime" |
| 表格行列错位 | 没强调网格 + 边线 | 明确 "thin gray separator lines between cells, aligned grid layout" |
| 底栏 emoji 没渲染或位置错 | emoji 在不同字体里宽度不同 | 接受这一格容错，文字部分准确即可，或改用线条图标描述 |
| 整张图比例不对 | 没指定尺寸 | 必须明示 vertical 3:4 或 square 1:1，推荐 2048×2048 起 |

---

## 十、工作流程

1. **判断输入模式**：A（一句话故事）还是 B（完整 5 镜脚本）
2. **确定四组锚点**：Character / Setting / Palette+Light / Style——这是 5 张剧照统一的基础
3. **规划 5 镜叙事弧**：按 3-3-4-3-2 公式（模式 A）或按用户给定（模式 B）
4. **填表**：每镜确定 7 列字段 + 底栏 5 项
5. **装配 prompt**：按第八节模板顺序拼装，先中文版后英文版
6. **检查清单**：
   - ✅ 标题"「15秒导演流程图」"出现在 prompt 里
   - ✅ 7 个中文表头逐字给出
   - ✅ 5 行内容齐全（含时间码、景别、动作、音效）
   - ✅ 底栏 5 项齐全
   - ✅ 强调"infographic, NOT a film image"
   - ✅ 强调"5 stills share identical style"
   - ✅ 字体定位（sans-serif Chinese）出现
   - ✅ 输出尺寸明示

---

## 十一、参数表（用户自定义）

| 用户说 | 技能响应 |
|--------|---------|
| "改成 6 镜" / "7 镜" | 调整节奏公式（如 6 镜走 2-3-3-3-2-2，7 镜走 2-2-3-3-2-2-1），重排表格行数 |
| "横版" / "16:9" | 改为横版布局，表格可能改为 5 列 × 7 行的转置版式 |
| "全英文表头" | 表头改英文（Shot / Time / Framing / Visual / Camera / Action / Audio）|
| "亮色背景" | 改 light theme（#fafafa 底 + 深色字 + 暖色调强调） |
| "去掉底栏" | 跳过底栏装配段，只保留主表 |
| "古风" / "现代都市" / "悬疑" / "科幻" | 替换 Setting + Style 锚点，剧照风格随之切换 |
| "我已经有 5 个镜头了" | 进入模式 B，直接采纳用户的镜头分配 |
| "只要中文" / "只要英文" | 跳过另一版 |
| "改时长" / "30 秒短片" | 节奏公式扩展为 5+5+8+7+5 之类，表格表头改"30秒导演流程图" |

---

## 十二、完整示例

**用户输入：**
> 黄昏巷口，一对情侣吵架，女主转身要走，男主一把拉住她吻了上去。

**输出：**

```
🎬 GPT Image 2「15秒导演流程图」分镜表 Prompt

【一致性锚点 / Consistency Anchors】
- Characters: A young East Asian man, mid-twenties, slim build, wearing round-frame glasses and a cream-white cotton t-shirt, soft brown hair. A young East Asian woman, early twenties, twin braids, wearing a lavender hoodie, expressive almond eyes.
- Setting: A narrow alley intersection in a Korean-style urban neighborhood at golden hour, warm street lamps starting to glow, distant shop signs in soft bokeh
- Palette/Light: Warm golden-hour amber light, deep shadows, cream and lavender highlights against muted street tones
- Style: K-drama urban romance, photorealistic, 35mm film grain, shallow depth of field, restrained and emotional tone

═══════════════════════════════════════
📐 GPT Image 2 Prompt
═══════════════════════════════════════

【中文版】
生成一张深色背景的电影级分镜信息图（不是一张电影画面，而是一张表格化的导演脚本卡），竖版 3:4 或正方形 1:1 比例，分辨率 2048×2048 以上，背景近黑色（#0a0a0a），文字为奶白色与暖白色，整体设计为专业导演手卡风格。

顶部标题，加粗中文黑体大字："「15秒导演流程图」(分镜头脚本)"，右侧副标题小字："黄昏巷口 · 堵嘴一吻"。所有中文使用清晰的 PingFang 或思源黑体风格无衬线字体，字号有层级（标题 > 表头 > 正文）。

标题下方为一个 7 列 × 5 行的表格，单元格之间为细灰色分隔线，整齐对齐。表格列表头（从左到右）：
"镜头号" | "时间" | "景别" | "画面内容" | "运镜方式（示意图）" | "画面描述 / 动作" | "音效 / 音乐"

第 1 行：
- 镜头号："1"
- 时间："0:00–0:03 (3秒)"
- 景别："中近景 (街口)"
- 画面内容：嵌入一张 16:9 比例的电影剧照，画面为：黄昏巷口街角，年轻女子刚刚转身，眼眶通红，鼻尖泛红；男子站在两步之外，神情紧绷
- 运镜方式："手持 / 双人对峙"，旁边一个简洁的双人位 + 摄影机线条小图标
- 画面描述 / 动作："女主猛回身用开手，眼眶通红，鼻尖泛红，呼吸急促，倔强咬唇。"
- 音效 / 音乐："远处车流声，风过巷口的低响，低频心跳声压底。"

第 2 行：
- 镜头号："2"
- 时间："0:03–0:06 (3秒)"
- 景别："胸前特写 (正反打)"
- 画面内容：嵌入剧照，分屏式正反打——左侧男子戴眼镜低声开口，右侧女子抢话回击
- 运镜方式："手持 / 正反打快切 (Rapid Cuts)"，旁边两个摄影机 + 双向箭头小图标
- 画面描述 / 动作："男主低声用力——'你根本不明白——'；女主抢说——'都你说嘛！你倒是说啊——'"
- 音效 / 音乐："心跳声拉到顶，环境音瞬间抽空（Audio Drop）。"

第 3 行：
- 镜头号："3"
- 时间："0:06–0:10 (4秒)"
- 景别："侧脸特写 (吻戏)"
- 画面内容：嵌入剧照，男子一手扣住女子后脑俯身堵吻，女子睫毛闭合，双手悬在他胸前
- 运镜方式："缓推 / Slow Push-in"，旁边摄影机 + 向前箭头小图标
- 画面描述 / 动作："男主一手扣后脑俯身堵吻，女主睫毛后猛地阖眼，双手悬在他胸前不敢落下。"
- 音效 / 音乐："心跳回归，柔软弦乐起抽。"

第 4 行：
- 镜头号："4"
- 时间："0:10–0:13 (3秒)"
- 景别："中景 (拥抱)"
- 画面内容：嵌入剧照，吻轻轻分开后，男子将女子搬入怀中紧紧扣住
- 运镜方式："Steady / 缓慢拉远"，旁边摄影机 + 向后箭头小图标
- 画面描述 / 动作："吻轻轻分开，男主直接将女主搬入怀中紧紧扣住，女主双手收紧。"
- 音效 / 音乐："弦乐渐强，环境音柔化。"

第 5 行：
- 镜头号："5"
- 时间："0:13–0:15 (2秒)"
- 景别："中近景 (定格)"
- 画面内容：嵌入剧照，男子低头贴在女子耳边，街灯落在他们侧脸上
- 运镜方式："Hold / 定格"，旁边摄影机 + 静止符号小图标
- 画面描述 / 动作："男主低头在女主耳边——'我哪儿都不去。'；女主声音闷在他胸口带哭腔——'——骗子。'"
- 音效 / 音乐："弦乐推到顶，最后半秒突然收束，仅留两人呼吸声。"

表格下方为底栏全局参数条，分为 5 段，每段一个图标 + 标题 + 内容小字：
🎨 整体风格："韩剧都市爱情 / 黄昏暖光 / 浅景深 / 35mm 胶片质感 / 克制隐忍"
📷 摄影参数："24fps / 手持微抖 / 35mm 焦段 / Golden Hour / Shallow DOF"
🫂 动作设计："抢手对峙 / 正反打吵架 / 堵嘴一吻 / 紧紧拥抱 / 沉默收束"
🎵 音效设计："环境底噪 / 心跳压底 / Audio Drop / 弦乐渐强 / 自然收束"
⏱ 总时长："0:15"

整张图所有 5 张嵌入剧照风格严格一致：相同人物（戴圆框眼镜的年轻男子 + 双辫紫色帽衫年轻女子）、相同黄昏暖光、35mm 胶片质感、浅景深、写实电影质感。剧照不是漫画、不是插画、不是动漫风格。

【English】
Create a single dark-themed cinematic storyboard infographic (NOT a film image, NOT a comic page), vertical 3:4 or square 1:1 format, resolution at least 2048×2048, near-black background (#0a0a0a) with cream-white and warm-white text, designed as a professional director's shot-list reference card.

Top header in bold large Chinese sans-serif: "「15秒导演流程图」(分镜头脚本)". Subtitle to the right in smaller font: "黄昏巷口 · 堵嘴一吻". All Chinese text uses clean PingFang or Source Han Sans-style sans-serif typography with hierarchical sizing (title > header > body).

Below the header, a 7-column × 5-row table with thin gray separator lines, neatly aligned. Column headers left to right (in Chinese):
"镜头号" | "时间" | "景别" | "画面内容" | "运镜方式（示意图）" | "画面描述 / 动作" | "音效 / 音乐"

Row 1:
- 镜头号: "1"
- 时间: "0:00–0:03 (3秒)"
- 景别: "中近景 (街口)"
- 画面内容: embedded 16:9 film still — a young woman just turning back at a golden-hour alley intersection, red-rimmed eyes, red nose tip; a young man standing two steps away, jaw tense
- 运镜方式: "手持 / 双人对峙" with a small line-art icon of two figures + camera
- 画面描述 / 动作: "女主猛回身用开手，眼眶通红，鼻尖泛红，呼吸急促，倔强咬唇。"
- 音效 / 音乐: "远处车流声，风过巷口的低响，低频心跳声压底。"

Row 2:
- 镜头号: "2"
- 时间: "0:03–0:06 (3秒)"
- 景别: "胸前特写 (正反打)"
- 画面内容: embedded film still — split shot-reverse-shot, the bespectacled man speaking low on the left, the woman cutting in on the right
- 运镜方式: "手持 / 正反打快切 (Rapid Cuts)" with a small icon of two cameras + bidirectional arrow
- 画面描述 / 动作: "男主低声用力——'你根本不明白——'；女主抢说——'都你说嘛！你倒是说啊——'"
- 音效 / 音乐: "心跳声拉到顶，环境音瞬间抽空（Audio Drop）。"

Row 3:
- 镜头号: "3"
- 时间: "0:06–0:10 (4秒)"
- 景别: "侧脸特写 (吻戏)"
- 画面内容: embedded film still — the man's hand cradling the back of the woman's head as he leans down to kiss her, her lashes closed, her hands hovering at his chest
- 运镜方式: "缓推 / Slow Push-in" with a small icon of camera + forward arrow
- 画面描述 / 动作: "男主一手扣后脑俯身堵吻，女主睫毛后猛地阖眼，双手悬在他胸前不敢落下。"
- 音效 / 音乐: "心跳回归，柔软弦乐起抽。"

Row 4:
- 镜头号: "4"
- 时间: "0:10–0:13 (3秒)"
- 景别: "中景 (拥抱)"
- 画面内容: embedded film still — the kiss gently parting, the man pulling the woman tightly into his chest
- 运镜方式: "Steady / 缓慢拉远" with a small icon of camera + backward arrow
- 画面描述 / 动作: "吻轻轻分开，男主直接将女主搬入怀中紧紧扣住，女主双手收紧。"
- 音效 / 音乐: "弦乐渐强，环境音柔化。"

Row 5:
- 镜头号: "5"
- 时间: "0:13–0:15 (2秒)"
- 景别: "中近景 (定格)"
- 画面内容: embedded film still — the man's head bent down at the woman's ear, a streetlamp catching the side of their faces
- 运镜方式: "Hold / 定格" with a small icon of camera + static symbol
- 画面描述 / 动作: "男主低头在女主耳边——'我哪儿都不去。'；女主声音闷在他胸口带哭腔——'——骗子。'"
- 音效 / 音乐: "弦乐推到顶，最后半秒突然收束，仅留两人呼吸声。"

Bottom parameter bar below the table, divided into 5 segments, each with an icon + title + body text:
🎨 整体风格: "韩剧都市爱情 / 黄昏暖光 / 浅景深 / 35mm 胶片质感 / 克制隐忍"
📷 摄影参数: "24fps / 手持微抖 / 35mm 焦段 / Golden Hour / Shallow DOF"
🫂 动作设计: "抢手对峙 / 正反打吵架 / 堵嘴一吻 / 紧紧拥抱 / 沉默收束"
🎵 音效设计: "环境底噪 / 心跳压底 / Audio Drop / 弦乐渐强 / 自然收束"
⏱ 总时长: "0:15"

CRITICAL: All 5 embedded film stills share IDENTICAL cinematic style — same characters (bespectacled young man + twin-braided young woman in lavender hoodie), same golden-hour amber light, 35mm film grain, shallow depth of field, photorealistic K-drama aesthetic. The stills are cinematic photography, NOT comic art, NOT illustration, NOT anime.

═══════════════════════════════════════
📋 5 镜叙事弧
═══════════════════════════════════════

| 镜 | 时长 | 景别 | 功能 | 一句话内容 |
|---|------|------|------|----------|
| 1 | 3秒 | 中近景 | 开场建立 | 巷口女主转身用开他的手 |
| 2 | 3秒 | 胸前特写 | 冲突顶点 | 正反打吵架 |
| 3 | 4秒 | 侧脸特写 | 转折高潮 | 堵嘴一吻 |
| 4 | 3秒 | 中景 | 缓冲 | 拥入怀中 |
| 5 | 2秒 | 中近景 | 收束 | 耳边低语"我哪儿都不去" |

---
💡 出图建议：竖版 3:4，2048×2730，节奏走 3-3-4-3-2 的心跳曲线，最长的 4 秒永远留给情绪转折点（本片是吻戏）。
```

---

## 十三、注意事项

- **不解释这张图怎么做出来的**，直接给可用的中英双版 prompt
- **不写 negative prompt**（GPT Image 2 不支持）
- **嵌入剧照必须明示"photorealistic film still"**，不然容易出卡通插画
- **中文表头逐字给死**，让 GPT Image 2 照抄而不是自己造词
- **底栏 emoji 接受容错**——如果模型把 🫂 渲染不好，文字部分准确即可
- **如果用户给出已有的人物设定**（比如来自 `realistic-character-prompt` 的产出），直接复用为 Character 锚点
- **如果用户已经有完整 5 镜脚本**，进入模式 B，原文采纳，不要替用户改剧情
- **风格不限于韩剧**——古风、悬疑、科幻、动漫都可以，但 Style 锚点要相应替换
