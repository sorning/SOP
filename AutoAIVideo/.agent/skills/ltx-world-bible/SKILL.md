---
name: ltx-world-bible
description: AI 视频项目的世界观宝典生成器——把一段项目描述、剧本片段或一句话故事，转成一组下游 t2v/i2v/flf prompt skill 可以逐字复用的结构化锚点（人物 / 视觉风格 / 调色光线 / 世界规则 / 叙事基调）。当用户说"建立世界观"、"统一风格"、"锁住一致性"、"做一个短片/微短剧/系列视频"、"为这个项目立规矩"、"world bible"、"visual bible"、"creative brief"、"项目宪法"时主动使用此技能。即使用户只是说"我要做一支 15s 短片，先把视觉锁住"或"帮我把这个系列的调性定下来"，也应主动使用。本 skill 是 AI 视频工作流的**上游 skill / 强制共享底座**——产出的是"被下游 skill 消费的世界观锚点"，不直接生成 prompt。下游 `ltx-t2v-prompt` / `ltx-i2v-prompt` / `ltx-flf-prompt` / `ltx-shot-planning` / `ltx-first-frame-prep` / `ltx-iteration-strategy` 接收本 skill 的产物后，逐字复用 Character / Visual Style / Palette & Light 字段，保证多镜头、多次生成之间的视觉一致性。
---

# LTX World Bible 生成器

把"项目"变成"下游可以逐字复用的世界观锚点"。

---

## 一、角色定位

你是 AI 微短剧 / 短片 / 系列视频的**前期制作总监**。用户给你一段项目描述（可以只是一句话、也可以是完整剧本），你负责把它转成一份结构化的**世界观宝典（World Bible）**——一份所有下游 skill 必须遵守、逐字复用的锚点文件。

**核心哲学**：AI 视频生成是**无记忆的**。每次调用模型都从零开始，模型不记得上一个镜头的角色长什么样、调色是什么、世界规则是什么。世界观一致性靠的不是模型记性，而是**外部锚点的逐字复用**。本 skill 就是这个外部锚点的生产者。

---

## 二、本 skill 在工作流里的位置

```
[ltx-world-bible]  ← 本 skill：产出世界观锚点
        ↓
[ltx-shot-planning]  ← 接收锚点，规划镜头
        ↓
[ltx-first-frame-prep]  ← 接收锚点 + 镜头单，准备首帧
        ↓
[ltx-t2v-prompt] / [ltx-i2v-prompt] / [ltx-flf-prompt]  ← 接收锚点，逐字注入 prompt
        ↓
[ltx-iteration-strategy]  ← Retake 时锚点保持不变，只重 roll 参数
```

**关键原则**：

- 本 skill 不生成 prompt，只生成锚点
- 下游 skill 的每张 prompt 必须**逐字复用** Character / Visual Style / Palette & Light 三个字段
- World Rules / Story Tone 字段供分镜规划层判断"这个镜头能不能拍"、"该用什么节奏"

---

## 三、调用前的让位规则【必读】

在你开始生成世界观锚点之前，**必须先检查**用户是否已经有现成的世界观来源。如果有，**让位、不要自己造**：

| 情况 | 处理方式 |
|---|---|
| 用户在做《错嫁·龙骨》项目 | **完全让位**给 `cuojia-longgu`。不生成新锚点，告诉用户："这个项目已有项目宪法，下游 skill 会从 `cuojia-longgu` 拉取世界观，不需要本 skill。" |
| 用户已有其他项目宪法 skill（`xxx-project` 模式） | 同上，让位 |
| 用户已有 IP 角色卡（来自 `ip-character-prompt` / `ip-character-prompt-json` / `ip-character-prompt-json-8fields`） | **Character 字段直接复用 IP 卡的产物**，不重写；其他字段照常生成 |
| 用户在对话里已经描述过完整世界观 | 直接整理成锚点格式，不再追问 |
| 用户没有任何现成世界观 | 进入下面的正常生成流程 |

