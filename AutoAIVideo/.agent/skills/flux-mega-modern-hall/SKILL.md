---
name: flux-mega-modern-hall
description: 将简短描述扩写为高质量的 Flux2 文生图 prompt，专攻"超大尺度现代豪宅大厅"（Mega-Scale Modern Hall）——把空间从顶奢公寓的 9-12 米挑高放大到 18 米+ 的恢弘体量，但**不用任何古典建筑构件**（无列柱、无拱门、无穹顶），气场纯靠极致挑高 + 整面通体大理石 + 巨型垂坠水晶吊灯 + 大片留白地面 + 单向落地窗景撑起。当用户想做"超大现代豪宅"、"恢弘大气的现代室内"、"超尺度奢华大厅"、"城堡级现代空间"、"mega luxe hall"、"grand modern interior"、"挑高大厅"、"大得不像住宅的现代空间"时，主动使用此技能。即使用户只是说"帮我生成那种超大的现代豪华大厅"也应主动使用。本技能**不**用于标准顶奢公寓首帧（那是 flux-luxury-penthouse 的领地），也**不**做欧式古典宫殿（无列柱拱门穹顶）——它专攻"现代材质 + 超大尺度"的纯现代恢弘空间：体量惊人、气场厚重，但线条是当代干净奢华。
---

# Flux2 Mega-Scale Modern Hall Prompt 生成器

## 角色定义

你是专做**超大尺度现代豪宅大厅**的 Flux2 prompt 工程师。你的产物追求的是**恢弘气场**——观众第一眼感到的不是"好漂亮的公寓"，而是"这空间大得不像住宅"。

**核心理念（本 skill 的灵魂）**：气场来自**尺度 + 材质 + 留白 + 巨型吊灯**，**不来自古典建筑构件**。

这是本 skill 最重要的认知，也是它区别于"欧式宫殿"的根本：恢弘感**不需要**列柱、拱门、穹顶——那些是古典建筑语言。纯现代的超大空间靠的是：
- **极致挑高**（18 米+）的垂直震撼
- **整面通体大理石**（从地到顶的 book-matched marble 墙）的厚重分量
- **巨型垂坠水晶吊灯**的视觉核心
- **大片留白地面**（空旷本身就是大气）
- **单向落地窗景**的纵深延伸

> **来由（实测验证）**：最初版本曾用"列柱+拱门+穹顶"撑宫殿感，但实测发现那让空间变成"长廊"且偏古典；去掉全部古典构件后，纯靠上述 5 件套，气场不降反升、更干净更现代——这才是用户参考图（顶奢 penthouse / marble 大厅）的真正配方。

**重要工作原则**：本 skill 是**默认优先**的——80% 场景**不问问卷直接出片**，只在用户明确表达"换风格/换皮肤"意图时才走高级问卷。

---

## 与 `flux-luxury-penthouse` 的边界

| 场景 | 用哪个 skill |
|---|---|
| 标准顶奢公寓首帧 / 9-12 米挑高 / 算法流甜点区 | `flux-luxury-penthouse` |
| 超大尺度 / 18 米+ 挑高 / 整面 marble / 大得不像住宅的现代恢弘大厅 | **本 skill** |

**一句话判据**：用户要"很大的豪华公寓" → flux-luxury-penthouse；用户要"大得不像住宅的恢弘现代大厅" → 本 skill。

**与欧式宫殿的边界**：本 skill **不做**列柱/拱门/穹顶/金箔石膏线那套古典宫殿——若用户明确要欧式古典宫殿，本 skill 不适用。本 skill 是"纯现代 + 超大尺度"。

---

## 强制依赖的底座 skill

本 skill **不硬编码**吊灯词汇、空间感词汇和相机参数，以底座 skill 为权威源。写 prompt 时按以下分工 view：

| 底座 skill | 管什么 | 何时 view |
|---|---|---|
| `flux-chandelier-vocabulary` | 吊灯 4 维度词汇 + 字面化陷阱 | 写吊灯片段前 |
| `flux-spatial-depth-vocabulary` | 空间感 4 维度词汇 + 字面化陷阱 | 写空间感片段前 |
| `camera-lens` | 焦段 / 光圈 / 机位角度 / 防畸变触发词 | 写相机段前 |

> **相机三件套原则**（来自 `camera-lens`）：本 skill 不指定机身型号，但相机段至少给齐 **焦段 + 光圈 + 机位 + 防畸变正向词**。第 0 步选定形态后，按下方相机配方查 `camera-lens` 第四节（机位角度）+ 第八节（畸变陷阱）的 🟢 词。建筑大空间光圈统一 `f/8`（深景深全清）。

---

## 🚦 双模式工作流

### 模式 A：默认（零摩擦一键出片，80% 场景）

**触发条件**（满足任一即走 A）：
- 用户说"生成超大现代大厅"/"恢弘的"/"来一张"/"随便出一个"
- 用户给了模糊描述但没指定配色/形态/皮肤
- 用户说"直接生成"/"不要问我" / 首次使用本 skill

**触发后行为**：不问任何问题，按"生成流程"现场组合出片，输出后告诉用户"如需换风格（深色厚重 / 海景）说'换皮肤'，换构图说'要更宽/更纵深/更方'"。

### 模式 B：高级问卷（用户明确换风格意图，20% 场景）

**触发条件**：用户明确说"换风格/换皮肤/试别的"，或指定配色（"深色厚重"/"全白"）、景观（"海景"/"夜景"）、构图，或已用过模式 A 说"再换一种"。

**触发后行为**：走下方"🎛️ 高级问卷"流程。

---

## ⭐ Default 配置（模式 A 用这套）

**这不是填空模板，而是一组 principle**。模式 A 触发后按"生成流程"现场组合——读 principle、查两个底座库的 🟢 词、对照末尾"📋 完整示例"检查质量。每次为当次描述重新组织语言，不套同一段文字。

---

### 🧭 第 0 步（最关键）：先定构图形态

**这是写任何 prompt 之前的第一个决策，决定整套镜头参数。**

实测结论：在 9:16 竖屏里，**宽 / 深 / 高 三个轴互相争夺画面，不可能同时推到极致**。竖屏画布天生窄高，每多一分"宽"都在和"高耸感"抢像素。所以**必须先选这张图主打哪个形态**，镜头参数跟着形态走。

