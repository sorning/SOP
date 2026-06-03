---
name: flux-modern-palatial-hall
description: 将简短描述扩写为高质量的 Flux2 文生图 prompt，专攻"现代宫殿尺度大厅"（Modern Palatial Grand Hall）——在保留现代材质与干净线条的前提下，把空间从顶奢公寓的 9-12 米挑高放大到 18 米+ 穹顶级宫殿体量，靠对称列柱、拱顶、enfilade 拱门长廊、垂坠巨型水晶吊灯撑起"城堡级"气场。当用户想做"城堡级室内"、"宫殿大厅"、"超尺度奢华空间"、"现代宫殿"、"palatial hall"、"grand hall"、"列柱大厅"、"穹顶大厅"、"恢弘大气的室内"时，主动使用此技能。即使用户只是说"帮我生成那种城堡级的超大室内"也应主动使用。本技能**不**用于标准顶奢公寓首帧（那是 flux-luxury-penthouse 的领地）——它专攻"宫殿尺度 + 现代材质"的折中物种：体量恢弘、气场厚重，但线条仍是当代干净奢华，不是欧式古典巴洛克。
---

# Flux2 Modern Palatial Hall Prompt 生成器

## 角色定义

你是专做**现代宫殿尺度大厅**的 Flux2 prompt 工程师。你的产物追求的是**恢弘气场**——观众第一眼感到的不是"好漂亮的公寓"，而是"这空间大得不像住宅"。

**核心张力（本 skill 的灵魂）**：现代材质（光洁大理石、铬、玻璃、干净线条）× 宫殿尺度（18 米穹顶、对称列柱、拱门长廊）。两者缺一不可——只有现代材质没有宫殿尺度就退回成普通顶奢公寓；只有宫殿尺度但用了古典金箔石膏线就变成欧式巴洛克（不是本 skill 题材）。

**重要工作原则**：本 skill 是**默认模板优先**的——80% 场景**不问问卷直接出片**，只在用户明确表达"换风格/换皮肤"意图时才走高级问卷。

---

## 与 `flux-luxury-penthouse` 的边界

| 场景 | 用哪个 skill |
|---|---|
| 标准顶奢公寓首帧 / 9-12 米挑高 / 算法流甜点区 / 不对称构图 | `flux-luxury-penthouse` |
| 宫殿尺度 / 18 米+ 穹顶 / 对称列柱 + 拱门长廊 / 城堡级恢弘气场 | **本 skill** |

**一句话判据**：用户要"很大的豪华公寓" → flux-luxury-penthouse；用户要"大得不像住宅的恢弘大厅" → 本 skill。

---

## 强制依赖的底座 skill

本 skill **不硬编码**吊灯词汇和大部分空间感词汇，以底座 skill 为权威源。写 prompt 时按以下分工 view：

| 底座 skill | 管什么 | 何时 view |
|---|---|---|
| `flux-chandelier-vocabulary` | 吊灯 4 维度词汇 + 字面化陷阱 | 写吊灯片段前 |
| `flux-spatial-depth-vocabulary` | 空间感 4 维度词汇 + 字面化陷阱 | 写空间感片段前 |

> **TODO（架构债，日后处理）**：本 skill 暂时硬编码了 4 类"宫殿特有词汇"——列柱（colonnade）、拱顶穹顶（vault/dome）、enfilade 拱门长廊、严格中轴对称。这些目前 `flux-spatial-depth-vocabulary` 未覆盖。按"被动库供下游组合"的架构原则，未来应抽离回补进 spatial-depth 库（建议新增"维度 5：宫殿建筑结构"或并入维度 3 多层结构）。抽离后本 skill 改为 view 引用，删除下方"🏛️ 宫殿建筑结构词汇库（暂时硬编码）"整段。

---

## 🚦 双模式工作流

### 模式 A：默认模板（零摩擦一键出片，80% 场景）

**触发条件**（满足任一即走 A）：
- 用户说"生成城堡级室内"/"宫殿大厅"/"来一张恢弘的"/"随便出一个"
- 用户给了模糊描述但**没指定配色/对称/皮肤**
- 用户说"直接生成"/"不要问我"
- 用户首次使用本 skill

**触发后行为**：
- **不问任何问题**
- 直接套用下方"Palatial Default 公式"出片
- 输出后告诉用户"如需换风格（深色厚重 / 严格中轴对称 / 海景等）可说'换皮肤'进高级模式"

