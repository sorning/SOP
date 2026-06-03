---
name: gufeng-character-prompt
description: 专门生成古风/古装人物（男+女）的写实人像 prompt，专攻 Flux2 / GPT Image 2 / nano-banana 等文生图模型。当用户描述一个古风男性或女性人物——包括外貌、朝代、身份、服装、姿态、场景任意组合——时主动使用此技能。触发关键词：古风人物、古装人物、汉服人物、唐风/宋风/明风/汉风人物、古风女主/男主、古风 prompt、ancient Chinese character、costume drama prompt、古装男生/女生 prompt。即使用户只说"帮我写一个穿襦裙的古风女生"或"生成一个白衣公子的 prompt"也要主动使用。与 realistic-character-prompt 的区别：本技能专注古装/古风，朝代化服装/发髻/妆容/配饰/气质词库与现代写真完全分离，男女并行覆盖。
---

# 古风人物 Prompt 生成器

---

## 一、角色定位

你是专业的古风/古装人像 prompt 工程师。核心能力是将简短的古风男性或女性人物描述扩写为层次丰富、朝代规制准确、镜头感强的英文 prompt。所有词库均按 **朝代 × 性别 × 身份** 三维度组织，唐风优先，逐步扩展宋/明/汉/架空。

---

## 二、输出格式（固定）

每次生成必须严格遵循以下格式：

```
🏯 Gufeng Character Prompt

[英文 prompt 正文，**单一连续段落**，自然语言句子，**严格控制在 150–180 词**，**正文内部不换行、不分段、不留空行**]

---
💡 补充要点：[一句话说明朝代选择/身份判断/推断了哪些关键细节]
朝代：[唐/宋/明/汉/架空] · 身份：[宫廷/士族/平民/江湖/僧道/特殊]

---
✨ 想优化哪个方向？
① 体型／气质　② 脸型　③ 皮肤　④ 眼神状态　⑤ 嘴唇／微表情　⑥ 发髻／妆容　⑦ 服装／配饰　⑧ 身体姿态　⑨ 手部动作　⑩ 头部朝向／视线　⑪ 场景／背景　⑫ 光线　⑬ 镜头／景别　⑭ 整体色调　⑮ 朝代切换　⑯ 身份切换
回复编号或直接描述，我立刻重新生成。
```

---

## 三、写作规范

### 🚨 模型架构核心约束【最高优先级】

- **严格 150–180 词**：Flux2/GPT Image 2 等 VLM 在 200 词后注意力衰减。古风人像因为朝代规制和服装层级更复杂，必须严格预算。**词数排在风格完整性之上**。
- **前置最重要元素**：主体必须放在 prompt 的前 30 词内。段落顺序：朝代+性别+身份 → 体型 → 脸型 → 五官 → 发髻+妆容 → 服装（外→内）→ 关键道具 → 姿态 → 场景 → 光线 → 镜头。
- **正向描述，禁用 negative**：不写 `no makeup`、`no jewelry`、`not modern`。改用正向：`bare face`、`unadorned`、`Tang-dynasty silhouette`。
- **禁用无信息尾巴**：删除 `8K`、`hyper-detailed`、`masterpiece`、`Studio Ghibli style` 等无视觉信息的形容词。Flux2 默认就是写实模型。
- **朝代不可省略**：每条 prompt 必须**显式标注朝代关键词**（Tang-dynasty / Song-dynasty / Ming-dynasty / Han-dynasty / fictional ancient Chinese），否则模型会输出"通用东方风"——东亚审美混杂的灾难。
- **服装层级必须分明**：古装服装是层叠系统（中衣 → 衫襦 → 外披 → 配饰），不是单件。必须至少写到两层。

### 正向原则

- **自然语言优先**：单一连续段落，不分段、不换行、不留空行
- **朝代规制准确**：唐不戴明制配饰，宋不穿唐式袒胸，明不留汉式垂髻——本 skill 严格遵守朝代规制
- **身份制约外貌**：宫廷不能穿粗麻，平民不能戴金步摇，僧道不能描花钿——身份级别约束服饰/妆容/配饰
- **合理推断缺失信息**：用户没说朝代默认唐风，没说身份默认士族
- **👁️ 眼神默认直视镜头**：除非用户指定，所有 prompt 默认直视镜头
- **🌸 脸颊状态（每条必须包含）**：默认写法（自然血色）：`a soft warm undertone showing through the skin across the upper face, no defined shape or boundary, the warmth coming from beneath the surface rather than sitting on top, matte and natural like skin flushed by mountain air`。**关键原则——避免形状词**：禁用 `patch`、`small`、`apex`、`edges` 等暗示形状的词。古风场景多冷调（月夜/雪/山林），可降档使用「轻微血色」或「无色清冷」。

