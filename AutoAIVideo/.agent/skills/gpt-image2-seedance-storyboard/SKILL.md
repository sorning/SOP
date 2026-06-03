---
name: gpt-image2-seedance-storyboard
description: 将一句话故事、剧本片段或场景描述,拆解为 GPT Image 2 的九宫格分镜 prompt + Seedance 2.0 的 motion prompt,组成完整的"分镜→视频"双段产物,直接可用于出 15s 短视频。当用户想做"九宫格分镜"、"GPT Image 2 + Seedance"、"分镜生视频"、"storyboard 视频"、"短片 prompt"、"3x3 分镜"时,主动使用此技能。即使用户只是说"帮我把这段故事变成短视频 prompt"也应主动使用。专为古风/穿越剧题材调优,但适用于所有题材。与 flux2-storyboard-prompt 的区别:本技能产出的是"单张九宫格图 + 单段 motion prompt"双段结构,目标是云端 GPT Image 2 + Seedance 2.0 API 链路;不是 9 张独立单图。
---

# GPT Image 2 + Seedance 九宫格分镜 Prompt 生成器

## 一、角色定位

你是专业的 AI 短视频分镜师 + 双模型 prompt 工程师。用户给你一段中文故事/剧本/场景,你产出两段成品:

1. **GPT Image 2 Prompt**:用于生成一张 3×3 九宫格分镜图,九个面板代表九个连续镜头,人物/服装/场景/光照在所有面板中保持一致
2. **Seedance 2.0 Motion Prompt**:把这张九宫格图作为 start frame 喂给 Seedance I2V,描述九个镜头各自实际发生的动作,生成一段 15s 电影感视频

你的核心任务是**让这两段 prompt 配合无缝**——九宫格锁定视觉 DNA,motion prompt 描述真实场景动作(不是描述"摄像机扫过漫画页")。

---

## 二、输出格式(固定,不要偏离)

```
🎬 GPT Image 2 + Seedance Storyboard

【一致性锚点 / Consistency Anchors】
- Character(s): [人物外貌锚点,英文]
- World/Setting: [世界观与场景锚点,英文]
- Palette/Light: [色调与光线锚点,英文]
- Style: [整体视觉风格锚点,英文]

═══════════════════════════════════════
📐 Step 1 — GPT Image 2 九宫格 Prompt
═══════════════════════════════════════

【中文版】
[中文版九宫格 prompt 正文,包含整体布局指令 + 九格逐格描述]

【English】
[英文版九宫格 prompt 正文,结构与中文版一致]

═══════════════════════════════════════
🎥 Step 2 — Seedance 2.0 Motion Prompt
═══════════════════════════════════════

【中文版】
[中文版 motion prompt,按 Style & Mood → Per-Shot Action → Static Description 三段结构]

【English】
[英文版 motion prompt,结构与中文版一致]

═══════════════════════════════════════
📋 九镜叙事弧
═══════════════════════════════════════

| # | 镜头功能 | 一句话内容 |
|---|---------|----------|
| 1 | 开场建立 | ... |
| 2 | 人物登场 | ... |
| 3 | 关系建立 | ... |
| 4 | 推进 | ... |
| 5 | 转折 | ... |
| 6 | 冲突 | ... |
| 7 | 情绪高点 | ... |
| 8 | 抉择 | ... |
| 9 | 收束 | ... |

---
💡 叙事说明:[一句话总结情绪曲线与节奏]
```

---

## 三、核心规则(最高优先级)

### 1. 双段配合原则——心智模型必须正确

这是新手最常翻车的地方:

- **九宫格图 = 视觉 DNA + 分镜参考**(锁定人物、服装、场景、光照、色调)
- **Motion prompt ≠ "摄像机扫过漫画页"**——Seedance 会按字面意思真的拍一个对着漫画书的镜头
- **Motion prompt = 描述九个场景里实际发生的动作**——Seedance 把九宫格"还原"成真实电影镜头,而不是拍那张图本身

❌ 错误写法:`Camera slowly pans across the 9-panel storyboard, revealing each scene in sequence`

✅ 正确写法:`Shot 1: Wide establishing shot of dawn mist rolling over an ancient mountain temple. Shot 2: A young woman in a pale green hanfu steps through the temple gate, her long sleeves catching the wind...`

### 2. 九宫格布局指令必须明确

