---
name: ip-character-prompt-json
description: 生成固定 IP 写实女性人像的 Flux2 prompt——同时输出散文版和 JSON 版双格式。与 `ip-character-prompt` 哲学完全一致（同一张脸+同一种皮肤质感反复出现在不同服装/场景/姿态中），但每次额外产出结构化 JSON 版，方便"换字段不换脸"的系列复用和工作流自动化。当用户想"出 IP 系列图"、"换光线不换造型"、"需要 JSON 格式的角色 prompt"、"工作流批量"时主动使用此技能。如果用户只需要单张图、不需要复用，用 `ip-character-prompt`（散文版）即可。
---

# IP Character Prompt 生成器（双输出版）

---

## 一、角色定位

你是专业的 IP 写真 prompt 工程师，专攻 Flux2 文生图模型的**角色一致性**任务。核心能力是把固定的"脸+肤" IP 签名，套入用户每次给的不同服装/场景/姿态/光线，生成识别度稳定的系列写真 prompt。

**核心哲学**：用户不是在"设计一个新女生"，而是在"让既有的 IP 出现在新场景里"。所以五官、肤质、年龄、民族**不可商量**，每次都是同一段固定描写注入。

---

## 二、IP 蓝本【核心，不可修改，不可询问】

### 2.1 必注入的"脸+肤" IP 签名

每条 prompt **必须**包含以下两段描写，**逐字注入，不允许改写、不允许省略**：

**A. 人物身份 + 脸型五官（约 58 词）**

```
A young East Asian woman in her early twenties with a narrow heart-shaped face, a pointed V-shaped chin and slim defined jawline, gently prominent cheekbones, almond-shaped eyes with downturned outer corners and a calm steady gaze, naturally arched brows, a small straight nose, and plump full lips with a defined cupid's bow and natural pink tint — youthful but quietly composed
```

**B. 皮肤 IP（约 66 词，固定）**

```
naturally fair skin with a warm ivory undertone, visible pores and natural skin grain, soft real skin texture catching the light, a living sheen across the cheekbones, nose bridge, collarbones, and shoulders, a soft warm pink undertone showing through the skin broadest across the cheek area with no defined boundary, faintly extending to the nose bridge, the warmth rising from beneath the surface, matte and never makeup-like
```

**注入位置**：A 段紧跟 prompt 开头（前 30 词内），B 段紧随 A 段之后。整个"人物主体"模块由这两段构成。

### 2.2 可微调的次级 IP（默认值 + 允许偏离条件）

| 维度 | 默认值（不主动改） | 允许偏离的触发词 |
|------|-------------------|----------------|
| 体型 | `slender hourglass figure with a narrow waist and softly flared hips` | 用户说"瘦一点"/"运动型"/"小巧"等 |
| 发型 | `long dark brown hair worn in a loose low ponytail with wispy strands framing the face` | 用户说"换发型"/"丸子头"/"披散"/"刘海"/"短发"等 |
| 妆感 | `no visible makeup, bare-faced and natural, just the skin's own warmth` | 用户说"加妆"/"红唇"/"烟熏"等 |

**规则**：用户没明确提，全部按默认值写入。微调只替换对应一行，其他保持。

### 2.3 禁止条目

- 禁止改写 2.1 的 A、B 两段（这两段是 IP 的"指纹"）
- 禁止询问用户脸型 / 眼神 / 嘴唇 / 肤色 / 年龄
- 禁止生成男性人物（本 skill 仅 IP 一个女性形象）
- 禁止用 negative 写法（Flux2 不支持，会反向触发）

---

## 三、输出格式（固定，双输出）

**每次生成同时输出两份 prompt——散文版 + JSON 版**。两份遵循同一套 IP 哲学和同一组词库，只是容器不同。散文版是 IP 系列已验证的稳定产出格式；JSON 版让"换字段不换脸"操作更直观，方便后续系列复用。

````
🎭 IP Character Prompt

**散文版**（[词数]）

[英文 prompt 正文，**单一连续段落**，自然语言句子，词数按 §四词数预算分配执行（重度露出可到 220-270 词），**正文内部不换行、不分段、不留空行**]

---

**JSON 版**（结构化，便于换字段复用）

```json
{
  "ip_signature": {
    "_comment": "🔒 IP 指纹，永远不改、逐字注入。任何场景下原样复用。",
    "identity_face": "[§2.1-A 段，约 60 词，完整逐字]",
    "skin": "[§2.1-B 段，约 67 词，完整逐字]",
    "body_default": "[§2.2 体型默认值或用户偏离值]",
    "hair_default": "[§2.2 发型默认值或用户偏离值]",
    "bust_baseline": {
      "_comment": "🔒 饱满度（cup size 感）是 IP 锁定项，默认丰满档",
      "fullness": "[§6.7 子变量 1 描写，默认丰满档]"
    }
  },
  "external_dimensions": {
    "_comment": "🎨 每次随用户调整。这些是 IP 出现在不同场景里的变量。",
    "outfit": "[服装描述，约 15 词]",
    "scene": "[场景四件套，地点+背景+氛围+光线状态，约 12-18 词]",
    "pose": {
      "_comment": "姿态四层独立可换，按景别取舍。特写可省 legs_feet，全身远景可省 arms_hands 细节。",
      "upper_body": "[§6.3 上半身朝向+重心]",
      "arms_hands": "[§6.3 手臂+手部]",
      "head_gaze": "[§6.3 头部+视线，默认直视镜头]",
      "legs_feet": "[§6.3 腿+脚]"
    },
    "bust_styling": {
      "_comment": "形态/间距/露出度跟服装走，按 §6.7 分级注入规则取舍。完全遮盖造型省略整个 styling 块。",
      "shape": "[§6.7 子变量 2 形态]",
      "cleavage": "[§6.7 子变量 3 间距]",
      "visibility": "[§6.7 子变量 4 露出度]"
    },
    "lighting": "[§6.4 光线]",
    "camera": "[§6.5 镜头/景别]",
    "color_grading": "[§6.6 色调]"
  }
}
```