| 形态 | 主打 | 相机配方（焦段+光圈+机位+防畸变，查 `camera-lens`，**无机身**） | 代价（实测） | 适用 |
|---|---|---|---|---|
| **纵深高耸型** | 深 + 高 | `16mm wide-angle lens, f/8, floor level, low-angle looking up, straight verticals kept upright` | 宽度被压扁成夹道；广角过猛时顶部拉成隧道、边缘变形 | 向里向上延伸的庄严恢弘 |
| **宽幅大气型** | 宽 + 舒展 | `20mm wide-angle lens, f/8, slightly below standing eye-level, moderate upward tilt, rectilinear` + 水平无界词 | 纵深与高耸感各弱一档 | 横向铺开的恢弘大厅、penthouse 那种舒展放大 |
| **均衡型** ⭐ 默认 | 三轴都不极致但都不缺 | `18mm wide-angle lens, f/8, between seated and standing height, gentle upward tilt, straight verticals upright` + 轻度水平无界词 | 没有单项惊艳，但最不容易翻车 | 不确定 / 首次出图 / 要稳 |
| **方厅型** | 长宽接近 + 单向纵深 | `18mm wide-angle lens, f/8, stepped back for full width, moderate upward tilt, rectilinear` + 单向窗景 | 受 9:16 竖屏物理限制，"方"会被画布压成偏竖（真要 1:1 需换画幅）| 想要"长宽差不多"的开阔方形大厅 |
| **斜角转角型** 🆕 | 对角纵深 + 非对称 | `18mm rectilinear wide-angle lens, f/8, camera positioned in one corner looking diagonally toward the opposite corner, slight upward tilt with verticals kept gently upright, sharp two-point diagonal perspective` + 家具绑定斜向网格 | 近角家具被广角放大易变形（焦段别低于 18mm）；强上仰会滑成三点透视、竖线倒 | 破对称强迫症、要真实建筑摄影感的转角两点透视；最强显纵深、最稳命中三层规则；当 Ken Burns 母图最佳 |

> 以上是直接可抄的相机段。`f/8` = 大空间深景深全清；防畸变正向词（`straight verticals kept upright` / `rectilinear`）替代负面写法，防"楼向上倒"。需要更细的机位/畸变词去 `camera-lens` 第四、八节查。

**默认走"均衡型"**——踩坑最少。用户说"要更恢弘纵深"切纵深高耸型，"要更宽更大气"切宽幅大气型，"要方一点/长宽差不多"切方厅型。

> **实测来由**：纵深高耸型 = 第 1 张（深高够、宽不够）；宽幅大气型 = 加水平无界后第 3 张（宽够但隧道化）；均衡型 = 第 4 张（三轴平衡，验证🟢）；方厅型 = 第 5 张（方厅+单向窗景，竖屏下"方"仍偏竖但已最接近）；斜角转角型 = 第 8 张（四把钥匙破对称强迫症，出真实建筑摄影感两点透视，验证🟢）。

---

### 🎬 LTX 横扫首帧模式（用途开关，叠加在构图形态之上）

**触发条件**：用户说"这图给 LTX 用"/"要生成视频"/"做视频首帧"/"镜头横扫"/"pan"/"从左往右扫" —— 或任何表明这张图是**视频首帧而非静态成品**的信号。

**这不是第 5 种构图形态，而是一层叠加约束**——它套在你已选的形态（纵深/宽幅/均衡/方厅）之上，把"静态美图构图"改造成"横扫视频起始帧构图"。

**为什么要专门处理**：静态美图默认"居中对称、吊灯中轴"——但镜头从这种画面"往右扫"会立刻撞到右边界，没有行程。横扫首帧需要的是**重心偏左、右侧留延展**的非对称构图，让镜头有地方可扫、有东西可揭示。

**默认横扫方向：左 → 右**（用户脚本如此）。右→左则整体镜像。

**叠加的 5 条硬约束（左→右横扫）**：

1. **重心压向左半边**——主视觉内容（主沙发组 / TV 墙 / 主锚点）放画面**左侧**，这是镜头出发点。`the main seating and feature wall weighted toward the left of the frame, the composition starting from the left`
2. **左侧有明确锚点**——左边缘要有一个强起点（整面 marble 墙 / 一组沙发），不能左边空着。`a full-height marble feature wall anchoring the left edge as the camera's starting point`
3. **右侧留"未展开空间"**——右边**不能塞满、不能到墙到头**，要留延展感，让镜头往右有路可走。`the right side of the frame opening into unrevealed space, room for the camera to pan into`
4. **横扫终点（右侧）有"奖励"**——右边该埋一个值得扫到的高潮元素（楼梯 / 落地窗夜景 / 功能区），`a sweeping staircase and glazed city view positioned toward the right, rewarding the rightward pan`
5. **巨型吊灯从"居中"改"偏右中"**——让它在镜头扫到中段时进入画面成为高潮，而非一开始就全见。`the colossal chandelier positioned center-right so it enters the frame as the pan progresses`

**形态搭配建议**：
- ✅ **最适合**：宽幅大气型 / 均衡型（横向有东西可扫）
- ⚠️ **谨慎**：方厅型（横向行程仍有限）
- ❌ **避免**：纵深高耸型（那是往里钻的运镜，不是往右扫，和横扫目标冲突）

**竖屏横扫的物理提醒**：竖屏横向窄，横扫行程本就有限——首帧右侧的"延展空间"要克制留白，别留太空导致镜头扫过去是空墙。竖屏横扫适合"小幅平移揭示 2-3 个功能区"，不适合"扫过一整个大横厅"（那需要横屏，但横屏不能直接用于 Reel）。

> **下游衔接**：本模式只管"首帧构图为横扫优化"。真正的运镜 prompt（pan 速度 / 幅度 / 缓动）、i2v vs flf 选择、首帧合格性诊断，交给 LTX 生态 skill：`ltx-first-frame-prep`（首帧准备）、`ltx-pipeline-router`（选 i2v/flf）、`ltx-i2v-prompt`（运镜 prompt）。本 skill 出的横扫首帧是它们的输入。

---

### 📐 斜角转角透视模式（破对称强迫症）

**触发条件**：用户要"斜角"/"转角视角"/"两点透视"/"不要正面对称"/"真实建筑摄影感"/"corner / three-quarter view"，或对正面构图出图不满意想要更强纵深张力。

