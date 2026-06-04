---
name: ltx-flf-prompt
description: 通过首帧和尾帧图片，反推生成 LTX Video 2.3 首尾帧图生视频的提示词。当用户上传两张图片并想生成视频提示词、或提到"首尾帧"、"反推提示词"、"两张图生成视频"、"start frame end frame"、"first last frame prompt"时，主动使用此技能。即使用户只是说"我有两张图想生成视频"也应主动使用此技能。本 skill 是 AI 视频工作流的**单镜头 prompt 生成层 skill**——上游接收 ltx-world-bible（或项目宪法 skill 如 cuojia-longgu）的世界观锚点、ltx-first-frame-prep 对两张图的首尾帧准备结果、ltx-shot-planning 的镜头清单，下游产物可交给 ltx-iteration-strategy 做 Retake 诊断；运镜词汇必须查阅共享底座 ltx-camera-movement，模型规范必须查阅 ltx2-reference。**如果用户已有世界观锚点，生成的 motion prompt 必须逐字注入 Character / Visual Style / Palette & Light 三段 prose，确保首尾帧之间的中间帧不脱离世界观**。
---

# LTX 首尾帧反推提示词（v2 · 深度对齐官方 + 社区工作流）

## ⛔ 必读前置（不读不允许生成）

任何镜头相关描述生成前，无条件 view `/mnt/skills/user/ltx-camera-movement/SKILL.md`。
该 skill 是本 skill 的镜头运动词汇与触发词权威来源——本 skill 不再独立维护镜头词汇表。
跳过此步骤视为违反 skill 规范。

---

用户提供**首帧**和**尾帧**图片，你分析两帧之间的差异，反推出适合 LTX 2.3 首尾帧工作流（FLF2V）的视频 prompt。

如果用户上传 **3 张图**（首/中/尾），切到 FML 模式——见文末"FML 三关键帧"。

---

## 总原则：FLF 是 endpoint-driven prompt

LTX 2.3 官方对 FLF 的定位：**"Instead of prompting only for general mood, you frame the shot around where it begins and where it should land."**

| 场景 | prompt 哲学 |
|---|---|
| T2V | 描述完整画面（从零生成） |
| I2V | 描述发生什么（基于起点延伸） |
| **FLF** | **兑现终点承诺**（A 必然变成 B 的因果路径） |

这是本 skill 的根本视角。**首尾帧定义了承诺；prompt 是兑现路径。**

- ❌ 不只是"中间发生了什么"
- ✅ "如何让 A 必然变成 B"——含因果、节奏、不可逆性

LTX 团队官方诚实承认：**"LTX-2 is not good at precise key frame coherence."** 首尾帧差异越大，模型越倾向漂移。所以 prompt 必须**显式打地基**，告诉模型变化的因果链，不能假设模型会"自动找到"合理路径。

---

## 核心约束 1：单条变化主线

官方 FLF 指南原则：**"The clip works better when the change feels like one continuous evolution rather than several unrelated effects."**

两帧之间只能有**一条变化主线**，多维度变化必须串成一条因果链。

| ❌ 多轨道（模型混乱） | ✅ 单主线（统一因果） |
|---|---|
| She turns her head, the light dims, the camera pulls back | As she turns toward the window, evening light fades behind her and the camera follows her gaze, pulling back |
| The product rotates, the background changes color, particles appear | The product rotates into its hero angle, **and as it does**, the background warms into amber, releasing soft particles |

**判断方法**：写完 prompt 后问自己——"中间任何一句被删，整段还成立吗？"如果是，说明那一句是独立轨道，要重写成"因为 X 所以 Y"。

---

## 核心约束 2：镜头简化建议（按 LTX 实测难度分级）

官方 FLF 指南：**"A fixed frame, slow push-in, or gentle tracking move usually gives the transition more coherence than an overly complex camera change."**

FLF 场景**镜头越简单，过渡越稳**。所有运镜按 `ltx-camera-movement` skill 的 LTX 实测难度分级：

