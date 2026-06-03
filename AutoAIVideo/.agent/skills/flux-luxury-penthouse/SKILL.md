---
name: flux-luxury-penthouse
description: 将简短描述扩写为高质量的 Flux2 短视频首帧 prompt，专攻 Reels/抖音算法流的"超奢华梦核公寓"视觉公式——基于 Hevvv 主页 6 张高播放爆款实测数据归纳。当用户想做短视频首帧、Reels 风格室内、抖音奇观豪宅、算法流豪华公寓、AI 梦核空间、超现实奢华、巨型吊灯居中构图时，主动使用此技能。触发关键词：Reels 首帧、Reels 室内、短视频豪宅 prompt、抖音奢华公寓、mega luxe、algorithmic luxury、dream-core penthouse、Hevvv 风格、九宫格滑屏豪宅。即使用户只是说"帮我生成那种短视频里刷到的超豪华公寓 prompt"也应主动使用此技能。本技能**不**用于真实可建造的杂志建筑摄影——那是 flux2-interior-luxury 的领地；本技能专注超现实、视觉糖、算法流的"AI 梦核奇观"。
---

# Flux2 Reels Mega-Luxe Prompt 生成器

## 角色定义

你是专做**短视频算法流首帧**的 Flux2 prompt 工程师。你的产物是**视觉糖**——观众滑到的瞬间被吊灯/反光/纵深感钉住手指。

**重要工作原则**：本 skill 是**默认模板优先**的——80% 场景**不问问卷直接出片**，只在用户明确表达"换风格"意图时才走高级问卷。

---

## 与 `flux2-interior-luxury` 的边界

| 场景 | 用哪个 skill |
|---|---|
| 杂志大片 / 真实可建造 / 编辑级建筑摄影 | `flux2-interior-luxury` |
| Reels/抖音首帧 / 算法流奇观 / 超现实梦核 | **本 skill** |

## 强制依赖的底座 skill

本 skill **不硬编码**吊灯词汇和空间感词汇,以底座 skill 为权威源。写 prompt 时按以下分工 view:

| 底座 skill | 管什么 | 何时 view |
|---|---|---|
| `flux-chandelier-vocabulary` | 吊灯 4 维度词汇（悬挂/形状/水晶/金属色调）+ 字面化陷阱 | 写吊灯片段前 |
| `flux-spatial-depth-vocabulary` | 空间感 4 维度词汇（Z 轴纵深/挑高/多层/广角张力）+ 字面化陷阱 | 写空间感片段前 |

---

## 🚦 双模式工作流（最关键的判断）

### 模式 A：默认模板（零摩擦一键出片，80% 场景）

**触发条件**（满足任一即走 A）：
- 用户说"生成豪宅"/"Hevvv 风格"/"来一张"/"随便出一个"
- 用户给了模糊描述但**没指定皮肤/材质/景观**
- 用户说"直接生成"/"不要问我"
- 用户首次使用本 skill

**触发后行为**：
- **不问任何问题**
- 直接套用下方"Hevvv Default 公式"出片
- 输出后告诉用户"如需换风格可说'我要换皮肤'进高级模式"

### 模式 B：高级问卷（用户明确换风格意图，20% 场景）

**触发条件**（满足任一即走 B）：
- 用户明确说"换风格"/"试别的变体"/"我要 XX 皮肤"
- 用户指定具体材质（"我要全黑"/"暖金调"）
- 用户指定景观（"我要海景"/"夜景城市"）
- 用户已经用过模式 A 一次，说"再换一种"

**触发后行为**：走下方"高级问卷"流程。

---

## ⭐ Hevvv Default 公式（模式 A 用这套）

这是基于主页 6 张高播放爆款（1.5万-2万播放）实测归纳的**真实爆款公式**——所有元素都在数据里得到验证。

### 默认锁死的 8 个维度

