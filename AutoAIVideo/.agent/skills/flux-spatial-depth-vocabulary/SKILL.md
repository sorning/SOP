---
name: flux-spatial-depth-vocabulary
description: 空间深度词汇库——奢华室内 Reels 主线下,按四维度（Z 轴纵深与分层 / 挑高垂直 / 多层结构 / 广角张力）提供原子词汇 + Flux2 友好度评级 + 模型字面化陷阱清单。当 Claude 需要为任何文生图 prompt（Flux2 / SDXL / Midjourney / GPT Image 等）撰写"空间感"、"纵深感"、"挑高"、"layered composition"、"广角透视"等描述,或被问到"画面怎么更有空间感"、"怎么写挑高"、"远景纵深 prompt"、"广角畸变怎么避免"时,调用此 skill。本 skill 是**被动参考材料**——不主动生成完整 prompt、不提供风格预设、不打包组合、不给完整英文句、不点名具体家具或建筑物体,只提供原子词汇供下游 prompt skill 自由组合。也可在用户直接问"空间感词汇有哪些"、"spatial vocabulary"时主动加载。**边界**：本 skill 只管奢华室内场景的"空间形态语义"（怎么纵深 / 怎么挑高 / 怎么多层 / 怎么广角）,不碰配色、不碰材质、不碰具体家具命名、不碰光线效果、不碰吊灯（吊灯归 chandelier-vocabulary）,也不覆盖餐厅 / 工业 / 复古 / 极简等非奢华室内主线题材。
---

# 空间深度词汇库（奢华室内 Reels 主线）

## 定位与边界

本 skill 是**底座型被动参考材料**,与多个 prompt skill 形成生态:

| Skill | 职责 | 和本 skill 的关系 |
|---|---|---|
| `chandelier-vocabulary` | 吊灯词汇 | **姐妹 skill**——视觉元素分别归口 |
| `flux-luxury-penthouse` | Reels 算法流首帧 prompt | **下游消费者**——写空间感时 view 本 skill |
| `flux2-interior-luxury` | 杂志建筑流室内 prompt | **下游消费者**——同上（未来改造时接入） |

### ✅ 本 skill 覆盖

- **Z 轴纵深与分层**：纵深的几何机制 + 前/中/远景的抽象位置语义
- **挑高垂直**：天花板高度、垂直张力词汇
- **多层结构**：楼梯、夹层、走廊层的描述
- **广角张力**：镜头焦距、透视畸变、边缘拉伸
- **Flux2 字面化陷阱**：哪些空间感词会被模型按字面渲染

### ❌ 本 skill 不覆盖

- **配色**（60-30-10 等 → 各 prompt skill 自管）
- **具体家具命名**（沙发 / 茶几 / TV 墙 / 餐桌等具体物体 → 各 prompt skill 自管,本 skill 只写抽象位置语义如 `foreground anchor` / `mid-ground framing element`）
- **材质 / 装饰**（→ 各 prompt skill 自管）
- **吊灯 / 天花几何**（→ `chandelier-vocabulary`）
- **光线效果**（投影 / 反射 / 折射 → 未来 lighting-vocabulary 范畴）
- **梦核刻度**（奇观强度判断 → 各 prompt skill 自管）
- **风格预设**（不打包"常用组合"——留给下游自由组合）
- **完整 Flux2 英文句**——本 skill 给词汇片段,下游负责拼成句
- **非奢华室内主线题材**——餐厅、工业、复古、极简等不在覆盖范围

### 未来归口提示

**维度 4（广角张力）**未来如果建 `camera-angle-vocabulary` skill,会迁出本 skill 归到那里。目前因为没建,先放本 skill 里。下游 skill view 词汇时不需要关心这件事。

---

## ⚠️ 关于 Flux2 友好度评级

每个词汇标注 **Flux2 友好度**：