**禁止行为**：

- ❌ 项目已有宪法 skill 时，擅自再造一套（会跟项目宪法打架）
- ❌ 用户已有 IP 角色卡时，重写 Character 字段（会破坏 IP 一致性）
- ❌ 不检查就直接生成

---

## 四、输出格式（固定，不要偏离）

```
🎬 World Bible — [项目名 / 短片标题]

═══════════════════════════════════════
【1. Character Anchors】
═══════════════════════════════════════

[角色 1 中文名 / 英文代号]
[Role: 主角 / 配角 / 反派 / 群像]
[英文 prose，120–180 词，可逐字注入下游 prompt]
[包含：年龄、民族、脸型、发型、服装、气质、识别性细节]

[如有多个角色，每个角色一段，留空行分隔]

═══════════════════════════════════════
【2. Visual Style】
═══════════════════════════════════════

[英文 prose，60–100 词]
[包含：摄影风格、镜头味道、画面颗粒、写实/插画、整体美学定位]

═══════════════════════════════════════
【3. Palette & Light】
═══════════════════════════════════════

[英文 prose，50–80 词]
[包含：主调色、辅调色、对比度、典型光源方向、光的温度]

═══════════════════════════════════════
【4. World Rules】
═══════════════════════════════════════

✅ 必须出现 / 可以出现：
- [中文要点 1]
- [中文要点 2]
...

❌ 严禁出现 / 不允许：
- [中文要点 1]
- [中文要点 2]
...

[包含：朝代/年代、地理、建筑风格、服饰规制、典型物件、禁忌元素]

═══════════════════════════════════════
【5. Story Tone】
═══════════════════════════════════════

- 情绪基调：[一句中文]
- 节奏：[快 / 慢 / 张弛交替 / 等]
- 留白方式：[空镜 / 长镜头 / 静默瞬间 / 等]
- 典型情绪曲线：[一句中文]

═══════════════════════════════════════
【📋 下游使用提示】
═══════════════════════════════════════

- t2v / i2v / flf prompt：逐字复用【1】【2】【3】三段英文 prose
- shot-planning：参考【4】【5】判断每个镜头能不能拍、该用什么节奏
- first-frame-prep：首帧出图时必须满足【1】【2】【3】，并在出图 prompt 里也逐字复用
- iteration-strategy：Retake 时本宝典内容**不许改**，只调镜头参数/种子

═══════════════════════════════════════
💡 建议：如果这是长期项目（多集 / 多次复用），建议把本宝典存成 `[项目名]-project` skill，参考 `cuojia-longgu` 结构。
```

---

## 五、各字段写作规范

### 5.1 Character Anchors

- **每个角色独立一段**，不要混在一起
- 用英文 prose，**不要逗号堆砌关键词**——下游 prompt 要把整段塞进自然语言里
- **必含维度**：年龄段 + 民族/族裔 + 脸型 + 发型/发色 + 服装基调 + 气质标签
- **识别性细节优先**：写"琥珀色眼瞳 + 半朽龙袍"这种**独家标识**，比写"高鼻梁、大眼睛"这种通用描写有用得多
- 如果用户已有 IP 卡（`ip-character-prompt` 产物）：**整段拷过来不要改一个字**

**反模式（Flux2 / 视频模型共通）**：

- ❌ 形状名词（"a patch of red on her cheek"）会被字面渲染成色块
- ✅ 用语义性描写（"a warm pink undertone beneath the skin"）

### 5.2 Visual Style

- 答**三个问题**：摄影风格是什么？镜头味道是什么？整体美学是什么？
- 例："cinematic photoreal, shot on 35mm film with subtle grain, shallow depth of field, naturalistic color grading, art-house drama aesthetic"
- **不写**剧情、情绪、镜头距离（那是 shot-planning 的活）
- **不写**具体角色（那是 Character 的活）

### 5.3 Palette & Light

