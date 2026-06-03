---
name: camera-lens
description: 静态摄影"相机配置"知识库与文生图触发词词典——焦段 / 光圈景深 / 景别 / 机位角度 / 特殊镜头 / 产品机位 / 透视畸变 / 相机品牌的权威参考底座。模型中立，适用于 Flux2 / SDXL / Midjourney / GPT Image / nano-banana 等任意文生图模型。本 skill 是 flux2-prompt-generator / realistic-character-prompt / ip-character-prompt / flux2-interior-luxury / flux-luxury-penthouse / flux-mega-modern-hall / flux-modern-palatial-hall / 珠宝产品图等所有文生图生成型 skill 的强制共享底座。任何涉及文生图 prompt 中"用什么镜头 / 焦段 / 光圈 / 景深 / 机位 / 拍摄角度 / 相机型号 / camera / lens / focal length / aperture"的描述时，都应先加载本 skill 作为权威参考。本 skill 不主动生成具体题材的 prompt，仅作被动参考材料被其他 skill 引用。也可在用户直接询问"摄影镜头有哪些 / 焦段怎么选 / 拍人像用什么镜头 / 85mm vs 50mm / 移轴是什么 / 拍产品用什么相机"时主动加载。本 skill 是 `ltx-camera-movement`（动态运镜底座）的静态摄影姊妹篇——前者管视频"镜头怎么动"，本 skill 管静态图"用什么镜头、站在哪、多大光圈、什么相机"。
---

# 静态摄影相机配置知识库（文生图底座）

## 本 skill 的定位

这是所有文生图生成型 skill 的**强制共享底座**，是 `ltx-camera-movement`（动态运镜）的**静态摄影姊妹篇**。**模型中立**——沉淀的是摄影通用知识（焦段/光圈/机位/相机品牌），适用于 Flux2 / SDXL / Midjourney / GPT Image / nano-banana 等任意文生图模型；下方触发词以 Flux2 措辞为主，迁移到其他模型时按其语法习惯微调即可。两者分工：

| 底座 | 管什么 | 服务对象 |
|---|---|---|
| `ltx-camera-movement` | 视频镜头**怎么动**（运镜） | LTX 视频生成 skill |
| **`camera-lens`（本 skill）** | 静态图**用什么镜头、站哪、多大光圈、什么相机** | 所有文生图 skill |

本 skill 专门沉淀：

1. **焦段分类**（超广角→长焦）+ Flux2 触发词 + 适用题材 + 字面化陷阱
2. **光圈与景深**（虚化/全清晰的正确写法）
3. **拍摄距离/景别**（特写→环境）
4. **机位/角度**（平视/仰俯/夹层等，按构图目的分类）
5. **特殊镜头**（移轴/微距/anamorphic/折返等）
6. **产品/静物专属机位**（珠宝、桌面、flat lay）
7. **透视压缩与畸变**（跨题材认知核心）+ **镜头画质副作用**（光晕/暗角/色散）
8. **题材 × 焦段推荐矩阵**（导航速查）
9. **相机品牌/型号 × 胶片色彩科学**（质感定调）
10. **写 Flux2 镜头 prompt 的核心原则** + 竖屏三轴互搏

本 skill 本身**不生成 prompt**——它是被引用的字典，不是工具。

---

## ⚠️ 验证状态标记说明

每条触发词标注验证状态（对齐 `ltx-camera-movement` 机制）：

- ✅ **已验证**：在 Flux2 实际跑过，触发词有效
- ⚠️ **待验证**：基于通用摄影知识 + Flux2 行为推断，**未经系统测试**，使用时留意效果
- ❌ **已证失败**：跑过但 Flux2 处理不好，不推荐

随项目推进，待验证条目陆续升级。当前多数条目来自现有 skill（interior-luxury / character / penthouse / mega-hall）的实战沉淀，标注来源。

---

## 🔑 三件套总原则（贯穿全文）

一条完整的 Flux2 相机配置 = **机身 + 镜头 + 机位**三件套：

```
[相机品牌型号（第九节）] + [焦段（第一节）] + [光圈（第二节）] → 锁定"用什么拍"
[景别（第三节）] + [机位角度（第四节）] → 锁定"站在哪、拍多近"
```

下游 skill 写 prompt 末尾的相机段时，至少给齐"**机身型号 + 焦段 + 光圈**"，再按题材叠加景别/机位/畸变/胶片色彩。例：
`shot on Canon EOS R5, 85mm f/1.4, shallow depth of field, three-quarter portrait`