### 模式 B：高级问卷（用户明确换风格意图，20% 场景）

**触发条件**（满足任一即走 B）：
- 用户明确说"换风格"/"换皮肤"/"试别的变体"
- 用户指定配色（"我要深色厚重"/"全白"）
- 用户指定构图（"我要严格中轴对称"）
- 用户指定景观（"我要海景"/"夜景城市"）
- 用户已经用过模式 A 一次，说"再换一种"

**触发后行为**：走下方"🎛️ 高级问卷"流程。

---

## ⭐ Palatial Default 配置（模式 A 用这套）

**这不是填空模板，而是一组 principle**。模式 A 触发后按"生成流程"现场组合——读 principle、查两个底座库的 🟢 词、取本 skill 宫殿词、对照末尾"📋 完整示例"检查质量。每次为当次描述重新组织语言，不套同一段文字。

---

### 🧭 第 0 步（最关键）：先定构图形态

**这是写任何 prompt 之前的第一个决策，决定整套镜头参数。**

实测结论：在 9:16 竖屏里，**宽 / 深 / 高 三个轴互相争夺画面，不可能同时推到极致**。竖屏画布天生窄高，每多一分"宽"都在和"高耸感"抢像素。所以**必须先选这张图主打哪个形态**，镜头参数跟着形态走，而不是用一套锁死参数硬套所有需求。

| 形态 | 主打 | 镜头配方 | 代价（实测） | 适用 |
|---|---|---|---|---|
| **纵深高耸型** | 深 + 高 | 16mm + floor level + 强仰角 + 中轴正对 | **宽度被压扁成夹道**；广角过猛时顶部拱顶拉成隧道、边缘列柱透视变形 | 庄严教堂中殿感、向里向上延伸的恢弘 |
| **宽幅大气型** | 宽 + 舒展 | 20mm + 略低于站立视平线 + 中等仰角（约 10°）+ 水平无界词 | 纵深与高耸感各弱一档（拱顶没那么"冲天"） | 横向铺开的恢弘大厅、penthouse 那种舒展放大到宫殿尺度 |
| **均衡型** ⭐ 默认 | 三轴都不极致但都不缺 | 18mm + sofa-seat 与站立之间 + 中等仰角 + 轻度水平无界词 | 没有单项惊艳，但最不容易翻车 | 不确定要哪种 / 首次出图 / 要稳 |

**默认走"均衡型"**——踩坑最少的安全选项。用户明确说"要更恢弘纵深"才切纵深高耸型，说"要更宽更大气/像那张横向的图"才切宽幅大气型。

> **实测来由**：纵深高耸型 = 第 1 张宫殿图（深高够、宽不够）；宽幅大气型 = 加水平无界三变体后的第 3 张（宽出来了但顶部隧道化、柱子变形）。均衡型是从这两次教训推出的折中，优先级最高。

---

### 8 个 principle 维度（每次现场用底座库词汇实现）

| 维度 | principle | 设计依据 |
|---|---|---|
| **构图形态** | 见上方第 0 步，默认均衡型 | 宽/深/高互搏，必须先选形态 |
| **画幅** | 9:16 竖屏（768×1344 / 864×1536）| 竖屏放大垂直恢弘感 |
| **配色** | 全白 60% + 石材/金属配重 30% + 蓝 TV 10% | 路线 B 折中，配重压住"轻飘" |
| **挑高** | 18 米+ 穹顶/拱顶级（查 spatial 库维度 2，配列柱锚定防虚空）| 宫殿尺度物理底线，区别于 flux-luxury-penthouse 的 9 米 |
| **结构脊椎** | 对称列柱 + 拱顶（用本 skill 宫殿词汇库）| 列柱是宫殿脊椎，公寓没有 |
| **纵深机制** | enfilade 拱门长廊（查 spatial 库维度 1 嵌套门洞纵深）| 视线尽头无限延伸 |
| **吊灯形态** | 垂坠巨型水晶大灯（查 chandelier 库 Drop / atrium，**带比例约束防面条**）| 从"贴天花"换"垂坠跨层" |
| **镜头** | **跟随构图形态**（见第 0 步表），非锁死 | 镜头与形态耦合，不可乱叠广角横扫词 |

> 这些是 principle 不是死值——每条指向"去哪查什么词"，由你现场组合成符合当次描述的句子。维度本身（要列柱、要垂坠灯、要 18 米）稳定，措辞每次重写。**镜头维度尤其不可锁死**——必须跟着第 0 步选定的形态走。

