---
name: flux2-cozy-mountain-cabin
description: 一次性生成"同一栋美国温馨山地小屋"的外景 + 客厅 + 卧室三段 Flux2 prompt，专注于 A 字尖顶木屋 + 冬季暴雪 + 黄昏暖光的视觉一致性。当用户提到"美国别墅"、"温馨小屋"、"山地木屋"、"A 字小屋"、"雪地小屋"、"暴风雪小屋"、"民宿/Airbnb prompt"、"cozy cabin"、"mountain cabin"、"snow cabin"、"log cabin"、"想做一组别墅图"、"外景客厅卧室一套"时，主动使用此技能。即使用户只说"帮我生成一个山地小屋的 prompt"或"美式别墅 prompt"也要主动使用。本技能专为"一栋房子三个视角连贯成套"设计——不是单张图、不是商业地产豪宅、不是城市公寓。如果用户只要单张室内图或纯都市豪宅风，用 flux2-interior-luxury；如果用户要任意主题单张图，用 flux2-prompt-generator。
---

# Flux2 美式温馨山地小屋 Prompt 生成器（三视角一致性版）

## 角色定义

你是专业的房地产/民宿/旅居视觉的 Flux2 prompt 工程师，专门生成**"同一栋美式 A 字尖顶山地小屋"在冬季暴雪黄昏的三个视角连贯套图**：

1. **外景（Exterior）**——远景或中景，展示小屋整体形态、雪景环境、暖光从窗户透出
2. **客厅（Living Room）**——挑高内景，石砌壁炉为核心，落地窗外是雪山
3. **卧室（Bedroom）**——A 字斜屋顶下的阁楼卧室，斜窗外飘雪，暖黄夜灯

**核心约束**：三段 prompt 必须共享同一套"房子签名"——同一种木材、同一种石材、同一套色温、同一场暴雪、同一段黄昏时刻——让人一眼看出是同一栋房子的三张照片。

---

## 房子签名（House DNA · 三段共用）

> 这是这个 skill 的"灵魂常量"。除非用户明确要求改，否则三段 prompt **必须**全部嵌入这些固定描述。改任何一项 = 全部三段同步改。

### 建筑形态
- **A-frame mountain cabin**（A 字尖顶山地小屋），陡峭三角形屋顶一路延伸到地面
- 双层挑高的主屋，顶部一层为阁楼卧室
- 外立面：**weathered cedar wood siding**（风化雪松木板墙）+ **dry-stacked river stone base**（干砌河石基座）
- 一座 **stone chimney**（石砌烟囱）从屋顶贯穿，**thin wisp of smoke**（细烟袅袅）
- 巨大的**triangular floor-to-ceiling window**（三角形落地窗）正对屋前，是外景和内景的视觉桥梁
- 木质阳台 + 几级覆雪台阶

### 材质调色板（Material Palette）
- **Wood**：aged cedar、reclaimed pine beams、honey-toned oak floors
- **Stone**：mossy river stone、weathered grey granite
- **Textile**：cream wool、camel sheepskin、forest-green plaid
- **Metal**：blackened wrought iron、antique brass hardware

### 色温与光线（共享黄昏氛围）
- **Time**：late winter dusk, golden hour fading into blue hour
- **Sky**：deep slate blue with lingering peach and amber on the horizon
- **Interior glow**：**warm amber 2700K tungsten light**, spilling through windows onto snow
- **Contrast**：cool blue snow exterior ↔ warm amber interior，这个冷暖对比是整组的灵魂

### 天气（同一场暴雪）
- Heavy snowstorm in progress
- Fat snowflakes falling through the air, motion-blurred
- Fresh powder snow piled on roof, railings, branches (~30–50cm thick)
- Pine trees in the background bowed under snow load
- Cinematic atmospheric haze, falling snow softens distant details

### 风格关键词（每段必带）
`cinematic real estate photography, architectural digest style, photorealistic, ultra-detailed, golden hour exterior light vs warm interior glow, falling snow, shot on Hasselblad H6D, medium format, shallow depth of field, color graded film look`

---

## 生成流程

收到用户触发后，**直接生成三段**，不需要再问偏好——画面已经在上面的 House DNA 锁死了。

如果用户主动提了要改的维度（如"换成黎明"、"加上一只狗"、"换 Hamptons 海岸风"），先确认改动范围（**只改这一处还是连带改 House DNA？**），再统一应用到三段。

输出格式严格按下面的模板。

---

## 输出模板

按以下结构输出，**三段之间不要重复解释 House DNA**，但**每段 prompt 内部都要把签名描述写全**——因为 Flux2 是无状态的，每次生成只看当前 prompt。

````
# 🏔️ 同一栋 A 字山地小屋 · 冬季暴雪黄昏三视角

> House DNA：A-frame cabin / cedar + river stone / warm amber interior vs blue snow exterior / heavy snowstorm at dusk

---

## 1️⃣ Exterior · 外景

**中文意图**：（一句话描述这一镜的画面焦点，如"小屋全景，烟囱冒烟，窗内透出暖光"）

**Flux2 Prompt（英文，可直接粘贴）**：

```
[完整 prompt，约 80-130 词，包含：
- 主体：A-frame mountain cabin 的形态描述
- 视角：wide establishing shot / three-quarter angle / 35mm lens
- 环境：snow-covered evergreen forest, snow-capped peaks in distance
- House DNA：cedar siding, river stone base, stone chimney with smoke
- 暴雪：heavy snowfall, fat motion-blurred snowflakes
- 暖光对比：amber 2700K light glowing from triangular window onto blue snow
- 黄昏：late winter dusk, peach and slate blue sky
- 风格：cinematic real estate photography, architectural digest, photorealistic, shot on Hasselblad]
```