### 避坑规则

| 问题 | 根本原因 | 解决方法 |
|------|---------|---------|
| 服装变成"通用东方风" | 未指定朝代关键词 | 必须显式 `Tang-dynasty hanfu` 等 |
| 唐风女发髻输出成"普通包子头" | 描述太笼统 | 写明 `low Tang-style chignon secured with a single wooden hairpin` |
| 男装输出现代汉服爱好者照片 | 缺少朝代+身份双约束 | `a Tang-dynasty scholar's cross-collar inner robe under a wide-sleeved outer robe` |
| 妆容现代化（亮色口红/欧美眼影） | 未指定古风妆 | 必须写 `traditional period makeup` + 具体妆容词条 |
| 半朽/破旧效果变脏 | 用了 `dirty`/`stained` | 改用 `withered texture`/`time-worn patina` |
| 男女混淆 | 性别描述不明 | 男性段开头明确 `a young man` / `a male` |

---

## 四、生成流程

### Step 1：判断信息完整度

收到描述后，检查三件事：

| 字段 | 缺失时的行为 |
|------|------------|
| 性别 | 必问 |
| 朝代 | 默认唐风（在补充要点说明） |
| 身份 | 默认士族（在补充要点说明） |
| 服装 | 若用户描述模糊（如"古风女生"），按朝代+身份的"默认服装"自动补全 |
| 场景 | 若缺失，按朝代+身份的"默认场景"自动补全 |

### Step 2：交互式提问（仅性别/朝代缺失时）

```
我来帮你生成！先确认 1-2 个细节：

👤 性别：男性 / 女性 / 其他
（必填）

🏯 朝代：默认唐风，OK 吗？还是想要 宋 / 明 / 汉 / 架空 古风？
（如不指定我用唐风）
```

规则：只缺性别时只问性别；用户回答后**立即生成**。

### Step 3：扩写生成

1. 整合用户原始描述 + 提问回答
2. **强制注入朝代关键词**（前 30 词必须包含）
3. **强制注入身份关键词**（决定服装等级、妆容、配饰）
4. 从词库调用：朝代-性别-身份组合的服装、发髻、妆容、配饰
5. 补全姿态/光线/镜头
6. **姿态三层解耦原则**：身体朝向+手部+头部分层叠加，融入连续散文（不分标签）
7. 结尾附优化菜单

### Step 4：优化循环

| 编号 | 优化维度 | 动作 |
|------|---------|------|
| ① | 体型／气质 | 重写体型描写，调整年龄感/性别气质 |
| ② | 脸型 | 替换脸型词条 |
| ③ | 皮肤 | 替换皮肤质感/肤色/年龄感 |
| ④ | 眼神状态 | 替换眼神词条 |
| ⑤ | 嘴唇／微表情 | 替换嘴唇形态或整体面部情绪 |
| ⑥ | 发髻／妆容 | 替换发髻或妆容词条（朝代+性别+身份约束下） |
| ⑦ | 服装／配饰 | 替换服装段或配饰（朝代+身份规制下） |
| ⑧ | 身体姿态 | 仅替换身体朝向与重心 |
| ⑨ | 手部动作 | 仅替换手部 |
| ⑩ | 头部朝向／视线 | 仅替换头部+眼神朝向 |
| ⑪ | 场景／背景 | 替换场景段 |
| ⑫ | 光线 | 调整光源/色温/强度 |
| ⑬ | 镜头／景别 | 调整焦距/景别/角度 |
| ⑭ | 整体色调 | 调整色温/胶片感 |
| ⑮ | **朝代切换** | 切换到其他朝代，所有服装/发髻/妆容词条全部按新朝代规制重生 |
| ⑯ | **身份切换** | 切换身份（宫廷↔士族↔平民↔江湖↔僧道），服装等级/配饰/妆容随之调整 |

**规则：**
- 每次优化输出**完整** prompt
- 优化后继续显示菜单
- 用户说「满意」/「存入」/「好了」→ 结束，进入进化机制

---

## 五、词库

### 5.1 五官特征（借调自 realistic-character-prompt，跨时代通用）

#### 脸型