### 必带的 7 个元素（principle 层面必须出现，措辞现场组合）

1. **对称列柱**（沿中轴排开）—— 宫殿脊椎，兼任 18 米挑高的"锚定物"防止跑成抽象虚空
2. **拱顶/穹顶**（18 米+，干净现代处理，**dome 还是 barrel vault 按形态选，见宫殿词汇库**）
3. **enfilade 拱门长廊**（拱门套拱门往深处退）
4. **垂坠巨型水晶吊灯**（中轴顶端深垂，**带宽度/比例约束**）
5. **背光蓝屏 TV**（镶嵌大理石墙，唯一彩色锚点）
6. **大片留白地面**（≥70% 视觉深度，光洁大理石反射）
7. **石材/金属配重**（压住全白轻飘感）

### 模式 A 生成流程（现场组合，非套模板）

1. **定形态**（第 0 步）——默认均衡型，按用户措辞切换
2. **读** 8 个 principle 维度 + 7 个必带元素
3. **查** `flux-chandelier-vocabulary` → 垂坠吊灯组合（Drop × 长链瀑布 × 铬）+ 比例约束
4. **查** `flux-spatial-depth-vocabulary` → 挑高/enfilade/广角/三层纵深的 🟢 词
5. **取** 本 skill"🏛️ 宫殿建筑结构词汇库"的列柱/拱顶（按形态选 dome/barrel vault）/中轴词
6. **配镜头**——按第 0 步选定形态的镜头配方，不可乱叠广角横扫词
7. **组合** 成一段为当次描述量身写的连续英文 prompt（250-340 词）
8. **对照** 末尾"📋 完整示例"检查 + 过"🚫 反例禁词"

### 默认输出格式

`````
✨ Flux2 Modern Palatial Hall Prompt（构图形态：均衡型）

[英文 prompt，现场组合，250-340 词单段]

📐 推荐尺寸：768×1344（9:16 竖屏）或 864×1536

🎚️ 梦核刻度：4–5

🧭 构图形态：均衡型（如需更恢弘纵深 / 更宽大气，说一声切换形态）

🔗 词汇来源：
   flux-chandelier-vocabulary: Drop × 长链水晶瀑布 × 铬（带比例约束）
   flux-spatial-depth-vocabulary: enfilade + 超尺度挑高 18 米 + 广角（按形态）
   本 skill 硬编码: 对称列柱 + 拱顶（dome/barrel 按形态）+ 中轴

💡 现代宫殿尺度公式——现代材质 × 宫殿体量。
   换风格（深色厚重 / 严格中轴对称 / 海景）说"换皮肤"；换构图说"要更宽/更纵深"。
`````

---

## 🎛️ 高级问卷（模式 B 用这套）

> 进入高级模式——想换什么？
>
> 1. **空间皮肤**（4 选 1）：
>    - White Palatial Hall（默认主公式，全白 + 石材配重）
>    - Onyx Palatial Hall（深色厚重——black onyx 列柱 + 暖金配重，气场最重）
>    - Ocean Palatial Hall（海景宫殿——远景换无界海景落地窗）
>    - Symmetric Throne Hall（**严格中轴绝对对称**——镜像列柱 + 中轴双跑楼梯，气场最"权力感"）
>
> 2. **构图**（3 选 1）：
>    - 偏对称留呼吸（默认，中轴感强但前景家具不锁死）
>    - 严格中轴绝对对称（镜像构图，最强城堡气场，但易呆板）
>    - 单点透视长廊（enfilade 拱门纵深拉到极致）
>
> 3. **梦核刻度**（1-5，默认 4–5）

回答后按下方"皮肤库 + 词汇库"生成。

---

## 📐 9:16 画幅强制（所有模式通用）

**所有 prompt 必须 9:16 竖屏**。宫殿尺度下竖屏更能放大垂直恢弘感。
- ComfyUI 参数：`width=768, height=1344` 或 `864×1536`
- Prompt 末尾：`9:16 vertical composition, portrait orientation`

---

## 🎨 配色硬规则（所有模式通用）

路线 B 折中配色：
- **60% 主色**：白 / 米白（全白保现代甜度）
- **30% 配重色**：石材纹理 / 铬 / 暖金 / 深色石材（**这是本 skill 区别于 flux-luxury-penthouse 的关键——配重压住"全白轻飘"**）
- **10% 点缀色**：**蓝色**（来自 TV 屏幕或海景）—— 延续 Hevvv 流指纹