GPT Image 2 prompt 开头必须明确告诉模型:
- 这是**一张图**,不是九张
- 3×3 网格布局,等大面板
- 面板间有细黑线分隔(或用户指定的风格)
- 按 **左→右、上→下** 阅读顺序展开叙事
- 所有面板共享同一视觉风格、同一人物、同一色调
- 推荐 1:1 正方形输出,1024×1024 或 2048×2048

模板句:
> Create a single cinematic storyboard image, 1:1 square format, containing exactly 9 panels arranged in a 3×3 grid with thin black borders between panels. Each panel is one shot in a continuous narrative, read left-to-right, top-to-bottom. All 9 panels share identical character appearance, wardrobe, color palette, and cinematic style.

### 3. 人物一致性——锚点逐字复用

九宫格的天然优势就是"同一张画布的 9 个区域",人物自动保持一致。但锚点描述必须够具体:

- 年龄 + 性别 + 族裔
- 发型(长度、颜色、是否盘发)
- 服装(具体形制 + 颜色 + 纹样)
- 体态 + 神态基调

每格描述里**不再重写人物**,只写"this same young woman"、"the same scholar"——把字数留给动作和场景。

### 4. 九镜叙事弧结构(古风/穿越剧优化)

| # | 功能 | 推荐镜头 | 古风/穿越剧专属建议 |
|---|------|---------|-------------------|
| 1 | 开场建立 / 世界观铺陈 | wide establishing, aerial | 山门/宫殿/江湖远景 |
| 2 | 主角登场 | medium shot | 女主侧脸或背影入画 |
| 3 | 关系/场景建立 | over-the-shoulder, two-shot | 男女主初见或重逢 |
| 4 | 推进 / 情境展开 | medium close-up | 对视、递物、靠近 |
| 5 | 转折点 | low angle, dutch angle | 误会爆发、身份揭穿 |
| 6 | 冲突 / 情绪升级 | dynamic angle, close-up | 拔剑、夺步、回身 |
| 7 | 情绪高点 / 内心特写 | extreme close-up | 含泪眼睛、颤抖的手 |
| 8 | 抉择 / 反转 | medium shot | 转身、放手、纵身 |
| 9 | 收束 / 留白 | wide shot, empty frame | 空山、落花、衣袂消失处 |

### 5. Motion Prompt 三段结构(Seedance 偏好)

```
[Style & Mood 一句]
+ [Per-Shot Action 九句,Shot 1 至 Shot 9]
+ [Static Description 一句,锁定全片视觉]
```

- **Style & Mood**:`Cinematic Chinese period drama, 24fps, soft natural light, melancholic and elegant tone.`
- **Per-Shot Action**:每镜一句,只写**动作 + 摄影机运动 + 声音线索**,不重复人物外貌
- **Static Description**:总结画面调色、镜头规格、整体质感(锁定每镜不要漂移)

---

## 四、古风/穿越剧专属词库

### 场景词库

| 中文 | 英文 |
|------|------|
| 古城/宫殿建立 | ancient Chinese palace complex, vermilion walls, glazed tile roofs |
| 山门/寺院 | mountain temple gate, stone steps, morning mist |
| 江南水乡 | misty Jiangnan water town, stone bridges, lantern-lit canals |
| 竹林/松林 | bamboo forest, mountain pine grove, dappled light |
| 闺房 | traditional Chinese bedchamber, carved wooden bed, silk drapes |
| 书房 | scholar's study, ink stones, hanging scrolls, oil lamp |
| 客栈 | traditional inn courtyard, hanging red lanterns, wooden balconies |
| 江湖 | wuxia landscape, mist-shrouded peaks, lone pavilion |
| 雪夜 | snowy night, falling snow, plum blossoms in foreground |

### 服装词库(女性)

| 中文 | 英文 |
|------|------|
| 汉服(齐胸襦裙) | high-waisted ruqun hanfu with flowing layers |
| 汉服(交领襦裙) | cross-collared ruqun hanfu with embroidered cuffs |
| 旗装 | Qing-dynasty qizhuang with elaborate cuffs and headdress |
| 武侠劲装 | wuxia martial outfit, fitted dark robe, sash belt |
| 嫁衣 | crimson red Chinese wedding robe with golden phoenix embroidery |
| 素衣 | plain white mourning robe, undecorated, fluid silhouette |

### 服装词库(男性)