| 维度 | 默认值 | 数据依据 |
|---|---|---|
| **画幅** | 9:16 竖屏（768×1344）| 所有爆款都竖屏 |
| **主色** | 全白（60% 占比）| 6 张里 5 张全白 |
| **副色** | 深灰/黑（30% 占比）| 6 张里 6 张都有深色家具锚定 |
| **点缀色** | 蓝色（10% 占比，来自 TV 屏幕）| 6 张里 5 张有蓝屏 TV |
| **吊灯形态** | 嵌入式水晶平吊灯 | 6 张里 5 张是嵌入式而非悬垂 |
| **天花几何** | 嵌套菱形 LED 灯带 | 6 张里 3 张菱形（冠军），2 张方形 |
| **空间结构** | 双层挑高 + 白色楼梯 + 玻璃围栏 | 6 张里 4 张有楼梯+夹层 |
| **构图** | 偏对称仰视，远景纵深 | 所有爆款共有结构 |

### 默认必带的 5 个元素

1. **背光蓝屏 TV** 镶嵌在大理石电视墙（**唯一彩色锚点**）
2. **白色 L-sectional 沙发** 偏一侧
3. **嵌入式水晶平吊灯** 居中天花
4. **远景功能区**（餐厅/厨房岛/楼梯）延伸到画面深度 60% 处
5. **嵌套菱形天花 + LED 灯带勾边**

### 默认 prompt 骨架（直接套用，不要重新发明轮子）

```
A double-height all-white luxury penthouse living room with ceilings soaring nearly nine meters, lateral space continuing beyond the left and right frame edges with cropped side architecture suggesting larger volume beyond, shot with a gentle 20mm wide-angle perspective at sofa-seat height with a 10-degree upward tilt, subtle edge stretch from the wide-angle field of view. A monumental flush-mount square-shaped chandelier embedded directly into a matching square ceiling recess, no chain or rod, the square chandelier shape appearing diamond-rotated due to the upward camera angle, dense vertical crystal strands filling the entire square area with short crystal drops cascading just below the ceiling plane, slim chrome armature with minimal visible metal framework, crystals glittering and refracting light densely across the full square footprint. A nested diamond-pattern ceiling traces the outer edges around the central square recess, LED cove lighting outlining each tier. A large white L-sectional sofa serves as the dominant foreground anchor in the lower-left quadrant, paired with an oversized rectangular marble coffee table holding a hydrangea arrangement. A backlit blue-screen TV embedded in a Calacatta marble feature wall acts as the mid-ground architectural framing element, separating foreground from background. A white curved staircase with frameless glass balustrade rises on the right, leading to a mezzanine gallery above. The dining zone and the kitchen island recede into the deep background through successive layered framing each revealing the next deeper space, with a distant view continuing into a further beyond, occupying at least 60% of the visual depth with clear separation between foreground anchor, mid-ground framing, and deep-background functional zones. Polished white marble flooring reflects every light source, chandelier reflections dancing across the surface. Cinematic dream-like quality, 9:16 vertical composition.
```

**约 280 词,单段输出,可直接复制使用**。每次基于具体用户描述微调（比如换个景观远景、换楼梯位置）,但**8 大维度不允许变动**。本版默认吊灯升级为"嵌入式方形几何 + 密集填充式垂直水晶 + 铬+骨架最小化"组合(实验 2/2 验证)——这是 Hevvv 流梦核刻度 4 的标准吊灯形态。空间感保留 A+C 无界强化(`lateral space continuing beyond... cropped side architecture` + `successive layered framing... further beyond`)。蓝色仅来自 TV(60-30-10 配色硬规则)。**输出统一为单段,不分段**。

### 默认输出格式

````
✨ Flux2 Reels Mega-Luxe Prompt（默认模板）

[英文 prompt，基于骨架微调，约 110-120 词]

📐 推荐尺寸：768×1344（9:16 竖屏）或 864×1536

🎚️ 梦核刻度：4

💡 这是 Hevvv 流默认公式——基于主页 6 张高播放爆款数据。
   如需换风格（深色调 / 海景 / 卧室等），说"换皮肤"进入高级模式。
````

---

## 🎛️ 高级问卷（模式 B 用这套）

只在用户明确换风格时启动。

### 问卷三件套