- 🟢 **稳**：Flux2 / SDXL 主流模型理解准确,跑出结果与描述一致
- 🟡 **需引导**：模型理解偏差或需要明确语义修饰
- 🔴 **难稳定**：模型容易跑偏,需要反复抽卡或额外约束

**重要免责**：评级基于 Flux2 / SDXL 跨模型实测推断,**未经大规模系统化测试**。不同模型、不同版本表现有差异。遇到不符以实际为准。

---

## 维度 1：Z 轴纵深与分层

**画面深度怎么从前景拉到远景**——奢华室内 Reels 主线把"二维像素"拉成"三维空间感"的核心维度。本维度分两段：A 段管"用什么几何机制拉纵深",B 段管"前/中/远景三层的抽象位置语义"。

### A 段：纵深的几何机制

| 类别 | 英文词汇 | 视觉特征 | Flux2 友好度 |
|---|---|---|---|
| **层叠纵深** | `layered spatial recession` / `multiple functional zones receding into the deep background` / `architectural layers receding through the space` / `successive layers of architectural framing each revealing the next deeper space` / `quadruple-layered depth: foreground anchor / mid-ground framing / background functional zone / distant exterior view` / `distant view extending through layered openings into a further beyond` | 多个区在 Z 轴上排开,可深化为 4 层递归（前景 / 中景 / 远景 / 远景的远景）| 🟢 |
| **单点纵深** | `one-point perspective with central vanishing point at the far wall` / `convergent perspective lines drawing the eye toward the back of the space` / `axial recession to a distant focal point` | 消失点 + 透视收敛 | 🟢 |
| **廊道纵深** | `corridor-like recession through the space` / `long axis extending from foreground to distant background` / `tunnel-like recession bounded by architectural frames` | 长轴空间 + 边框收束 | 🟢 |
| **窗景纵深** | `floor-to-ceiling glazing extending the visual depth beyond the interior` / `distant exterior view continuing the spatial depth through the windows` / `glazed wall opening the space to a distant view` | 玻璃 + 远景延伸到画外 | 🟢 |
| **嵌套门洞纵深** | `nested archways receding into the distance` / `successive door openings revealing deeper rooms` / `enfilade composition with aligned openings each framed by the previous one` | 一层套一层的门洞 / 拱门 | 🟡 `enfilade` 词冷门,需补释 |
| **水平无界** | `lateral space continuing beyond the left and right edges of the frame` / `walls extending beyond the frame edges` / `cropped side architecture suggesting larger volume beyond` / `composition framed with no visible side walls in the field of view` | 画面两侧墙被裁断,空间向画外延伸 | 🟢 |

### B 段：前/中/远景的抽象位置语义

**重要**：本段只写**位置语义**,不点名具体物体（沙发 / 茶几 / TV 墙等）。下游 skill 决定每个位置放什么物体后,从本段抄"画面位置词"嵌入。

| 位置 | 英文词汇 | 占画面 | Flux2 友好度 |
|---|---|---|---|
| **前景锚点** | `dominant foreground anchor in the lower-third` / `prominent foreground element occupying the lower-left quadrant` / `large foreground subject anchoring the bottom edge of the frame` | 下半幅 30-40% | 🟢 |
| **中景框** | `mid-ground architectural framing element separating foreground from background` / `central mid-ground vertical anchor` / `mid-ground feature dividing the depth into clear zones` | 中段 30-40% | 🟢 |
| **远景纵深** | `recessive deep-background functional zone` / `distant elements visible at the rear of the space` / `far background extending the perceived depth` | 上半 / 中后段 20-30% | 🟢 |

### 三层叠加的硬规则

**奢华室内 Reels 主线下,一张图应同时具备 前景锚点 + 中景框 + 远景纵深 三层**。缺一层画面会被压扁:

- 缺前景 → 画面看着"漂着没着落"
- 缺中景 → 前景与远景之间断层,Z 轴拉不出来
- 缺远景 → 空间感被锁在前景小盒子里