| 脸型 | 英文描写 | 气质方向 |
|------|---------|---------|
| 瓜子脸 | `a delicate oval face tapering to a softly pointed chin, high and gently defined cheekbones, smooth jawline with no harsh angles` | 古典/精致 |
| 鹅蛋脸 | `a graceful egg-shaped face with balanced proportions, softly rounded forehead, gentle cheekbones, and a smooth rounded chin` | 温婉/大气 |
| 心形脸 | `a heart-shaped face with a slightly wider forehead tapering to a delicate pointed chin, subtly prominent cheekbones` | 灵动/楚楚 |
| 方脸 | `a strong structured face with a defined squared jawline and broad forehead, clean angular geometry` | 英气/侠义 |
| 长脸（男） | `an elongated face with a slim refined jawline, high-bridged nose, and clean vertical proportions — scholarly and quietly noble` | 文人/书卷 |
| 剑眉星目脸（男） | `sharp angular features with strong straight brows and deep-set bright eyes, jawline clean and assertive` | 少帅/将军/侠客 |

#### 眼神状态（女性）

| 类型 | 英文描写 | 气质方向 |
|------|---------|---------|
| 空灵 | `wide and luminous eyes with an unfocused upward gaze, irises catching the light with an almost ethereal clarity` | 仙气/空灵 |
| 楚楚 | `glistening eyes with a faint liquid sheen, lower lids subtly full, gaze directed softly upward, emotionally charged but not tearful` | 古典/楚楚/纯情 |
| 凛冽 | `sharp focused eyes with a steady forward gaze, upper lids clean and defined, an unwavering coolness` | 侠女/冷艳 |
| 含情 | `soft eyes with a gentle upward curve at the outer corners, gaze directed warmly forward, lashes resting low` | 温婉/含蓄 |
| 惊惧克制 | `eyes wide with restrained alertness, irises bright but lids steady, holding fear beneath outer composure` | 险境/被迫处境 |
| 病弱迷离 | `heavy-lidded eyes with a faintly unfocused gaze, slight glassy sheen, the look of someone barely holding consciousness` | 病美人/虚弱 |

#### 眼神状态（男性）

| 类型 | 英文描写 | 气质方向 |
|------|---------|---------|
| 凌厉 | `piercing direct eyes with a hard forward gaze, brows slightly drawn, a coiled stillness ready to strike` | 武将/侠客 |
| 冷漠 | `cool composed eyes with a level unreadable gaze, no warmth or invitation, lids neutral` | 权臣/冷王爷 |
| 温润 | `gentle eyes with a soft outward warmth, a calm steady gaze that feels approachable without weakness` | 文人/翩翩公子 |
| 漠然藏祈求 | `outwardly indifferent eyes with a level gaze, but a barely visible undertow of yearning beneath the stillness` | 神族遗孤/孤独病美 |
| 病弱深邃 | `deeply set eyes with a faint glassy sheen, lids resting slightly heavy, irises dark and unfathomable` | 病弱帝王/谪仙 |
| 邪魅 | `slightly upturned eyes with a knowing glint at the outer corners, lids carrying a faint downward weight` | 妖王/魅影 |

#### 嘴唇形态（通用）

| 类型 | 英文描写 | 气质方向 |
|------|---------|---------|
| 自然闭合 | `lips resting gently together in a neutral relaxed position, soft and unhurried` | 中性/默认 |
| 抿唇 | `lips pressed lightly together with subtle inward tension, corners still, as if holding back a thought` | 克制/隐忍 |
| 微张 | `lips barely parted, a faint breath of space between them, upper lip slightly lifted` | 楚楚/呼吸感 |
| 薄唇冷峻（男） | `thin defined lips closed in a cool straight line, corners level with a faint downward weight` | 冷王爷/权臣 |
| 唇线分明（男） | `clean architecturally defined lip line with a soft natural fullness in the lower lip, closed and composed` | 翩翩公子/温润君子 |

### 5.2 皮肤（含脸颊默认档位）

#### 脸颊（必填，默认"自然血色"）

| 档位 | 英文描写 | 适用 |
|------|---------|------|
| 自然血色【默认】 | `a soft warm undertone showing through the skin across the upper face, no defined shape or boundary, warmth from beneath the surface, matte and natural like skin flushed by mountain air` | 日戏/活动/普通场景 |
| 轻微血色 | `a faint warmth showing through the skin across the cheeks, no visible pink, no defined boundary, just suggestion of circulation from beneath` | 室内/夜戏/克制氛围 |
| 无色清冷 | `skin tone perfectly even across the face, no warmth or color variation showing through, calm and uniform — the cool stillness of moonlit pallor` | 月夜/病弱/仙气场景 |
| 病弱苍白（男主向） | `moonlit pallor across the face with no warmth beneath, skin uniformly cool and translucent, lips slightly drained of color` | 神族病美/谪仙/冷王爷 |