| 难度 | 运镜 | FLF 适用度 |
|---|---|---|
| ⭐ | Static / Locked-off、Zoom | 🥇 最稳——主体内变化首选 |
| ⭐⭐ | Dolly In / Out、Pan、Tilt、Steadicam | 🥈 推荐——FLF 主力配置 |
| ⭐⭐⭐ | Slide/Truck、Pedestal/Boom、Handheld、Rack Focus | 🥉 可用——明确首尾构图后稳定 |
| ⭐⭐⭐⭐ | Tracking、POV | ⚠️ 谨慎——身份漂移/失代入风险 |
| ⭐⭐⭐⭐⭐ | Arc/Orbit、Crane/Jib | 🚫 强烈不建议 FLF——3D 一致性崩溃 |
| ❌ | Roll/Dutch Tilt、Dolly Zoom | 🚫 LTX 完全做不出 |

**反推时如果出现"复杂镜头嫌疑"，主动建议用户简化**。例：

> "首尾帧暗示镜头有升降 + 转向 + 推近三种动作叠加（属于 Crane/Jib ⭐⭐⭐⭐⭐），FLF 场景下复杂运镜易破坏过渡连贯性。建议简化为'缓慢推近'（Dolly In ⭐⭐），或考虑重新选尾帧让镜头变化更单一。"

### FLF 运镜 prompt 写法（衍生自 camera-movement 五原则）

`ltx-camera-movement` 的 5 条核心原则在 FLF 场景下具体化：

**1. 必须有"任务感"——明确起点和终点**

LTX 运镜表现取决于是否给了明确起止。FLF 场景下"任务感"等同于 endpoint-driven 哲学：

- ❌ 弱：`the camera pans`
- ✅ 强：`the camera pans from the fireplace, ending framed on the window`

**2. 用"动作的结果"描述运动**

跟核心约束 1 的因果链原则同源。具体到镜头：

- ❌ 弱：`slides horizontally to the right`
- ✅ 强：`slides right; the left-side stove exits the frame, the right-side lantern enters the view`

**3. 速度词不如时间分配（重要——覆盖 v2 之前的 `slowly` 默认）**

LTX 经常**忽略形容词**（`slowly` / `gently` / `gradually`）。强制时间分配更稳：

- ❌ 弱：`very slowly pans`（LTX 可能仍较快）
- ✅ 强：`pans, completing by the fourth second, then holds steady`

**FLF 默认结构**：`[运镜动作], completing by the [N-1]th second, then holds steady`——最后 1-2 秒定格让画面稳定。

**4. 避免反指令陷阱（FLF 特别危险）**

不要在运镜指令里加"保持 X 居中"。首尾帧已经隐含构图约束，再加居中指令 = LTX 优先满足约束、破坏运镜：

- ❌ 错误：`slides right while keeping the central window centered` → LTX 改做 dolly
- ✅ 正确：`slides right; the camera moves, the window naturally shifts to the left of the frame`

**对称构图首帧警告**：当首帧是对称构图（中心物体、左右平衡），LTX 会**自动把 slide 改为 dolly out**——这是已观察到的强偏好。若用户要 slide 必须明确指令"the camera moves, X shifts to the side"。

**5. 避免否定方向描述**

- ❌ 弱：`pans left, not right`
- ✅ 强：`pans from right to left`

### 末尾衰减应对（长 FLF 必读）

运镜越长，LTX 越容易末尾衰减（画面变暗、光照减弱、火焰熄灭）。FLF 应对：

1. **运镜时长不要超过 7 秒**（低光/黄昏场景上限 5 秒）
2. **明确写"末帧匹配首帧"**：`the final frame matches the first frame in lighting, exposure, color temperature` ——这条对 FLF 特别有效，因为已经有尾帧锁定基准
3. **避免用 `dusk` / `blue hour` / `golden hour`** 等隐含时间流逝的词作起点描述
4. **运镜完成后保留 2-3 秒定格**（已并入原则 3 的默认结构）

---

## 镜头反推（区分主体动 vs 镜头动）

**首尾帧分析的核心能力**：从两张静图反推时，**必须先区分主体在动还是镜头在动**——两种写法完全不同，误判会让模型抓不准重点。