---

## 一、焦段类（视角与透视的本质属性）

焦段是镜头最本质的属性，决定**视角宽窄**和**透视压缩感**。Flux2 对具体焦段数字（如 `85mm`、`24mm`）响应良好，应优先写具体数字而非 `wide lens` 这类模糊词。

### 1. 鱼眼 8–15mm ⚠️ 极端畸变

视角接近或超过 180°，直线被弯成强烈桶形弧线。

- **特征**：球面畸变，中心放大、边缘极度弯曲
- **适用**：创意/超现实/极端空间张力；**慎用于写实**
- **触发词**：⚠️ `fisheye lens, extreme barrel distortion, 180-degree field of view, curved horizon`
- **陷阱**：Flux2 容易把鱼眼做成"普通广角"，必须明写 `curved/bent straight lines` 才出弧线效果

### 2. 超广角 14–24mm ⭐ 空间/建筑主力

视角极宽、纵深夸张、近大远小强烈。**这是空间设计 skill 的核心档**。

- **特征**：强烈纵深感、边缘拉伸、垂直线易汇聚（除非矫正）
- **适用**：建筑室内、挑高大厅、风光、环境叙事
- **触发词**：
  - ✅ `shot on a 14mm ultra-wide lens, eye-level, architectural interior photography, exaggerated depth and scale`（interior-luxury 验证）
  - ✅ `gentle 20mm wide-angle perspective`（penthouse 验证）
  - ⚠️ `16mm wide-angle, deep spatial perspective`
- **焦段内部区分（空间题材实测，mega-hall 沉淀）**：
  - `16mm` → 纵深高耸型（深+高，宽被压扁成夹道）
  - `18mm` → 均衡型（三轴都不极致但不缺，**默认最稳**）
  - `20mm` → 宽幅大气型（横向舒展，纵深与高耸各弱一档）
- **陷阱**：广角过猛会"隧道化/边缘变形"——见第七节畸变；要直线平行需配移轴（第五节）

### 3. 广角 24–35mm ⭐ 环境人像/街拍

轻微畸变，视角宽但接近自然。

- **特征**：主体带环境、轻度透视、35mm 最接近"带场景的自然视角"
- **适用**：环境人像、街拍、纪实、风光
- **触发词**：
  - ✅ `shot on 35mm f/2.0, slightly wider angle, subject in context of environment`（character 验证）
  - ⚠️ `24mm environmental portrait, subject within the scene`
- **陷阱**：**不要用 35mm 以下拍面部特写**——会拉宽鼻子/脸盘畸变（见第七节）

### 4. 标准 40–60mm（经典 50mm）⭐ 最自然

最接近人眼视角，畸变最小，透视最自然。

- **特征**：无明显压缩或拉伸，"所见即所得"
- **适用**：自然人像、半身、纪实、通用
- **触发词**：✅ `shot on Sony A7IV, 50mm f/1.8, natural perspective, balanced compression`（character 验证）

### 5. 中长焦/人像 85–135mm ⭐⭐ 人像黄金段

轻微空间压缩，背景虚化漂亮，面部比例最讨喜。**85mm f/1.4 是人像经典**。

- **特征**：背景压缩拉近、奶油虚化、面部不变形
- **适用**：人像（首选）、特写、半身、产品
- **触发词**：
  - ✅ `shot on Canon EOS R5, 85mm f/1.4, shallow depth of field, creamy bokeh`（character 验证）
  - ✅ `shot on 135mm f/2.0, strong background compression, subject isolated`（character 验证）
- **认知**：85mm 是"人像默认"，135mm 是"强压缩隔离感"。要"背景更扁、主体更突出"往长焦走

### 6. 长焦 200–400mm ⚠️ 强压缩

把远处拉近、背景压平。

- **适用**：野生动物、体育、舞台、强隔离人像
- **触发词**：⚠️ `200mm telephoto, heavy background compression, flattened perspective, distant subject pulled close`
- **陷阱**：室内/小空间用不上；Flux2 对极端压缩感表现一般，需明写 `flattened/compressed background`

### 7. 超长焦 500mm+ ⚠️ 待验证

打鸟、月亮、远距体育。文生图罕用，列此备查。
- **触发词**：⚠️ `600mm super-telephoto, extreme compression, isolated distant subject`

---

## 二、光圈与景深（虚化 vs 全清晰）