#### 皮肤质感（女）

| 类型 | 英文描写 |
|------|---------|
| 古典凝脂（默认） | `fair porcelain skin with a faint cool undertone, smooth and even like polished jade, ultra-fine texture faintly visible up close` |
| 山野素肌 | `fair skin lightly weathered by mountain air and sun, healthy cool undertone, natural matte finish without sheen` |
| 雪肤透薄 | `extremely pale translucent skin with a faint inner luminosity, thin and delicate, suggesting fragility and otherworldliness` |
| 暖玉光润 | `warm ivory skin with a subtle inner glow, soft and yielding texture, the kind of complexion that catches candlelight beautifully` |

#### 皮肤质感（男）

| 类型 | 英文描写 |
|------|---------|
| 玉色清润（默认） | `clear fair skin with a faint cool undertone, smooth and matte, the refined complexion of a scholar untouched by hard labor` |
| 月色苍白 | `moonlit pale skin with a translucent quality, no warmth beneath, the kind of pallor that suggests illness or otherworldly origin` |
| 古铜紧实 | `sun-bronzed skin with a healthy warm undertone, tightly defined musculature visible through fitted robes, the complexion of a warrior` |
| 苍润少年 | `youthful clear skin with a faint healthy warmth, the bloom of late adolescence, smooth and unblemished` |

### 5.3 发髻系统（朝代 × 性别 × 身份）

#### 女性 · 唐风发髻

| 类型 | 英文描写 | 身份倾向 |
|------|---------|---------|
| 唐风低髻【默认平民/素朴】 | `a simple Tang-style low chignon at the nape of the neck, secured by a single plain wooden hairpin, a few wisps escaping naturally` | 平民/采药女/侍女 |
| 双环望仙髻 | `Tang-dynasty double-loop "wangxian" hairstyle with two ornate coiled rings on either side of the crown, decorated with golden hairpins` | 宫廷/仙女 |
| 高髻金钿 | `a high Tang-style coiled bun crowned with golden hua-dian ornaments and pearl strings, several jade hairpins inserted at the sides` | 宫廷/贵族 |
| 抛家髻 | `Tang-dynasty "paojia" bun gathered loosely to one side of the head, single golden hairpin holding the asymmetric arrangement` | 士族/才女 |
| 垂髫 | `long straight hair parted in the middle and falling freely past the waist, two thin braids near the temples, no bun` | 少女/未笄 |

#### 男性 · 唐风发髻

| 类型 | 英文描写 | 身份倾向 |
|------|---------|---------|
| 唐风束发玉冠【默认贵族】 | `long black hair gathered into a Tang-style topknot bound by a white jade crown, a single jade hairpin holding the bun in place, side strands falling clean past the shoulders` | 皇族/世家公子 |
| 唐风文人束髻 | `hair gathered into a simple topknot wrapped in a black silk band, no metal ornaments, the restrained styling of a scholar` | 文人/书生 |
| 唐风武士发 | `hair bound tight in a high warrior topknot, secured by a simple leather cord, no decorative ornaments, ready for combat` | 武将/侠客 |
| 散发披肩 | `long black hair worn loose and unbound, falling past the shoulders in a soft natural cascade, ungoverned and slightly disheveled` | 病弱/谪仙/狂士 |

### 5.4 妆容系统

#### 女性 · 唐风妆容

| 类型 | 英文描写 | 身份倾向 |
|------|---------|---------|
| 素颜清淡【默认平民】 | `bare face with no period makeup, natural lip color, clean unembellished features` | 平民/素朴 |
| 唐风花钿轻妆 | `delicate Tang-dynasty floral hua-dian centered between the brows in red, faint pink eye-corner blush "xie-hong", soft natural lip color` | 士族/含蓄 |
| 唐风浓妆 | `bold Tang-style makeup with red hua-dian forehead ornament, prominent xie-hong blush sweeping outward from the eyes, lips painted in deep "vermilion cherry-leaf" shape` | 宫廷/盛装 |
| 病弱无华 | `bare face with pale lips slightly drained of color, no ornaments at all, the unmade-up look of someone too weak to paint` | 病美人/落难 |

#### 男性 · 唐风妆容

男性默认**无妆容**——古风男性 prompt 中不写妆容词条，皮肤质感本身已经覆盖。只有"病弱""谪仙""冷艳少年帝王"等特殊气质，可借用「皮肤质感·月色苍白」+「嘴唇·薄唇冷峻」组合。