### 写 prompt 时的提示词补强

- **60% 深度硬规则**：`functional zones recede into the deep background,occupying at least 60% of the visual depth`
- **三层都要明确画面位置词**：`foreground` / `mid-ground` / `background` 或 `lower-left foreground quadrant` / `central mid-ground` / `deep background`
- **加分层强化句**：`clear visual separation between foreground,mid-ground,and background layers`
- **嵌套门洞 → 加 `each opening framed by the previous one`**（避免模型理解成单一门洞）
- **4 层递归深化（C 方向加码）→ 加 `successive layers of architectural framing each revealing the next deeper space,with a distant view continuing into a further beyond`**
- **水平无界（A 方向加码）→ 加 `lateral space continuing beyond the left and right frame edges,with cropped side architecture suggesting larger volume beyond the visible field`**——避免画面两侧出现完整墙面切断空间感

---

## 维度 2：挑高垂直

**天花板有多高、垂直方向的张力**。这条线只管"高",不管"地面到天花板之间发生什么"（那是维度 1 和维度 3 的事）。

| 类别 | 英文词汇 | 视觉特征 | Flux2 友好度 |
|---|---|---|---|
| **标准挑高（5-7 米）** | `double-height ceiling` / `lofty ceiling` / `vaulted living area` | 标准复式高度 | 🟢 |
| **极致挑高（9-12 米）** | `soaring ceilings nearly nine meters high` / `monumental vertical volume` / `ceilings towering overhead` | 大宅级 / 算法奇观区间 | 🟢 |
| **超尺度挑高（12 米+）** | `triple-height atrium reaching twelve meters` / `grand-scale vertical void` / `dizzying ceiling height emphasizing vertical scale` | 极致奇观 | 🟡 易被理解成纯抽象空间 |
| **仰视张力** | `dramatic upward perspective emphasizing ceiling height` / `slight low-angle composition amplifying vertical scale` / `tilted-up framing accentuating the vertical reach` | 镜头仰视带出垂直感 | 🟢 |
| **垂直元素辅助** | `floor-to-ceiling vertical feature stretching upward` / `full-height columns drawing the eye vertically` / `tall vertical drapery extending the perceived height` | 用墙/柱/帘加强垂直感 | 🟢 |

### 写 prompt 时的提示词补强

- 高度数字化是稳的（`soaring nearly nine meters` 比 `very tall` 准）,但**避免低于 5 米的具体数字**——模型会理解成普通住宅而不是奢华挑空
- 仰视张力词必须配 `20mm wide-angle` 或 `slight low-angle` 等镜头词,单独写 `dramatic upward perspective` 模型常理解成异形透视

---

## 维度 3：多层结构

**楼梯、夹层、走廊层的描述**——画面里有几个水平层在视觉上叠加。**本维度不点名具体家具,只写"层"的属性**。

| 类别 | 英文词汇 | 视觉特征 | Flux2 友好度 |
|---|---|---|---|
| **楼梯主角** | `grand staircase rising as the dramatic focal point` / `sweeping sculptural staircase ascending dramatically` / `monumental staircase as a primary visual anchor` | 楼梯戏剧化为主角 | 🟢 |
| **楼梯副角** | `staircase rising along one side of the space` / `staircase tucked at the rear,leading to upper level` / `secondary staircase visible at the edge of the frame` | 楼梯辅助、不抢戏 | 🟢 |
| **夹层 / Mezzanine** | `mezzanine gallery above overlooking the double-height living volume` / `upper-level walkway visible from below` / `cantilevered mezzanine projecting into the volume` | 夹层悬挑或贯通 | 🟢 |
| **多层贯通** | `triple-stack horizontal layers visible: ground level + mezzanine + upper level` / `three floors stacked vertically within the visual frame` | 三层水平层视觉叠加 | 🟡 需明确层数和功能 |
| **围栏处理** | `glass balustrade preserving visual continuity between floors` / `frameless glass railing maintaining open spatial flow` / `slim metal handrail with minimal visual interruption` | 围栏的透明度与连续性 | 🟢 |