| 观察 | 推断 | 写法 |
|------|------|------|
| 尾帧主体更小，背景显示出**更多**画面外的内容 | 镜头拉远（dolly out） | `the camera slowly pulls back, revealing more of the surroundings` |
| 尾帧主体更小，背景**没有**显示更多内容 | 主体在远离镜头 | `she walks away from the camera` |
| 尾帧主体更大，背景**减少** | 镜头推近（dolly in） | `the camera slowly pushes in toward her` |
| 尾帧主体更大，背景**不变** | 主体在靠近镜头 | `she steps toward the camera` |
| 主体在画面里横向移动，背景**跟着动** | 镜头跟随（tracking） | `the camera tracks alongside her` |
| 主体在画面里横向移动，背景**不动** | 主体在画面内走动 | `she moves across the frame` |
| 主体位置不变，背景在变 | 镜头平移/旋转 | `the camera slowly pans / arcs around her` |
| 画面上下错位，主体高度变 | 倾斜 tilt / 升降 crane | `the camera tilts up` / `cranes upward` |
| 主体大小变化但透视未变 | 变焦 zoom（非位移）| `the lens slowly zooms in` |

判断不确定时，**优先写成镜头运动**——LTX 2.3 对镜头运动的还原比对主体走位更稳定。

**⚠️ 写入最终 prompt 时**：上表"写法"列里的 `slowly` 仅作识别示意。最终 prompt 必须按核心约束 2 原则 3 改为时间分配——例如把 `the camera slowly pushes in toward her` 改写为 `the camera pushes in toward her, completing by the fourth second, then holds steady`。

---

## 分析步骤

### Step 0：一致性闸门（前置）

判断两帧是否属于**同一连续镜头**。三个问题**全部 yes** 才能进入下一步：

1. 同场景？（同一物理空间，光线体系一致）
2. 同主体？（人脸/物体身份一致，未换人换物）
3. 同时间体系？（不是跨越几小时或日夜的硬切）

任一 no → 直接告诉用户："这两帧不像同一镜头的延续，FLF 难以生成自然过渡。建议：(a) 改用 T2V 分别生成两个独立镜头再剪辑，或 (b) 重选一张让两帧属于同一镜头。"

### Step 1：逐帧识图 + 标注变化

分别识别两帧的 6 个维度，每个维度标注两帧之间是否变化（无 / 微小 / 中等 / 大幅）：

| 维度 | 看什么 |
|------|--------|
| 景别 | 全景 / 中景 / 近景 / 特写 / 微距 |
| 主体姿势/位置 | 身体朝向、画面内坐标 |
| 视线/朝向 | 看向哪里 |
| 表情/物理线索 | 嘴角、眉毛、肩膀、下颌（不写情绪标签） |
| 镜头角度 | 平视 / 仰角 / 俯角 / 侧面 |
| 光线/氛围 | 方向、强度、颜色、阴影 |

**关键：必须识别接触/施力关系。** 如果首帧中物体 A 与 B 有接触，在尾帧位置发生变化，要判断是 A 推动 B、B 让位、还是各自独立运动。误判因果关系会导致 prompt 完全跑偏。

### Step 2：矛盾检测

首尾帧之间是否有**隐含矛盾**？常见类型：

- 首帧表情中性，尾帧大笑——但中间时长只够"自然过渡"
- 首帧手在 A 位，尾帧手在 B 位——但首帧手被衣袖挡住看不见路径
- 首帧白天，尾帧黄昏——但中间只有 3 秒
- 主体首帧静止，尾帧动作幅度极大——但中间没有起手动作

命中矛盾 → 在输出里**先于过渡描述**给出警告："首尾帧之间存在 [具体矛盾]，建议 (a) 调整 X 帧 或 (b) 延长视频时长至 Y 秒。"

### Step 3：难度评级

**评级管的是过渡能否被 LTX 还原**——不是图像内容难度（那是风险提示，见下方）。

- **🟢 高成功率**：单一维度变化，幅度微小到中等，主体身份稳定
- **🟡 中等成功率**：两个维度同时变化但可串成一条主线，景别跨两级，转身不超过 45°
- **🔴 低成功率**：三个以上维度且难以串成主线，转身超过 90°，光线/场景大幅突变，**景别跨三级且同时伴随主体姿势变化**（纯镜头推拉不算 🔴，归为 🟡）

🔴 评级时**必须**给出尾帧调整建议，不能只说"难度高"。

---

## 输出格式