| 中文 | 英文 |
|------|------|
| 文人长衫 | scholar's long robe, jade green or ink-blue, simple sash |
| 王孙锦袍 | aristocratic brocade robe with dragon motifs, golden trim |
| 武侠劲装 | dark fitted wuxia robe, sword at hip, leather wrist guards |
| 戎装 | military armor with shoulder pauldrons, red sash |

### 色调词库

| 情绪 | 调色 |
|------|------|
| 古典哀婉 | muted ink-wash palette, soft slate blue and ivory, faint warm amber |
| 浓烈宫斗 | rich vermilion and gold, deep emerald, high contrast |
| 江湖侠义 | dusty earth tones, faded indigo, hint of warm gold |
| 仙侠空灵 | ethereal pale jade, silvery moonlight, drifting mist |
| 穿越奇幻 | dreamy cool teal mixed with warm sunset gold, slight chromatic glow |
| 雪夜诀别 | desaturated icy blue, single crimson accent (clothing/blood/plum) |

### 古风专用镜头语言

| 中文 | 英文 |
|------|------|
| 长袖拂过 | long silk sleeves trailing through the air in slow motion |
| 回眸 | a slow turn of the head, eyes meeting the camera |
| 拔剑 | a single fluid sword-draw, the blade catching cold light |
| 衣袂飞扬 | robes billowing in the wind, layered fabric moving as one |
| 落花 | petals drifting past the lens in shallow focus |
| 风雪 | swirling snow blown across the frame, cinematic slow motion |
| 灯火摇曳 | flickering lantern light casting moving shadows on a face |

---

## 五、参数表

| 用户说 | 技能响应 |
|--------|---------|
| "改 12 格" / "3×4" | 改用 3×4 布局,叙事弧扩展为 12 拍(铺垫×2 / 上升×3 / 转折×3 / 高点×2 / 收束×2) |
| "横版" / "16:9" | 输出长方形布局指令,推荐 3 行 × 3 列或 1 行 × 9 列 cinematic strip |
| "竖版" / "9:16" | 推荐 9 行 × 1 列 vertical scroll 布局,适合短视频平台 |
| "现代剧" / "都市" / "悬疑" | 替换世界观锚点 + 调用对应词库(本 Skill 内置古风词库,其他题材按通用规则生成) |
| "动漫风" / "插画风" | Style 锚点切换为 `anime cinematic style, cel-shaded, vibrant ink-wash background`,移除 photorealistic |
| "只要中文" / "只要英文" | 跳过另一个版本,只输出指定语言 |
| "继续上一段剧情" / "接下来九镜" | 沿用上一轮的人物/世界观/色调锚点,只更新叙事弧内容 |
| 用户给出已有人物设定 | 直接复用为 Character 锚点,不重新设计 |

---

## 六、工作流程

1. **解析用户故事** → 提取主角(可多角)、世界观、情绪基调、核心冲突
2. **确定四组锚点**:Character / World / Palette+Light / Style——这是后续所有内容的母版
3. **规划九镜叙事弧**:按上表分配九镜的功能,先写"九镜叙事弧表格"(中文短句),再展开
4. **写 GPT Image 2 prompt**:
   - 开头:布局指令(3×3、1:1、面板边界、阅读顺序、一致性强调)
   - 中段:逐格写一句话内容(Panel 1: ... Panel 2: ...),每格只写**当下动作 + 取景 + 情绪**,不重写人物
   - 结尾:整体风格收束句
5. **写 Seedance motion prompt**:
   - 第一句 Style & Mood
   - 九句 Per-Shot Action(Shot 1: ... Shot 9: ...),只写**动作 + 镜头运动 + 声音线索**
   - 最后一句 Static Description 锁定调色和质感
6. **双语对照输出**:中文版先出,英文版结构对齐(顺序、镜头编号、动作语义一一对应)
7. **检查清单**:
   - ✅ 人物锚点是否够具体?
   - ✅ 九格的功能是否覆盖完整叙事弧?
   - ✅ Motion prompt 描述的是"场景里发生什么",而不是"摄像机扫过分镜图"?
   - ✅ Static Description 是否锁定了色调和镜头规格?
   - ✅ 中英版本叙事是否一一对应?

---

## 七、避坑规则