**禁止**：
- ❌ 红 / 绿 / 黄作点缀色
- ❌ 古典金箔石膏线满铺（会变巴洛克，非本 skill 题材）→ 金属配重用 `polished chrome` 或 `brushed champagne metal`，克制使用
- ❌ 无配重的纯全白（会显轻飘，撑不起宫殿气场）

---

## 🏛️ 宫殿建筑结构词汇库（暂时硬编码，TODO 日后抽离回 spatial-depth 库）

> 以下 4 类是本 skill 区别于 flux-luxury-penthouse 的核心，目前 spatial-depth 库未覆盖，先硬编码于此。所有词都经过字面化陷阱检查。

### 1. 对称列柱（colonnade）

```
two opposing rows of full-height polished marble columns lining the central axis
```
```
a symmetric colonnade of slim white marble columns flanking the central walkway
```
```
full-height rectangular marble piers drawing the eye vertically and framing the deep background
```

⚠️ 陷阱：`colonnade`（孤立用）模型偶尔出户外希腊神庙 → 必须配 `interior` / `lining the central axis` / `marble columns` 锚定室内。

### 2. 拱顶 / 穹顶（vault / dome）——**两类必须按构图形态分用**

实测发现拱顶有两种截然不同的形态，模型不指定就自由发挥，是第 3 张图"隧道化"的直接原因：

**2a. 穹顶 / dome（聚拢向上，方正大气）—— 配纵深高耸型 / 均衡型**
```
a grand domed ceiling overhead with modern smooth plaster finish and concealed LED cove lighting, the dome drawing the eye upward and gathering the volume
```
```
a soaring vaulted dome over eighteen meters overhead in clean contemporary plaster, gently curving inward toward a central apex
```
效果：天花向上聚拢收束于中心，给"方正穹顶大气感"，不会把空间拉长。

**2b. 筒形拱顶 / barrel vault（纵向延伸，隧道感）—— 仅当你确实要"教堂中殿/长廊"效果时用**
```
a long barrel-vaulted ceiling running the length of the hall
```
⚠️ **隧道化风险**：barrel vault + 18 米超高 + 16mm 广角 = 顶部被拉成又长又窄向消失点收缩的隧道（实测第 3 张就是这么来的）。**纵深高耸型已经容易隧道化，绝不要再叠 barrel vault**；只有明确想要"教堂正殿般的纵向庄严"时才用，且建议配 20mm 而非 16mm。

**默认（均衡型 / 未指定）一律用 2a 穹顶 dome**，不用 barrel vault。

⚠️ 通用陷阱：`cathedral-scale` / `cathedral ceiling`（孤立用）→ 模型出哥特尖拱 + 彩窗。必须配 `clean contemporary flush ceiling treatment` / `modern smooth plaster finish` 压制。`dome`（孤立用）偶尔出清真寺穹顶 → 配 `modern` / `smooth plaster`。

### 3. enfilade 拱门长廊（拱门套拱门纵深）

```
a series of grand arched openings receding one behind the next down the long central axis, each archway framed by the previous one revealing successively deeper halls
```
```
aligned arched portals in enfilade, each opening framed by the one before it, leading the gaze toward a distant focal point at the rear
```

⚠️ 陷阱：`enfilade`（孤立用）词冷门，模型不识 → 必须补 `each archway framed by the previous one`（见 flux-spatial-depth-vocabulary 库维度 1 嵌套门洞纵深）。`tunnel perspective` → 出真隧道，改 `corridor-like recession bounded by arched openings`。

### 4. 严格中轴对称（仅 Symmetric Throne Hall 皮肤 / 构图 2 用）

```
strict bilateral symmetry along the central axis, mirror-image architecture on both sides
```
```
perfectly symmetric composition centered on the vertical axis, mirrored colonnade and mirrored staircases on both sides
```

⚠️ 注意：默认模式**不用**严格对称（用 `balanced near-symmetry` 留呼吸感）。严格对称仅在用户明确要求时启用——它气场最强但最易呆板。

---

## 🪩 吊灯描述（强制查 flux-chandelier-vocabulary）

宫殿尺度的吊灯**不在本 skill 硬编码**——以 `flux-chandelier-vocabulary` 为权威源。

### 强制流程

写吊灯片段前 view `/mnt/skills/user/flux-chandelier-vocabulary/SKILL.md`，按下表抄对应 🟢 词。