> 进入高级模式——想换什么？
>
> 1. **空间皮肤**（5 选 1）：
>    - All-White Penthouse（默认主公式，回到这个意义不大除非要 reset）
>    - White Cathedral with Mezzanine（白色双层 + 楼梯戏剧化）
>    - Black Onyx Lounge（深灰/黑色冷调，小众戏剧选项）
>    - Ocean Vista Suite（海景落地窗 + 自然蓝点缀）
>    - Crystal Apex Bedroom（卧室专属，吊灯压床头）
>
> 2. **构图**（3 选 1）：
>    - 偏对称仰视（默认，单层简单客厅）
>    - 仰视吊灯主角（吊灯极致放大）
>    - 单点透视走廊（长轴空间用）
>
> 3. **梦核刻度**（1-5，默认 4）

回答后按下方"皮肤库 + 构图模板 + 词汇库"生成。

---

## 📐 9:16 画幅强制（所有模式通用）

**所有 prompt 必须 9:16 竖屏**。这是公式的物理基础，不可变。

**实现**：
- ComfyUI 参数：`width=768, height=1344` 或 `864×1536`
- Prompt 末尾：`9:16 vertical composition, portrait orientation, mobile aspect ratio`

---

## 🎨 60-30-10 配色硬规则（所有模式通用）

每张图必须遵守：
- **60% 主色**：白 / 米 / 暖金（**白色优先**——6 张爆款里 5 张全白）
- **30% 副色**：黑 / 深灰（家具锚定）
- **10% 点缀色**：**蓝色**（来自 TV 屏幕或海景）—— **几乎是 Hevvv 流的指纹**

**禁止**：
- ❌ 红色、绿色、黄色作为点缀色
- ❌ 主色暖木材（除非 Snow 类皮肤，但已删除）
- ❌ 无彩色点缀（蓝屏 TV 不能省略）

---

## 🏗️ 必备元素清单（所有模式通用）

每张图必须包含——

### 🔴 硬性 7 件套（缺一不可）

1. **巨型吊灯**（占画面上 1/3-1/2,**优先嵌入式水晶平吊灯**）—— 查 flux-chandelier-vocabulary
2. **嵌套几何天花**（**菱形优先**,方形次之,至少 2 层 LED 灯带勾边）
3. **背光蓝屏 TV**（镶嵌大理石墙,蓝色画面,唯一彩色锚点）
4. **极致挑高**（至少 9 米,12 米更佳,双层挑高最强）—— 查 flux-spatial-depth-vocabulary 维度 2
5. **高光泽地面**（polished marble,必须反射吊灯）
6. **Z 轴三层硬规则**（前景锚点 + 中景框 + 远景纵深）—— 查 flux-spatial-depth-vocabulary 维度 1 B 段
   - 前景锚点（沙发 / 茶几占下半幅 30-40%）
   - 中景框（TV 墙 / 柱列 占中段 30-40%）
   - 远景纵深（餐厅 / 厨房 / 楼梯 延伸至画面深度 ≥60%）
7. **微仰广角镜头**（20mm + sofa-seat height + 10° 上仰,带 `gentle subtle edge stretch`）—— 查 flux-spatial-depth-vocabulary 维度 4

### 🟡 强烈推荐（双层皮肤必有）

8. **白色楼梯**（弧形 或 直角，画面左侧或右侧 1/4 位置）
9. **玻璃围栏夹层**（楼梯通往二楼，二楼围栏可反射吊灯）
10. **白色 L-sectional 沙发**（偏一侧，下半幅锚定）

### 🟢 加分项（按皮肤决定）

11. **窗外景观**（海景/城市夜景，仅 Ocean Vista 必有）
12. **花艺**（白色绣球/苍兰，茶几正中）
13. **大理石电视墙**（Calacatta 白纹理 或 Nero 黑纹理）

---

## 🪩 吊灯描述（强制查 flux-chandelier-vocabulary）

本顶奢公寓公式的吊灯词汇**不在本 skill 里硬编码**——以 `flux-chandelier-vocabulary` skill 为权威源。

### 强制流程

写任何 prompt 的吊灯片段前，view `/mnt/skills/user/flux-chandelier-vocabulary/SKILL.md`，按下表的 4 维度类别去抄对应 🟢 英文词汇，再拼成 prompt 片段。

### Hevvv Default 公式的吊灯组合（模式 A 用)

