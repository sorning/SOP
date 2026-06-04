---
name: flux-chandelier-vocabulary
description: 吊灯词汇库——基于 Hevvv 主页 13 张高播放奢华室内爆款实测数据归纳 + 实证补充亚类（嵌入式方形几何、密集填充式垂直水晶等），按四维度（悬挂方式 / 主体形状 / 水晶处理 / 金属色调）提供原子词汇 + 真实出现频率 + Flux2 友好度评级 + 模型字面化陷阱清单 + 形状-透视写作原则。当 Claude 需要为任何文生图 prompt（Flux2 / SDXL / Midjourney / GPT Image 等）撰写奢华室内的吊灯描述，或被问到"吊灯怎么写"、"水晶吊灯英文"、"chandelier"、"crystal lighting"、"水晶灯 prompt"、"豪华吊灯词汇"、"嵌入式吊灯"、"flush-mount chandelier"时，调用此 skill。本 skill 是**被动参考材料**——不主动生成完整 prompt，不提供风格预设、不打包组合、不给完整英文句，只提供原子词汇供下游 prompt skill 自由组合。也可在用户直接问"吊灯有哪些类型"、"chandelier vocabulary"时主动加载。**边界**：本 skill 只管奢华室内吊灯的"形态语义"（怎么挂 / 什么形状 / 什么水晶 / 什么色调），不碰光线效果、不碰天花板、不碰梦核刻度判断、不碰具体生成场景的配置原则，也不覆盖餐厅 / 工业 / 复古 / 极简等非奢华室内主线题材。
---

# 吊灯词汇库（基于 13 张爆款实测数据）

## 定位与边界

本 skill 是**底座型被动参考材料**，与三类 skill 形成生态：

| Skill | 职责 | 和本 skill 的关系 |
|---|---|---|
| `camera-angle-vocabulary` | 摄影角度词汇 | **姐妹 skill**——视觉元素分别归口 |
| `flux-luxury-penthouse` | Reels 算法流首帧 prompt | **下游消费者**——写吊灯时 view 本 skill |
| `flux2-interior-luxury` | 杂志建筑流室内 prompt | **下游消费者**——同上 |

### ✅ 本 skill 覆盖

- **悬挂方式**：从齐顶嵌入到三层中庭深垂
- **主体形状**：球形、矩形、花篮、锥形、平板、嵌入式方形几何、巨型环形 LED 等奢华室内常见形态
- **水晶 / 材质处理**：长链瀑布、多层环、水晶板、密集填充式垂直水晶等
- **金属色调**：金、铜、铬、黑、做旧
- **写作原则**：形状名词 + 透视解释（应对"仰视广角导致的几何视觉误差"）
- **Flux2 字面化陷阱**：哪些词模型会按字面理解，怎么改
- **真实数据**：每个核心词汇标注 13 张爆款里的出现频率,新亚类标注实证次数

### ❌ 本 skill 不覆盖

- 吊灯**位置**（占画面比例 / 居中度 → 各 prompt skill 自管）
- 吊灯**光效**（投影 / 反射 / 折射 → 光线词汇范畴）
- 吊灯**梦核刻度**（真实度 vs 奇观度 → 主观判断，归各 prompt skill）
- 吊灯**风格预设**（不打包"常用组合"——留给下游自由组合）
- **完整 Flux2 英文句**——本 skill 给词汇片段，下游负责拼成句
- **非奢华室内主线题材**——餐厅、工业、复古、极简等不在覆盖范围

---

## ⚠️ 关于 Flux2 友好度评级

每个词汇标注 **Flux2 友好度**：

- 🟢 **稳**：Flux2 / SDXL 主流模型理解准确，跑出结果与描述一致
- 🟡 **需引导**：模型理解偏差或需要明确语义修饰
- 🔴 **难稳定**：模型容易跑偏，需要反复抽卡或额外约束

**重要免责**：评级基于本次 13 张爆款数据 + Flux2 实测推断，**未经大规模系统化测试**。不同模型、不同版本表现有差异。遇到不符以实际为准。