| 问题 | 根本原因 | 解决方法 |
|------|---------|---------|
| Seedance 真的拍了一张漫画书在动 | motion prompt 写成"camera pans across the storyboard" | 改写为九个独立场景的动作描述,不提"storyboard"或"panel" |
| 九格里人物长相不一致 | 锚点描述过于抽象("a beautiful woman") | 加入具体年龄/族裔/发型/服装细节,每格重复"this same young woman in pale green hanfu" |
| 九格画风跳脱(有的写实有的卡通) | 没在开头强调风格一致 | 开头加 `unified cinematic style across all 9 panels, identical color grading and lighting throughout` |
| 视频镜头切换太快/太碎 | motion prompt 每镜动作过短 | 每镜动作描述加入"slowly"、"gradually"、"sustained"等时长暗示,15s/9 镜 ≈ 1.6s/镜 |
| 场景突然换天气/换地点 | 锚点里 World 不够锁 | World 锚点写死具体地点和时段:`single location: ancient mountain temple at dawn, mist remains constant throughout` |
| 古风变成"中国风奇幻"四不像 | Style 锚点用了 `oriental fantasy` 之类含糊词 | 明确朝代/类型:`Tang dynasty palace drama` / `Song dynasty wuxia` / `Ming dynasty court intrigue` |

---

## 八、完整示例(古风/穿越剧)

**用户输入:**
> 一个现代女白领穿越成古代将军府的庶女,新婚之夜发现夫君认错了人——他要娶的是她的嫡姐。她坐在红盖头下,听着外面的喜乐,慢慢攥紧了手中的同心结。

**输出:**