| flux-chandelier-vocabulary 维度 | 类别 | 数据依据 |
|---|---|---|
| 悬挂方式 | **Flush-mount** | 5/6 嵌入式爆款 + 实验 2/2 验证 |
| 主体形状 | **嵌入式方形几何** ⭐ | **实验 2/2 验证,梦核刻度 4 标准形态** |
| 水晶处理 | **密集填充式垂直水晶** ⭐ | **实验 2/2 验证** |
| 金属色调 | **铬 + 骨架最小化组合** ⭐ | **实验 2/2 验证** |

**重要写作约束**(必须配合使用,见 flux-chandelier-vocabulary 的"⭐ 写作原则:形状名词 + 透视解释")：

1. `flush-mount square-shaped chandelier embedded directly into a matching square ceiling recess`
2. `the square chandelier shape appearing diamond-rotated due to the upward camera angle`
3. `no chain or rod, sitting flush within the ceiling cavity`
4. `slim chrome armature with minimal visible metal framework`

### 各皮肤的吊灯组合（模式 B 用）

| 皮肤 | 悬挂 | 形状 | 水晶 | 金属 |
|---|---|---|---|---|
| All-White Penthouse | Flush-mount | **嵌入式方形几何** ⭐ | **密集填充式垂直水晶** ⭐ | **铬 + 骨架最小化** ⭐ |
| White Cathedral | Drop / Triple-height atrium | 球形 + 短裙摆 | 长链水晶瀑布 | 金色 |
| Black Onyx Lounge | Pendant | 球形 + 短裙摆 | 长链水晶瀑布 | 哑光黑 |
| Ocean Vista Suite | Pendant | 多层锥形 | 长链水晶瀑布 | 铬 |
| Crystal Apex Bedroom | Drop | 矩形 / 方柱 | 长链水晶瀑布 | 金色 |

### 吊灯字面化陷阱（→ 查 flux-chandelier-vocabulary）

凡涉及吊灯描述，必须参考 flux-chandelier-vocabulary 的"⚠️ Flux2 字面化陷阱"清单，本 skill 不复述。高发速记：

- `crystal waterfall` → 模型出真的水流，改 `cascading crystal strands descending vertically`
- `chandelier basket` → 出真的菜篮子，改 `Empire-style basket-shaped chandelier with curved metal frame`
- `crystal column` → 出大理石柱子带水晶，改 `rectangular vertical crystal block as chandelier body`
- `Empire chandelier`（孤立用）→ 出整套波拿巴风室内，改 `Empire-style basket chandelier with crystal skirt`

---

## 🔲 天花词汇库（按数据重排）

### ⭐ 几何模式 A：嵌套菱形（**冠军，3/6 爆款用**）

```
nested diamond-pattern ceiling with three concentric diamond layers 
stepping inward toward the central chandelier
```

```
diamond-pattern ceiling grid with continuous LED inset lighting 
tracing every edge, perfectly symmetric across both axes
```

### 🥈 几何模式 B：嵌套方形（**亚军，2/6 爆款用**）

```
nested square soffits stepping inward toward the central chandelier, 
warm-white LED cove lighting tracing every tier
```

```
concentric tiered square recess radiating outward, each layer 
backlit with hairline LED perimeter
```

### LED 处理（通用）

```
continuous warm-white LED cove lighting tracing every architectural edge
```

```
hairline luminous perimeter outlining each tier of the soffit
```

### 进阶（刻度 5 用）

```
star-field fiber optic ceiling embedded in the central diamond panel
```

```
mirror-clad ceiling reflecting the entire room below
```

---

## 📺 蓝屏 TV 词汇库（必备元素）

每个 prompt 必须从下面选一句：

```
a large backlit TV screen embedded in a Calacatta marble feature 
wall displaying abstract blue ocean imagery
```

```
a wall-mounted television showing serene blue ocean waves, 
recessed into the marble accent wall mid-ground
```

```
a backlit blue-screen television set into the polished marble wall, 
displaying an abstract blue waveform pattern
```

```
a flush-mounted TV displaying calming blue underwater imagery, 
embedded in book-matched marble paneling
```

---

## 🪜 楼梯 + 夹层词汇库（双层皮肤必有）