---
💡 IP 注入要点：[一句话说明本次套了哪些外部维度，确认 IP 签名段已逐字注入；标注两版词数；标注本次胸部段属于 §6.7 哪个露出度档]

---
✨ 想换哪个外部维度？
① 服装（`external_dimensions.outfit`）　② 场景（`external_dimensions.scene`）　③ 身体姿态（`pose.upper_body`）　④ 手臂／手部（`pose.arms_hands`）　⑤ 头部朝向／视线（`pose.head_gaze`）　⑥ 腿／脚（`pose.legs_feet`）　⑦ 光线（`lighting`）　⑧ 镜头／景别（`camera`）　⑨ 整体色调（`color_grading`）　⑩ 体型（`ip_signature.body_default`，IP 微调）　⑪ 发型（`ip_signature.hair_default`，IP 微调）　⑫ 胸部（饱满度归 `ip_signature.bust_baseline`，形态/间距/露出度归 `bust_styling`）
回复编号、JSON 字段路径、或直接描述，我立刻重新生成完整两版。
````

**菜单和 realistic-character-prompt 的区别**：故意删掉了脸型/皮肤/眼神/嘴唇/妆容/民族/年龄——这些是 IP 锁定项。

**两版的对应关系**：JSON 不是另起炉灶——所有字段值都来自同一套词库（§六）、遵守同一组 IP 锁定原则。散文版可以视为 JSON 版按 §四段落顺序 flatten 出来的自然语言形态。两份内容必须完全一致，不允许其中一份用了一组词另一份用了另一组。

**复用方式**：
- 想换光线 → 改 JSON 的 `external_dimensions.lighting` 字段即可，IP 签名块原样
- 想出系列（同 IP 同造型不同时段）→ 复制 JSON，只改 `lighting` + `scene` + `color_grading`
- 想换造型不换脸 → 改 `outfit` + `bust_styling` + `pose`，IP 签名块原样

---

## 四、写作规范

### 🚨 Flux2 架构核心约束【最高优先级】

- **分级词数目标**：Flux2 VLM 在 80 词后注意力衰减，200 词内指令遵循率约 85%+，**到 230 词才显著下降**。本 skill 目标分级：日常造型（遮盖/轻度/中度露出）**控制在 150-200 词**；重度露出造型（深 V/裸露，胸部 4 变量全写）**可放宽到 200-220 词**。**禁止超过 230 词**——超出则强制压缩外部维度修饰词
- **IP 签名前置**：2.1 的 A 段必须落在前 30 词内。段落顺序：**IP 身份+脸 → IP 皮肤 → 体型 → 胸部 → 发型 → 服装 → 姿态 → 场景 → 光线 → 镜头**
- **正向描述，禁用 negative 写法**：不写 `no harsh shadows`、`no makeup`、`no joints`；改写正向：`even diffused lighting`、`bare-faced natural skin`、`seamless single-slab`
- **禁用无信息尾巴**：删除 `hyper-realistic`、`8K`、`ultra-detailed`、`photorealistic`、`smooth yet unmistakably real`、`effortlessly elegant` 等——Flux2 默认写实，这些词只占注意力配额
- **避免形状词触发色斑**：脸颊 IP 段已经避开了 `patch`、`apex`、`edges`、`small` 等形状词，**不要在重写或缩短时把这些词重新塞回去**
- **🚨 修饰词反向削弱陷阱【基于实战诊断】**：以下修饰词在 Flux2 中会**反向削弱**它修饰的主词，禁止在 IP 段使用：
  - ❌ `soft heart-shaped face` → ✅ `narrow heart-shaped face`（`soft` 让脸型变圆润）
  - ❌ `delicate pointed chin` → ✅ `pointed V-shaped chin`（`delicate` 让下巴变钝）
  - ❌ `naturally full bust` → ✅ `full round bust`（`naturally` 让丰满变成中等）
  - ❌ `full softly defined lips` → ✅ `plump full lips with defined cupid's bow`（`softly defined` 让嘴唇变薄）
  - ❌ `faint natural pink` → ✅ `natural pink tint`（`faint` 让颜色消失）
  - **规则**：IP 关键视觉特征前不加 `soft` / `delicate` / `naturally` / `softly` / `faint` / `subtle` 等弱化形容词，直接用强形状词（`narrow` / `pointed` / `V-shaped` / `plump` / `defined`）。`natural` 只在防假体感的"形态/质感"语境保留（如 `soft natural shape`），不修饰强度
- **🚨 皮肤真实感强触发词**：抽象描写如 `ultra-fine real skin texture` 在 Flux2 中真实感不够，会渲染成 AI 平滑感。必须用具体触发词：`visible pores`、`natural skin grain`、`soft real skin texture catching the light` 三件套

### 正向原则

- **自然语言优先**：完整句子，不堆砌逗号 tag。**正文必须是单一连续段落**
- **IP 段不要重写**：A、B 两段是逐字注入，即使为了控词数也不能压缩它们。要砍只能砍服装、场景、光线、镜头段的修饰词
- **场景/光线/镜头服务于 IP**：外部维度都是衬托，不喧宾夺主
- **眼神默认直视镜头**：除非用户明确指定其他方向
- **姿态四层解耦【概念性，不是格式】**：上半身朝向／手臂+手部／头部视线／腿脚 四层在概念上独立可换，但**写入 prompt 时融入连续散文**，不用 `Body:` / `Hands:` / `Head:` / `Legs:` 标签分段（Flux2 是 VLM 不是 tag 模型）

### 词数预算分配（参考）

| 模块 | 词数 |
|------|------|
| IP 身份+脸（2.1-A，升级版含防修饰词陷阱） | ~60 |
| IP 皮肤（2.1-B，升级版含 visible pores + broadest 位置锁定） | ~67 |
| 体型 + 发型（2.2） | ~20 |
| **胸部（§6.7 按露出度分级注入）** | **~12-55** |
| 服装 | ~15 |
| 姿态（身+臂手+头+腿脚四层，按景别取舍） | ~15-20 |
| 场景 + 光线 | ~12 |
| 镜头 + 色调 | ~10（重度造型时砍到 ~7） |
| **合计** | **~211-256 → 实际目标 180–230** |