---

## 维度 1：悬挂方式

镜头看到的吊灯**距离天花板有多远**。

| 类别 | 英文词汇 | 视觉特征 | 13 张占比 | Flux2 友好度 |
|---|---|---|---|---|
| **Flush-mount** | `flush-mount` / `flush-mounted` / `ceiling-flush` | 齐顶嵌入，无下沉 | 15%（2 张）| 🟡 易被理解成普通吸顶灯 |
| **Semi-flush** | `semi-flush` / `low-profile pendant` / `close-to-ceiling` | 浅悬挂，约 30cm 下沉 | 15%（2 张）| 🟡 词较冷门 |
| **Pendant** | `pendant chandelier` / `suspended chandelier` / `hanging chandelier` | 中悬挂，60-100cm | **46%（6 张）⭐** | 🟢 模型理解最稳 |
| **Drop chandelier** | `drop chandelier` / `multi-story chandelier` / `cascading from above` | 深垂吊，跨双层 | **23%（3 张）⭐** | 🟢 跨双层指令清晰 |
| **Triple-height atrium** | `triple-height atrium chandelier` / `chandelier descending through three floors` / `grand-scale vertical chandelier spanning multiple stories` | 三层中庭跨垂，巨型 | 同主线常见（13 张未出现）| 🟡 需明确层数 |

### 写 prompt 时的提示词补强

如果选 Flush-mount / Semi-flush 这类冷门类别，建议补一个明确修饰：

- Flush-mount → 加 `embedded directly into the ceiling, no chain or rod`
- Semi-flush → 加 `suspended just below the ceiling plane, about 30cm drop`
- Triple-height atrium → 加 `chandelier extends through stairwell void, top anchored at third-floor ceiling, bottom hovering above ground-floor lounge`（明确空间结构）

---

## 维度 2：主体形状

吊灯的**整体几何轮廓**——这是观众第一眼看到的形态。

| 类别 | 英文词汇 | 视觉特征 | 13 张占比 | Flux2 友好度 |
|---|---|---|---|---|
| **球形 + 短裙摆** | `dome with crystal skirt` / `spherical chandelier with descending tier` / `rounded chandelier body with crystal fringe` | 上球下短裙 | **31%（4 张）⭐⭐** | 🟢 |
| **矩形 / 方柱** | `rectangular crystal column` / `square crystal pillar` / `vertical crystal block` | 长方体柱状 | **23%（3 张）⭐** | 🟢 |
| **Empire / 花篮** | `Empire-style basket chandelier` / `inverted basket chandelier` / `Empire crystal basket` | 倒扣花篮，古典 | 23%（3 张）| 🟡 `Empire` 词需上下文 |
| **多层锥形** | `tiered conical chandelier` / `layered cone-shaped fixture` / `stacked cone chandelier` | 多层金骨架圆锥 | 15%（2 张）| 🟢 |
| **嵌入式平板** | `flush crystal panel` / `embedded crystal plate` / `recessed light panel` | 齐顶平面 | 8%（1 张）| 🟡 需配 flush 修饰 |
| **嵌入式方形几何** | `flush-mount square-shaped chandelier embedded directly into a matching square ceiling recess` / `square chandelier sitting flush within a square ceiling cavity` / `embedded square geometric fixture aligned with ceiling recess` | 正方形/矩形几何体嵌入天花同形凹槽,有体积但贴天花,被仰视广角拍成菱形外观 | 同主线常见（实验 2/2 验证）| 🟢 **必须配"形状+透视解释"原则,见下方写作原则** |
| **巨型环形 LED** | `oversized LED ring chandelier` / `monumental circular halo fixture` / `large-scale luminous ring suspended horizontally` | 巨型单环或多环水平悬浮 | 同主线常见（13 张未出现）| 🟢 |

### 几何衍生词汇（任意主体形状都可叠加）