```
a white curved staircase with glass balustrade rises on the right, 
leading to a mezzanine gallery above
```

```
sweeping white marble staircase along the left wall, glass railing 
ascending to the second-floor gallery
```

```
mezzanine gallery above with glass balustrade overlooking the 
double-height living volume, reflecting the chandelier
```

---

## 🚪 空间感描述（强制查 flux-spatial-depth-vocabulary）

本顶奢公寓公式的空间感词汇**不在本 skill 里硬编码**——以 `flux-spatial-depth-vocabulary` skill 为权威源。

### 强制流程

写任何 prompt 的空间感片段前,view `/mnt/skills/user/flux-spatial-depth-vocabulary/SKILL.md`,按下表的 4 维度类别去抄对应 🟢 英文词汇,再拼成 prompt 片段。

### Hevvv Default 公式的空间感组合（模式 A 用）

| flux-spatial-depth-vocabulary 维度 | 必选类别 | 数据依据 |
|---|---|---|
| 维度 1 A 段（纵深机制）| **层叠纵深** 或 **廊道纵深** | 6/6 爆款远景延伸 ≥60% |
| 维度 1 B 段（三层硬规则）| **前景锚点 + 中景框 + 远景纵深** 三层必备 | 所有 Hevvv 爆款都有三层 |
| 维度 2 挑高垂直 | **极致挑高（9-12 米）** | 6/6 爆款双层挑高 |
| 维度 3 多层结构 | **楼梯主角 + 夹层 + 玻璃围栏** | 4/6 爆款有楼梯+夹层 |
| 维度 4 广角张力 | **微仰视广角**（20mm + sofa-seat height + 10° 上仰）| 6/6 爆款共有镜头特征 |

### 各皮肤的空间感组合（模式 B 用)

| 皮肤 | 纵深机制 | 挑高 | 多层 | 镜头 |
|---|---|---|---|---|
| All-White Penthouse | 层叠纵深 | 极致挑高 9 米 | 楼梯主角 + 夹层 | 微仰视 20mm |
| White Cathedral | 单点纵深 | 超尺度挑高 12 米+ | 楼梯主角戏剧化 + 多层贯通 | 微仰视 20mm |
| Black Onyx Lounge | 廊道纵深 | 极致挑高 9 米 | 楼梯副角 + 夹层 | 微仰视 20mm |
| Ocean Vista Suite | 窗景纵深 | 极致挑高 9 米 | 楼梯副角 | 微仰视 20mm（朝向海景）|
| Crystal Apex Bedroom | 单点纵深（卧室对称例外）| 极致挑高 9 米 | 不必有楼梯 | 仰视吊灯主角 |

### 空间感字面化陷阱（→ 查 flux-spatial-depth-vocabulary）

凡涉及空间感描述,必须参考 flux-spatial-depth-vocabulary 的"⚠️ Flux2 字面化陷阱"清单,本 skill 不复述。高发速记:

- `infinite depth` → 模型出无限远地平线,改 `extending toward distant functional zones`
- `wide-angle distortion` → 出鱼眼,改 `gentle 20mm wide-angle perspective with subtle edge stretch`
- `forced perspective` → 戏剧化变形,改 `slight low-angle 20mm perspective with natural depth`
- `spatial layering`（孤立用）→ 抽象几何图层,改 `clear separation between foreground anchor, mid-ground framing element, and deep-background functional zone`

---

## 5 种空间皮肤（高级模式用）

### ⚪ All-White Penthouse（默认主公式回访）
- 时段：bright daylight or dusk gold
- 景观：optional city skyline / clerestory glazing
- 色调：60% 全白 + 30% 深灰 + 10% 蓝 TV
- 材质：book-matched white Calacatta marble + glossy white surfaces
- 吊灯：**Flush-mount / 嵌入式方形几何 / 密集填充式垂直水晶 / 铬+骨架最小化** ⭐(实证 2/2,梦核刻度 4 标准形态,→ flux-chandelier-vocabulary 查词 + 必须配"形状-透视解释"原则)
- 必备：blue-screen TV + white staircase + mezzanine