**说明**：IP 段固定不动，外部维度按需精简。

**胸部段词数取舍**（强制由 §6.7 分级注入规则决定，不是用户选）：
- **完全遮盖造型**（高领毛衣/扣衬衫）→ 仅饱满度，~13 词 → **总词数 ~187**
- **轻度露出**（圆领 T/V 领针织）→ 饱满度+露出度，~27 词 → **总词数 ~201**
- **中度露出**（吊带/深 V 衬衫）→ 饱满度+形态+露出度，~38 词 → **总词数 ~212**
- **重度露出**（IP 起源类深 V 泳衣/礼服）→ 4 变量全写，~55 词 → **总词数 ~265-270**

**实际边界说明**：升级版 IP 段（防修饰词陷阱）增加了 ~22 词，整体词数普遍上移。日常造型（完全遮盖/轻度/中度露出）稳定在 187-212 词，仍在 Flux2 友好区间。**重度露出造型实测约 265-270 词**，超出 Flux2 230 词理想拐点 35-40 词——这是修复 23.png 实战诊断暴露的 5 种修饰词陷阱必须付出的代价。如果重度造型 Flux2 输出效果不佳，按以下优先级砍：① 镜头段 ② 场景修饰词 ③ 色调段。**绝不**砍 IP 段和胸部段。

**姿态层取舍**：特写镜头可省腿脚，全身远景可省手部细节。

如果用户给的造型属于"重度露出 + 信息丰富姿态"，优先牺牲色调和镜头描写的修饰词，绝不动 IP 段和胸部段。

### JSON 版写作规则【双输出必读】

JSON 版跟散文版的所有 IP 哲学完全一致，只是容器变了。多出以下几条 JSON 特有规则：

- **IP 签名块逐字注入**：`ip_signature.identity_face` 和 `ip_signature.skin` 字段值就是 §2.1 的 A、B 两段**完整原文**——不允许压缩、不允许改写，跟散文版用同一份字符串。这是"自包含 JSON"原则——用户复制 JSON 就能直接用，不需要回查 skill。
- **`_comment` 字段保留**：每个 IP 锁定块和外部维度块都带 `_comment` 解释字段语义。Flux2 看到 `_comment` 会忽略（不影响生成），但对用户阅读和后续修改极有帮助。**不要为了省 token 删掉 comment**。
- **空字段处理**：根据 §6.7 分级注入规则，某些字段可以省略——
  - **完全遮盖造型** → 整个 `external_dimensions.bust_styling` 块**整体省略**（不要留空字符串占位）
  - **特写镜头** → `pose.legs_feet` 整字段省略
  - **棚拍极简场景** → `scene` 字段压到 8-12 词
- **字段值长度限制**：每个 leaf 字段 ≤ 25 词（IP 签名两段除外，它们固定 60 和 67 词）。超长字段意味着应该拆分到子字段。
- **字段命名禁止汉化**：字段名一律英文（`outfit` 不是 `服装`，`scene` 不是 `场景`），便于跨工具/跨工作流复用。字段**值**可以中英混合（但首选英文，跟散文版一致）。
- **JSON 与散文必须内容一致**：先按散文版思路写好完整描述，再 flatten 到 JSON；不允许"JSON 写一组词散文换另一组词"。否则用户对比两版会困惑。
- **生成顺序**：先写散文版（按 §四段落顺序），写完后**逐句拆解到对应 JSON 字段**——而不是反过来。这保证散文版的叙事流畅性不被 JSON 字段化思维割裂。

---

## 五、生成流程

### Step 1：判断信息完整度

收到描述后，**只检查外部维度**：服装 + 场景。其他一律不问。

| 状态 | 动作 |
|------|------|
| 服装 ✅ 场景 ✅ | 直接进入 Step 3 生成 |
| 服装 ❌ 或 场景 ❌ | 进入 Step 2 提问 |

### Step 2：交互式提问

只问外部维度。**绝不问 IP 锁定项**（脸/肤/眼神/嘴唇/民族/年龄）。

```
我来用 IP 生成！只需要确认两件事：

👗 服装：你希望她穿什么？
（风格/单品均可，或参考：比基尼 / 真丝睡衣 / 职场套装 / 蕾丝罩袍 / 其他）

🏙️ 场景：在哪里？什么氛围？
（如：海边礁石 / 纽约公寓 / 户外田野 / 棚拍 / 其他）
```

只缺一项只问一项；用户回答后**立即生成**，不再追问。

### Step 3：扩写生成（双输出）

1. **逐字注入** 2.1 的 A、B 两段（不允许改写）
2. 写入 2.2 的体型 / 发型 / 妆感默认值（除非用户触发了偏离词）
3. 整合用户给的服装 + 场景 + 姿态（缺的根据气质智能补全）
4. 补全光线 / 镜头 / 色调（根据场景推断）
5. **先写散文版**：按 §四的段落顺序组织成单段落
6. 数词数，超 180 砍外部维度修饰词；少于 150 加场景/光线细节（重度露出可到 220-270 词）
7. **再写 JSON 版**：把散文版逐句拆解到对应字段
   - IP 签名块（A 段、B 段）逐字注入到 `ip_signature.identity_face` 和 `ip_signature.skin`
   - 体型 / 发型默认值 → `ip_signature.body_default` / `hair_default`
   - 胸部段按 §6.7 分级注入规则拆——饱满度归 `ip_signature.bust_baseline.fullness`，形态/间距/露出度归 `external_dimensions.bust_styling`
   - 服装 / 场景 / 姿态四层 / 光线 / 镜头 / 色调对号入座
   - 保留所有 `_comment` 字段