### 写 prompt 时的提示词补强

- 楼梯位置必须明确（`on the right` / `along the left wall`）——模糊位置词模型常出双楼梯
- 玻璃围栏 → 配 `frameless` 或 `minimal frame` 避免出粗框架
- 多层贯通 → 加 `each level visible simultaneously from the camera position`（确保镜头能同时看到多层）

---

## 维度 4：广角张力 / 透视畸变

**镜头本身怎么放大空间感**——焦距、视角、畸变。

**未来归口**：本维度未来会迁出到 `camera-angle-vocabulary`,目前因为没建,先放本 skill。

| 类别 | 英文词汇 | 视觉特征 | Flux2 友好度 |
|---|---|---|---|
| **标准广角 20mm** | `20mm wide-angle lens` / `wide-angle perspective` / `wide field of view capturing the full spatial volume` | Reels 主流 | 🟢 |
| **超广角 14-16mm** | `14mm rectilinear wide-angle preserving straight lines` / `extreme wide-angle composition` / `expansive ultra-wide framing` | 极致空间感,边缘有畸变 | 🟡 易出鱼眼 |
| **中广角 24-28mm** | `24mm moderate wide-angle` / `slightly wide field of view with minimal distortion` | 真实建筑摄影 | 🟢 |
| **微仰视广角** | `slight low-angle 20mm wide-angle at sofa-seat height with 10-degree upward tilt` / `low-camera wide-angle emphasizing ceiling presence` | Hevvv 默认 | 🟢 |
| **前景放大效应** | `foreground objects exaggerated in scale due to wide-angle proximity` / `prominent foreground furniture from wide-angle near-field` | 前景物体被广角放大 | 🟢 |
| **边缘拉伸** | `subtle edge stretching from wide-angle field of view` / `gentle barrel-effect at frame edges` | 画面边缘的拉伸感 | 🟡 易出鱼眼变形 |
| **远景收缩** | `distant elements compressed at the vanishing point` / `background elements visually compressed due to wide-angle recession` | 远景元素被压缩 | 🟢 |

### 写 prompt 时的提示词补强

- **避免单独用 `wide-angle distortion`** —— 模型常理解成鱼眼。改 `gentle wide-angle perspective with subtle edge stretch`
- **避免 `forced perspective`** —— 模型理解成戏剧化变形。改 `slight low-angle 20mm perspective,natural depth`
- **超广角必须配正向替代** —— Flux2 对负向词响应差,稳的写法是 `14mm rectilinear wide-angle preserving straight lines`
- **镜头高度词必带** —— `at sofa-seat height` / `at standing eye level` / `at floor level` 三选一,空着不写模型常出怪角度

---

## ⚠️ Flux2 字面化陷阱

模型常把"空间感"词按**字面**渲染成画面里的物体或异形畸变。下面是高发陷阱：