焦段管视角，**光圈管景深**——这是范本（运镜）没有、但静态图表现力第一梯队的维度。Flux2 对光圈值响应一般，**应优先描述"景深结果"而非只写 f 值**。

| 光圈档 | f 值 | 景深结果 | 适用 | Flux2 写法 |
|---|---|---|---|---|
| **大光圈** | f/1.2–f/1.8 | 极浅景深，奶油虚化 | 人像、特写、隔离主体 | ✅ `f/1.4, shallow depth of field, creamy bokeh, background completely melted` |
| **中大光圈** | f/2.0–f/2.8 | 浅景深，主体清晰背景柔 | 半身、产品、街拍 | ✅ `f/2.8, shallow depth of field, softly blurred background` |
| **中光圈** | f/4–f/5.6 | 适中，主体环境兼顾 | 环境人像、小组 | ⚠️ `f/4, moderate depth of field, subject sharp with gently soft background` |
| **小光圈** | f/8–f/16 | 大景深，前后全清晰 | 建筑、风光、产品全清 | ✅ `deep focus, sharp from foreground to background`（interior-luxury 验证） |

### 关键认知

- **建筑/风光/产品要"全清晰"**：不要写浅景深。interior-luxury 明确——建筑摄影标配 `deep focus, sharp front to background`，**不要 shallow depth of field**
- **f 值不如结果词**：写 `f/16` Flux2 未必给全清晰，必须补 `deep focus, everything in sharp focus`
- **虚化质量词**：`creamy bokeh`（奶油）/ `swirly bokeh`（旋焦，复古镜头）/ `oval bokeh`（椭圆，anamorphic）/ `bokeh balls`（光斑成圆）
- **散景来源**：背景有点光源才出漂亮光斑——`background city lights melting into bokeh balls`

---

## 三、拍摄距离 / 景别（人像核心轴）

景别和焦段是**两回事**——85mm 既能拍特写也能拍全身，靠的是拍摄距离。人像 prompt 必须明确景别。

| 景别 | 英文触发词 | 内容范围 | 适用 |
|---|---|---|---|
| **大特写** | `extreme close-up, macro detail` | 眼睛/唇/局部 | 五官细节、质感 |
| **特写** | `close-up portrait, head and shoulders` | 头肩 | 表情、眼神 |
| **半身** | `medium shot, waist-up framing` | 腰以上 | 人像主力 |
| **七分身** | `three-quarter shot, mid-thigh up` | 大腿中以上 | 服装+表情兼顾 |
| **全身** | `full body shot, head to toe` | 全身 | 服装、姿态、场景 |
| **环境人像** | `wide environmental portrait, subject small within the scene` | 人占小、环境占大 | 叙事、氛围 |

### 认知

- **景别 + 焦段要同时给**：`85mm + close-up`（压缩特写）vs `35mm + full body`（环境全身）效果天差地别
- 空间/建筑题材一般不写景别，用第四节"机位角度"代替

---

## 四、机位 / 角度（视线高度与构图目的）

机位决定**视线高度**和**观看心理**。下表按**构图目的**组织（继承 interior-luxury 五类目的，通用化到全题材）。

### 🏛️ 展示尺度/体量（让观者感到大）
| 角度 | 触发词 |
|---|---|
| 超广角平视 | ✅ `eye-level, architectural photography, exaggerated depth and scale` |
| 低角度仰视 | ✅ `low-angle shot looking upward, emphasizing soaring height, dramatic vertical perspective` |
| 微仰广角（Reels） | ✅ `at sofa-seat height with a 10-degree upward tilt, subtle edge stretch`（penthouse 验证） |

### 🗺️ 展示布局/关系（看清结构）
| 角度 | 触发词 |
|---|---|
| 高位俯视 | ✅ `elevated bird's-eye view, showcasing the layout below` |
| 45°斜俯视 | ✅ `elevated 45-degree angle, three-quarter view, showing depth and volume` |
| 夹层俯视 | ✅ `view from mezzanine looking down into the volume below` |

### 🌊 制造沉浸感（身处其中）
| 角度 | 触发词 |
|---|---|
| 坐姿视角 | ✅ `seated eye-level perspective at ~90cm height, intimate and immersive` |
| 转角对角线 | ✅ `diagonal composition from corner, maximizing perceived depth, leading lines` |