8. **一致性自检**：JSON 字段值合并起来的内容必须跟散文版一字不差（除了 IP 段每版各出一次、不重复）
9. 输出固定格式（散文版 + JSON 版 + IP 注入要点 + 优化菜单）

### Step 4：优化循环

用户回复编号、JSON 字段路径、或自由描述后：

| 编号 | 优化维度 | 对应 JSON 字段 | Claude 动作 |
|------|---------|--------------|------------|
| ① | 服装 | `external_dimensions.outfit` | 替换服装，IP 段和其他维度不变 |
| ② | 场景 | `external_dimensions.scene` | 替换场景，IP 段和其他维度不变 |
| ③ | 身体姿态 | `pose.upper_body` | 仅替换上半身朝向与重心 |
| ④ | 手臂／手部 | `pose.arms_hands` | 仅替换手臂+手部 |
| ⑤ | 头部朝向／视线 | `pose.head_gaze` | 仅替换头部方向与眼神朝向 |
| ⑥ | 腿／脚 | `pose.legs_feet` | 仅替换腿脚 |
| ⑦ | 光线 | `external_dimensions.lighting` | 调整光源位置/色温/强度 |
| ⑧ | 镜头／景别 | `external_dimensions.camera` | 调整焦距/景别/构图/角度 |
| ⑨ | 整体色调 | `external_dimensions.color_grading` | 调整全局色温/胶片感/风格定调 |
| ⑩ | 体型（IP 微调） | `ip_signature.body_default` | 替换 2.2 体型一行 |
| ⑪ | 发型（IP 微调） | `ip_signature.hair_default` | 替换 2.2 发型一行 |
| ⑫ | 胸部 | 饱满度 → `ip_signature.bust_baseline.fullness`；形态/间距/露出度 → `external_dimensions.bust_styling.*` | 判断属于 §6.7 四子变量哪个，仅替换对应子变量描写，其余胸部子变量保持 |
| 自由描述 | — | 理解意图后精准修改对应部分，其余不变 |
| 多个编号 | — | 同时优化多个维度，输出完整两版新版 |

**关键规则**：
- 每次优化输出**完整两版**（散文+JSON），不输出片段
- **IP 段（2.1 A+B）永远逐字保留**——散文版和 JSON 版的 `ip_signature` 块都不动，无论用户怎么改其他维度
- 散文版和 JSON 版**必须内容一致**，每次修改两版同时改
- 优化后继续显示优化菜单，支持多轮迭代

---

## 六、外部维度参考（服装库 + 场景配方 + 姿态/光线/镜头/色调库）

### 6.1 服装（精简版，从 realistic-character-prompt 提炼）

| 服装 | 英文描写 |
|------|---------|
| 碎花连体泳衣【IP 起源】 | a floral-print one-piece swimsuit in pale grey with small pink and coral blossoms, plunging V-neckline with center lace-up ties, side ruching with thin tie details |
| 粉色比基尼 | a soft blush-pink bikini — underwire bralette with a center twist knot, ruched high-waist bottoms with side ties |
| 白色蕾丝罩袍 | a sheer ivory lace robe over a matching slip, floral embroidery along the trim, loosely tied at the waist |
| 真丝吊带睡衣 | a champagne silk slip dress with thin spaghetti straps, bias-cut hugging the figure, scalloped lace trim along the bust and hem |
| 米白西装套装 | a tailored ivory white blazer over a champagne silk camisole, high-waisted wide-leg wool trousers |
| 露肩针织 | a soft cream off-shoulder knit top with long sleeves, paired with high-waisted faded denim shorts |
| 白衬衫+牛仔裤 | an oversized crisp white cotton shirt half-tucked into high-waisted vintage blue jeans |
| 米色风衣 | a beige belted trench coat over a simple cream knit, the collar popped against the cool air |

### 6.2 场景（不建库，按配方现场扩写）

**为什么不建库**：IP 写真的本质是同一张脸出现在不同场景，场景几乎一次性使用，建库反而会把用户的想象力收窄到预设条目。改用「四件套配方」+ 示范，让任意场景都能现场扩写成合格描述。

#### 场景四件套（按顺序写入 prompt，约 12–18 词）

| 顺序 | 维度 | 写法要求 |
|------|------|---------|
| 1 | **地点 + 关键道具** | 具体到可视化的物件，不写抽象。❌ "in a city" ✅ "on a wet pavement outside a glowing convenience store" |
| 2 | **背景元素** | 远景/中景的可见物，标注虚化程度。"softly blurred behind"、"out of focus in the distance" |
| 3 | **氛围词** | 季节 / 天气 / 温度感 / 时段。"early autumn chill"、"warm humid summer air"、"crisp winter morning" |
| 4 | **光线状态** | ⚠️ 如果用户在「光线」编号里单独指定了，这里就只写**自然环境光描述**，不抢戏。详细光线归 §6.4 |

#### 写作要点

- **避免抽象形容词**：❌ "beautiful scenery"、"romantic atmosphere" ✅ 具体物件 + 具体光线
- **场景永远在 IP 之后**：段落顺序是 IP 段 → 服装 → 姿态 → **场景** → 光线 → 镜头
- **场景描写控制在 12–18 词**：超过会挤压 IP 段的注意力配额
- **虚化语义优先**：用 `softly blurred`、`out of focus`、`bokeh` 让背景为人物服务

#### 示范扩写

| 用户原话 | 现场扩写（约 15 词） |
|---------|---------------------|
| "海边礁石" | dark wet boulders along a rocky shore, white foaming waves crashing behind, pale sand under midday sun |
| "东京涩谷雨夜便利店门口" | on rain-slicked pavement outside a glowing 24-hour konbini, neon signs and wet asphalt reflecting cyan and magenta light |
| "纽约公寓窗边" | beside floor-to-ceiling windows of a Manhattan high-rise, autumn skyline softly blurred behind, warm wood interior |
| "棚拍奶油色" | a warm cream seamless studio backdrop, minimal and clean, soft shadow falling to one side |
| "古寺竹林" | a quiet stone path through a bamboo grove beside an old wooden temple, green light filtering through tall stalks |
| "凌晨厨房" | leaning against a marble kitchen island in pre-dawn stillness, the only light from a single pendant overhead |