```
## 帧差异分析

**首帧**：[一句话描述]
**尾帧**：[一句话描述]
**变化维度**：[列出变化项]
**变化主线**：[一句话——这次变化的统一因果是什么]

**难度评级**：🟢/🟡/🔴 [简短说明]

[矛盾检测命中时：⚠️ 矛盾警告 + 建议]
[🔴 时：尾帧调整建议]
[复杂镜头嫌疑时：📷 镜头简化建议]

---

🎬 LTX 2.3 Video Prompt

[英文 prompt，单段落，按下方"长度按时长校准"表选择长度]

🀄 中文对照

[中文版本]

⏱️ 建议时长：[X 秒] — [理由]

🎛️ 推荐 strength 配置：first_strength [X] / last_strength [Y] — [理由]

📷 镜头实测难度：[运镜名称] [⭐ 星级] — [简短说明：FLF 适用度]

💡 风险提示：[仅在命中下方"高风险元素清单"时输出，否则省略]
```

---

## strength 参数与 prompt 策略

社区共识的 FLF 参数区间：

- **`first_strength`**：0.95–1.0（首帧锁紧，几乎总是接近 1）
- **`last_strength`**：**0.6–0.9（必须低于 first）**——两个都拉满 = 没有空间生成运动 = 输出几乎静态

**默认假设**：用户没指定时，按 `first=1.0 / last=0.75` 给推荐。三档对应的 prompt 策略：

| last_strength | 尾帧含义 | prompt 策略 |
|---|---|---|
| **0.9–1.0**（硬锁尾帧） | 尾帧是必须命中的精确终点 | 详细描述"终点是必然的"——含明确因果（"as A unfolds, **she lands in** ...") |
| **0.7–0.85**（推荐默认） | 尾帧是视觉目标，允许小幅漂移 | 标准过渡描述，可用 `approximately settles toward` / `arrives near` 等柔化词 |
| **0.5–0.7**（软目标） | 尾帧仅作风格/构图暗示 | prompt 主导叙事，尾帧让运动自然落地，避免硬性描述结束状态 |

**Strength 互动规则**：
- 用户没给图像，只描述需求 → 默认 `first=1.0 / last=0.75`，标记"如硬锁尾帧请调高 last 到 0.95"
- 用户首尾帧差异极大 → 推荐 `last=0.65–0.75`（防漂移过强）
- 用户首尾帧差异极小 → 推荐 `last=0.6–0.7`（**否则输出会是静态图**——见下方失败诊断）

---

## 失败模式诊断（社区 #1 痛点）

### "输出是静态图 / 几乎没运动"

LTX FLF 最高频失败。命中以下条件时主动警告：

| 触发条件 | 原因 | prompt 应对 |
|---|---|---|
| 两帧视觉差异 < 10%（接近相同） | 模型看不出该动什么 | **主动注入运动叙事**：`slowly tilts and emerges` / `gradually awakens` 等强动词 + 渐变副词。**不要被动描述变化** |
| 视频时长 < 3 秒 / 帧数 < 49 | 模型来不及生成可见运动 | 短句 + 强动词 + 最小镜头变化；建议时长升到 ≥4 秒 |
| 首尾帧太相似但用户要求长视频 | 模型会原地踏步 | 建议用户改用 I2V（单帧 + 长 prompt），或重选差异更大的尾帧 |

### "尾帧不匹配 / 视频漂走了"

- 拉高 `last_strength` 到 0.9–1.0
- 缩短视频时长
- prompt 里加明确的"承诺兑现"语言（`arrives at` / `lands on` / `culminates in`）

---

## FLF Prompt 写法核心规则

### 写什么 / 不写什么

| 要素 | 处理 |
|---|---|
| **角色外观**（发色、服装、年龄） | ❌ 不写——首尾帧已锁 |
| **起始/结束的景别和镜头角度** | ❌ 不写——首尾帧已锁 |
| **起始/结束的光线颜色、纹理、场景** | ❌ 不写——首尾帧已锁 |
| **情绪标签**（sad / confused / nervous） | ❌ 禁止——官方明确禁止，必须改写为物理线索 |
| **矛盾描述**（"calm throughout" 但尾帧大笑） | ❌ 禁止——自相矛盾会让模型混乱 |
| **过度量化**（"3 degrees per second"） | ❌ 禁止——LTX 不接受数值规格，用自然语言 |
| **过渡过程的主体动作** | ✅ 必写——含物理线索（`her jaw tightens` / `his shoulders relax`） |
| **因果链接词**（as / because / so that） | ✅ 必写——串联多维度变化 |
| **镜头运动** | ✅ 必写——或明确 `the camera holds steady` |
| **光线变化** | ✅ 两帧光线/氛围有差异时必写（`dims gradually` / `sun fades`） |
| **音频** | ✅ 建议写——见下方"audio 作为节奏控制工具" |
| **对话**（角色台词） | ✅ 有则写——见下方"dialogue 写法" |