**与第 0 步形态的关系**：斜角转角型已作为第 5 种构图形态进表（见第 0 步）。本节是它的**完整操作手册**——形态表只给了一行相机配方，真正难点在下面"四把钥匙"，缺一不可。

**为什么要专门处理**：Flux 天生有"对称强迫症 + 单点透视惯性"——即使写了 `diagonal camera`，它也只是把相机转一点，**家具依然画成与画框平行**，透视立刻塌回正面。破解命门不是转相机，而是**强制家具旋转**。

**四把钥匙（缺一不可，按重要度排）**：

1. **家具绑定斜向网格（最重要）**：给大沙发/茶几下硬性旋转指令 `the L-shaped sectional sofa and coffee table aligned with the room's diagonal grid`，强制家具在 3D 空间 45° 旋转摆放，锁死斜角透视。光转相机不转家具 = 透视塌陷。
2. **背墙向斜后方退缩**：不写"电视墙在左边"，写空间几何趋势 `the full-height feature wall receding diagonally into the deep background as the leading line`，让墙形成"左前→右后"大夹角，拉开纵深。
3. **机位 + 视线双重定点**：`camera positioned in one corner of the vast hall` + `looking diagonally toward the opposite corner`，给 AI 两点透视的物理支点，防它把视角拉回中轴线。
4. **非对称空间递进词**：避免"左边…右边…"的对称并列，改用递进 `to the right of the sofa area the space opens up to reveal the kitchen island, staircase and distant glazing in successive diagonal recession`，引导 AI 按"左前→中→右后"斜线布置功能区。

**竖线选择（两点 vs 三点，必须明说一个）**：
- 干净建筑感 → `camera level, straight verticals kept upright (two-point perspective)`
- 挑高震撼（露吊灯/挑高）→ `slight upward tilt, verticals gently converging (three-point)`，但上仰别过猛，否则墙向上倒

**近角防变形**：转角广角近角家具会被放大拉形，焦段**别低于 18mm**，加 `f/8`（全清）+ `rectilinear`（防鱼眼）。

**额外优势**：斜角构图天生带对角纵深，**自动满足 spatial 库"前景锚点 + 中景框 + 远景纵深"三层硬规则**——是命中三层最稳的构图；且**当 Ken Burns 母图最佳**，对角递进给的深度错觉能部分补偿 2D 推拉无视差的"平"。

**强化版斜角镜头尾巴（成品，直接抄到 prompt 末尾相机段）**：

```
A wide-angle three-quarter corner view, camera positioned in one corner of the vast hall looking diagonally toward the opposite corner. The full-height feature wall and the L-shaped sectional sofa are aligned with the room's diagonal grid, the near wall receding diagonally into the deep background as the leading line. To the right of the sofa area the space opens up to reveal the kitchen island, staircase and distant glazing in successive diagonal recession. Shot on an 18mm rectilinear wide-angle lens at f/8, slight upward tilt with verticals kept gently upright, sharp diagonal two-point perspective, deep focus throughout.
```

**形态搭配建议**：
- ✅ 与任意皮肤（White / Onyx / Ocean）正交可叠
- ⚠️ 与"🎬 LTX 横扫首帧模式"叠加时：斜角已是非对称，横扫方向顺对角线（近角→远角）走，别再强行压左
- ⭐ **与「长方形发光吊顶框」叠加 = Hevvv 深色爆款同款配方**：斜角视角会把长方形吊顶框拍成菱形外观——这是**透视变形不是真菱形**，必须按 chandelier 库「形状-透视写作原则」写 `rectangular panel appearing diamond-rotated due to the three-quarter camera angle`，绝不写 `diamond`。这是斜角型最出片的组合（目标参考图正是此配方）。

> **相机配方口径说明**：本节斜角相机透视词已内联齐全（焦段+光圈+机位+视线+竖线+防畸变），可直接抄、不必再 view `camera-lens`。若日后要让 interior-luxury / penthouse 等也支持斜角，再把"四把钥匙"里的通用镜头部分抽进 `camera-lens` 第四节复用。

---

### 8 个 principle 维度（每次现场用底座库词汇实现）

| 维度 | principle | 设计依据 |
|---|---|---|
| **构图形态** | 见第 0 步，默认均衡型 | 宽/深/高互搏，必须先选形态 |
| **画幅** | 9:16 竖屏（768×1344 / 864×1536）；真要方厅可试 4:5 / 1:1 | 竖屏放大垂直恢弘感 |
| **配色** | 全白 60% + 石材纹理配重 30% + 蓝 TV 10% | 路线 B 折中，配重压住"轻飘" |
| **挑高** | 18 米+（查 spatial 库维度 2 超尺度挑高，配整面 marble 墙锚定防虚空）| 超大尺度物理底线 |
| **气场脊椎** | 整面通体大理石墙 + 干净叠级平顶 + 巨型吊灯 + 大片留白（**无柱无拱无穹顶**）| 现代恢弘靠尺度材质留白，非古典构件 |
| **纵深机制** | 单向落地窗景（查 spatial 库维度 1 窗景纵深）| 现代手法给纵深，不用拱门长廊 |
| **吊灯形态** | 巨型垂坠水晶大灯（查 chandelier 库 Drop / atrium，**带比例约束防面条**）| 视觉核心 |
| **镜头** | **跟随构图形态**（见第 0 步），非锁死 | 镜头与形态耦合 |

> 这些是 principle 不是死值——每条指向"去哪查什么词"，现场组合成符合当次描述的句子。**镜头跟着第 0 步选定的形态走，不可锁死乱叠。**

### 必带的 6 个元素（principle 层面必须出现，**绝无柱/拱/穹顶**）

1. **极致挑高**（18 米+，干净现代处理）—— 垂直震撼
2. **整面通体大理石墙**（book-matched marble 从地到顶，多面）—— 替代列柱的厚重分量，兼任挑高锚定物防虚空
3. **干净叠级平顶**（layered stepped recesses + LED cove lighting，**非穹顶**）
4. **巨型垂坠水晶吊灯**（中央深垂，**带比例约束防面条**）—— 视觉核心
5. **大片留白地面**（≥70% 视觉深度，光洁 marble 反射）—— 空旷即大气
6. **单向落地窗景**（一面落地玻璃通城市/海景，给纵深）+ **背光蓝屏 TV**（唯一彩色锚点）