- `concentric tiered` — 同心层叠
- `radiating outward` — 向外辐射
- `stepped` — 阶梯式
- `cascading` — 倾泻式

---

## 维度 3：水晶 / 材质处理

吊灯的**主体材质如何呈现**——决定反光效果和视觉密度。

| 类别 | 英文词汇 | 视觉特征 | 13 张占比 | Flux2 友好度 |
|---|---|---|---|---|
| **长链水晶瀑布** | `cascading crystal strands` / `long crystal chains descending` / `crystal waterfall` / `tiered crystal cascade` | 垂直流动，长串水晶 | **54%（7 张）⭐⭐⭐** | 🟢 模型理解最稳 |
| **多层水晶环** | `tiered crystal rings` / `concentric crystal layers` / `stacked crystal tiers` / `horizontal crystal bands` | 水平嵌套，环形分层 | **31%（4 张）⭐** | 🟢 |
| **水晶板 + 短水晶** | `crystal panel with short crystal accents` / `flush crystal surface` / `embedded crystal grid` | 平面板嵌点缀 | 15%（2 张）| 🟡 |
| **密集填充式垂直水晶** | `dense vertical crystal strands filling the entire shape area` / `short crystal drops cascading densely across the full footprint` / `crystals glittering and refracting light densely across the full area` | 短而密的垂直水晶串瀑布,填满吊灯主体几何边界范围 | 同主线常见（实验 2/2 验证）| 🟢 |

### 水晶细节修饰（任意类别都可叠加）

- `faceted` — 切面（最常用）
- `teardrop` — 泪滴形
- `prismatic` — 棱镜状
- `glittering` — 闪烁
- `refracting light` — 折射光
- `catching every angle of light` — 接住每个角度的光

---

## 维度 4：金属色调

吊灯骨架、连接件、装饰条的**主色**——决定时代感与奢华质感。**限奢华室内主线常见色**。

| 色调 | 英文词汇 | 风格倾向 | 13 张占比 | Flux2 友好度 |
|---|---|---|---|---|
| **金色 / 黄铜** | `golden metal frame` / `polished brass armature` / `gilded gold finish` | 古典奢华、Empire、花篮 | **38%（5 张）⭐⭐** | 🟢 |
| **铬 / 抛光银** | `polished chrome frame` / `mirror-finish silver armature` / `nickel-plated structure` | 现代奢华、几何线条 | 23%（3 张）| 🟢 |
| **古铜 / 做旧黄铜** | `antique brass` / `aged bronze` / `patinated brass armature` | 偏古典、做旧奢华 | 15%（2 张）| 🟢 |
| **哑光黑** | `matte black metal frame` / `blackened steel armature` / `gunmetal finish` | 当代奢华、对比 | 同主线常见（13 张未出现）| 🟢 |
| **透明 / 无明显金属** | `near-invisible mounting` / `minimal metal hardware` / `crystal-dominated with hidden frame` | 极致水晶感、无骨架视觉 | 同主线常见（13 张未出现）| 🟡 易出多余结构 |

### 写 prompt 时的提示词补强

- **混搭警告**：奢华室内主线**强烈倾向单色金属**——同时写 `golden frame and chrome accents` 模型常只用其中一色，且容易出现金属色冲突。如必须混搭，明确写 `primarily golden armature with chrome detail at top crown only`。
- **透明 / 无金属**：加 `crystal mass appears suspended without visible armature` 强制隐去骨架。
- **铬 + 骨架最小化组合**(实证 2/2):写 `slim chrome armature with minimal visible metal framework` 比单独写"透明 / 无金属"更稳——保留"有骨架但不明显"的真实质感,而不是完全消失。常配合"嵌入式方形几何 + 密集填充式垂直水晶"使用。

---

## ⭐ 写作原则:形状名词 + 透视解释

**问题**:当吊灯本体是**正方形/矩形几何体**,但镜头是**仰视广角**时,模型容易"字面化"误判——把"square"渲染成"从下面看也是正方形"的扁平形状,而不是"从下面看变成菱形"的立体方形。