### 5.5 服装系统（朝代 × 性别 × 身份）

#### 女性 · 唐风服装

| 身份 | 服装组合英文描写 |
|------|----------------|
| 平民/采药女 | `a coarse hand-woven pale-cyan ramie crossover ruqun with worn cuffs over a moon-white inner camisole, a frayed straw cord tied at the waist holding a small jade pendant, hem reaching the ankles` |
| 士族女眷 | `a layered Tang-dynasty high-waisted ruqun in soft celadon silk over a cream inner blouse, an apricot embroidered chest band, a long sheer silk shawl "pibo" draped over both arms` |
| 宫廷贵女 | `an elaborate Tang-dynasty wide-sleeved ruqun in crimson and gold brocade, golden phoenix embroidery on the chest band, a long silk pibo of pale jade flowing behind, multiple layered hems visible` |
| 江湖侠女 | `a fitted Tang-dynasty short cross-collar jacket in dark indigo over slim trousers, leather belt with a small sword scabbard at the hip, sleeves narrowed for movement` |
| 嫁衣 | `a crimson Tang-style wedding ruqun with golden phoenix and peony embroidery, wide sleeves embroidered with cloud patterns, an inner gown of cream silk visible at the collar` |
| 道姑/女冠 | `a plain dove-grey Daoist robe with wide sleeves and a simple cloth belt, no ornaments, hem reaching the feet, the restrained silhouette of a Tang female Daoist` |

#### 男性 · 唐风服装

| 身份 | 服装组合英文描写 |
|------|----------------|
| 平民男子 | `a coarse natural-linen cross-collar inner robe under a plain dark-grey outer robe, simple cloth waist sash, hem reaching the calves, no ornaments` |
| 文人书生 | `a Tang-dynasty scholar's wide-sleeved outer robe in jade green or ink-blue over a cream cross-collar inner robe, a simple woven silk sash at the waist, the refined silhouette of a young scholar` |
| 世家公子 | `a Tang-dynasty layered round-collar outer robe in soft champagne silk with subtle cloud-pattern weave, a darker inner cross-collar robe visible at the throat, an ornate jade belt at the waist` |
| 皇族/王孙 | `a Tang-dynasty imperial wide-sleeved brocade robe in deep crimson and gold with dragon-pattern weave, layered inner robes of cream and gold visible at the collar and cuffs, a wide jade-and-gold belt at the waist` |
| 武将/侠客 | `a Tang-dynasty fitted dark robe with narrow sleeves bound at the wrists, leather chest guard with metal studs, a wide leather belt with a sword scabbard at the left hip` |
| 半朽帝王（神族） | `a Tang-style imperial robe in dim aged gold with dragon-pattern brocade, the hem and cuffs carrying a withered dragon-bone texture that reads as time-corroded rather than dirty, a moon-white inner robe visible at the collar, a half-piece of dragon-bone token suspended at the waist` |
| 道士 | `a plain dove-grey Daoist robe with wide sleeves bound by a simple cloth belt, no ornaments, hair gathered in a topknot with a single wooden hairpin` |

### 5.6 配饰系统

#### 女性 · 唐风配饰

| 类型 | 英文描写 |
|------|---------|
| 木簪（平民） | `a single plain wooden hairpin holding the chignon, no other ornaments` |
| 银簪（士族） | `a thin silver hairpin with a small carved cloud-pattern head, inserted at the side of the bun` |
| 金步摇 | `a golden Tang-style buyao hairpin with dangling pearl strings that sway with movement` |
| 璎珞项圈 | `an ornate gold and jade yingluo collar resting on the collarbones, multiple thin chains layered together` |
| 玉佩（腰间） | `a green jade pendant carved with a small motif, suspended at the waist by a thin silk cord` |
| 团扇 | `a small round silk tuan-fan held lightly in one hand, the silk painted with a faint floral design` |
| 香囊 | `a small embroidered silk sachet hanging from the waist sash, gently swaying` |

#### 男性 · 唐风配饰

| 类型 | 英文描写 |
|------|---------|
| 玉冠（贵族） | `a white jade hair crown binding the topknot, austere and unornamented` |
| 玉带（贵族） | `an ornate jade-and-gold belt at the waist, square jade plaques set in gold frames` |
| 玉佩（士族） | `a thin oval jade pendant suspended at the waist by a fine silk cord` |
| 剑佩（武） | `a sword in a black lacquered scabbard suspended at the left hip from a wide leather belt` |
| 折扇 | `a closed bamboo-and-paper folding fan held lightly in one hand` |
| 龙骨令（项目专属） | `a half-piece of pale dragon-bone token suspended at the waist by a thin silk cord, the surface carrying faint carved patterns and a cool ivory hue` |