### 👤 人像机位（视线高度定情绪）
| 角度 | 触发词 | 心理 |
|---|---|---|
| 平视 | ✅ `shot at eye level, direct and natural` | 平等、亲切 |
| 轻微仰拍 | ✅ `shot from ~10 degrees below eye level, giving a tall elegant presence`（character 验证） | 高挑、强势、大片 |
| 轻微俯拍 | ⚠️ `shot from slightly above eye level, looking down gently` | 显小脸、可爱、柔弱 |
| 顶光俯拍 | ⚠️ `high-angle looking down on the subject` | 戏剧、压迫 |

### 构图法（所有题材通用，继承 character）
| 构图 | 触发词 |
|---|---|
| 三分法 | `composed using rule of thirds, subject on the left vertical third` |
| 居中对称 | `centered symmetrical framing, subject perfectly centered` |
| 留白 | `subject occupying one third of frame, generous negative space` |
| 对角线 | `dynamic diagonal composition` |
| 框中框 | `subject framed within a doorway or window` |

---

## 五、特殊镜头

### 移轴 Tilt-Shift ⭐ 建筑标配
矫正透视让垂直线保持平行，或制造微缩景观。
- **触发词**：✅ `shot on a 17mm tilt-shift lens, perspective correction, vertical lines kept parallel`（interior-luxury 验证）
- **认知**：建筑摄影专业感的关键——没有它，超广角拍高空间垂直线会向上汇聚（楼歪）。微缩效果反向用：`tilt-shift miniature effect, toy-like`

### 微距 Macro ⭐ 产品/珠宝核心
1:1 放大拍极小物体。**珠宝产品图首选**。
- **触发词**：✅ `macro lens, 1:1 magnification, extreme detail, shallow depth of field on a single point`
- **适用**：珠宝、昆虫、水珠、纹理、质感特写
- **认知**：微距景深极浅，要明写"哪个点清晰"——`sharp focus on the gemstone facet, everything else melting away`

### Anamorphic 变形宽银幕 ⭐ 电影感
横向压缩，出椭圆虚化和横向蓝色光晕。
- **触发词**：✅ `anamorphic lens with characteristic horizontal lens flare and oval bokeh`（character 验证）
- **适用**：电影感人像、戏剧场景

### 折返镜头 Mirror/Catadioptric ⚠️ 待验证
甜甜圈形虚化光斑。
- **触发词**：⚠️ `catadioptric mirror lens, distinctive donut-shaped bokeh rings`

### 柔焦 Soft Focus ⚠️ 待验证
朦胧梦幻，复古人像。
- **触发词**：⚠️ `soft-focus lens, dreamy hazy glow, vintage portrait softness`

---

## 六、产品 / 静物专属机位（珠宝/桌面/电商）

空间和人像 skill 都不覆盖的题材，B 方案通用底座的核心增量。

| 机位 | 触发词 | 适用 |
|---|---|---|
| **平拍正视** | `straight-on eye-level product shot, centered, clean` | 标准电商主图 |
| **45°三视** | `45-degree three-quarter product angle, showing top and front faces` | 立体感、主流商品图 |
| **俯拍顶视 flat lay** | `top-down flat-lay, shot directly from above, items arranged on a surface` | 平铺布局、配饰组合 |
| **微距特写** | `extreme macro close-up on the product detail, single sharp point` | 珠宝刻面、材质、工艺 |
| **桌面浅景深** | `tabletop product photography, shallow depth of field, soft gradient background` | 高端单品 |
| **悬浮/无影** | `product floating on seamless white, no shadows, even diffused light` | 极简电商 |

### 珠宝专项认知
- 珠宝要**反光与火彩**：`gemstone catching light with brilliant fire and sparkle, faceted reflections`
- 金属要**质感分级**：`polished gold with mirror reflections` vs `brushed matte gold`
- 微距 + 大光圈隔离单点：`macro, f/2.8, only the central diamond in razor-sharp focus`
- 这是首帧/i2v 友好的"动态种子"来源（与 LTX 珠宝视频衔接）：`light glinting across the facets`

---

## 七、透视压缩 / 畸变 + 镜头画质副作用（底座灵魂节）

这是本 skill 的"易混淆对比"节，对标 `ltx-camera-movement` 第五节。**用户/下游最容易写错的认知都在这**。

### 焦段 vs 拍摄距离：谁决定"脸的形状"

| | 短焦近拍（35mm 凑近） | 长焦远拍（85mm 退后） |
|---|---|---|
| 面部 | 鼻子放大、脸盘变宽、畸变 | 比例自然、讨喜 |
| 背景 | 拉伸、推远 | 压缩、拉近 |
| 结论 | ❌ 别用短焦拍特写 | ✅ 人像特写永远长焦 |