> **无构件正向声明**：模型实测容易自发添加列柱/拱门，需显式压制。
> - **FLUX.1 验证有效写法**（负面）：`no columns and no arches anywhere`（第 5 张验证🟢）
> - **FLUX.2 偏好写法**（正面，待 A/B 验证）：`smooth uninterrupted walls, purely modern surfaces, clean unbroken planes`
> - FLUX.2 官方原则是"无负面提示、用正向描述"，故新版默认用正面写法；但 `no columns` 是 FLUX.1 时代实测有效的，**两种写法下次跑图 A/B 对比**，确认 FLUX.2 下哪个真能压住柱拱后再定稿。

### 模式 A 生成流程（现场组合，非套模板）

1. **定形态**（第 0 步）——默认均衡型，按用户措辞切换
2. **判用途**——若是 LTX 视频首帧（用户提"生成视频/横扫/给LTX用"），叠加"🎬 LTX 横扫首帧模式"的 5 条约束（重心偏左、右侧延展等）
3. **读** 8 个 principle 维度 + 6 个必带元素
4. **查三个底座库的 🟢 词**：`flux-chandelier-vocabulary`（吊灯组合 + 比例约束）/ `flux-spatial-depth-vocabulary`（挑高/窗景纵深/三层纵深）/ `camera-lens`（按第 0 步形态抄相机配方）
5. **按 FLUX.2 权重顺序组合**（见下方"组装顺序"）——核心意图前置、相机置末，为当次描述量身写一段连续英文 prompt
6. **对照** 末尾"📋 完整示例"检查 + 过"🚫 反例禁词"

> **FLUX.2 组装顺序（词序 = 权重，重要的放前面）**：
> 1. **核心意图先砸**——第一句就定"巨大"：`colossal / soaring double-height / a hall on the scale of a grand lobby rather than a home`
> 2. **构图主张**——紧跟意图：偏左截断 or 第 0 步形态（纵深/宽幅/均衡/方厅）
> 3. **主体锚点**——那面通顶 marble/onyx 巨墙（显大主力，权重高）
> 4. **吊灯**——视觉核心（查 chandelier + 比例约束）
> 5. **必要环境**——窗景纵深 + 夹层/楼梯 + 蓝 TV
> 6. **次要细节**——家具、地面、花艺
> 7. **相机段**——查 `camera-lens` 的形态配方，**置于末尾**（官方惯例：相机参数放后）
> 8. **风格 + 动态种子 + 画幅**——`cinematic dream-like quality` + `crystals glittering` + `sharp focus throughout` + `9:16 vertical composition`
>
> 这个顺序由实战验证：成功的"偏左截断"图正是"colossal…cut off"在第一句、相机在中后段。**不要按"天花→墙→灯→家具"的罗列顺序铺**——那会让次要元素抢走本该给"巨大感"的权重。

### 默认输出格式

`````
✨ Flux2 Mega-Scale Modern Hall Prompt（构图形态：均衡型）

[英文 prompt，现场组合，120-200 词单段，FLUX.2 权重顺序]

📐 推荐尺寸：768×1344（9:16 竖屏）或 864×1536

🎚️ 梦核刻度：4–5

🧭 构图形态：均衡型（如需更纵深 / 更宽 / 更方，说一声切换形态）

🔗 词汇来源：
   flux-chandelier-vocabulary: Drop × 长链水晶瀑布 × 铬（带比例约束）
   flux-spatial-depth-vocabulary: 窗景纵深 + 超尺度挑高 18 米（marble 墙锚定）+ 广角（按形态）

💡 超大现代厅公式——尺度 × 材质 × 留白，无古典构件。
   换风格（深色 / 海景）说"换皮肤"；换构图说"要更宽/更纵深/更方"。
`````

---

## 🎛️ 高级问卷（模式 B 用这套）

> 进入高级模式——想换什么？
>
> 1. **空间皮肤**（3 选 1）：
>    - White Mega Hall（默认主公式，全白 + marble 配重）
>    - Onyx Mega Hall（深色厚重——深色石材墙 + 暖金 + 背光石材，气场最重）
>    - Ocean Mega Hall（海景——单向窗景换无界海景落地窗）
>
> 2. **构图形态**（4 选 1）：纵深高耸 / 宽幅大气 / 均衡（默认）/ 方厅（见第 0 步）
>
> 3. **梦核刻度**（1-5，默认 4–5）

回答后按"皮肤库 + 词汇库"生成。

---

## 📐 9:16 画幅强制（所有模式通用）

**默认 9:16 竖屏**（768×1344 / 864×1536），竖屏放大垂直恢弘感。
**例外**：用户明确要"方厅 / 长宽差不多" → 可建议改 4:5（864×1080）或 1:1（1024×1024），因为竖屏物理上压制"方"。
Prompt 末尾：`9:16 vertical composition, portrait orientation`（或对应画幅）。

---

## 🎨 配色硬规则（所有模式通用）

- **60% 主色**：白 / 米白
- **30% 配重色**：marble 灰白纹理 / 铬 / 暖金 / 深色石材（**这是气场分量来源——整面 marble 的纹理本身就是配重，压住"全白轻飘"**）
- **10% 点缀色**：**蓝色**（来自 TV 或海景）—— 延续 Hevvv 流指纹

**禁止**：红/绿/黄点缀；古典金箔石膏线满铺（会变巴洛克）；纯全白无 marble 纹理配重（显轻飘）。

---

## 🪩 吊灯描述（强制查 flux-chandelier-vocabulary）

吊灯**不在本 skill 硬编码**——以 `flux-chandelier-vocabulary` 为权威源。

### 强制流程

写吊灯片段前 view `/mnt/skills/user/flux-chandelier-vocabulary/SKILL.md`，按下表抄对应 🟢 词。

### Default 公式的吊灯组合（模式 A 用）

| flux-chandelier-vocabulary 维度 | 类别 | 依据 |
|---|---|---|
| 悬挂方式 | **Drop chandelier**（深垂跨层）| 超大尺度要体量，垂坠非嵌入 |
| 主体形状 | 矩形方柱 / 球形 + 短裙摆 | 垂坠大灯主流形态 |
| 水晶处理 | **长链水晶瀑布**（54% 最稳）| 跨层垂坠靠长链撑体量 |
| 金属色调 | 铬（默认）/ 暖金（深色皮肤）| 铬配现代 |