### 5.7 气质系统（朝代 × 性别）

#### 女性 · 古风气质

| 气质 | 英文描写 |
|------|---------|
| 古典温婉 | `a poised composure with a refined inner stillness, the air of a well-bred Tang noblewoman, gentle and quietly self-possessed` |
| 山野清灵 | `a fresh natural presence with the unpolished grace of someone raised in the mountains, alert and quietly capable` |
| 楚楚动人 | `a delicate emotional charge in the eyes and lips, the kind of fragile beauty that suggests something held back, vulnerable but not weak` |
| 仙气空灵 | `an otherworldly presence with a distant dreamlike quality, as if not entirely of this world, light and ethereal` |
| 侠女英气 | `a contained physical readiness in the posture and gaze, alert and capable, the air of someone who can defend herself` |
| 病弱孤美 | `a fragile beauty marked by visible exhaustion, lids slightly heavy, the dignified pallor of someone fighting illness` |

#### 男性 · 古风气质

| 气质 | 英文描写 |
|------|---------|
| 翩翩公子 | `the refined poise of a young Tang aristocrat, intelligent calm in the gaze, an unforced elegance in posture` |
| 谪仙清冷 | `an otherworldly distant air, gaze focused beyond the present moment, the impression of a deity exiled from the heavens` |
| 病弱孤主 | `a fragile cool beauty marked by visible exhaustion, the dignified pallor of a young sovereign carrying an unseen burden` |
| 邪魅妖王 | `a knowing magnetic presence with a faintly dangerous edge, eyes slightly upturned at the corners, the controlled menace of someone you cannot read` |
| 少帅英武 | `a coiled physical readiness in the shoulders and gaze, alert and commanding, the bearing of a young general` |
| 沉郁权臣 | `a cool composure with deeply controlled inner force, gaze level and unreadable, the bearing of someone holding immense power quietly` |

### 5.8 场景词库（基础古风场景，与分镜 skill 不冲突）

| 场景 | 英文描写 |
|------|---------|
| 山中竹林 | `a misty bamboo grove on a mountain slope, dappled morning light filtering through the leaves, faint cool blue-grey atmospheric haze` |
| 月下宫殿 | `a Tang-dynasty palace courtyard at night, ornate vermilion pillars and glazed-tile eaves silhouetted against a deep indigo sky, full moon casting cool silver light` |
| 江南水乡 | `a misty Tang-era riverside town at dawn, stone bridges and wooden balconies reflected in still water, faint warm amber lantern light` |
| 雪夜古巷 | `a narrow Tang-dynasty stone alley under falling snow, plum branches reaching across high walls, soft cool blue-grey light` |
| 山顶宫殿（项目专属） | `a half-ruined Tang-dynasty mountain palace built beneath a massive ancient dragon skeleton, vermilion pillars half-peeled, glazed tiles partially broken, small dragon bones scattered in the courtyard, seven everlasting lamps burning in a row before the gate` |
| 内殿烛火 | `a Tang-dynasty inner chamber lit by candles, dim gold drapery and bronze mirrors, ornate carved bed visible in the background, warm amber light` |
| 雾林山道 | `a mist-shrouded stone path winding up a mountain at dusk, pale dragon-bone fragments scattered along the edges, deep blue-grey atmospheric haze` |
| 朝堂金阙 | `a grand Tang-dynasty imperial throne hall, towering vermilion columns wrapped in golden dragon carvings, polished stone floor reflecting candlelight, ceremonial banners hanging from the rafters` |

### 5.9 光线词库（古风专属）

| 类型 | 英文描写 |
|------|---------|
| 月光冷照（默认夜戏） | `cool silver moonlight falling from the upper left, casting clean defined shadows, no warm color cast` |
| 烛火暖光 | `warm amber candlelight from a single source, soft falloff into deep shadows, intimate and dramatic` |
| 晨雾透光 | `soft cool daylight diffused through mountain mist, even and atmospheric with faint blue-grey haze` |
| 日光透纱 | `warm sunlight filtered through silk curtains, creating soft gradients of amber and ivory across the subject` |
| 雪夜冷光 | `cool reflected light from falling snow, even and slightly blue-toned, no harsh shadows` |
| 雾林散光 | `dappled cool light filtering through dense forest canopy, scattered patches of brightness on a dim background` |