### 物理线索而非情绪标签

LTX 不会把"sad"翻译成可见画面。必须改成身体能演出来的具体动作：

| ❌ 情绪标签 | ✅ 物理线索 |
|---|---|
| She looks sad | Her eyes lower, jaw tightens |
| He becomes nervous | His shoulders stiffen, fingers fidget |
| She feels relieved | Her shoulders drop, breath releases |

**无人场景等价**（物体/环境）：
| ❌ 抽象标签 | ✅ 可见线索 |
|---|---|
| The room feels tense | The air thickens with stillness, dust motes hang suspended |
| The product feels premium | Light glides slowly across its polished surface |
| The scene becomes magical | Particles drift upward, the glow intensifies at the edges |

### 写过渡，不写终点

尾帧已经锁定，不需要描述终点是什么样，要描述"中间发生了什么"。

| ❌ 错误 | ✅ 正确 |
|---------|---------|
| She ends up in close-up | The camera slowly pushes in toward her face |
| Her hand reaches her ear | She raises her hand and gradually tucks her hair |
| The scene becomes darker | The light dims gradually as clouds pass |

### Audio 作为节奏控制工具

官方原话："**Audio descriptions have more impact** [in 2.3]."

LTX 2.3 的 audio 与视频联合生成——**audio 描述会反向影响视频运动节奏**：

| audio 描述 | 对运动的影响 |
|---|---|
| `deep slow breathing, room tone` | 画面动作变慢，呼吸节奏可见 |
| `rain steady on glass, distant traffic` | 主体动作变沉稳，环境运动（雨水、人影）增加 |
| `sudden gust of wind, leaves rustling` | 主体可能被推动，环境元素活化 |
| `silence, only faint heartbeat` | 极简化运动，强调微动作 |

**FLF 控制运动节奏的隐藏手柄**：当用户想要"慢一点 / 急一点"，调 audio 描述比改运动词更有效。

### Dialogue 写法（若两帧之间有台词）

官方推荐结构：**短句 + 表演指示穿插 + 引号包裹 + 标注语言**。例：

```
A woman in her thirties speaks in a quiet, measured voice in Mandarin Chinese, "我以为你不会回来了。"
She pauses, her gaze drops toward her hands, then she continues, "可是你来了。"
Her shoulders soften. The camera holds steady throughout. Audio is intimate with faint room tone.
```

短台词更稳；长独白容易让模型把表演压缩成机械朗读。

### 关键写作技巧

- **时间分配优先于速度词**：`completing by the Xth second, then holds steady` 比 `slowly` 更可靠（运镜节奏控制详见核心约束 2 原则 3）
- **渐变副词**作辅助：`gradually / over the course of the shot / smoothly`——配合时间分配使用，单独用 LTX 会忽略
- **因果链接词**：`as / because / so that / which causes`
- **承诺兑现词**（last_strength 高时）：`arrives at / lands on / culminates in / settles into`
- **柔化词**（last_strength 低时）：`approximately / drifts toward / settles near`
- **接触动作明确因果**：`pressing against ... pushes ... downward`，避免悬浮歧义

### 最小化原则（保留 + 修订）

用户描述什么动作，就写什么动作。不要为了句子结构而加入起始/收尾等用户没要求的过渡动作。

**但 LTX 2.3 倾向长 prompt——prompt 越长输出越稳定**。所以不强行扩写 ≠ 写得太短。下限按"长度按时长校准"表，不再统一卡 3 句。

---

## 长度按视频时长校准（不是按难度）

官方明确警告："**Short prompts for long videos leave the model without enough direction to fill the duration.**"

旧版按"难度"分长度是错的，正确校准按视频时长：