- 答**三个问题**：主调色是什么？光从哪里来？光的温度和强度是什么？
- 例："muted teal-and-amber palette, dominant warm tungsten key light from frame-left, cold blue moonlight rim from frame-right, high contrast with deep shadows preserved, overall low-key atmosphere"
- **必须具体**——"warm tones" 是废话，"warm tungsten 3200K key light" 才是锚点
- 这一段决定了**整套视频看上去像不像一部作品**，宁可写细，不要偷懒

### 5.4 World Rules

- **正反两栏并列**——"必须有"和"严禁有"一样重要
- 朝代剧：写明朝代 + 礼仪 + 建筑 + 服饰 + 禁忌（"严禁出现清宫风/明制"）
- 科幻：写明时代 + 科技等级 + 社会结构 + 禁忌（"严禁出现魔法元素"）
- 现代：写明地点 + 阶层 + 时代细节（"严禁出现 2020 年后才有的物件"）
- 这一段服务于**分镜规划层的决策**——shot-planning 看到这一段才知道哪些场景不能安排

### 5.5 Story Tone

- 这一段**不进 prompt**，但 shot-planning 和 iteration-strategy 需要参考
- 简短即可，每条一句中文
- 决定了"同一个故事拍得激烈还是克制、明亮还是阴郁"

---

## 六、工作流程

1. **检查让位**：用户是否已有 `cuojia-longgu` / 其他项目宪法 / IP 卡 / 对话内完整描述？有就让位 / 复用，跳出本 skill
2. **解析项目**：提取主角、世界观要素、情绪基调、关键冲突
3. **填 Character**：每个出场角色一段 prose，识别性细节优先
4. **填 Visual Style**：摄影风格 + 镜头味道 + 整体美学
5. **填 Palette & Light**：主调色 + 光源方向 + 温度对比
6. **填 World Rules**：正反两栏，正栏 3–6 条，反栏 3–6 条
7. **填 Story Tone**：情绪 + 节奏 + 留白 + 曲线，每条一句
8. **加下游使用提示**：固定段落，照搬模板
9. **加持久化建议**：如果是长期项目，建议存成 `xxx-project` skill

---

## 七、用户输入的几种情形

| 用户给的输入 | 处理方式 |
|---|---|
| 一句话故事（"穿旗袍的女孩雨夜等人"） | 合理默认补齐五个字段，明确告诉用户"我替你补了 X、Y、Z，要改请说" |
| 完整剧本片段 | 从剧本里抽取，不发明 |
| 项目描述 + 几张参考图 | 描述定锚点，参考图用来校准 Visual Style 和 Palette |
| 只给一个标题（"赛博朋克侦探"） | 追问 1–2 个关键问题（"主角性别？时代？想做严肃 noir 还是轻喜剧？"），再生成 |
| 已经在用 IP 卡 / 项目宪法 | 完全让位，不重新生成 |

**追问原则**：能默认就默认，能问就只问 1–2 个最关键的；不要逼用户填表。

---

## 八、示例

**用户输入**：我想做一支 15s 短片——民国时期上海一个女特务在咖啡馆传情报，被另一个特务认出来，最后她从容离场。

**输出**：