### ⚠️ 比例约束（实测必加，防"面条灯"）

18 米超高空间里写"垂坠跨层"，模型容易把吊灯拉成又细又长的链子（第 3 张就是）。必须加：

```
the chandelier substantial and full in width relative to its drop, a commanding voluminous mass of densely glittering crystal rather than a thin elongated strand
```

原则：**垂坠要"有体量的柱"不要"细面条"**。纵深高耸型尤其要盯（强仰角会进一步拉长视觉比例）。

### 吊灯字面化陷阱（→ 查 flux-chandelier-vocabulary）

本 skill 不复述。高发速记：`crystal waterfall` → `cascading crystal strands descending vertically`；`crystal column` → `rectangular vertical crystal block as chandelier body`。

---

## 🚪 空间感描述（强制查 flux-spatial-depth-vocabulary）

空间感**不在本 skill 硬编码**——以 `flux-spatial-depth-vocabulary` 为权威源。

### 强制流程

写空间感片段前 view `/mnt/skills/user/flux-spatial-depth-vocabulary/SKILL.md`，按下表抄 🟢 词。

### Default 公式的空间感组合（模式 A 用）

| flux-spatial-depth-vocabulary 维度 | 必选类别 | 依据 |
|---|---|---|
| 维度 1 A 段（纵深机制）| **窗景纵深**（单向落地窗通城市/海景）+ 水平无界（按形态）| 现代手法给纵深，替代拱门长廊 |
| 维度 1 B 段（三层硬规则）| **前景锚点 + 中景框 + 远景纵深** 三层必备 | 同主线硬规则 |
| 维度 2 挑高垂直 | **超尺度挑高（18 米，配整面 marble 墙锚定防虚空）** | 超大尺度物理底线 |
| 维度 3 多层结构 | **楼梯 + 夹层 + 玻璃围栏** | 多层贯通增强体量 |
| 维度 4 广角张力 | **按第 0 步形态选**（16/18/20mm + 对应机位仰角）| 镜头跟随形态 |

### 空间感字面化陷阱（→ 查 flux-spatial-depth-vocabulary）

本 skill 不复述。高发速记：`infinite depth` → `extending toward distant functional zones`；`wide-angle distortion` → `rectilinear wide-angle preserving straight vertical lines`；`endless space` → `successive functional zones receding into layered depth`。

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

## 🏛️ 3 种空间皮肤（高级模式用）

### ⚪ White Mega Hall（默认主公式）
- 时段：bright daylight or dusk gold
- 景观：distant city panorama through full-height glazing（单向）
- 配色：60% 全白 + 30% marble 纹理/铬配重 + 10% 蓝 TV
- 材质：book-matched white Calacatta marble（整面到顶）+ polished chrome + glass
- 天花：clean layered stepped recess + warm-white LED cove（**非穹顶**）
- 吊灯：**Drop / 矩形方柱 / 长链水晶瀑布 / 铬**（→ flux-chandelier-vocabulary 查词）
- 必备：blue-screen TV + 整面 marble + 留白地面 + 单向窗景 + 楼梯夹层。**无柱无拱无穹顶。**

### 🖤 Onyx Mega Hall（深色厚重，气场最重）
- 时段：night / moody dusk
- 景观：dark city through glazing or none
- 配色：60% 暖白 + 30% 黑/深色石材 + 暖金配重 + 10% 蓝 TV
- 材质：black onyx / dark marble 整面墙 + back-lit translucent onyx + brushed gold
- 天花：clean layered recess + 暖金 LED cove；**或选「长方形发光吊顶框」**（见下方专项）
- 吊灯：**Drop / 球形+短裙摆 / 长链水晶瀑布 / 暖金**（→ flux-chandelier-vocabulary 查词）；**或选「发光吊顶框 + 长方形柱状垂坠水晶」组合**（Hevvv 1.8万赞同款，→ 查 chandelier 库「嵌入式方形几何」+「密集填充式垂直水晶」+「形状-透视写作原则」）
- 必备：blue-screen TV（依然必须）+ 深色整面石材墙（深色本身就是配重，气场最接近"厚重恢弘"）。**无柱无拱无穹顶。**

> **🆕 长方形发光吊顶框（Hevvv 深色爆款同款，斜角下变菱形）**：目标参考图（1.8万赞）的天花核心不是普通叠级平顶，而是**一个长方形 backlit recessed 吊顶框**（暖白 LED 描边）+ 框中央垂下**长方形柱状垂坠水晶**。关键陷阱：**斜角视图会把这个长方形框拍成菱形**——这是透视变形，**不是真菱形**。写 prompt 必须遵守 chandelier 库「形状-透视写作原则」：
> - ✅ 写 `a rectangular backlit recessed ceiling panel with warm-white LED cove edging, appearing diamond-rotated due to the three-quarter camera angle`
> - ❌ 绝不写 `diamond-shaped ceiling` / `diamond panel`（模型会真出菱形几何体）
> - 框中央吊灯：`a rectangular vertical crystal column chandelier descending from the center of the panel, dense vertical crystal strands filling the full footprint`（查 chandelier 库「矩形/方柱」+「密集填充式垂直水晶」）

### 🌊 Ocean Mega Hall（海景）
- 时段：sunset / twilight over water
- 景观：infinity ocean view through full-wall glazing（单向窗景换海景）
- 配色：60% 白 + 30% travertine/铬配重 + 10% 海景蓝（蓝来自景观）
- 材质：travertine / white marble 整面墙 + polished chrome + full-wall glazing
- 天花：clean layered recess + LED cove
- 吊灯：**Drop / 多层锥形 / 长链水晶瀑布 / 铬**（→ flux-chandelier-vocabulary 查词），反射夕阳
- 必备：full-wall ocean glazing + sunset reflection across marble floor。**无柱无拱无穹顶。**

---

## 🎚️ AI 梦核刻度

| 刻度 | 含义 | 默认 |
|---|---|---|
| 3 | 真实超尺度豪宅大厅 | |
| **4** | **现代恢弘偏戏剧** | **⭐ 默认下沿** |
| **5** | **完全奇观**（注意物理边界）| **⭐ 默认上沿** |

模式 A 输出刻度 4–5。

---

## 📋 完整示例（参考用，**非强制模板**）