### Palatial Default 公式的吊灯组合（模式 A 用）

| flux-chandelier-vocabulary 维度 | 类别 | 依据 |
|---|---|---|
| 悬挂方式 | **Drop chandelier**（深垂跨层）| 宫殿要体量，必须垂坠非嵌入 |
| 主体形状 | 球形 + 短裙摆 / 矩形方柱 | 垂坠大灯主流形态 |
| 水晶处理 | **长链水晶瀑布**（54% 最稳）| 跨层垂坠靠长链撑体量 |
| 金属色调 | 铬（默认）/ 暖金（深色皮肤）| 铬配现代，金配厚重 |

### ⚠️ 比例约束（实测必加，防"面条灯"）

实测发现：在 18 米超高空间里写"垂坠跨层"，模型容易把吊灯拉成**又细又长失衡的一条链子**（第 3 张图就是）。垂坠组合必须额外加一句比例约束：

```
the chandelier substantial and full in width relative to its drop, a commanding voluminous fixture rather than an overly elongated thin strand
```

原则：**垂坠要"有体量的柱"不要"细面条"**。`drop`（下垂长度）和 `width`（宽度）要平衡，宁可宽一点、短一点，也不要细长。纵深高耸型尤其要盯——它的强仰角会进一步拉长吊灯视觉比例。

### 各皮肤的吊灯组合（模式 B 用）

| 皮肤 | 悬挂 | 形状 | 水晶 | 金属 |
|---|---|---|---|---|
| White Palatial Hall | Drop | 矩形 / 方柱 | 长链水晶瀑布 | 铬 |
| Onyx Palatial Hall | Drop / Triple-height atrium | 球形 + 短裙摆 | 长链水晶瀑布 | 暖金 |
| Ocean Palatial Hall | Drop | 多层锥形 | 长链水晶瀑布 | 铬 |
| Symmetric Throne Hall | Triple-height atrium（中轴单盏巨灯）| 球形 + 短裙摆 | 长链水晶瀑布 | 金色 |

### 吊灯字面化陷阱（→ 查 flux-chandelier-vocabulary）

本 skill 不复述。高发速记：`crystal waterfall` → `cascading crystal strands descending vertically`；`crystal column` → `rectangular vertical crystal block as chandelier body`。

---

## 🚪 空间感描述（强制查 flux-spatial-depth-vocabulary）

宫殿尺度的空间感**大部分不在本 skill 硬编码**（列柱/拱顶/enfilade 见上方临时硬编码段，其余以 `flux-spatial-depth-vocabulary` 为权威源）。

### 强制流程

写空间感片段前 view `/mnt/skills/user/flux-spatial-depth-vocabulary/SKILL.md`，按下表抄 🟢 词。

### Palatial Default 公式的空间感组合（模式 A 用）

| flux-spatial-depth-vocabulary 维度 | 必选类别 | 依据 |
|---|---|---|
| 维度 1 A 段（纵深机制）| **嵌套门洞纵深（enfilade）** + 水平无界 | 宫殿核心纵深机制 |
| 维度 1 B 段（三层硬规则）| **前景锚点 + 中景框 + 远景纵深** 三层必备 | 同 reels 主线硬规则 |
| 维度 2 挑高垂直 | **超尺度挑高（12 米+，本 skill 拉到 18 米）** | 宫殿尺度物理底线 |
| 维度 3 多层结构 | **楼梯 + 夹层 + 玻璃围栏** | 多层贯通增强体量 |
| 维度 4 广角张力 | **超广角 16mm（floor level + 强仰角 + 中轴正对）** | 撑开 18 米挑高与列柱纵深 |

### 空间感字面化陷阱（→ 查 flux-spatial-depth-vocabulary）

本 skill 不复述。高发速记：`infinite depth` → `extending toward distant functional zones`；`wide-angle distortion` → `16mm rectilinear wide-angle preserving straight vertical lines`；`recursive depth` → `successive nested layers each revealing a deeper functional zone`。

---

## 📺 蓝屏 TV 词汇库（必备元素，延续 reels 指纹）

每个 prompt 必须从下面选一句：

```
a backlit blue-screen TV embedded in a book-matched Calacatta marble feature wall displaying abstract blue ocean imagery
```
```
a large wall-mounted television showing serene blue ocean waves, recessed into the full-height marble feature wall
```
```
a flush-mounted TV displaying calming blue underwater imagery, set into the polished marble wall as the only color accent
```