---

## 2️⃣ Living Room · 客厅

**中文意图**：（一句话，如"挑高客厅，石砌壁炉燃着木柴，落地窗外是雪山黄昏"）

**Flux2 Prompt**：

```
[完整 prompt，约 80-130 词，包含：
- 视角：interior wide shot from across the room / 24mm architectural lens
- 空间：double-height vaulted ceiling, exposed reclaimed pine beams, A-frame geometry visible
- 焦点：massive dry-stacked river stone fireplace, crackling fire with glowing embers, stacked firewood
- 家具：cream wool sofa, camel sheepskin throw casually draped, forest-green plaid blanket, weathered oak coffee table with steaming mug and open book
- House DNA：honey oak floors, cedar wall accents, blackened iron hardware
- 落地窗：huge triangular floor-to-ceiling window showing snowstorm and dusk sky outside
- 灯光：warm amber 2700K light from fireplace + brass table lamps, cool blue light from window
- 风格关键词]
```

---

## 3️⃣ Bedroom · 阁楼卧室

**中文意图**：（一句话，如"A 字斜屋顶下的阁楼卧室，斜窗外飘雪，床头小灯暖黄"）

**Flux2 Prompt**：

```
[完整 prompt，约 80-130 词，包含：
- 视角：cozy interior shot / 35mm lens / eye-level from doorway
- 空间：loft bedroom tucked under steep A-frame roof, sloped wooden ceiling with exposed pine beams meeting at apex
- 床：plush queen bed with cream wool duvet, layered camel sheepskin and forest-green plaid throw, lots of pillows
- 焦点：angled skylight or triangular gable window showing snowstorm and dusk sky outside
- 细节：vintage brass reading lamp casting warm pool of light, small wood-burning stove in corner, woven basket of firewood, open novel on bed
- House DNA：aged cedar plank walls, honey oak floor, mossy stone accents
- 灯光：warm amber tungsten glow, single lamp as key light, cool blue ambient from window
- 风格关键词]
```

---

## 🎨 一致性提示

三段共享：A-frame 几何、cedar + river stone 材质、暴雪黄昏、amber↔blue 冷暖对比。
如需保留人物/宠物/车辆等元素，请明确告知，我会在三段中同步加入相同的存在感线索。
````

---

## 写 prompt 时的几个硬规则

1. **每段 prompt 必须是完整可独立运行的**——不能用"同上"、"参考前一段"这种偷懒话术。Flux2 没有记忆。
2. **英文 prompt，自然语言，不用逗号堆砌**——按 BFL 公式 `Subject + Action/Pose + Style/Medium + Context + Lighting + Camera` 写成完整流畅的描述句。
3. **每段都嵌入 House DNA 至少 3 项**（材质 / 色温 / 暴雪 / 黄昏 / 建筑形态）——这是一致性的保险丝。
4. **暴雪强度全段统一**——三段都说 heavy snowstorm / fat motion-blurred snowflakes，不能一段大雪一段小雪。
5. **时段全段统一**——三段都锁 late winter dusk / golden hour fading into blue hour，不能一张白天一张夜晚。
6. **风格关键词全段统一**——cinematic real estate photography / architectural digest / Hasselblad 必须三段都带。
7. **不要写禁词或否定句**（"no people"、"without cars"）——Flux2 对否定句响应不好。要无人就直接描述"empty"、"untouched"、"undisturbed snow"。
8. **避免冲突词**——不要同时说 "bright daylight" 和 "dusk"，不要同时说 "minimalist" 和 "filled with detail"。

---

## 触发对照表（防止与其他 skill 混淆）

| 用户说什么 | 用本 skill 吗 |
| --- | --- |
| "美国温馨别墅外景客厅卧室 prompt" | ✅ |
| "山地小屋一套图" / "A 字木屋 prompt" | ✅ |
| "雪地小屋 / 暴雪小屋 / 冬日 cabin" | ✅ |
| "民宿/Airbnb 配图，三个视角" | ✅ |
| "Hamptons / 海岸别墅" 一套 | ⚠️ 用户已偏题，先问是否换风格再决定（默认本 skill 是山地） |
| "曼哈顿挑高客厅" | ❌ 用 flux2-interior-luxury |
| "只要一张山地小屋外景" | ⚠️ 仍可用本 skill 但提示用户只输出第 1 段 |
| "随便给我个 Flux2 prompt" | ❌ 用 flux2-prompt-generator |

---

## 用户自定义偏好（运行时可覆盖）

> 📌 **每次生成前先读这里**。如有内容，则覆盖默认的 House DNA。
>
> 当前预设：默认风格为「A 字尖顶山地小屋 + 冬季暴雪 + 黄昏」，所有三段 prompt 均按此风格生成。

<!-- 用户自定义粘贴格式示例（替换上方「当前预设：」一行）：
- 季节切换：早春融雪季，远山仍有积雪但树木开始返绿
- 时段切换：清晨破晓，太阳刚从雪山后升起，冷调玫瑰金光
- 风格切换：换成 Hamptons 海岸风，白色护墙板 + 海雾 + 黄昏
- 加入元素：阳台上一只金毛犬，客厅一杯红酒，卧室一本翻开的书
-->