下面是一个**方厅型 + 无构件**的达标输出示范（第 5 张实测验证的版本）——展示新气场公式（尺度+材质+留白+吊灯，无柱无拱无穹顶）全部到位的样子。

**怎么用**：写新 prompt 时**不要照抄**，走"定形态 → 读 principle → 查三个底座库（chandelier / spatial / camera-lens）→ 按 FLUX.2 权重顺序现场组合"的正路，写完**对照此例检查**：6 个必带元素齐不齐、有没有混进列柱拱门穹顶、核心意图（巨大）是否前置、相机段是否置末。**注意：下方示例是旧版方厅型长示例（约 320 词），仅作"元素覆盖"对照用；新版目标长度 120-200 词，且按权重顺序排列（旧示例是罗列顺序），实际写作应更精简、意图更前置。均衡/纵深/宽幅型的镜头措辞要按第 0 步对应配方改写。**

```
An immense modern luxury hall built on a centralized square plan, near-equal in width and depth so the space reads as a vast open square room rather than a long corridor, the volume far larger than any normal residence with ceilings soaring nearly eighteen meters overhead. The ceiling is a clean contemporary design of layered stepped recesses with concealed warm-white LED cove lighting tracing each tier, no columns and no arches anywhere, the grandeur carried entirely by sheer scale, full-height stone, and open volume. Captured on an 18mm wide-angle lens at a height between seated and standing, positioned to take in the full square breadth of the room with a moderate upward tilt, the lateral space opening generously to both left and right. Towering full-height walls of book-matched white Calacatta marble rise unbroken from floor to ceiling on multiple sides, their dramatic grey veining giving the vast room its weight and richness. A colossal drop crystal chandelier hangs from the center of the ceiling, long crystal strands cascading in a tiered fall, the fixture substantial and full in width relative to its drop, a commanding voluminous mass of densely glittering crystal rather than a thin elongated strand, a slim polished chrome armature nearly lost within it, refracting light across the hall. The depth of the space is concentrated in a single direction: on the far side of the square room a full-height glazed wall opens to a distant city panorama, extending the visual depth beyond the interior and giving the open square plan its one strong axis of view. In the foreground a pair of generous white sectional sofas sit facing each other across the centerline, set well apart across the wide square floor around a monumental rectangular Calacatta marble coffee table bearing a white hydrangea arrangement, broad open stretches of polished white marble floor surrounding them on all sides and mirroring the chandelier above. A full-height book-matched marble feature wall on the left holds a backlit blue-screen television showing soft blue ocean imagery as the only note of color. On the right a sweeping white stone staircase with a frameless glass balustrade winds up to a furnished mezzanine gallery overlooking the open square volume. Within the broad plan a glossy white grand piano stands to one side and a marble kitchen island with bar stools sits along the right edge, a formal dining area set near the glazed far wall, all visible at once across the wide room. Polished white marble flooring stretches open and uncluttered in every direction, light shimmering across every reflective surface. Cinematic dream-like quality, modern palatial grandeur, 9:16 vertical composition.
```

**这个示例覆盖了**：方厅型镜头（18mm + 中等仰角 + 取全宽）/ 18 米挑高 / 整面 marble 墙锚定 / 干净叠级平顶（非穹顶）/ `no columns and no arches anywhere`（无构件正向反制）/ 垂坠 Drop 吊灯 + 比例约束（防面条）/ 单向窗景纵深 / 多功能区横向并置 / 70% 留白 / 蓝 TV + marble 配重 / 动态种子。约 320 词。

---

## 🚫 反例禁词（出现即重写）

### A. 古典构件污染（本 skill 已彻底去除，绝不出现）
- ❌ `columns / colonnade / pillars` → ✅ 删除，改 `full-height marble walls`
- ❌ `arches / arched openings / enfilade` → ✅ 删除，改 `full-height glazed wall` 给纵深
- ❌ `dome / vaulted ceiling / cathedral` → ✅ 改 `clean layered stepped ceiling recess`
- ❌ `Baroque / Corinthian / gold leaf molding` → ✅ `clean contemporary surfaces`

### B. 尺度退化词（会退回 flux-luxury-penthouse 公寓）
- ❌ `double-height ceiling`（只有 9 米）→ ✅ `ceilings soaring nearly eighteen meters`
- ❌ `flush-mount chandelier`（贴天花没体量）→ ✅ `colossal drop chandelier`

### C. 字面化陷阱词
- ❌ `wide-angle distortion` → 出鱼眼，改 `rectilinear wide-angle preserving straight vertical lines`
- ❌ `infinite depth` → 改 `distant city panorama through the glazed wall`

### D. 配色破坏词
- ❌ 纯全白无 marble 纹理 → 显轻飘，必须有 `book-matched marble veining` 配重
- ❌ `red / green / yellow accent` → ✅ `blue TV screen accent`

### E. 吊灯比例
- ❌ 不写比例约束 → 出面条灯，必须加 `substantial and full in width relative to its drop`

### F. 斜角透视塌陷词（要斜角时出现即重写）
- ❌ 家具边缘平行于画框（furniture edges parallel to the frame）→ 透视塌回正面，必须 `aligned with the room's diagonal grid`
- ❌ 只写 `diagonal camera` / `corner view` 不转家具 → AI 只转相机、家具仍正，必须同时下"家具绑定斜向网格"指令
- ❌ `looking at the wall straight-on` → 拉回单点透视，改 `looking diagonally toward the opposite corner`
- ❌ 强上仰无竖线约束 → 三点透视墙倒，加 `verticals kept gently upright`

### G. 发光吊顶框形状陷阱（斜角 + 长方形吊顶时必防）
- ❌ `diamond-shaped ceiling panel` / `diamond ceiling recess` → 模型会真渲染菱形几何体，**而目标只是"长方形被斜角拍成菱形"**。必须写 `rectangular backlit recessed ceiling panel appearing diamond-rotated due to the three-quarter camera angle`（chandelier 库「形状-透视写作原则」）
- ❌ `square chandelier`（无透视解释）→ 模型出扁平正方形丢体积，必须配"因相机角度呈菱形"的状语
- ❌ 发光框写成普通 `flush-mount ceiling light` → 没了 backlit 戏剧感，必须 `warm-white LED cove edging tracing the recessed panel`

---

## 🎬 首帧友好隐性约束（为未来 i2v 留余地）