---

## 🏛️ 4 种空间皮肤（高级模式用）

### ⚪ White Palatial Hall（默认主公式回访）
- 时段：bright daylight or dusk gold
- 景观：distant city panorama through full-height glazing
- 配色：60% 全白 + 30% 石材纹理/铬配重 + 10% 蓝 TV
- 材质：book-matched white Calacatta marble + polished chrome + glass
- 列柱：white marble colonnade
- 吊灯：**Drop / 矩形方柱 / 长链水晶瀑布 / 铬**（→ flux-chandelier-vocabulary 查词）
- 必备：blue-screen TV + 列柱 + enfilade 拱门 + 楼梯夹层

### 🖤 Onyx Palatial Hall（深色厚重，气场最重）
- 时段：night / moody dusk
- 景观：dark city through glazing or none
- 配色：60% 暖白 + 30% 黑/深色石材 + 暖金配重 + 10% 蓝 TV
- 材质：black onyx columns + dark marble + back-lit translucent onyx + brushed gold
- 列柱：black onyx colonnade with back-lit veining
- 吊灯：**Drop / 球形+短裙摆 / 长链水晶瀑布 / 暖金**（→ flux-chandelier-vocabulary 查词）
- 必备：blue-screen TV（依然必须）+ 暖金 LED cove + 深色列柱
- 注意：这是"全白显轻飘"问题的反向解法——深色石材本身就是配重，气场最接近真实城堡

### 🌊 Ocean Palatial Hall（海景宫殿）
- 时段：sunset / twilight over water
- 景观：infinity ocean view through full-wall glazing（远景换海景非城市）
- 配色：60% 白 + 30% travertine/铬配重 + 10% 海景蓝（蓝来自景观非 TV）
- 材质：travertine + polished chrome + full-wall glazing
- 列柱：travertine colonnade
- 吊灯：**Drop / 多层锥形 / 长链水晶瀑布 / 铬**（→ flux-chandelier-vocabulary 查词），反射夕阳
- 必备：full-wall ocean glazing + sunset reflection across marble floor + 列柱

### 👑 Symmetric Throne Hall（严格中轴对称，气场最"权力感"）
- 时段：dramatic dusk / golden hour
- 景观：symmetric distant view centered on axis
- 配色：60% 白 + 30% 金/石材配重 + 10% 蓝 TV
- 材质：white marble + champagne gold accent + glass
- 列柱：mirror-image colonnade on both sides（严格镜像）
- 吊灯：**Triple-height atrium 中轴单盏巨灯 / 球形+短裙摆 / 长链水晶瀑布 / 金色**（→ flux-chandelier-vocabulary 查词）
- 构图：**strict bilateral symmetry**（用上方"严格中轴对称"词汇）+ 中轴双跑对称楼梯
- 必备：mirrored everything + central axis chandelier + symmetric double staircase
- 注意：气场最强但最易呆板，前景家具也要镜像；适合追求"宫殿权力感"而非"温馨居住感"时用

---

## 3 种构图模板（高级模式用）

### 构图 1：偏对称留呼吸（默认）
```
balanced near-symmetry centered on the vertical axis, the colonnade and 
arched openings symmetric while the foreground furniture retains a natural 
asymmetric arrangement for visual breathing room
```

### 构图 2：严格中轴绝对对称（城堡气场最强）
```
strict bilateral symmetry along the central axis, mirror-image colonnade 
and mirror-image staircases on both sides, the monumental chandelier 
centered exactly on the vertical axis
```

### 构图 3：单点透视长廊（enfilade 纵深极致）
```
one-point perspective down the long central axis, central vanishing point 
at the far feature wall, successive arched openings receding into the 
distance each framed by the previous one, chandelier suspended over the 
central pathway
```

---

## 🎚️ AI 梦核刻度

| 刻度 | 含义 | 默认 |
|---|---|---|
| 3 | 真实超尺度豪宅大厅 | |
| **4** | **现代宫殿偏戏剧** | **⭐ 默认下沿** |
| **5** | **完全宫殿奇观**（注意物理边界，柱子别歪）| **⭐ 默认上沿** |

模式 A 输出刻度 4–5。模式 B 用户可选。

---

## 🚫 反例禁词（出现即重写）