**实证发现**:`square chandelier appearing diamond-rotated due to upward camera angle` 这种**"几何上是 X,视觉上是 Y 因为 Z"**的写法,能让模型正确理解几何与视觉的关系,2/2 实验完美命中。

### 标准写法模板

```
[形状名词] chandelier appearing [视觉外观] due to [透视/镜头原因]
```

### 适用场景

| 场景 | 推荐写法 |
|---|---|
| 正方形/矩形吊灯被仰视广角拍 | `square chandelier appearing diamond-rotated due to upward camera angle` |
| 椭圆形吊灯被侧视镜头拍 | `oval chandelier appearing as ellipse from side-view perspective` |
| 圆形吊灯被强透视拍 | `circular chandelier appearing oval-flattened due to wide-angle distortion` |
| 几何复杂吊灯被广角扭曲 | `[shape] chandelier with [visual appearance] visible from the camera angle` |

### 不推荐的反例

| 写法 | 为什么错 |
|---|---|
| `diamond-shaped chandelier`(指本体几何) | 模型会真渲染菱形几何体,而不是"方形被仰视成菱形" |
| `square chandelier`(无透视解释) | 模型可能渲染成扁平正方形,丢失体积感 |
| `chandelier from a low angle`(无形状说明) | 几何形态不确定,模型自由发挥 |

### 配套约束

写"嵌入式方形几何 + 密集填充式垂直水晶"组合时,以下三组词必须**全部出现**(实验验证):

1. `flush-mount [shape]-shaped chandelier embedded directly into a matching [shape] ceiling recess` — 三重嵌入式锚定
2. `[shape] chandelier shape appearing [visual] due to upward camera angle` — 透视解释
3. `no chain or rod, sitting flush within the ceiling cavity` — 防垂悬

---

## ⚠️ Flux2 字面化陷阱

模型常把"形状名词"或"动作名词"按**字面**渲染成画面里的物体，而不是按你想要的语义。下面是**奢华室内吊灯描述**里高发陷阱：

| 陷阱词 | 模型常误解为 | 推荐改法 |
|---|---|---|
| `crystal waterfall` | 真的水从吊灯往下流 | → `cascading crystal strands descending vertically` |
| `crystal rain` | 真的下雨 | → `crystal teardrops suspended in mid-air pattern` |
| `crystal cascade` | 单独此词偏 OK，但配上 `falling` 会被字面化 | → 加 `static crystal cascade frozen in place` |
| `chandelier basket` | 真的菜篮子挂在天花板 | → `Empire-style basket-shaped chandelier with curved metal frame` |
| `crystal patch` | 一块补丁状物体 | → `cluster of short crystal accents` |
| `crystal column` | 大理石柱子带水晶 | → `rectangular vertical crystal block as chandelier body` |
| `chandelier apex` | 顶端冒出三角尖 | → `chandelier crown` 或直接描述顶部金属环 |
| `crystal teardrops falling` | 眼泪 / 液体下落 | → `teardrop-shaped crystal pendants hanging suspended` |
| `chandelier exploding outward` | 物理爆炸碎片 | → `chandelier with crystal strands radiating outward in fixed arrangement` |
| `crystal shower` | 真的淋浴 | → `dense vertical array of crystal pendants` |
| `Empire chandelier`（孤立用） | 模型可能渲染成法国波拿巴风格室内整套 | → `Empire-style basket chandelier with crystal skirt` 把"Empire"钉到吊灯类别上 |

### 通用避坑原则

1. **名词 + 状语 优于 单名词**：`crystal column` 模糊 → `rectangular vertical crystal block as chandelier body` 明确
2. **避免动作 / 物理状态形容词**：`exploding` / `falling` / `melting` / `pouring` 容易被字面化
3. **给"是什么"明确语义锚**：用 `as chandelier body` / `as fixture frame` / `as pendant shade` 把抽象词钉到吊灯部位上
4. **风格词不能孤立用**：`Empire` / `Art Deco` / `Baroque` 后面必须跟 `chandelier` / `basket` / `frame` 类具体物体词