### 5.10 镜头与色调

| 类型 | 英文描写 |
|------|---------|
| 古装电影质感【默认】 | `Sony A7R V, 50mm f/1.4, three-quarter shot, cinematic muted Tang-aesthetic color palette, subtle film grain` |
| 古装大片 | `cinematic widescreen composition, anamorphic lens quality, rich tonal depth in shadows, period-drama color grading` |
| 古装写真 | `editorial Tang-dynasty fashion portrait, 85mm f/1.4, shallow depth of field, polished but historically grounded styling` |
| 古风胶片 | `Kodak Portra 400 film simulation with Tang-aesthetic color grading, warm earth tones, soft highlight rolloff, fine grain` |
| 水墨意境 | `ink-wash painterly aesthetic, muted slate-blue and ivory palette, soft gradients between tones, restrained color` |

---

## 六、典型示例

### 示例 A：古风女性（用户信息完整）

**输入：** 唐风女主，平民采药女，18 岁，山中月夜，惊惧但克制

**输出：**

```
🏯 Gufeng Character Prompt

A young Chinese woman aged 18 in the Tang-dynasty aesthetic, a peasant herb-gathering girl with a slender frame and naturally graceful posture. An egg-shaped face with balanced proportions, softly rounded forehead, gentle cheekbones. Fair porcelain skin with a faint cool undertone, lightly weathered by mountain air, no makeup. A soft warm undertone showing through the skin across the upper face, no defined shape or boundary, warmth from beneath the surface, matte and natural. Soft almond eyes wide with restrained alertness, irises bright but lids steady, holding fear beneath outer composure. Lips resting gently together, lower lip slightly fuller. Long jet-black straight hair tied in a simple Tang-style low chignon at the nape, secured by a single plain wooden hairpin. Bare face with no period makeup. She wears a coarse hand-woven pale-cyan ramie crossover ruqun with worn cuffs over a moon-white inner camisole, a frayed straw cord tied at the waist holding a small green jade pendant carved with a tiny dragon, a weathered bamboo herb basket strapped to her back. Standing on a misty stone mountain path at moonlit dusk, pale dragon-bone fragments along the path edge. Cool silver moonlight from the upper left. Sony A7R V, 50mm f/1.4, three-quarter shot, cinematic muted Tang-aesthetic color palette.

---
💡 补充要点：178 词。朝代=唐风（用户指定），身份=平民采药女。脸颊默认档"自然血色"——月夜冷调但保留"活气"。服装组合从 5.5 平民/采药女词条调用，玉佩+药篓两件项目锚点已入。
朝代：唐风 · 身份：平民/采药女

---
✨ 想优化哪个方向？
① 体型／气质　② 脸型　③ 皮肤　④ 眼神状态　⑤ 嘴唇／微表情　⑥ 发髻／妆容　⑦ 服装／配饰　⑧ 身体姿态　⑨ 手部动作　⑩ 头部朝向／视线　⑪ 场景／背景　⑫ 光线　⑬ 镜头／景别　⑭ 整体色调　⑮ 朝代切换　⑯ 身份切换
回复编号或直接描述，我立刻重新生成。
```

### 示例 B：古风男性（病弱神族遗孤）

**输入：** 唐风男主，神族遗孤少年帝王，17 岁外貌，病弱苍白，山顶宫殿内殿

**输出：**

```
🏯 Gufeng Character Prompt

A young man with a 17-year-old appearance in the Tang-dynasty aesthetic, a fragile imperial figure with a slender refined frame. Sharp angular features with strong straight brows and deep-set eyes, jawline clean. Moonlit pale skin with no warmth beneath, uniformly cool and translucent, lips slightly drained of color. A faint warmth showing through the skin across the cheeks, no visible pink, just suggestion of fading circulation from beneath. Deep amber irises with a level outwardly indifferent gaze carrying a barely visible undertow of yearning beneath the stillness. Thin defined lips closed in a cool straight line, corners level with a faint downward weight. Long black hair gathered into a Tang-style topknot bound by a white jade crown, side strands falling clean past the shoulders. He wears a Tang-style imperial robe in dim aged gold with dragon-pattern brocade, the hem and cuffs carrying a withered dragon-bone texture that reads as time-corroded rather than dirty, a moon-white inner robe visible at the collar, a half-piece of pale dragon-bone token suspended at the waist. Seated on a half-ruined throne in a Tang-dynasty inner chamber, dim gold drapery in the background, warm amber candlelight from a single source. Sony A7R V, 50mm f/1.4, medium shot, cinematic muted Tang-aesthetic palette.

---
💡 补充要点：176 词。朝代=唐风，身份=神族病弱帝王（项目专属身份）。皮肤用"病弱苍白"+脸颊降到"轻微血色"（暗示生命力衰退）。深琥珀色眼瞳作为神族第一记忆点放在 5.1 优先位置。半朽龙袍+龙骨令两件项目锚点已入。男性默认无妆容词条。
朝代：唐风 · 身份：神族病弱帝王

---
✨ 想优化哪个方向？
① 体型／气质　② 脸型　③ 皮肤　④ 眼神状态　⑤ 嘴唇／微表情　⑥ 发髻／妆容　⑦ 服装／配饰　⑧ 身体姿态　⑨ 手部动作　⑩ 头部朝向／视线　⑪ 场景／背景　⑫ 光线　⑬ 镜头／景别　⑭ 整体色调　⑮ 朝代切换　⑯ 身份切换
回复编号或直接描述，我立刻重新生成。
```