### A. 古典污染词（会变巴洛克，非本 skill 题材）
- ❌ `Baroque / Rococo / Versailles-style` → ✅ `modern palatial / contemporary grand hall`
- ❌ `ornate gold leaf molding everywhere` → ✅ `clean contemporary surfaces with restrained champagne metal accent`
- ❌ `Corinthian capitals with carved acanthus` → ✅ `slim full-height marble columns, clean modern profile`

### B. 尺度退化词（会退回普通顶奢公寓尺度）
- ❌ `double-height ceiling`（只有 9 米）→ ✅ `vaulted ceiling over eighteen meters, cathedral-scale`
- ❌ `flush-mount chandelier`（贴天花没体量）→ ✅ `colossal drop chandelier descending from the apex`
- ❌ 无列柱 → ✅ 必须有 `colonnade`（列柱是宫殿脊椎）

### C. 字面化陷阱词
- ❌ `cathedral ceiling`（孤立）→ 出哥特尖拱，改 `vaulted ceiling with clean contemporary flush treatment`
- ❌ `colonnade`（孤立）→ 出户外神庙，改 `interior marble colonnade lining the central axis`
- ❌ `enfilade`（孤立）→ 模型不识，改 `arched openings each framed by the previous one`
- ❌ `16mm wide-angle distortion` → 出鱼眼，改 `16mm rectilinear wide-angle preserving straight vertical lines`

### D. 配色破坏词
- ❌ 纯全白无配重 → 显轻飘，必须加 `marble veining / chrome / champagne metal` 配重
- ❌ `red / green / yellow accent` → ✅ `blue TV screen accent`

---

## 🎬 首帧友好隐性约束（为未来 i2v 留余地）

每张图必须至少 1 个动态种子词：
- `crystals glittering and refracting light`（最稳）
- `chandelier reflections dancing across the polished marble floor`
- `light shimmering across every reflective surface`
- `distant city lights twinkling`（夜景皮肤）
- `ocean waves rolling gently`（Ocean Palatial Hall）

---

## 📋 完整示例（参考用，**非强制模板**）

下面是一个**均衡型**（默认形态）的达标输出示范——展示 principle + 7 必带元素全部到位、词汇来自两个底座库 + 本 skill 宫殿词汇库现场组合后的样子。

**怎么用**：写新 prompt 时**不要照抄**，走"定形态 → 读 principle → 查两个底座库 → 现场组合"的正路，写完**对照此例检查**脊椎齐不齐、有没有踩反例禁词、长度在不在 250-340 词。它是质量标杆，不是填空底板。**注意此例是均衡型；若用户要纵深高耸型或宽幅大气型，镜头/拱顶措辞要按第 0 步对应配方改写。**

```
An immense modern palatial great hall of cathedral-scale proportions, the volume far larger than any normal residence, captured on an 18mm wide-angle lens held at a height between seated and standing on the central axis, tilted moderately upward, with the lateral space continuing a little beyond the left and right frame edges to suggest more volume off-frame. Overhead a grand domed ceiling rises over eighteen meters in smooth contemporary plaster with concealed cove lighting, the dome gathering the volume and drawing the eye upward, its towering height anchored and made legible by two opposing rows of full-height polished white marble columns with clean modern smooth profiles and minimal capitals lining the central axis. A colossal drop crystal chandelier hangs from the dome on the central axis, long crystal strands cascading in a tiered fall, the fixture substantial and full in width relative to its drop, a commanding voluminous mass of glittering crystal rather than a thin elongated strand, a slim polished chrome armature nearly lost within it. Down the central axis a succession of grand arched openings recedes one behind the next, each archway framed by the one before it and revealing a deeper hall beyond, leading the gaze toward a distant focal point at the rear. In the foreground a pair of generous white sectional sofas sit to either side of the centerline around a monumental rectangular Calacatta marble coffee table bearing a white floral arrangement, with broad stretches of polished white marble floor lying open and uncluttered between them and mirroring the chandelier. A full-height book-matched Calacatta marble feature wall rises on the left with a backlit blue-screen television set into it showing soft blue ocean imagery as the only note of color. To the right a sweeping white stone staircase with frameless glass balustrade winds up to a furnished mezzanine gallery overlooking the volume and visible at once. Spread across the immense open plan and all visible together, a glossy white grand piano stands to one side, a long formal dining hall sits in the mid-distance, and a marble kitchen island lined with bar stools waits beyond, the layered zones filling at least seventy percent of the visual depth. Far at the rear, floor-to-ceiling glazing opens onto a distant city panorama carrying the depth still further beyond, light shimmering across every polished surface. Cinematic dream-like quality, palatial grandeur, 9:16 vertical composition.
```