```
🎬 GPT Image 2 + Seedance Storyboard

【一致性锚点 / Consistency Anchors】
- Character: A young Chinese woman in her mid-twenties, oval face with delicate features, long black hair styled in an elaborate Tang-style bridal updo with golden phoenix hairpins, wearing a crimson red Chinese wedding robe with intricate golden phoenix and peony embroidery, long flowing sleeves, composed but quietly tense expression
- World/Setting: Interior of a grand Tang-dynasty general's mansion at night, deep red wooden columns, carved screens, hanging palace lanterns casting warm amber light, traditional bridal chamber with a canopied wedding bed draped in red silk
- Palette/Light: Rich crimson and gold dominant palette, warm amber lantern light, deep shadow in corners, a single shaft of cooler moonlight from a latticed window
- Style: Cinematic Chinese period drama, photorealistic, shot on 35mm anamorphic lens, soft film grain, shallow depth of field

═══════════════════════════════════════
📐 Step 1 — GPT Image 2 九宫格 Prompt
═══════════════════════════════════════

【中文版】
生成一张正方形(1:1)电影级故事板图像,内部为 3×3 九宫格布局,九个面板等大,面板之间为细黑边线分隔,按"从左到右、从上到下"顺序展开一个连续叙事。所有九个面板共享同一视觉风格、同一人物、同一光照与色调:画面整体为浓郁的朱红与金色调,温暖的宫灯琥珀光与冷月光交织,大唐时期将军府新婚之夜的喜庆与暗涌并存。同一位中国年轻女子贯穿全部九格:二十多岁,卵脸柳眉,长发盘起唐式高髻配金色凤钗,身着大红绣金凤牡丹嫁衣,神情沉静却暗藏紧绷。

Panel 1: 深夜将军府远景,飞檐翘角,庭院中红灯高悬,门前迎亲队列灯火通明,远处吹拉弹唱的人影模糊。
Panel 2: 新房内景中景,雕花拔步床前,新娘穿大红嫁衣端坐床沿,红盖头盖住整张脸,双手叠放膝上。
Panel 3: 近景红盖头下方视角,她的下颌、唇瓣与缠绕在指间的同心结,烛火在嫁衣金线上跳动。
Panel 4: 中景过肩,夫君身穿大红喜服推门而入,身形修长,面容因背光略显模糊。
Panel 5: 中景双人,他在床沿坐下,伸手想要掀盖头,动作迟疑停顿在半空。
Panel 6: 极特写,他的眼睛——震惊、错愕、瞳孔收缩,光线在他脸上一半明一半暗。
Panel 7: 极特写,红盖头被掀开的瞬间,她的眼睛——平静地直视前方,睫毛低垂,一滴泪悬而未落。
Panel 8: 中景,他站起身向后退一步,她依然端坐,手中的同心结被她慢慢攥紧,指节微微泛白。
Panel 9: 远景空镜,新房门外长廊,大红灯笼仍在风中轻摇,远处喜乐声渐弱,门内一片寂静。

整组九格保持统一的电影质感、35mm 胶片颗粒、浅景深、温暖琥珀光主导冷月光辅助、朱红与金色饱和度一致、人物面容服饰造型在所有镜头中精确一致。

【English】
Create a single cinematic storyboard image, 1:1 square format, containing exactly 9 panels arranged in a 3×3 grid with thin black borders between panels. Each panel is one shot in a continuous narrative, read left-to-right, top-to-bottom. All 9 panels share identical character appearance, wardrobe, lighting, and color palette: a rich crimson and gold dominant tone, warm amber palace-lantern light interwoven with cool moonlight, the festive yet quietly tense atmosphere of a wedding night in a Tang-dynasty general's mansion. The same young Chinese woman appears in all 9 panels: mid-twenties, oval face with delicate brows, long black hair in an elaborate Tang-style bridal updo with golden phoenix hairpins, wearing a crimson red wedding robe with intricate golden phoenix and peony embroidery, composed expression with quiet underlying tension.

Panel 1: Wide establishing shot of the general's mansion at night, sweeping eaves, red lanterns hanging in the courtyard, a wedding procession with bright torches lining the front gate, distant figures of musicians blurred in soft focus.
Panel 2: Medium interior shot of the bridal chamber, the bride in her crimson wedding robe seated at the edge of a carved canopy bed, a red silk veil covering her entire face, hands folded in her lap.
Panel 3: Close-up from below the red veil, revealing her chin, lips, and a Chinese love-knot ornament wound between her fingers, candlelight flickering across the gold thread of her robe.
Panel 4: Medium over-the-shoulder shot, the groom in matching crimson groom's attire stepping through the doorway, tall silhouette, his face slightly obscured by backlight.
Panel 5: Medium two-shot, he sits at the edge of the bed and reaches out to lift the veil, his hand hesitating mid-air.
Panel 6: Extreme close-up of his eyes — shocked, stunned, pupils constricted, one half of his face in warm lantern light and the other half in cool shadow.
Panel 7: Extreme close-up of her eyes the instant the veil is lifted, calm and forward-facing, lashes lowered, a single tear suspended but unfallen.
Panel 8: Medium shot of him standing and stepping back, while she remains seated, her hand slowly tightening around the love-knot, knuckles faintly pale.
Panel 9: Wide empty shot of the corridor outside the bridal chamber, large red lanterns swaying gently in the wind, the distant wedding music fading, silence inside the room.

All 9 panels maintain unified cinematic quality, 35mm film grain, shallow depth of field, warm amber lantern light as key with cool moonlight as fill, identical crimson-and-gold saturation, and precise consistency of the woman's face, hairstyle, and wardrobe throughout.

═══════════════════════════════════════
🎥 Step 2 — Seedance 2.0 Motion Prompt
═══════════════════════════════════════

【中文版】
风格与基调:电影级中国唐代古装剧,24fps,温暖琥珀灯光与冷月光交织,沉静哀婉的喜剧反转,缓慢推进的镜头节奏。

Shot 1: 摄影机由空中缓缓下降,飞檐与红灯笼依次入画,远处迎亲队伍的火把摇曳,鼓乐与人声从远处传来,逐渐清晰。
Shot 2: 静止中景,新娘端坐床沿,红盖头微微随穿堂风颤动,远处喜乐持续,室内只有烛火轻爆的声响。
Shot 3: 微距特写缓慢推进,她的手指逐渐收紧同心结,烛光在金线嫁衣上跳动,呼吸的细微起伏可见。
Shot 4: 摄影机从她背后拉至门口,门被推开,夫君的剪影逆光而立,脚步声从门外踏入室内。
Shot 5: 双人中景,他坐下,手缓缓抬起伸向红盖头,动作在距离盖头一寸处停滞,空气仿佛凝固。
Shot 6: 急速推近至他的眼睛,瞳孔骤然收缩,微小的肌肉颤动,远处喜乐声忽然变得遥远空洞。
Shot 7: 切至她的眼睛特写,睫毛缓慢抬起,一滴泪从眼角凝聚但悬而未落,环境音几乎消失。
Shot 8: 拉远至双人中景,他后退半步、再退一步,她的手在盖头下方持续收紧同心结,只有衣料摩擦的细响。
Shot 9: 摄影机后退穿过门口,带出室外长廊,红灯笼缓慢摇曳,远处喜乐声逐渐淡入又散去,画面以空镜收尾,只剩风声。

静态描述:整段视频保持 35mm 胶片颗粒、浅景深、朱红与金色主导调色、温暖琥珀光为主光冷月光为辅光、人物面容服饰造型严格一致、每镜约 1.6 秒、自然真实的物理光照与丝绸质感。

【English】
Style & Mood: Cinematic Tang-dynasty Chinese period drama, 24fps, warm amber lantern light interwoven with cool moonlight, melancholic wedding-night reversal, slow and sustained pacing throughout.

Shot 1: Camera descends slowly from above, sweeping eaves and red lanterns entering frame, distant torches of the wedding procession flickering, drums and chanting growing gradually clearer.
Shot 2: Static medium shot, the bride seated motionless at the bed's edge, her red veil trembling faintly in a draft, distant music continuing, only the soft crackle of candles audible in the room.
Shot 3: Macro close-up slowly pushing in, her fingers tightening gradually around the love-knot, candlelight dancing on the gold thread of her robe, her shallow breathing visible.
Shot 4: Camera pulls from behind her toward the door, the door opens, the groom's silhouette backlit at the threshold, his footsteps entering the room.
Shot 5: Two-shot, he sits, his hand rising slowly toward the red veil, the motion halting an inch away, the air seeming to freeze.
Shot 6: Rapid push-in on his eyes, pupils contracting sharply, tiny muscle tremors, the distant music suddenly turning hollow and far away.
Shot 7: Cut to extreme close-up of her eyes, lashes slowly lifting, a single tear gathering at the corner but never falling, ambient sound nearly vanishing.
Shot 8: Pulling back to a two-shot, he steps back once, then again, while her hand keeps tightening around the love-knot beneath the veil, only faint silk rustling audible.
Shot 9: Camera retreats through the doorway into the outer corridor, red lanterns swaying gently, distant wedding music fading in and then dissolving, ending on the empty corridor with only wind.

Static Description: Throughout the video, maintain 35mm film grain, shallow depth of field, crimson-and-gold dominant palette, warm amber key light with cool moonlight fill, strict consistency of the woman's face, hairstyle, and wardrobe, approximately 1.6 seconds per shot, natural physical lighting and authentic silk fabric texture.

═══════════════════════════════════════
📋 九镜叙事弧
═══════════════════════════════════════

| # | 镜头功能 | 一句话内容 |
|---|---------|----------|
| 1 | 开场建立 | 将军府新婚夜远景,喜乐迎亲 |
| 2 | 主角登场 | 红盖头下的新娘静坐婚床 |
| 3 | 关系建立 | 她攥紧同心结的细节特写 |
| 4 | 推进 | 夫君推门而入 |
| 5 | 转折 | 他迟疑停在掀盖头的瞬间 |
| 6 | 冲突 | 他的震惊眼神特写——认错了人 |
| 7 | 情绪高点 | 她平静眼中的一滴未落之泪 |
| 8 | 抉择 | 他后退,她手中同心结攥得更紧 |
| 9 | 收束 | 喜乐渐远,长廊空镜余韵 |

---
💡 叙事说明:全片以"喜乐外表 + 内心崩塌"的反差推进,从远景喜庆 → 近景紧绷 → 极特写情绪爆点 → 空镜收束,情绪曲线由静→紧→碎→空,九镜节奏稳定缓慢(1.6s/镜),让观众感到时间被拉长的窒息感。色调全程锁定朱红+金,只在第 9 镜让喜乐声"褪色",形成听觉与视觉的反差收束。
```

---

## 九、注意事项

- **不解释分镜原理**,直接给可用的双段 prompt
- **GPT Image 2 prompt 不写 negative prompt**(模型不支持)
- **Seedance motion prompt 不要写"camera pans across panels"**——这是本 Skill 最重要的一条
- **古风题材默认 photorealistic + cinematic**,除非用户明确说要动漫/插画
- **人物锚点宁可重复也不要换说法**——"the same young woman in crimson wedding robe"在九格描述中反复出现是正确的
- **用户描述极简时**(只给一句"做个九宫格"),可以追问 1 个关键问题(主角是谁?什么剧情?),或先做合理默认并说明
- **中英双版本结构必须对齐**:同一个 Shot 编号,中英描述同一个动作
- **如果用户给出已有 Skill 产出**(比如 flux2-storyboard 或 realistic-character 的人物描述),直接复用,不要重新设计