### 🤍 White Cathedral with Mezzanine
- 时段：bright daylight pouring in
- 景观：clerestory windows or skylight
- 色调：all white + cream accent + 蓝 TV 点缀
- 材质：book-matched white Calacatta marble everywhere
- 吊灯：Drop / Triple-height atrium / 球形+短裙摆 / 长链水晶瀑布 / 金色，cathedral-scale（→ flux-chandelier-vocabulary 查词）
- 必备：grand white staircase（戏剧化为主角）+ mezzanine + 至少 3 个挑高层

### 🖤 Black Onyx Lounge
- 时段：night, no exterior or moody city
- 景观：none or dark city through glazing
- 色调：60% 深灰 + 30% 黑 + 10% 蓝 TV（**反转白色公式**）
- 材质：dark grey marble + back-lit translucent onyx + smoked mirror + dark chrome
- 吊灯：Pendant / 球形+短裙摆 / 长链水晶瀑布 / 哑光黑（→ flux-chandelier-vocabulary 查词）
- 必备：blue-screen TV（依然必须）+ dark grey sectional + amber LED cove

### 🌊 Ocean Vista Suite
- 时段：sunset or twilight over water
- 景观：infinity ocean view through full-wall glazing
- 色调：60% 白 + 30% 暖金 + 10% 海景蓝（**蓝色来自景观非 TV**）
- 材质：travertine + polished chrome + glass
- 吊灯：Pendant / 多层锥形 / 长链水晶瀑布 / 铬（→ flux-chandelier-vocabulary 查词），反射夕阳
- 必备：full-wall ocean glazing + sunset reflection across marble floor

### 🛏️ Crystal Apex Bedroom
- 时段：dusk or night
- 景观：optional city / ocean / mountains
- 色调：warm intimate luxury，仍带 10% 蓝色点缀（窗外或背景画）
- 材质：upholstered headboard wall + polished marble accent + mirror nightstands
- 吊灯：Drop / 矩形+方柱 / 长链水晶瀑布 / 金色（→ flux-chandelier-vocabulary 查词），directly above the bed centerline，**对称压床头**
- 必备：platform bed centered on axis（**卧室是对称例外**，床本身是强对称主体）

---

## 3 种构图模板（高级模式用）

### 构图 1：偏对称仰视（默认）

镜头位置：约沙发坐高，微仰约 10°
镜头：20mm wide
关键句：
```
shot from a slight low angle with a 20mm wide-angle lens at 
sofa-seat height with approximately 10-degree upward tilt, the 
symmetric nested ceiling geometry filling the upper half while 
the asymmetric foreground furniture anchors the lower-left quadrant
```

### 构图 2：仰视吊灯主角（戏剧最强）

关键句：
```
extreme slight low-angle perspective looking upward toward the 
monumental chandelier, vertigo effect emphasizing the soaring 
ceiling height, the fixture filling the upper half of the frame
```

### 构图 3：单点透视走廊（纵深最强）

关键句：
```
one-point perspective down the long axis of the space, central 
vanishing point at the far feature wall, layered architectural 
frames receding into the distance, chandelier suspended over 
the central pathway
```

---

## 🎚️ AI 梦核刻度

| 刻度 | 含义 | 默认 |
|---|---|---|
| 1 | 接近真实顶奢 | |
| 2 | 顶奢偏戏剧 | |
| 3 | 算法甜点区下沿 | |
| **4** | **Hevvv 主区间** | **⭐ 默认** |
| 5 | 完全奇观（注意物理边界）| |

模式 A 永远输出刻度 4。模式 B 用户可选。

---

## 🚫 反例禁词（出现即重写）

### A. 杂志建筑流污染词
- ❌ `honed Nero Marquina` → ✅ `polished mirror-finish marble`
- ❌ `tilt-shift, perspective correction` → ✅ `slight low-angle wide lens`
- ❌ `Phase One XF IQ4` → ✅ `cinematic dream-like quality`
- ❌ `single sculptural pendant` → ✅ Hevvv 默认嵌入式水晶（按"吊灯组合表"+ flux-chandelier-vocabulary 查词）
- ❌ `perfectly bilateral symmetric composition` → ✅ `asymmetric-balanced composition`

### B. 首帧杀手词（i2v 友好）
- ❌ `frozen, static, motionless` → ✅ `glittering, sparkling, catching light`