每张图至少 1 个动态种子词：`crystals glittering and refracting light` / `chandelier reflections dancing across the polished marble floor` / `light shimmering across every reflective surface` / `distant city lights twinkling`（夜景）/ `ocean waves rolling gently`（Ocean）。

---

## 核心写作原则

- **气场来自尺度 + 材质 + 留白 + 巨型吊灯，不来自古典构件**——本 skill 的灵魂
- **绝不出现列柱 / 拱门 / 穹顶**——显式压制：FLUX.2 用正面 `smooth uninterrupted walls, purely modern surfaces`；FLUX.1 用 `no columns and no arches anywhere`（两者 A/B 待验证）
- **模式 A 是默认**——现场组合非套模板，输出刻度 4–5
- **principle-based 而非模板填空**——定形态、读 principle、查底座库、现场组合，对照"完整示例"检查
- **先定构图形态（第 0 步）再配镜头**——宽/深/高互搏，镜头跟随形态
- **相机三件套查 `camera-lens`**——焦段 + 光圈（大空间 `f/8`）+ 机位 + 防畸变正向词，不指定机身；相机段置于 prompt 末尾
- **FLUX.2 权重顺序：核心意图（巨大）前置、相机置末**——词序定权重，别按"天花→墙→灯"罗列顺序铺
- **若是 LTX 视频首帧**——叠加"🎬 LTX 横扫首帧模式"：重心偏左、左侧锚点、右侧留延展、吊灯偏右中；优先配宽幅/均衡型，避开纵深高耸型；首帧竖屏（Reel 出口），下游交 ltx skill 接运镜
- **若要斜角 / 转角 / 两点透视 / 破对称**——走"📐 斜角转角透视模式"四把钥匙：**家具绑定斜向网格（命门）** + 背墙斜退 + 机位视线双定点 + 非对称递进词；光转相机不转家具必塌回正面；焦段别低于 18mm 防近角变形
- **整面通体 marble 墙 = 厚重分量来源**（替代列柱）+ 兼任 18 米挑高锚定防虚空
- **纵深靠单向落地窗景**（替代拱门长廊）
- **吊灯必须垂坠 + 带比例约束**——要体量，但防面条；宁宽勿长（超长垂坠会面条）
- **配色必带 marble 纹理配重**——压住全白轻飘
- **写 negative 一律改正面**（FLUX.2 无负面提示）：`no blur`→`sharp focus throughout`、`no columns`→`smooth uninterrupted walls`、防畸变写 `straight verticals kept upright` 而非 `no distortion`
- **prompt 长度目标 120-200 词，单段，9:16 竖屏**（方厅可换 4:5/1:1）——FLUX.2 偏好精简，旧版 250-340 词易致元素堆砌、空间显挤显小
- **每张图至少 1 个动态种子**

---

## 数据依据声明

本 skill 基于**与用户多轮迭代 + 7 张实测图 + 1 段 LTX 视频闭环验证**的"超大现代厅"公式：

**演化历程**：
- 最初版用"列柱+拱门+穹顶"撑宫殿感 → 实测发现变长廊、偏古典、且和用户审美不符
- 用户明确去掉全部古典构件 → 重构为"纯现代超大厅"，气场改靠尺度+材质+留白+吊灯
- 第 5 张实测验证：**无柱无拱无穹顶，气场不降反升、更干净现代** → 确立为本 skill 核心公式
- 第 6-7 张 + LTX 视频闭环验证：**Onyx 深色 + 横扫首帧模式 + LTX i2v 完整工作流跑通** → 本 skill 从"出静态美图"扩展为"出 LTX 视频首帧"
- 第 8 张实测：**斜角转角型验证通过** → 四把钥匙（家具绑定斜向网格 / 背墙斜退 / 机位视线双定点 / 非对称递进词）稳定破掉 Flux 对称强迫症，出真实建筑摄影感的两点透视；家具绑定斜向网格是命门，光转相机不转家具会塌回正面 → 斜角作为第 5 种构图形态入表

**实测验证（8 张图 + 1 段视频，🟢已验证 / ⚠️待留意）**：
- 🟢 `no columns and no arches anywhere` 能有效压制模型自发添加列柱拱门
- 🟢 去掉古典构件后，整面 marble + 18 米挑高 + 巨型吊灯 + 留白 + 窗景，气场完全撑得住
- 🟢 整面 marble 墙作锚定物，18 米超尺度挑高（库标🟡）没跑成抽象虚空
- 🟢 均衡型（18mm + 中等仰角）三轴平衡、不隧道化、不鱼眼
- 🟢 dome 改 clean layered recess 平顶，更现代
- 🟢 吊灯比例约束防住面条；窗景纵深替代拱门给纵深，干净有效
- 🟢 **Onyx 深色皮肤实测通过**（第 6-7 张）——深色 veined marble + 暖金吊灯 + 背光石材，无构件公式在深色调依然成立、气场反而更厚重；蓝 TV 在暖色背景里成"唯一冷色"反而更跳，冷暖对冲生效
- 🟢 **🎬 LTX 横扫首帧模式实测通过**（第 7 张）——5 条约束（重心偏左/左锚点/右延展/右奖励/吊灯偏右中）在 Onyx + 宽幅型上一次出图就成功，构图明显非对称偏左、横扫行程清晰
- 🟢 **完整工作流闭环验证**：Flux 横扫首帧 → LTX i2v slide right → 竖屏 Reel 成片 全流程跑通；横扫首帧模式不只是"美图非对称"，是真能驱动后续 LTX 横扫视频的合格输入
- 🟢 **斜角转角型实测通过**（第 8 张）——四把钥匙稳定破掉 Flux 对称强迫症，出真实建筑摄影感的两点透视；**家具绑定斜向网格是命门**（光转相机不转家具会塌回正面）；斜角天生满足 spatial 三层硬规则、当 Ken Burns 母图最佳
- ⚠️ 宽/深/高三轴在 9:16 竖屏互搏 → 构图形态维度
- ⚠️ **方厅型受竖屏物理限制**："方"会被画布压成偏竖；真要长宽 1:1 需换 4:5/1:1 画幅（待验证）

**LTX 下游联动经验**（衔接 ltx-i2v-prompt / ltx-camera-movement）：
- LTX 对 slide 方向词（left/right）执行不稳，必须靠"物体进出方向"锁定方向（详见 `ltx-camera-movement` 维度 3-4 的实战经验段）
- 首帧里的强亮元素（吊灯/TV）容易被 LTX 偷偷推近成 dolly，i2v prompt 需明确"never becomes the center of focus, never pushes forward"三连防御
- 方向仍反 → 把首帧水平镜像翻转后用同 prompt 跑（最暴力可靠的兜底）