**核心**：要"接近主体"应该**换长焦+退后**，不是"用广角凑近"。凑近会畸变。

### 广角畸变的两种坑（空间题材高发，mega-hall 沉淀）

1. **隧道化**：广角过猛（14mm 强仰角）→ 顶部拉成隧道、边缘变形
   - 正向反制：`rectilinear wide-angle preserving straight vertical lines`（不要写 `wide-angle distortion`）
2. **垂直线汇聚**：仰拍高空间 → 楼向上倒
   - 正向反制：配移轴 `perspective correction, vertical lines kept parallel`

### 压缩 vs 透视：长焦不是"放大"

- 长焦 = **压缩空间**（背景变扁、拉近），不是单纯放大
- 要"背景压扁隔离主体" → 长焦；要"夸张纵深空旷" → 广角
- 写法：`135mm flattened/compressed perspective` vs `20mm exaggerated depth`

### 镜头画质副作用（Flux2 friendly 真实感触发词）

真实镜头的"缺陷"恰恰让 AI 图更像照片：

| 副作用 | 触发词 | 风格 |
|---|---|---|
| 光晕 | `anamorphic horizontal lens flare` / `subtle veiling glare` | 电影/逆光 |
| 暗角 | `gentle vignette darkening the corners, drawing focus to center`（character 验证） | 复古/聚焦 |
| 色散 | `very slight chromatic aberration at the edges, analog warmth`（character 验证） | 胶片/复古 |
| 呼吸效应 | ⚠️ `slight focus breathing` | 电影 |
| 漏光 | `soft light leak across one corner, warm amber`（character 验证） | 怀旧/梦幻 |

---

## 八、题材 × 焦段推荐矩阵（导航速查）

下游 skill 一眼定档（对标 `ltx-camera-movement` 难度评级表）：

| 题材 | 首选焦段 | 光圈 | 机位 | 相机档（第九节） |
|---|---|---|---|---|
| **人像特写** | 85mm | f/1.4–f/2.0 | 平视/微仰 | 全画幅微单 |
| **半身人像** | 50–85mm | f/1.8–f/2.8 | 平视 | 全画幅微单 |
| **环境人像** | 35mm | f/2.0–f/4 | 平视 | 全画幅 / 胶片 |
| **全身/时尚** | 50–85mm | f/2.8 | 微仰 | 全画幅 / 中画幅 |
| **建筑室内** | 16–24mm + 移轴 | f/8–f/16 全清 | 平视/低仰 | 中画幅数字背 |
| **挑高大厅** | 16–20mm（按形态） | 深景深 | 微仰广角 | 中画幅 / Reels 用电影感词 |
| **风光** | 16–35mm | f/8–f/11 全清 | 平视/低 | 全画幅 / 中画幅 |
| **珠宝/产品** | 100mm 微距 | f/2.8–f/8 | 45°/微距/顶视 | 中画幅 / 全画幅微距 |
| **街拍纪实** | 35mm | f/2.8–f/5.6 | 平视 | 全画幅 / 胶片 |
| **电影感** | 40–75mm anamorphic | f/2.0 | 平视 | 电影机 |

---

## 九、相机品牌 / 型号 × 胶片色彩科学（质感定调）

机身和色彩科学共同锁定 photoreal 质感。BFL 官方 `t2i-prompting` 强调：**具体相机+具体胶片，比 `ultra-photorealistic` 这类抽象词更稳**。

### 按定位分档

#### 中画幅数字背 — 极致细节/编辑级
- **机型**：`Phase One XF IQ4` / `Hasselblad X2D` / `Fujifilm GFX 100`
- **特征**：超高解析、宽容度大、画廊级、冷峻严谨
- **适配**：建筑、产品、高端时尚人像
- **触发词**：✅ `shot on Phase One XF IQ4, architectural editorial quality, ultra-photorealistic`（interior-luxury 验证）

#### 全画幅单反/微单 — 通用主力
- **机型**：`Canon EOS R5` / `Sony A7R V` / `Nikon Z9` / `Sony A7IV`
- **特征**：均衡、锐利、通用
- **适配**：人像、街拍、风光、产品
- **触发词**：✅ `shot on Canon EOS R5, 85mm f/1.4`（character 验证）/ ✅ `Sony A7R V, 16-35mm GM, clean digital tonality, high dynamic range`（interior-luxury 验证）