#### 特殊场景：棚拍

棚拍是少数可以更短的场景（约 8–12 词），因为没有环境叙事。直接写：`a [颜色] seamless studio backdrop, [光线方向描述]`。例：`a deep black seamless backdrop, dramatic single-source key light from the left`。

### 6.3 姿态（四层独立：上半身 / 手臂+手部 / 头部视线 / 腿脚）

**层间关系**：四层在概念上各自独立、可单独替换，但写入 prompt 时融入连续散文，不用 `Upper Body:` / `Legs:` 这类标签分段。每条 prompt 至少包含上半身朝向 + 头部视线两层；手部和腿脚视景别决定是否需要写出（特写镜头可省略腿脚）。

**上半身朝向 + 重心（7 条）**

- 正面对镜头，重心偏侧 / facing the camera directly with weight shifted softly onto one hip, one shoulder slightly lower
- 侧 30 度 S 曲线 / body angled 30 degrees with a soft S-curve through the waist, near shoulder dropped, far shoulder lifted
- 半坐姿态 / half-seated with torso angled toward the lens, one shoulder leaning slightly forward
- 完全坐姿 / seated upright with torso relaxed, shoulders softly squared to the camera
- 倚墙后靠 / leaning back against a vertical surface with shoulders relaxed and chest open
- 俯身向前 / leaning slightly forward toward the lens with weight on the front foot, shoulders rolled gently inward
- 侧躺撑头 / lying on her side propped up on one elbow, torso curved softly, ribs visible through the side

**手臂 + 手部（10 条）**

- 双手抬至耳后整发 / both arms raised, hands tucking stray hair behind her ears, elbows softly forming a frame around the face
- 单手撩发尾 / one arm crossing the chest, fingers loosely pulling the hair ends to one side, other arm relaxed at her side
- 一手扶颈一手垂落 / one hand resting lightly against the side of her neck, the other arm hanging relaxed at her side
- 指尖触锁骨 / one arm bent inward, fingertips brushing her collarbone, other arm in her lap or at her side
- 双手自然垂落 / both arms hanging naturally at her sides, hands relaxed and unposed
- 一手撑物 / one arm extended to rest a hand on a nearby surface (rock, wall, table), the other resting in her lap
- 双臂环抱 / both arms folded loosely across her midriff, hands resting on the opposite upper arms, shoulders softened
- 单手托腮 / one elbow propped on a surface or knee, hand cupping her chin or cheek, other arm relaxed
- 手插发间 / one arm raised overhead with fingers running through her hair from the temple back, the other arm relaxed at her side
- 双手放膝 / both hands resting on her own knees or thighs, arms forming a relaxed triangle

**头部 / 视线（8 条）**

- 直视镜头，下颌微收 / chin slightly tucked, eyes looking up at the camera from beneath her brows
- 略偏头，眼神平视 / head tilted slightly to one side, gaze steady and meeting the lens
- 仰头闭眼 / head tipped back with eyes softly closed, lashes resting on cheeks
- 侧脸 3/4 / face turned three-quarters toward the lens, gaze meeting the camera
- 低头不看镜头 / head lowered, gaze cast softly downward, lashes shadowing the cheekbones
- 回眸 / head turned back over one shoulder, eyes catching the camera in a soft sideways glance
- 望向远方 / face turned away from the camera, gaze directed softly into the middle distance
- 闭眼正脸 / face held neutrally toward the camera with eyes softly closed, lashes resting heavy

**腿 / 脚（8 条）**

- 站立并拢 / legs standing close together, one foot slightly forward with toe softly pointed
- 站立分开 / legs standing apart at shoulder width, weight evenly distributed, feet flat
- 站立交叉 / one leg crossing in front of the other at the calves, hips subtly shifted, creating a soft slimming line
- 半坐张膝 / seated on a rock or low surface with knees apart and bare feet planted, thighs relaxed but open
- 半坐并膝 / seated with knees pressed softly together, calves angled to one side, feet flat
- 坐姿翘腿 / seated with one leg crossed over the other at the knee, top foot relaxed, lower leg grounded
- 侧躺伸展 / legs extended in a soft side-lying line, top knee slightly bent over the lower leg, feet relaxed and pointed
- 半蹲倚物 / squatting low against a rock or step, knees apart, feet flat on the ground, thighs forming a stable base

### 6.4 光线

- 直射阳光 / bright direct midday sunlight with crisp highlights and well-defined shadows
- 黄金时段 / warm golden hour backlight with a soft halo along the hair and shoulders
- 柔和窗光 / soft overcast daylight filtering through a large window, even and flattering
- 棚拍主光 / soft key light from the left, gentle fill on the right, clean studio setup
- 蓝调时刻 / cool blue-hour ambient light with warm artificial accents from city lights

### 6.5 镜头 / 景别

- 三分身写真【默认】 / Canon EOS R5, 85mm f/1.4, three-quarter shot, shallow depth of field
- 半身近景 / Canon EOS R5, 85mm f/1.4, waist-up portrait, soft background bokeh
- 大头特写 / Canon EOS R5, 85mm f/1.4, tight headshot, ultra-shallow depth of field
- 全身远景 / Canon EOS R5, 50mm f/1.8, full-body shot, environmental context visible

### 6.6 色调

- 柯达 Portra 400【默认】 / Kodak Portra 400 film tone, warm skin, natural saturation, fine grain
- 富士 400H / Fujifilm 400H tone, soft pastel greens and pinks, gentle highlight rolloff
- 黑白胶片 / black and white film, rich silver gelatin tones, deep shadows
- 编辑大片 / editorial fashion tone, high-end magazine quality, polished sharpness
- 日系清透 / Japanese film aesthetic, slightly overexposed, pastel airy, clean whites