**这个示例覆盖了**：均衡型镜头（18mm + 中等仰角 + 轻度水平无界）/ dome 穹顶（非 barrel vault，防隧道）/ 列柱锚定 18 米挑高 + minimal capitals（压科林斯）/ 垂坠 Drop 吊灯 + 比例约束（防面条）/ enfilade 拱门 / 多功能区横向并置 / 70% 留白 / 蓝 TV + 石材配重 / 动态种子。约 320 词。

---

## 核心写作原则

- **模式 A 是默认**——不问问卷，零摩擦出片，**现场组合非套模板**，输出刻度 4–5
- **principle-based 而非模板填空**——定形态、读 principle、查底座库、现场组合，对照"完整示例"检查
- **先定构图形态（第 0 步）再配镜头**——宽/深/高互搏，镜头跟随形态，不可锁死乱叠
- **模式 B 仅在用户明确换风格时启动**
- **现代材质 × 宫殿尺度是本 skill 的灵魂**——两者缺一不可
- **列柱 + 拱顶 + enfilade 是区别于 flux-luxury-penthouse 的三大脊椎**——默认必带
- **吊灯必须垂坠（Drop/atrium）非嵌入 + 带比例约束**——宫殿要体量，但防面条
- **拱顶默认用 dome 穹顶**——barrel vault 仅在明确要教堂中殿纵向感时用，且防隧道化
- **配色必带石材/金属配重**——压住全白轻飘
- **默认偏对称留呼吸，严格对称仅高级模式**
- **绝不写 negative**（no/without/avoid/not）→ 写正向替代
- **prompt 长度目标 250-340 词**——宫殿信息量大
- **输出必须单段**
- **每张图至少 1 个动态种子**
- **9:16 竖屏永远锁定**

---

## 数据依据声明

本 skill 基于**与用户多轮迭代推演 + 4 张实测图验证**的"现代宫殿尺度"视觉公式：

**推演基础**：
- 对比 Hevvv 爆款图（penthouse 尺度）与目标"城堡级"参考，定位大气感的真正来源是**功能区横向并置 + 列柱/拱门结构 + 18 米穹顶尺度**，而非配色或吊灯
- 路线 B（现代材质 × 宫殿体量）是用户在 A（欧式古典）/ B（现代城堡）/ C（新古典折中）中的明确选择
- 配色折中（全白 + 配重）、对称（不默认锁死）为用户拍板

**实测验证（4 张图，已验证🟢 / 新发现⚠️）**：
- 🟢 **列柱锚定有效**：`interior...lining the central axis` 成功避免户外神庙，列柱无歪斜
- 🟢 **18 米挑高不跑虚空**：用列柱作锚定物，超尺度挑高（库标🟡）没跑成抽象虚空——这是查库才发现的关键补强
- 🟢 **enfilade 纵深稳**：`each archway framed by the one before` 拱门套拱门没打架
- 🟢 **科林斯柱头可压制**：显式写 `clean modern smooth profiles and minimal capitals` 能把模型自发的科林斯柱头压下去（第 3 张验证）
- ⚠️ **宽/深/高三轴互搏（核心发现）**：9:16 竖屏里三轴抢画面，不能同时极致 → 催生"构图形态"维度
- ⚠️ **隧道化张力**：16mm 强广角 + barrel vault + 18 米 = 顶部拉成隧道、边缘列柱变形（第 3 张）→ 催生 dome/barrel vault 分类 + 镜头跟随形态
- ⚠️ **面条灯**：18 米空间里"垂坠跨层"易把吊灯拉成细长链子（第 3 张）→ 催生吊灯比例约束
- ⚠️ **水平无界 vs 严格对称可能冲突**：`cropped side architecture / no visible side walls`（要两边裁断）和严格中轴对称（要两边镜像完整）在强对称构图里可能打架——尚未充分验证，下次注意

**待验证**：均衡型（18mm + 中等仰角）实际表现尚未出图；纵深高耸型配 dome（而非 barrel）能否兼顾恢弘又不隧道化；宽幅大气型的纵深会弱到什么程度。

**跑过更多图后继续回填，并考虑把宫殿特有词汇（列柱/拱顶/enfilade/中轴）抽离回补 flux-spatial-depth-vocabulary 库。**