---

## 📊 真实数据样本（13 张爆款分类表）

完整数据来源，方便下游 skill 验证或重新统计：

| # | 赞数 | 悬挂方式 | 主体形状 | 水晶处理 | 金属色调 | 占画面 |
|---|---|---|---|---|---|---|
| 1 | 3万 | Semi-flush | 球形+短裙 | 多层水晶环 | 金色 | 1/4 |
| 2 | 2.9万 | Pendant | 金色花篮+短裙 | 实心金属球+水晶 | 金色 | 1/4 |
| 3 | 2.9万 | Pendant | 多层金色锥形 | 长链水晶+金骨架 | 金色 | 1/3 |
| 4 | 2.6万 | Drop | 巨型矩形水晶柱 | 长链水晶瀑布(跨双层) | 铬 | 1/2 |
| 5 | 2万 | Flush | 嵌入式方塔 | 长水晶串瀑布 | 铬 | 1/3 |
| 6 | 1.8万 | Flush | 嵌入式平板 | 星空灯+短水晶 | 古铜 | 1/5 |
| 7 | 1.8万 | Drop | 矩形水晶柱 | 长链水晶瀑布 | 铬 | 1/3 |
| 8 | 1.8万 | Pendant | 菱形钻石 | 长链水晶瀑布 | 古铜 | 1/2 |
| 9 | 1.6万 | Pendant | 球形+短裙 | 多层水晶环 | 金色 | 1/3 |
| 10 | 1.5万 | Drop | 矩形水晶柱 | 长链水晶瀑布(跨双层) | 金色 | 1/2 |
| 11 | 1万 | Semi-flush | 圆形+短裙 | 多层水晶环 | 金色 | 1/4 |
| 12 | 7903 | Pendant | 金色花篮(Empire) | 长链水晶+金骨架 | 金色 | 1/4 |
| 13 | 4169 | Pendant | Empire 花篮 | 长链水晶 | 金色 | 1/3 |

**少数项备注**：第 8 张的"菱形钻石"主体、第 2 张的"实心金属球+水晶"水晶处理属于数据样本中的少数项，**未单独成类**。按需描述时直接用 `diamond-shaped crystal body` / `solid metal sphere surrounded by short crystals` 即可。

---

## 用法说明

写吊灯描述前 view 本 skill，从 4 维度各选一个类别，抄英文词汇组合。优先选 🟢 词；选 🟡/🔴 词时按各维度末尾补强修饰，或参考"Flux2 字面化陷阱"清单改写。下游 prompt skill 负责把词汇拼成连贯英文句。

---

## 数据依据声明

本 skill 词汇库和频率统计基于：

- **数据源**：Hevvv 主页 13 张高播放爆款图（4169-3万 赞，2026 年初截取）
- **题材**：奢华室内（客厅、复式空间为主）
- **画幅**：9:16 竖屏（Reels / 抖音算法流）
- **风格倾向**：算法奇观流（dream-core），非真实建筑摄影
- **补充词汇**（标注"同主线常见，13 张未出现"的项）：基于奢华室内 Reels 题材圈子的常见形态归纳，非本次 13 张样本统计
- **字面化陷阱清单**：基于 Flux2 / GPT Image / SDXL 跨模型实测观察

**适用范围**：
- ✅ 奢华室内（客厅 / 复式空间 / 大宅）的吊灯描述
- ✅ Reels / 抖音 / Stories 短视频首帧
- ✅ 杂志级建筑摄影室内（同奢华主线下）
- ❌ 餐厅 / 酒店大堂 / 剧院（题材不同，词汇未覆盖）
- ❌ 复古 / 工业 / 极简 / 自然系（题材不同，词汇未覆盖）

跑过 20+ 张更多场景图后如发现新形态或频率漂移，更新本 skill 数据样本表。