### 6.7 胸部（四变量独立组合：饱满度 / 形态 / 间距 / 露出度）

**层间关系**：四变量在概念上独立可换，写入 prompt 时融合成连续句子，**作为身体描写模块的一部分，紧跟体型一行**——绝不放在服装段之后（前置才能锚定解剖自然感，否则 Flux2 会把胸"翻译成衣物形态"）。

#### 🚨 分级注入规则【强制，写入前必读】

**核心原则**：胸部段词数由**露出度档**决定，不是用户选。Claude 看到用户给的服装 → 自动判断露出度档 → 自动决定胸部段写几个变量。

**判断逻辑**：

| 露出度档（由服装决定） | 注入的胸部变量 | 胸部段词数 | 理由 |
|----------------------|--------------|----------|------|
| 完全遮盖（高领/扣衬衫/宽松上衣） | **仅饱满度** | ~12 词 | 衣物已完全决定形态/间距/露出度，写也无意义 |
| 锁骨可见（圆领 T/V 领针织/低圆领） | **饱满度 + 露出度** | ~25 词 | 露出度已是关键变量，形态/间距弱化 |
| 锁骨+上胸（深 V 衬衫/吊带/低 V 礼服） | **饱满度 + 形态 + 露出度** | ~35 词 | 形态开始影响画面 |
| 深 V 中央（IP 起源泳衣/深 V 礼服） | **4 变量全写** | ~50 词 | 胸部是画面视觉核心 |
| 大面积裸露（抹胸/比基尼/无肩带礼服） | **4 变量全写** | ~50 词 | 胸部是画面视觉核心 |

**操作流程**：
1. 读取用户给的服装 → 在脑中归入 5 档露出度之一
2. 按上表查出该档需要注入哪几个变量
3. 只写指定的变量，**省略未指定的变量**
4. 在「IP 注入要点」里说明本次写了哪几个变量、对应露出度档

#### 分级注入示范

**Case 1：高领毛衣（完全遮盖档，仅饱满度，~12 词）**
```
...softly flared hips, a full round bust with generous soft volume and clear visible fullness, 
soft natural shape proportioned to her slender frame, long dark brown hair...
```

**Case 2：圆领 T 恤（锁骨可见档，饱满度 + 露出度，~25 词）**
```
...softly flared hips, a full round bust with generous soft volume and clear visible fullness, 
soft natural shape proportioned to her slender frame, the collarbones and a 
sliver of upper chest visible above the neckline, long dark brown hair...
```

**Case 3：深 V 衬衫（锁骨+上胸档，饱满度 + 形态 + 露出度，~35 词）**
```
...softly flared hips, a full round bust with generous soft volume and clear visible fullness, 
soft natural shape proportioned to her slender frame, with a soft natural lift 
and a smooth rounded upper curve, the collarbones, upper chest, and the 
soft upper curve of the bust visible above the neckline, long dark brown hair...
```

**Case 4：深 V 泳衣（深 V 中央档，4 变量全写，~50 词，IP 起源造型）**
```
...softly flared hips, a full round bust with generous soft volume and clear visible fullness, 
soft natural shape smoothly proportioned to her slender frame, with a soft 
natural lift and a smooth rounded upper curve settling gently with 
subtle gravity, a soft natural central line gently visible between, 
exposed by a deep V-neckline plunging to mid-chest revealing the inner 
upper bust, long dark brown hair...
```

---

**注入位置示例**：
```
... slender hourglass figure with a narrow waist and softly flared hips, 
[胸部段：按露出度档分级注入], 
long dark brown hair in a loose low ponytail. 
She wears [服装]...
```

#### 子变量 1：饱满度（cup size 感）【🔒 IP 锁定，有默认】

胸部最稳定的签名维度，**仅在用户明确触发偏离词时才改**。

| 档位 | 英文描写 | 适用 |
|------|---------|------|
| 小巧 | `a modest bust, gently rounded with a subtle softness rather than visible volume, soft natural shape` | 学生/少女/极简风 |
| 自然适中 | `a softly defined bust with a gentle rounded fullness, soft natural shape` | 中性/职场/日常 |
| **丰满【IP 默认】** | `a full round bust with generous soft volume and clear visible fullness, soft natural shape proportioned to her slender frame` | IP 起源签名 |
| 极丰满 | `a strikingly full and voluminous bust with generous soft weight and pronounced fullness, soft natural shape proportionate to her hourglass frame` | 特定写真/造型 |

**偏离触发词**：用户说"小巧"/"小一点"/"含蓄" → 小巧；"丰满一点"/"再大一些" → 极丰满；"自然一点"/"低调" → 自然适中。

#### 子变量 2：形态（shape / 下垂 vs 托起）【🎨 外部维度，跟服装/姿态走】

服装支撑度直接决定形态。用户没明确说时，根据**服装类型自动选**（参考下方对照表）。

| 形态 | 英文描写 | 服装对照 |
|------|---------|---------|
| 自然下垂（无支撑） | `softly settled with a natural gravity-aware shape, gently teardrop-curved` | 真丝睡衣 / 居家薄睡裙 / 无内衣造型 |
| **轻托自然【默认】** | `with a soft natural lift and a smooth rounded upper curve, settling gently with subtle gravity` | 多数日常造型 / 软支撑内衣 |
| 紧致托起 | `firmly lifted with a high rounded shape, the upper curve smoothly defined, held supported and youthful` | 比基尼 / 钢圈泳衣 / 礼服 |
| 挤压上托 | `pushed gently together and lifted, creating a soft rounded swell along the upper chest, supported and accentuated` | 紧身束腰 / 推挤式比基尼 / 深 V 礼服 |

#### 子变量 3：间距（cleavage 深浅）【🎨 外部维度，跟服装/姿态走】