| 陷阱词 | 模型常误解为 | 推荐改法 |
|---|---|---|
| `infinite depth` | 真的无限远地平线、空无一物 | → `extending toward distant functional zones visible at the rear of the space` |
| `endless space` | 空旷无物的虚空 | → `successive functional zones receding into layered depth` |
| `wide-angle distortion` | 鱼眼镜头效果 | → `gentle 20mm wide-angle perspective with subtle edge stretch` |
| `forced perspective` | 戏剧化变形 / 矮人巨人对比 | → `slight low-angle 20mm perspective with natural depth` |
| `vertigo effect`（孤立用）| 旋转头晕的扭曲画面 | → `slight low-angle composition emphasizing the soaring ceiling height` |
| `vertigo-inducing` | 同上,旋转扭曲 | → `dizzying ceiling height emphasizing vertical scale` |
| `cathedral-scale`（孤立用）| 真的出哥特教堂尖拱 | → `monumental vertical proportions with modern flush ceiling treatment` |
| `tunnel perspective` | 真的隧道 / 圆形管道 | → `corridor-like recession bounded by architectural frames` |
| `vanishing point`（孤立用）| 画面中心一个圆点 | → `central convergence at the far feature wall` |
| `spatial layering`（孤立用）| 抽象几何图层堆叠 | → `clear separation between foreground anchor, mid-ground framing element, and deep-background functional zone` |
| `dramatic depth` | 戏剧化阴影但空间没纵深 | → `pronounced spatial recession through multiple functional zones` |
| `eye drawn into the distance` | 真的画一只眼睛 | → `composition leading the viewer's gaze toward the deeper space` |
| `expansive volume` | 真的出气球膨胀感 | → `generous spatial volume with high ceilings and open functional flow` |
| `infinite horizontal space` | 真的出空旷大草原 / 海平面 | → `lateral space continuing beyond the left and right edges of the frame,with cropped side architecture` |
| `endless lateral space` | 同上 | → `walls extending beyond the frame edges,suggesting larger volume beyond the visible field` |
| `recursive depth` | 模型出递归画中画 / 镜中镜套娃 | → `successive nested layers each revealing a deeper functional zone` |
| `space without boundaries` | 抽象虚空 / 失去比例 | → `composition framed with no visible side walls,architecture continuing beyond frame` |

### 通用避坑原则

1. **名词 + 空间锚定 优于 抽象形容词**：`infinite depth` 模糊 → `functional zones receding into the deep background` 明确
2. **避免抽象空间感名词孤立用**：`depth` / `space` / `volume` / `perspective` 后面必须跟具体空间元素或位置词（`through the dining zone` / `bounded by columns` / `framed by the marble wall`）
3. **镜头词必带具体焦距**：`wide-angle` 模糊 → `20mm wide-angle` 明确,模型对数字焦距响应稳
4. **避免"感受词"**：`feels vast` / `sense of grandeur` / `gives a feeling of depth` 类词模型不会渲染,要写**视觉可见的具体元素**

---

## 用法说明

写空间感描述前 view 本 skill,从 4 维度按需选词,抄英文词汇组合。优先选 🟢 词;选 🟡/🔴 词时按各维度末尾补强修饰,或参考"⚠️ Flux2 字面化陷阱"清单改写。下游 prompt skill 负责把词汇拼成连贯英文句,并把维度 1 B 段的位置语义（如 `dominant foreground anchor`）替换成具体物体（如 `large white L-sectional sofa`）。

**维度 1（Z 轴纵深与分层）的三层硬规则是奢华室内 Reels 主线的硬规则——前景锚点 + 中景框 + 远景纵深 必须同时具备**。其他维度可按场景需要选用。

---

## 数据依据声明

本 skill 词汇库基于:

- **题材范围**：奢华室内 Reels 主线（与 chandelier-vocabulary 同范围）
- **维度 1 B 段的"三层硬规则"**：基于 Hevvv 主页爆款图通用观察,所有高赞图都同时具备前景锚点 + 中景框 + 远景延伸
- **词汇质量**：基于 Flux2 / SDXL 跨模型实测推断
- **字面化陷阱清单**：基于 Flux2 / GPT Image / SDXL 跨模型实测观察

**适用范围**：
- ✅ 奢华室内（客厅 / 复式空间 / 大宅）的空间感描述
- ✅ Reels / 抖音 / Stories 短视频首帧
- ✅ 杂志级建筑摄影室内（同奢华主线下）
- ❌ 餐厅 / 酒店大堂 / 剧院（题材不同,词汇未覆盖）
- ❌ 复古 / 工业 / 极简 / 自然系（题材不同,词汇未覆盖）

跑过实际生成图后如发现新形态或新陷阱,更新本 skill。