| 视频时长 | 推荐句数 | 推荐词数 | 说明 |
|---|---|---|---|
| 3 秒 | 3-4 句 | 60-100 词 | 极简过渡 |
| 4-5 秒 | 4-6 句 | 100-150 词 | 标准 FLF |
| 6-8 秒 | 6-8 句 | 150-220 词 | 含明显因果/光线/audio |
| 9-10 秒 | 8-10 句 | 200-300 词 | 多阶段叙事必填 |

**词数下限比句数下限更重要**——LTX 2.3 把 prompt 词数当时间填充信号。10 秒视频 80 词 = 模型会"跑通"再原地踏步。

官方硬上限：**单段落、单一连续段、≤300 词**。超过 300 词模型开始忽略后半段。

---

## 时长建议规则

按"难度区间"和"内容上限"取**交集下限**：

**按过渡难度（理想区间）**：
- 🟢 单维度微小变化 → 3-5 秒
- 🟡 双维度可串主线 → 5-7 秒
- 🔴 多维度或大幅变化 → 建议先调整尾帧，否则 ≥7 秒

**按内容硬上限**：
- 含人脸首尾帧过渡 → **≤5 秒**（超过身份漂移风险）
- 含珠宝/精细物体滑动 → **≤4-5 秒**（超过物体形变）
- 含文字/Logo 在主体上 → **≤3 秒**（超过必糊）

**最终时长 = min(难度区间上限, 所有内容硬上限)**。冲突时按内容硬上限走，**并主动告知用户**："过渡难度允许 7 秒，但含人脸特写硬上限 5 秒，按 5 秒推荐。"

---

## LTX 高风险元素清单（图像内容本身的难度）

**风险提示管的是图像里哪些"物"对 LTX 来说天然难处理**——不是两帧之间的变化。命中下列元素时在"风险提示"中明确警告：

- **人脸特写**：超过 5 秒易出现身份漂移、五官变形
- **珠宝/钻石/金属**：长时长易出现形变、闪烁、戒指变粗
- **文字/Logo**：几乎一定会糊掉或乱码，建议尾帧避开正面文字
- **手指接触物体**：易出现穿模、悬浮、抓握姿势变形
- **毛发/发丝**：飘动易变成模糊一团
- **快速运动**：超过中速的动作易出现拖影和断裂
- **多角色 / 多动作场景**：官方明确不擅长，角色越多越容易漏
- **矛盾光照**：暖色和冷色光源同时存在（除非有明确动机），LTX 会混乱
- **混乱物理**：复杂物理交互（爆炸、流体撞击）易出 artifact，舞蹈类规律性运动 OK

🔴 评级或命中多个风险时，建议生成 **2-3 个版本择优**，重点检查上述风险点。

---

## 特殊情况处理

- **两帧主体位置差异 > 画面 1/3** → 评 🔴，建议重新选尾帧
- **面部角度变化 > 45°** → 评 🟡 到 🔴，明确转身方向，警告身份漂移
- **只上传一张图** → 提示需要两张图（首帧+尾帧），或改用 `ltx-i2v-prompt`
- **首尾帧视觉差异 < 10%** → 见"失败模式诊断"的静态图条目，主动建议改用 I2V 或重选尾帧

---

## FML 三关键帧（首/中/尾）

LTX 2.3 已支持三关键帧条件化。用户上传 3 张图时按 FML 处理：

**核心差异 vs FLF**：
- 中间帧锚定了运动**节奏的中点**——模型不再自由分配前后半段时长
- 三帧之间的过渡必须**两段连贯**：A→B 和 B→C 各自符合 FLF 原则
- prompt 必须显式分两段叙事，用时间标记串联：`first ... then, midway through, ... finally ...`

**判断**：上传 3 张图、3 张图属于同一镜头延续 → 进入 FML 模式。否则按 FLF（取首尾两张）或建议拆分。

**FML strength 默认**：`first=1.0 / middle=0.85 / last=0.8`——中间帧锁得比尾帧稍紧，让节奏更稳。

---

## 写作风格

- prompt 用现在进行时描述过渡过程
- 单段落，单一连续段，≤300 词
- 始终输出中英双语
- 难度评级 + 时长建议 + strength 推荐 + 镜头实测难度为必输出项；矛盾警告/镜头简化/风险提示按命中输出

## 输出纪律

- 不输出 negative prompt（除非用户特别要求）
- 不生成反馈 Artifact
- 不调用 storage
- 输出完成即停