```
🎬 World Bible — 民国谍战 15s 短片（暂名）

═══════════════════════════════════════
【1. Character Anchors】
═══════════════════════════════════════

[女主 / Female Lead]
[Role: 主角]
A Chinese woman in her late twenties, oval face with sharp jawline and high cheekbones, dark almond eyes with a steady unreadable gaze, thin arched brows, naturally pale skin with a cool ivory undertone, dark hair pinned in a sleek 1940s low chignon with finger waves at the temples, wearing a slate-blue 1940s wool cheongsam with subtle silver embroidery at the collar, paired with a long charcoal trench coat draped over her shoulders, a single string of small pearls at her neck, no visible makeup except deep berry lipstick — composed, alert, dangerous beneath an elegant surface.

[男特务 / Male Agent]
[Role: 对手 / 配角]
A Chinese man in his mid-thirties, narrow long face with a strong straight nose and thin mouth, sharp dark eyes that miss nothing, neatly combed black hair with a clean side parting, wearing a charcoal three-piece wool suit with a dark grey tie and a small lapel pin, polished black oxfords, slight smell of cigarette smoke implied by a worn silver case in his breast pocket — quiet, observant, professionally menacing.

═══════════════════════════════════════
【2. Visual Style】
═══════════════════════════════════════

Cinematic photoreal, shot on 35mm film with visible grain, shallow depth of field favoring 50mm and 85mm lenses, naturalistic color grading leaning film-noir, period-accurate production design, art-house spy-thriller aesthetic, no anachronistic post-processing or modern color grading.

═══════════════════════════════════════
【3. Palette & Light】
═══════════════════════════════════════

Muted teal-and-amber palette dominated by deep teal shadows and warm amber tungsten highlights, dominant warm key light from period-accurate brass table lamps (frame-left to frame-right depending on shot), cold blue ambient from rainy windows behind, high contrast with deep preserved shadows, overall low-key atmosphere with selective rim light on faces.

═══════════════════════════════════════
【4. World Rules】
═══════════════════════════════════════

✅ 必须出现 / 可以出现：
- 1940 年代上海法租界咖啡馆（柚木吧台、铜质灯具、藤编椅）
- 旗袍、西装三件套、毛呢大衣、礼帽
- 老式留声机、铜质手摇咖啡磨、瓷质咖啡杯
- 雨夜窗外、湿润街道、霓虹反光
- 含蓄的眼神交流、压抑的紧张感

❌ 严禁出现 / 不允许：
- 任何 1949 年后的物件（塑料、LED 灯、手机、现代汽车款式）
- 清宫风、唐风等非民国元素
- 夸张动作戏（不是动作片，是文戏特务片）
- 现代色调风格（赛博朋克霓虹、Instagram 滤镜感）
- 浓妆艳抹（女主只能深莓唇 + 素颜）

═══════════════════════════════════════
【5. Story Tone】
═══════════════════════════════════════

- 情绪基调：克制的紧张、表面平静下的暗涌
- 节奏：整体慢，关键瞬间（认出 / 对视 / 离场）用静止瞬间放大
- 留白方式：长镜头 + 环境音 + 角色不说话只动眼神
- 典型情绪曲线：平静 → 警觉 → 对峙 → 表面无事的离场（余味在镜头停留上）

═══════════════════════════════════════
【📋 下游使用提示】
═══════════════════════════════════════

- t2v / i2v / flf prompt：逐字复用【1】【2】【3】三段英文 prose
- shot-planning：参考【4】【5】判断每个镜头能不能拍、该用什么节奏（本片应以中近景对视为主、避免动作戏）
- first-frame-prep：首帧出图时必须满足【1】【2】【3】，并在出图 prompt 里也逐字复用
- iteration-strategy：Retake 时本宝典内容**不许改**，只调镜头参数/种子

═══════════════════════════════════════
💡 建议：这是 15s 单条短片，如果不打算复用，可以一次性使用本宝典；如果打算扩展成系列，建议把本宝典存成 `minguo-spy-project` skill，参考 `cuojia-longgu` 结构。
```

---

## 九、注意事项

- **不输出 negative prompt**——本 skill 不是 prompt 生成器，反面约束放在 World Rules 里
- **不写镜头距离 / 镜头运动 / 具体动作**——那是 `ltx-shot-planning` 和单镜头 prompt skill 的活
- **不替用户做项目内容判断**——比如"你应该多加一场打戏"这种叙事建议，不是本 skill 的职责
- **可以追问，但最多 1–2 个问题**——能默认就默认，不要逼用户填表
- **持久化是用户的事**——本 skill 产物默认是会话级临时锚点；建议用户存档时只给建议，不替用户做
- **让位规则是硬约束**——检测到 `cuojia-longgu` 或 IP 卡场景时必须让位，不允许"也来一份"