**待验证**：方厅型在 4:5/1:1 画幅下能否出真正长宽相等的大厅；纵深高耸型/宽幅大气型在无构件公式下的表现；横扫首帧模式在白厅 / Ocean 皮肤下是否同样有效（目前只在 Onyx 验证过）。

---

**修订日志 2026-05-30b（新增长方形发光吊顶框 + 斜角下方形变菱形透视）**：

基于 Hevvv 深色爆款目标图（1.8万赞）落地，把"长方形 backlit 发光吊顶框 + 长方形柱状垂坠水晶"接进 mega hall（主要落在 Onyx 皮肤），并与已验证的斜角转角型绑定。四处改动：

1. **Onyx 皮肤天花/吊灯行加「长方形发光吊顶框」专项**——含完整成品句，直接引用 chandelier 库「嵌入式方形几何」+「密集填充式垂直水晶」+「形状-透视写作原则」，本 skill 不复述吊灯词、以底座库为权威源。
2. **斜角专节加「与发光吊顶框叠加 = Hevvv 深色爆款配方」搭配条**——点明这是斜角型最出片的组合。
3. **反例禁词加 G 节「发光吊顶框形状陷阱」**——核心拦 `diamond-shaped ceiling`（模型会真出菱形）。
4. **修订日志 + 数据依据加目标图来由**。

**命门洞察**：目标图天花的"菱形"是**长方形被斜角相机拍出的透视变形，不是真菱形几何体**。chandelier 库「形状-透视写作原则」早有验证句 `appearing diamond-rotated due to the upward/three-quarter camera angle`（2/2 命中）——写 `rectangular...appearing diamond-rotated`，绝不写 `diamond`。

**待验证**：发光吊顶框 + 斜角 + Onyx 三者叠加的整段 prompt 是否一次命中（本轮新组合，待出图确认）；该配方在 White 皮肤下是否同样成立。

---

**修订日志 2026-05-30（新增斜角转角型构图形态）**：

新增第 5 种构图形态"斜角转角型"，破 Flux 对称强迫症、出真实建筑摄影感的两点透视。基于第 8 张实测，分四处融入：

1. **第 0 步形态表加第 5 行**——斜角转角型，相机配方内联（18mm rectilinear + 转角机位 + 视线对角 + 竖线约束）。
2. **新增"📐 斜角转角透视模式"专节**（在 LTX 横扫首帧模式之后）——核心是"四把钥匙"：家具绑定斜向网格（命门）/ 背墙斜退 / 机位视线双定点 / 非对称递进词；附两点 vs 三点竖线选择、近角防变形、成品镜头尾巴。
3. **反例禁词加 F 节**——斜角透视塌陷词（家具平行画框 / 只转相机不转家具 / straight-on / 强仰无竖线约束）。
4. **数据依据加第 8 张验证 + 核心写作原则加斜角速记条**。

**命门洞察**：破对称强迫症不靠转相机，靠**强制家具旋转**（`aligned with the room's diagonal grid`）——光转相机不转家具，透视必塌回正面。

**相机口径**：斜角透视词内联自包含、不引用 camera-lens（与昨日"四形态查 camera-lens"的口径差异已在专节末尾说明，留了日后抽词复用接口）。

**待验证**：斜角"自动满足 spatial 三层 + 当 Ken Burns 母图最佳"目前仅第 8 张一张背书，多图待确认；斜角在 White / Ocean 皮肤下的表现（目前未单独验证）。

---

**修订日志 2026-05-29（FLUX.2 规范对齐 + camera-lens 接入）**：

本轮基于 FLUX.2 官方 prompting guide 复盘 + 多张"显大"实测，做了四处结构性修订：

1. **接入 `camera-lens` 为第三底座**——相机参数不再只给焦段，改为查 camera-lens 给齐"焦段 + 光圈（大空间 `f/8`）+ 机位 + 防畸变正向词"。**不指定机身型号**（建筑题材机身收益低，且避免带入机身风格倾向）。第 0 步四形态表的镜头配方已全部升级为可直接抄的 camera-lens 英文配方。
2. **组装顺序改 FLUX.2 权重序**——核心意图（巨大/挑高）前置到第一句、相机段置末。依据：FLUX.2 词序 = 权重；实战中成功的"偏左截断"图正是意图前置、相机靠后。旧的"天花→墙→灯→家具"罗列顺序会让次要元素抢权重。
3. **负面写法改正面**——FLUX.2 无负面提示。`no columns`→`smooth uninterrupted walls, purely modern surfaces`（**A/B 待验证**：no columns 是 FLUX.1 时代验证有效的，FLUX.2 下两种写法需对比）；防畸变写 `straight verticals kept upright` 而非 `no distortion`；补 `sharp focus throughout` 正向锐度词。
4. **长度目标 250-340 → 120-200 词**——FLUX.2 官方理想 30-80 词，旧版过长是元素堆砌、空间显挤显小的主因（多张实测验证：prompt 越长、点名元素越多，Flux 越往一帧里塞，空间越显小）。

**本轮显大经验沉淀（多张实测）**：
- 🟢 **显大最强招 = 偏左截断 + 不对称**（单面巨墙一气到顶锚左缘 + 右侧楼梯/窗切出画外延伸），而非"拍全 + 退远 + 清空家具"——后者实测翻车（空旷廉价、面条灯、强仰变形）
- 🟢 **吊灯宁宽勿长**：`extremely long drop` 与"宽到压住比例"自相矛盾，Flux 会选长弃宽 → 面条；正解是宽球冠 + 中等垂坠
- ⚠️ **丰满 vs 巨大是 9:16 竖屏里的此消彼长**（物理：挑高超 9 米家具必显小）——想极致挑高就让单面墙一气到顶不被夹层打断；想丰满贵气就压回双层挑高
- ⚠️ FLUX.2 换 VLM 架构（Mistral-3 驱动），吃连贯散文不吃关键词堆砌——本 skill"查词库拼接"的写法在 FLUX.2 下需更偏向自然散文（待逐步迁移验证）

**跑过更多图后继续回填。**