#### 胶片机 / 胶片色彩科学 — 色调定调
> ⚠️ 这一档管的是**色彩科学**而非机身，与机身正交叠加（机身给解析，胶片给色调）。可和 character skill 的胶片风格库打通。

- **柯达 Portra 400**：✅ `Kodak Portra 400 color science, warm skin tones, natural saturation, fine grain` — 暖肤色/人像
- **富士 400H**：⚠️ `Fujifilm 400H, soft pastel greens and pinks, gentle highlights` — 清新/小清新
- **Cinestill 800T**：⚠️ `Cinestill 800T, tungsten night look, red halation around lights` — 夜景/霓虹
- **柯达 Gold 200**：⚠️ `Kodak Gold 200, warm golden nostalgic tones` — 复古暖调
- **Leica M + 黑白**：⚠️ `shot on Leica M, black and white film, rich silver gelatin tones`

#### 电影机 — 电影动态范围
- **机型**：`ARRI Alexa` / `RED`
- **触发词**：⚠️ `shot on ARRI Alexa, cinematic dynamic range` + anamorphic（第五节）

### 🚨 两条关键认知（现有 skill 实战沉淀）

**1. 机身与胶片色彩科学互斥——一次只选一套**
> interior-luxury 明确：不要混用 `Phase One` + `Kodak Portra`，模型会困惑。中画幅数字背走"数字色彩"，胶片走"胶片色彩"，二选一。

**2. 高端 ≠ 万能，要题材匹配（防风格污染）**
> penthouse 明确把 `Phase One XF IQ4` 列为"杂志流污染词"——它会把 Reels 梦核拉向杂志写实。**Reels/算法流/梦核题材应改用 `cinematic dream-like quality`，不写专业机型**。品牌要和题材/风格匹配，不是越高端越好。

---

## 十、写 Flux2 镜头 prompt 的核心原则

### 原则 1：写具体焦段数字，不写模糊词
- ❌ 弱：`wide-angle lens`
- ✅ 强：`16mm wide-angle lens`（Flux2 对数字响应更准）

### 原则 2：光圈写"景深结果"，不只写 f 值
- ❌ 弱：`f/16`（未必出全清晰）
- ✅ 强：`deep focus, sharp from foreground to background`

### 原则 3：相机配置整组放 prompt 末尾
机身+焦段+光圈+色彩科学作为一个"技术尾巴"整组放末尾，符合摄影 prompt 惯例，Flux2 解读更稳。
- ✅ `...shot on Canon EOS R5, 85mm f/1.4, shallow depth of field, Kodak Portra 400.`

### 原则 4：机身与色彩科学不混搭
一次只选一套色彩来源（见第九节认知 1）。

### 原则 5：题材决定档位，别堆砌
按第八节矩阵选**一套**配置，不要把"85mm + 16mm + macro"全堆进去。一张图一个镜头。

### 原则 6：正向描述畸变，禁用 negative
- ❌ 弱：`no distortion`（Flux2 不支持 negative，可能反向触发）
- ✅ 强：`rectilinear, straight vertical lines preserved`

### 🖥️ 竖屏三轴互搏（空间题材独家认知，mega-hall 沉淀）

9:16 竖屏里，**宽 / 深 / 高三轴互相争夺画面像素，不可能同时推到极致**。写空间 prompt 前必须先选这张图主打哪个轴，镜头焦段跟着走：

| 主打 | 焦段配方 | 代价 |
|---|---|---|
| 深+高（纵深高耸） | 16mm + floor level + 强仰角 | 宽被压成夹道 |
| 宽+舒展（宽幅大气） | 20mm + 略低站立视平线 + 中仰 | 纵深与高耸各弱一档 |
| 三轴均衡 ⭐默认 | 18mm + sofa-seat 与站立之间 + 中仰 | 无单项惊艳但不翻车 |

人像/产品题材无此问题（主体单一，无三轴竞争）。

---

## 十一、更新日志

| 日期 | 更新内容 | 来源 |
|---|---|---|
| 2026-05-29 | 初版建立。十节结构：焦段/光圈景深/景别/机位/特殊镜头/产品机位/畸变与画质/题材矩阵/相机品牌/核心原则。沉淀自 interior-luxury、character、penthouse、mega-hall 四个现有 skill 的镜头实战经验 | 通用底座搭建对话 |

未来每次跑出新的镜头/相机效果，把"待验证⚠️"升级为"已验证✅"或"已证失败❌"，并补充触发词措辞与来源题材。