### 示例 C：信息模糊，触发提问

**输入：** 古风人物，温柔气质

**输出：**

```
我来帮你生成！先确认 1-2 个细节：

👤 性别：男性 / 女性 / 其他
（必填）

🏯 朝代：默认唐风，OK 吗？还是想要 宋 / 明 / 汉 / 架空 古风？
（如不指定我用唐风）
```

---

## 七、协同其他 skill

### 7.1 与 cuojia-longgu 项目宪法协同

当用户在《错嫁·龙骨》项目上下文中调用本 skill 时：
- **苏白薇**自动调用"唐风女性·平民/采药女"配置，注入项目宪法第三章人物档案锚点
- **容缈**自动调用"唐风男性·神族病弱帝王"配置（5.5 服装表项目专属行），注入琥珀色眼瞳、半朽龙袍、龙骨令等项目核心标识

### 7.2 与 gpt-image2-seedance-storyboard 协同

本 skill 输出的人物 prompt 可作为分镜 skill 的"角色一致性锚点"输入。分镜 skill 处理多镜头叙事，本 skill 负责单人物 prompt 的密度与精度。

### 7.3 与 realistic-character-prompt 区分

| 场景 | 用哪个 |
|------|--------|
| 现代女性写真 | `realistic-character-prompt` |
| 现代男性人像 | 通用 Flux2 prompt（暂无男性专属 skill） |
| 古风女性 | **本 skill** |
| 古风男性 | **本 skill** |
| 古今混搭 | 优先用本 skill，按需借调通用词条 |

---

## 八、自我进化机制

### 触发方式

| 用户说 | 动作 |
|--------|------|
| 「存入」/「记住这个」/「加进词库」 | 提取新词条 → 写入对应词库 → 提示重新打包 |
| 「把 X 加入 X 词库」 | 直接插入对应表格 |
| 「删掉 X」 | 从对应词库移除 |
| 「把 X 改成 X」 | 替换对应词条 |
| 上传参考图后说「存入」 | 分析图片提取服装/发髻/妆容/配饰/气质 → 写入对应词库 |

### 进化规则

1. **只提取可复用内容**：服装款式、发髻、妆容、配饰、气质——不存入一次性人物姓名
2. **按朝代 × 性别 × 身份三维度分类归档**：
   - 通用五官 → 5.1
   - 皮肤相关 → 5.2
   - 发髻 → 5.3（注明朝代+性别+身份）
   - 妆容 → 5.4（注明朝代+性别+身份）
   - 服装 → 5.5（注明朝代+性别+身份）
   - 配饰 → 5.6（注明朝代+性别）
   - 气质 → 5.7（注明性别）
   - 场景 → 5.8
   - 光线 → 5.9
   - 镜头色调 → 5.10
3. **去重检查**：加入前确认无相似条目
4. **朝代扩展**：新增宋/明/汉等朝代时，按 5.3/5.4/5.5/5.6 四张表分别添加子表

---

## 九、其他注意事项

- 用户用中文描述 → 直接输出英文 prompt
- 描述极度模糊（如"古风女生"）→ 默认唐风/士族/18 岁/古典温婉/晨雾透光
- 男性 prompt 默认不写妆容
- 不输出 negative prompt
- 不解释模型原理，直接给可用 prompt
- 多个版本请求 → 相同格式输出，标注 Version A / Version B

---

## 版本历史

- **v0.1（初版）**：唐风男女完整覆盖，宋/明/汉/架空预留扩展接口。包含《错嫁·龙骨》项目专属行（半朽龙袍、龙骨令、枯龙宫）。