### C. 配色破坏词
- ❌ `red accent, yellow accent, green accent` → ✅ `blue TV screen accent`
- ❌ `warm wood floor`（除 Snow 皮肤外，已删除）→ ✅ `polished white marble floor`
- ❌ `no TV mentioned`（蓝屏 TV 不能省略）→ ✅ 必须从 TV 词汇库选一句

### D. 天花几何错配
- ❌ `concentric circle ceiling`（实测无爆款）→ ✅ `nested diamond ceiling`
- ❌ `hexagonal coffered ceiling`（实测无爆款）→ ✅ `nested diamond` 或 `nested square`

### E. 吊灯相关禁词
凡吊灯描述的字面化陷阱（`crystal waterfall` / `chandelier basket` / `crystal column` / `Empire chandelier` 孤立用等），统一查 flux-chandelier-vocabulary 的"⚠️ Flux2 字面化陷阱"清单，本 skill 不复述。

---

## 🎬 首帧友好隐性约束（为未来 i2v 留余地）

每张图必须至少包含 1 个**动态种子**词：
- `crystals glittering and refracting light`（最稳，所有皮肤通用）
- `chandelier reflections dancing across the polished marble floor`
- `light shimmering across every reflective surface`
- `distant city lights twinkling`（夜景皮肤）
- `ocean waves rolling gently`（Ocean Vista）

---

## 完整工作流示例

### 示例 1：模式 A 触发（最常见）

**用户输入**："帮我生成一张豪宅图"

**Claude 反应**：直接出片，**不问任何问题**。

**输出**：

````
✨ Flux2 Reels Mega-Luxe Prompt（默认模板）

A double-height all-white luxury penthouse living room with ceilings soaring nearly nine meters, lateral space continuing beyond the left and right frame edges with cropped side architecture suggesting larger volume beyond, shot with a gentle 20mm wide-angle perspective at sofa-seat height with a 10-degree upward tilt, subtle edge stretch from the wide-angle field of view. A monumental flush-mount square-shaped chandelier embedded directly into a matching square ceiling recess, no chain or rod, the square chandelier shape appearing diamond-rotated due to the upward camera angle, dense vertical crystal strands filling the entire square area with short crystal drops cascading just below the ceiling plane, slim chrome armature with minimal visible metal framework, crystals glittering and refracting light densely across the full square footprint. A nested diamond-pattern ceiling traces the outer edges around the central square recess, LED cove lighting outlining each tier. A large white L-sectional sofa serves as the dominant foreground anchor in the lower-left quadrant, paired with an oversized rectangular marble coffee table holding a white hydrangea arrangement. A backlit blue-screen TV embedded in a Calacatta marble feature wall acts as the mid-ground architectural framing element, displaying abstract blue ocean imagery. A white curved staircase with frameless glass balustrade rises on the right, leading to a mezzanine gallery overlooking the space. The dining zone and the kitchen island recede into the deep background through successive layered framing each revealing the next deeper space, with a distant view continuing into a further beyond, occupying at least 60% of the visual depth with clear separation between foreground anchor, mid-ground framing, and deep-background functional zones. Polished white marble flooring reflects every light source, chandelier reflections dancing across the surface. Cinematic dream-like quality, 9:16 vertical composition.

📐 推荐尺寸：768×1344（9:16 竖屏）或 864×1536

🎚️ 梦核刻度：4(嵌入式方形吊灯 = 梦核刻度 4 的标准形态)

🔗 词汇来源：
   flux-chandelier-vocabulary: Flush-mount × 嵌入式方形几何 × 密集填充式垂直水晶 × 铬+骨架最小化(实证 2/2)
   flux-spatial-depth-vocabulary: 层叠纵深 + A 水平无界 + C 4 层递归 + Z 轴三层

💡 这是 Hevvv 流默认公式——基于主页 6 张爆款数据 + 嵌入式方形吊灯实证补充。
   默认吊灯组合升级为"嵌入式方形几何 + 密集填充式垂直水晶 + 铬+骨架最小化"
   (实验 2/2 验证)。如需换风格(深色调 / 海景 / 卧室等),说"换皮肤"进入高级模式。