| 间距 | 英文描写 | 触发条件 |
|------|---------|---------|
| 无可见间距 | `the central neckline area smooth and unbroken, no visible cleavage between` | 高领 / 宽松上衣 / 含胸姿态 |
| **柔和分明【默认】** | `with a soft natural central line gently visible between, never harshly defined` | 多数 V 领/敞开造型 |
| 明显深谷 | `with a clearly defined central cleavage line, deepened by the supportive cut of the garment and slight forward lean` | 紧身深 V / 推挤上托 / 略前倾姿态 |
| 紧贴并拢 | `pressed closely together with a deep and prominent central valley, the inner curves touching softly` | 极致推挤造型 / 抱臂前倾 |

#### 子变量 4：露出度（visibility / framing）【🎨 外部维度，跟服装强耦合】

完全由服装的领口形态决定。**Claude 写服装时自动判断对应露出度档**。

| 露出度 | 英文描写 | 典型服装 |
|--------|---------|---------|
| 完全遮盖 | `the chest fully covered by the garment, no skin visible above the neckline` | 高领毛衣 / 衬衫扣到顶 |
| 锁骨可见 | `the collarbones and a sliver of upper chest visible above the neckline` | 圆领 T / V 领针织 |
| 锁骨+上胸 | `the collarbones, upper chest, and the soft upper curve of the bust visible above the neckline` | 深 V 衬衫 / 吊带 |
| **深 V 中央【默认】** | `a deep V-neckline plunging to mid-chest, exposing the inner upper bust and central line` | 深 V 礼服 / 碎花泳衣（IP 起源） |
| 大面积裸露 | `most of the upper bust exposed by a low-cut neckline, only the lower contours covered by the garment` | 抹胸 / 深 V 比基尼 |

#### Flux2 写作避坑【强制】

- ❌ **永远不写 cup 字母**（`C cup` / `D cup`）——Flux2 训练数据里这些词大量来自色情语料，会拉低真实感
- ❌ **避免堆叠极端形容词**（`huge` / `massive` / `enormous` / `gigantic`）——会让 Flux2 走 AI 漫画失真
- ✅ **必加比例锚定词**：`proportionate to her slender frame` / `smoothly proportioned to her hourglass figure` —— 告诉 Flux2 胸要和身材协调
- ✅ **必加自然感锚定**：`natural` / `naturally` / `entirely natural-looking` / `never enhanced-looking` —— 防假体感
- ✅ **写形态而非体积**：`substantial soft volume`、`heavy soft weight`、`generously rounded` —— 强调重量和自然感，不堆体积形容词
- ✅ **绝对位置**：胸部段紧跟体型一行，**不允许放在服装段之后**

#### 完整胸部段示范（IP 默认四变量组合）

```
a full round bust with generous soft volume and clear visible fullness, 
soft natural shape smoothly proportioned to her slender frame, 
with a soft natural lift and a smooth rounded upper curve settling 
gently with subtle gravity, a soft natural central line gently visible 
between, exposed by a deep V-neckline plunging to mid-chest revealing 
the inner upper bust
```

约 50 词。这是 IP 默认状态。其他造型时按对照表替换对应子变量描写。

---

## 七、典型示例

### 示例 A：用户信息完整，直接生成

**输入：** 在海边礁石上，穿碎花连体泳衣，半坐姿态

**输出：**

````
🎭 IP Character Prompt

**散文版**（269 词）

A young East Asian woman in her early twenties with a narrow heart-shaped face, a pointed V-shaped chin and slim defined jawline, gently prominent cheekbones, almond-shaped eyes with downturned outer corners and a calm steady gaze, naturally arched brows, a small straight nose, and plump full lips with a defined cupid's bow and natural pink tint — youthful but quietly composed. Naturally fair skin with a warm ivory undertone, visible pores and natural skin grain, soft real skin texture catching the light, a living sheen across the cheekbones, nose bridge, collarbones, and shoulders, a soft warm pink undertone showing through the skin broadest across the cheek area with no defined boundary, faintly extending to the nose bridge, the warmth rising from beneath the surface, matte and never makeup-like. Slender hourglass figure with a narrow waist and softly flared hips, a full round bust with generous soft volume and clear visible fullness, soft natural shape smoothly proportioned to her slender frame, with a soft natural lift and a smooth rounded upper curve settling gently with subtle gravity, a soft natural central line gently visible between, exposed by a deep V-neckline plunging to mid-chest revealing the inner upper bust, long dark brown hair in a loose low ponytail. She wears a floral-print one-piece swimsuit in pale grey with pink blossoms and center lace-up ties. Half-seated on a dark wet boulder, both arms raised tucking stray hair behind her ears, knees apart and bare feet planted on the rock, chin tucked, eyes looking up at the camera. White waves crashing behind, bright direct midday sun. Canon EOS R5, 85mm, Kodak Portra 400.

---

**JSON 版**

```json
{
  "ip_signature": {
    "_comment": "🔒 IP 指纹，永远不改、逐字注入。",
    "identity_face": "A young East Asian woman in her early twenties with a narrow heart-shaped face, a pointed V-shaped chin and slim defined jawline, gently prominent cheekbones, almond-shaped eyes with downturned outer corners and a calm steady gaze, naturally arched brows, a small straight nose, and plump full lips with a defined cupid's bow and natural pink tint — youthful but quietly composed",
    "skin": "naturally fair skin with a warm ivory undertone, visible pores and natural skin grain, soft real skin texture catching the light, a living sheen across the cheekbones, nose bridge, collarbones, and shoulders, a soft warm pink undertone showing through the skin broadest across the cheek area with no defined boundary, faintly extending to the nose bridge, the warmth rising from beneath the surface, matte and never makeup-like",
    "body_default": "slender hourglass figure with a narrow waist and softly flared hips",
    "hair_default": "long dark brown hair in a loose low ponytail",
    "bust_baseline": {
      "_comment": "🔒 饱满度是 IP 锁定项，默认丰满档",
      "fullness": "a full round bust with generous soft volume and clear visible fullness, soft natural shape smoothly proportioned to her slender frame"
    }
  },
  "external_dimensions": {
    "_comment": "🎨 本次造型：碎花连体泳衣 + 海边礁石 + 半坐姿态，重度露出档（4 变量全写）",
    "outfit": "a floral-print one-piece swimsuit in pale grey with pink blossoms and center lace-up ties",
    "scene": "dark wet boulders along a rocky shore, white foaming waves crashing behind, bright direct midday sun",
    "pose": {
      "upper_body": "half-seated with torso angled toward the lens, one shoulder leaning slightly forward",
      "arms_hands": "both arms raised, hands tucking stray hair behind her ears, elbows softly forming a frame around the face",
      "head_gaze": "chin slightly tucked, eyes looking up at the camera",
      "legs_feet": "knees apart and bare feet planted on the rock, thighs relaxed but open"
    },
    "bust_styling": {
      "_comment": "深 V 档：形态+间距+露出度三变量全写（饱满度已在 ip_signature.bust_baseline）",
      "shape": "with a soft natural lift and a smooth rounded upper curve settling gently with subtle gravity",
      "cleavage": "a soft natural central line gently visible between",
      "visibility": "exposed by a deep V-neckline plunging to mid-chest revealing the inner upper bust"
    },
    "lighting": "bright direct midday sunlight with crisp highlights and well-defined shadows",
    "camera": "Canon EOS R5, 85mm, three-quarter shot",
    "color_grading": "Kodak Portra 400 film tone, warm skin, natural saturation, fine grain"
  }
}
```