````

### 示例 2：模式 B 触发

**用户输入**："给我来个 Black Onyx 风格的"

**Claude 反应**：识别到指定皮肤，进入高级模式。

**输出**：

````
✨ Flux2 Reels Mega-Luxe Prompt（高级模式 / Black Onyx）

A double-height luxury penthouse lounge with ceilings soaring nearly nine meters, lateral space continuing beyond the left and right frame edges with cropped side architecture suggesting larger volume beyond, shot with a gentle 20mm wide-angle perspective at sofa-seat height with corridor-like recession bounded by architectural frames. A monumental pendant crystal chandelier with cascading crystal strands descending vertically from a matte black metal frame, crystals glittering against deep dark backdrop. Back-lit translucent onyx wall panels glow amber from within, flanking a polished dark grey marble floor that mirrors the chandelier. A large dark grey velvet sectional serves as the dominant foreground anchor in the lower-left quadrant, with an oversized black marble coffee table holding a crystal decoration. A backlit blue-screen TV embedded in the dark Nero Marquina marble feature wall acts as the mid-ground architectural framing element, displaying abstract blue waveform imagery as the only color accent. Warm amber LED cove lighting traces every ceiling tier and wall edge. The dining zone and the kitchen island recede into the deep background through successive layered framing each revealing the next deeper space, with a distant view continuing into a further beyond, occupying at least 60% of the visual depth with clear separation between foreground anchor, mid-ground framing, and deep-background functional zones. Cinematic dream-like quality, 9:16 vertical composition.

📐 推荐尺寸：768×1344（9:16 竖屏）

🎚️ 梦核刻度：4

🔗 词汇来源：flux-chandelier-vocabulary（Pendant × 长链瀑布 × 哑光黑）
            flux-spatial-depth-vocabulary（廊道纵深 + A 水平无界 + C 4 层递归 + Z 轴三层）

💡 Black Onyx 皮肤:60% 深灰 + 30% 黑 + 10% 蓝 TV(反转白色公式);
   Black Onyx 不用默认嵌入式方形吊灯(那是 All-White 的标志),改 Pendant + 长链
   瀑布 + 哑光黑制造冷峻反差感。如需再调整,告诉我。
````

---

## 核心写作原则

- **模式 A 是默认**——不问问卷，零摩擦出片
- **模式 B 仅在用户明确换风格时启动**
- **8 大维度在模式 A 全锁死**——基于真实爆款数据
- **默认吊灯组合**(模式 A):**嵌入式方形几何 + 密集填充式垂直水晶 + 铬+骨架最小化**(实验 2/2 验证),必须配"形状-透视解释"原则
- **60-30-10 配色 + 蓝屏 TV 是所有模式的硬规则**
- **绝不写 negative**（no/without/avoid/not）→ 写正向替代
- **prompt 长度目标 180-280 词**——空间感强化后比之前稍长,但仍在 Flux2 甜点区
- **输出必须单段,不分段**——所有 prompt 主体合并为一个连续段落,不在中间换行/空行
- **每张图至少 1 个动态种子**——为未来 i2v 留余地
- **9:16 竖屏永远锁定**

---

## 数据依据声明

本 skill 的所有默认值和优先级**基于 Hevvv 主页 6 张实测爆款**（1.5万-2万播放区间）归纳 + **嵌入式方形吊灯亚类实验补充**：

- 5/6 全白主调 → 默认皮肤定为 All-White
- 5/6 嵌入式吊灯而非悬垂 → 形态定为 Flush-mount
- 5/6 有背光蓝屏 TV → 必备元素
- 3/6 嵌套菱形天花（冠军）→ 默认几何
- 4/6 双层楼梯结构 → 双层皮肤强制
- 6/6 远景延伸 60% 以上 → 纵深硬规则
- **嵌入式方形几何吊灯 + 密集填充式垂直水晶 + 铬+骨架最小化(实证 2/2)** → 升级为模式 A 默认吊灯组合
- A 水平无界 + C 4 层递归(实证 1/1 单 prompt 跑卡) → 空间感默认强化

跑过 20+ 张图后如发现新规律,更新本 skill 数据依据部分。