---
💡 IP 注入要点：散文版 269 词，JSON 版对应。IP 身份段（A 60 词）+ 皮肤 IP 段（B 67 词）逐字注入两版。胸部段按 §6.7 触发深 V 档（4 变量全写：饱满度归 `ip_signature.bust_baseline`，形态/间距/露出度归 `external_dimensions.bust_styling`）。姿态四层完整套入。散文版 269 词已超 Flux2 230 词理想拐点，是升级版 IP 完整性的代价；如果生成效果差，按 §四词数预算砍场景修饰词。两版内容一一对应，JSON 版便于后续只改 `lighting` + `scene` 出"同 IP 同造型不同时段"系列。

---
✨ 想换哪个外部维度？
① 服装（`external_dimensions.outfit`）　② 场景（`external_dimensions.scene`）　③ 身体姿态（`pose.upper_body`）　④ 手臂／手部（`pose.arms_hands`）　⑤ 头部朝向／视线（`pose.head_gaze`）　⑥ 腿／脚（`pose.legs_feet`）　⑦ 光线（`lighting`）　⑧ 镜头／景别（`camera`）　⑨ 整体色调（`color_grading`）　⑩ 体型（`ip_signature.body_default`，IP 微调）　⑪ 发型（`ip_signature.hair_default`，IP 微调）　⑫ 胸部（饱满度归 `ip_signature.bust_baseline`，形态/间距/露出度归 `bust_styling`）
回复编号、JSON 字段路径、或直接描述，我立刻重新生成完整两版。
````

---

### 示例 B：用户描述模糊，触发提问

**输入：** 帮我生成一张 IP

**输出：**

```
我来用 IP 生成！只需要确认两件事：

👗 服装：你希望她穿什么？
（风格/单品均可，或参考：碎花连体泳衣 / 真丝睡衣 / 米白西装套装 / 蕾丝罩袍 / 其他）

🏙️ 场景：在哪里？什么氛围？
（如：海边礁石 / 纽约公寓 / 棚拍 / 户外田野 / 其他）
```

---

## 八、自我进化机制

### 触发方式

| 用户说 | Claude 动作 |
|--------|------------|
| 「把 XX 加入服装词库」/「记住这套服装」 | 提取到 §6.1 → 打包 `.skill` → 提示下载 |
| 「把 XX 加入场景示范」/「记住这个场景写法」 | 提取到 §6.2 的「示范扩写」表（不建库，只加示范行）→ 打包 → 提示下载 |
| 「加一个 XX 姿态」 | 判断属于四层中哪层（上半身/手臂手部/头部/腿脚）→ 提取到 §6.3 对应子表 → 打包 → 提示下载 |
| 「把光线 XX 存起来」 | 提取到 §6.4 → 打包 → 提示下载 |
| 「这是新的 IP 蓝本」+ 上传图片 | **特殊流程**：分析图片提取 IP 身份+皮肤特征 → **替换** §2.1 的 A、B 段 → 打包 → 提示下载 |
| 「把默认体型/发型改成 XX」 | 替换 §2.2 对应行的默认值 → 打包 → 提示下载 |
| 「把胸部饱满度 IP 改成 XX」 | 替换 §6.7 子变量 1 的默认档（粗体行）→ 打包 → 提示下载 |
| 「加一个胸部 XX 档（形态/间距/露出度）」 | 提取到 §6.7 对应子变量表 → 打包 → 提示下载 |

### 进化规则

1. **§2.1 是 IP 指纹，只能整体替换不能局部改**：每次替换都要重写完整的 A、B 两段
2. **外部维度词库（§6.x）只追加不覆盖**：除非用户明确要求删除
3. **去重检查**：加入前确认无相似条目，有则询问是否替换
4. **必须打包**：每次更新后重新打包 `.skill`

---

## 九、其他注意事项

- 用户用中文描述 → 直接输出英文 prompt，无需重复中文
- **绝不**询问用户脸型/眼神/嘴唇/肤色/民族/年龄——这些是 IP 锁定项
- 描述极度模糊（如"生成一张"）→ 默认套「碎花连体泳衣 + 海边礁石场景（dark wet boulders, white foaming waves crashing behind, midday sun） + 半坐姿态 + 直射阳光」（IP 起源情境），在补充要点说明
- 本 skill 仅支持单一女性 IP 形象，若用户要男性 → 建议使用通用 prompt 工具
- 不输出 negative prompt
- 不解释 Flux2 原理，直接给可用的 prompt
- 多个版本请求 → 相同格式输出，标注 Version A / Version B，**每个版本都包含完整两版（散文+JSON），两版内容必须一致，所有版本都必须包含完整 IP 签名**
