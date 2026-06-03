---
name: ltx-delivery-protocol
description: AI 视频项目交付协议——定义 LTX 视频工作流所有生成型 skill 的标准化输出格式。当 Claude 为 LTX 项目生成镜头交付物（Flux2 首尾帧 prompt、LTX motion prompt、镜头计划、Pipeline 决策建议、抽卡记录、失败诊断、剪辑笔记等）时，必须先查阅本 skill 拿到字段定义和模板，然后按本协议输出。本 skill 是被动参考材料——不主动触发、不生成 prompt、不做决策；它是 LTX skill 生态的**格式约束层**，定义"输出长什么样"的统一规范。引用本 skill 的生成型 skill 包括 ltx-t2v-prompt / ltx-i2v-prompt / ltx-flf-prompt / ltx-shot-planning / ltx-pipeline-router / ltx-iteration-strategy / ltx-first-frame-prep。如果用户问"输出格式"、"标准模板"、"交付包"、"项目交付"、"protocol"、"项目记录"，或希望把当前 LTX 工作流产出整理成标准化格式时，使用本 skill。
---

# AI 视频项目交付协议(LTX Delivery Protocol)

## 本 skill 的定位

这是 LTX 视频 skill 生态的**格式约束层**——类似 `ltx-camera-movement` 是运镜词汇底座、`ltx2-reference` 是模型规范底座,本 skill 是**交付格式底座**。

```
                  ┌─────────────────────────────────────┐
                  │   ltx-delivery-protocol (本 skill)  │
                  │   定义所有交付物的字段和格式        │
                  └─────────────────┬───────────────────┘
                                    │ 被引用
        ┌───────────────────────────┼───────────────────────────┐
        ↓                           ↓                           ↓
ltx-shot-planning           ltx-pipeline-router        ltx-i2v-prompt
   输出按协议格式             输出按协议格式              输出按协议格式

        ↓                           ↓                           ↓
ltx-iteration-strategy      ltx-first-frame-prep       ltx-t2v-prompt / ltx-flf-prompt
   输出按协议格式             输出按协议格式              输出按协议格式
```

**本 skill 不做什么**:
- 不主动触发生成任何内容
- 不写 prompt
- 不做 pipeline 决策
- 不诊断失败

**本 skill 做什么**:
- 定义"镜头交付物长什么样"
- 定义"项目级元数据长什么样"
- 提供可粘贴的模板
- 统一跨 skill 的字段命名(避免"运镜 vs 运动类型 vs camera movement"这种术语漂移)

---

## 三级交付结构

LTX 项目交付物按三级组织,从粗到细:

```
Level 1 · Project Package(项目交付包)
  └─ 包含 1+ 个 Shot Deliverable
     └─ 每个 Shot Deliverable 包含 Shot Header + Pipeline Block + Prompt Block + Risk Block
```

**单镜头任务**:只需要 Level 2 (Shot Deliverable)
**多镜头项目**:Level 1 包裹多个 Level 2,加项目级元数据

---

## Level 2 · Shot Deliverable(单镜头交付物)

### 字段清单(必填 / 选填)

| 字段名 | 类型 | 必填? | 来源 skill | 说明 |
|---|---|---|---|---|
| `shot_id` | string | **必填** | shot-planning | 唯一标识,格式 `[project]-shot-[NN]-[role]` |
| `narrative` | string | **必填** | shot-planning | 一句话讲清这个镜头讲什么 |
| `shot_role` | enum | **必填** | shot-planning | establishing / detail / transition / climax / closer |
| `duration` | string | **必填** | shot-planning / pipeline-router | 如 `5s` |
| `aspect_ratio` | string | **必填** | shot-planning | 如 `9:16 vertical` / `16:9 horizontal` / `1:1 square` |
| `shot_scale` | enum | **必填** | shot-planning | extreme-wide / wide / medium / close-up / extreme-close-up |
| `camera_movement` | string | **必填** | shot-planning / camera-movement | 如 `locked-off` / `dolly-in` / `pan-left-to-right` |
| `pipeline` | enum | **必填** | pipeline-router | i2v / flf / t2v |
| `decision_source` | string | **必填** | pipeline-router | 如 `ltx-pipeline-router → scene i2v-A` |
| `decay_score` | int | 选填 | pipeline-router | 衰减计分(仅 i2v/flf 场景填),含命中因子 |
| `fallback_route` | string | **必填** | pipeline-router | 如 `i2v → flf (if 3-run decay confirmed)` |
| `ltx_params` | object | 选填 | iteration-strategy | 如 `{last_strength: 0.85}` |
| `first_frame_prompt` | string | i2v/flf 必填 | first-frame-prep + Flux2 | 英文 prompt block |
| `last_frame_prompt` | string | flf 必填 | first-frame-prep + Flux2 | 英文 prompt block;i2v 标 `N/A · i2v 不需要` |
| `motion_prompt_en` | string | **必填** | i2v/flf/t2v-prompt | 英文 LTX motion prompt |
| `motion_prompt_zh` | string | **必填** | i2v/flf/t2v-prompt | 中文对照翻译 |
| `duration_rationale` | string | **必填** | i2v/flf/t2v-prompt | 为什么选这个时长 |
| `rolling_strategy` | string | **必填** | i2v/flf/t2v-prompt | 跑几次 / seed 策略 / 选哪个标准 |
| `risk_watchlist` | array<string> | **必填** | i2v/flf/t2v-prompt | 本镜头需要观察的衰减/漂移点 |
| `fallback_plan` | string | **必填** | i2v/flf/t2v-prompt + iteration-strategy | 失败后的转换方案 |

### 标准模板(可直接复制)

````markdown
# Shot Deliverable

```yaml
shot_id: <project>-shot-<NN>-<role>
narrative: "<一句话讲清这个镜头讲什么>"
shot_role: <establishing | detail | transition | climax | closer>
duration: <Ns>
aspect_ratio: <9:16 vertical | 16:9 horizontal | 1:1 square>
shot_scale: <extreme-wide | wide | medium | close-up | extreme-close-up>
camera_movement: <locked-off | dolly-in | dolly-out | pan-left | pan-right | tilt-up | tilt-down | truck-left | truck-right | arc | handheld | pov | ...>
pipeline: <i2v | flf | t2v>
decision_source: "<ltx-pipeline-router → scene X-Y>"
decay_score: <integer> (<命中因子说明>)
fallback_route: "<主路 → 备选路>"
ltx_params: { <参数键>: <值> }
```

---

## 🖼️ First Frame Prompt (Flux2)

```
<英文 Flux2 prompt,可直接粘贴>
```

## 🖼️ Last Frame Prompt (Flux2)

*仅 flf pipeline 需要;i2v / t2v 留 `N/A · pipeline 不需要`*

```
<英文 Flux2 prompt 或 N/A>
```

## 🎬 Motion Prompt (LTX 2.3)

```
<英文 LTX motion prompt,可直接粘贴>
```

## 🀄 中文对照

<motion prompt 的中文翻译,信达雅>

## ⏱️ Duration

**<Ns>** — <理由,一两句>

## 🎲 Rolling Strategy

<跑几次 / seed 策略 / 怎么选最佳版本>

## 💡 Risk Watchlist

- <本镜头容易踩的坑 1>
- <本镜头容易踩的坑 2>
- ...

## 🆘 Fallback Plan

<如果主路稳定失败,转什么 pipeline / 需要什么准备工作>
````

---

## Level 1 · Project Package(多镜头项目交付包)

多于 1 个镜头的项目使用本结构包裹多个 Shot Deliverable。

### 字段清单

| 字段名 | 类型 | 必填? | 说明 |
|---|---|---|---|
| `project_id` | string | **必填** | 项目唯一标识 |
| `project_type` | enum | **必填** | single-shot / multi-shot / series-episode |
| `total_duration` | string | **必填** | 总时长 |
| `shot_count` | int | **必填** | 镜头数 |
| `aspect_ratio` | string | **必填** | 项目主画幅(可被单镜头覆盖) |
| `target_platform` | string | 选填 | TikTok / YouTube Shorts / WeChat / 影院 等 |
| `world_bible_skill` | string | 选填 | 引用的项目宪法 skill,如 `cuojia-longgu`,无则填 `none` |
| `world_bible_anchors` | object | 选填 | 从 world-bible 拉过来的固定字段(Character / Visual Style / Palette & Light / World Rules / Story Tone) |
| `seed_log` | array | 选填 | 每镜头使用的 Flux2 / LTX seed 记录 |
| `rolling_history` | array | 选填 | 每镜头抽卡历史(跑了几次,每次状况,哪次胜出) |
| `failure_log` | array | 选填 | 失败诊断记录(哪些镜头衰减过,怎么修的) |
| `seed_reuse` | object | 选填 | 黄金种子池 + 跨镜头复用关系 |
| `editing_notes` | array | 选填 | NLE 剪辑笔记(硬切/淡入淡出/转场/速率变化) |
| `audio_strategy` | object | 选填 | BGM / SFX / 环境音方案 |

### 标准模板(可直接复制)

````markdown
# Project Package: <project_id>

## Project Overview

```yaml
project_id: <project_id>
project_type: <single-shot | multi-shot | series-episode>
total_duration: <Ns>
shot_count: <N>
aspect_ratio: <主画幅>
target_platform: <平台>
world_bible_skill: <宪法 skill 名 | none>
```

## World Bible Anchors

*从 ltx-world-bible 或项目宪法 skill 拉过来的固定锚点,所有镜头共用。如无项目宪法,填 `N/A`*

```yaml
character: "<人物/主体锚点,逐字引用>"
visual_style: "<视觉风格锚点,逐字引用>"
palette_and_light: "<调色与光线锚点,逐字引用>"
world_rules: "<世界规则,逐字引用>"
story_tone: "<叙事基调,逐字引用>"
```

---

## Shot Manifest

### Shot 01: <shot_id>

[完整 Shot Deliverable 内容,按 Level 2 模板]

---

### Shot 02: <shot_id>

[完整 Shot Deliverable 内容,按 Level 2 模板]

---

[更多镜头...]

---

## Cross-Shot Tracking

### Seed Log

```yaml
shot-01:
  flux2_first_frame: { seed: <int>, run: <int>, status: <selected | rejected> }
  flux2_last_frame: { seed: <int>, run: <int> }  # 仅 flf
  ltx_motion: { seed: <int>, run: <int>, status: <selected | rejected> }
shot-02:
  ...
```

### Rolling History

```yaml
shot-01-ltx-motion:
  - { run: 1, seed: <int>, outcome: "末段天空变黑", verdict: rejected }
  - { run: 2, seed: <int>, outcome: "健康", verdict: selected ✅ }
  - { run: 3, seed: <int>, outcome: "烟囱消失", verdict: rejected }
shot-02-ltx-motion:
  ...
```

### Failure Log

```yaml
- shot: shot-01
  failure: "i2v 推近版本末段衰减,3 次稳定失败"
  root_cause: "低光暖色推近场景 i2v 物理短板"
  fix: "改 flf,补门口尾帧,问题解决"
  lesson: "推近 + 低光暖光 = 默认 flf,不要试 i2v"
```

### Seed Reuse

```yaml
golden_seeds:
  flux2_8472: { used_for: ["shot-01-first-frame", "shot-02-first-frame"], note: "本项目外景调色锚点" }
  ltx_3091: { used_for: ["shot-01-motion"], note: "静景微动稳定 seed,待跨镜头验证" }
```

### Editing Notes

```yaml
shot-01 → shot-02: 硬切 (参考视频原片就是硬切)
shot-02 末尾: 0.3s 黑场 fade-out
```

### Audio Strategy

```yaml
bgm:
  track: "<曲名或风格>"
  volume: <低 | 中 | 高>
  in_out: "<进出策略>"
sfx:
  shot-01: ["soft wind", "muffled snowfall"]
  shot-02: ["candle crackle", "wind through window"]
ambient: "<整体环境音方向>"
```
````

---

## 字段命名标准词典

跨所有 LTX skill 使用同一套术语,避免"运镜"在一处叫 camera_movement、另一处叫 motion_type 这种漂移。

### 镜头层术语

| 标准词 | 中文 | 取值 | 替代词(❌ 不要用) |
|---|---|---|---|
| `shot_id` | 镜头 ID | string | "分镜编号"、"clip ID" |
| `narrative` | 镜头叙述 | string | "镜头描述"、"内容说明" |
| `shot_role` | 镜头作用 | establishing / detail / transition / climax / closer | "镜头类型"、"镜头功能" |
| `shot_scale` | 景别 | extreme-wide / wide / medium / close-up / extreme-close-up | "镜头大小"、"框架" |
| `camera_movement` | 运镜 | 见 ltx-camera-movement 词典 | "运动方式"、"motion type"(motion type 专指视频动作类型,不是运镜) |
| `aspect_ratio` | 画幅 | `9:16 vertical` / `16:9 horizontal` / `1:1 square` | "比例"、"格式" |
| `duration` | 时长 | `Ns`(秒) | "长度"、"length" |

### Pipeline 层术语

| 标准词 | 中文 | 取值 | 替代词(❌ 不要用) |
|---|---|---|---|
| `pipeline` | 生成路线 | i2v / flf / t2v | "模式"、"方式"、"路径" |
| `motion_type` | 运动类型 | static / a-to-b / free / abstract | (注意:跟 camera_movement 不是一回事) |
| `decay_score` | 衰减计分 | integer (0-10) | "衰减分数"、"风险分" |
| `decision_source` | 选型依据 | string(引用场景图谱) | "选型理由"、"决策依据" |
| `fallback_route` | 兜底路线 | string(主路 → 备选) | "备选"、"plan B" |

### 资产层术语

| 标准词 | 中文 | 类型 | 替代词(❌ 不要用) |
|---|---|---|---|
| `first_frame` | 首帧 | 图片 / prompt | "起点帧"、"开头"、"start frame"、"image_in" |
| `last_frame` | 尾帧 | 图片 / prompt | "终点帧"、"结尾"、"end frame"、"image_out" |
| `motion_prompt` | 运动提示词 | string | "video prompt"、"运动描述" |
| `seed` | 种子 | integer | "随机数"、"random"、"seed_id" |
| `run` | 抽卡次数 | integer (1-indexed) | "trial"、"attempt"、"次" |

### 项目层术语

| 标准词 | 中文 | 类型 | 替代词(❌ 不要用) |
|---|---|---|---|
| `project_id` | 项目 ID | string | "项目编号"、"project name" |
| `world_bible` | 项目宪法 / 世界观 | 引用 skill 名 | "设定"、"bible"、"宪章" |
| `golden_seed` | 黄金种子 | int | "好 seed"、"best seed" |
| `rolling_history` | 抽卡历史 | array | "trial log"、"抽卡记录" |
| `failure_log` | 失败诊断记录 | array | "bug log"、"问题记录" |

---

## 被引用方式(给其他生成型 skill 看的部分)

### 引用本 skill 的 skill 应该做什么

1. **在 SKILL.md 顶部加一句引用声明**:
   ```
   > 输出格式遵循 ltx-delivery-protocol 协议。
   ```

2. **在输出生成前先 view `/mnt/skills/user/ltx-delivery-protocol/SKILL.md`**,拿到模板。

3. **填字段时严格按本 skill 的命名词典**,不创造同义词。

4. **填不出的字段标 `TBD` 或 `N/A · 原因`**,不要省略字段。省略 = 协议被打破。

### 各生成型 skill 的填字段责任

| skill | 填哪些字段 | 不填(留给别的 skill 填) |
|---|---|---|
| `ltx-shot-planning` | `shot_id`, `narrative`, `shot_role`, `duration`, `aspect_ratio`, `shot_scale`, `camera_movement` | pipeline 决策、prompt 内容、seed |
| `ltx-pipeline-router` | `pipeline`, `decision_source`, `decay_score`, `fallback_route`, `ltx_params` | prompt 内容、seed |
| `ltx-first-frame-prep` | `first_frame_prompt`, `last_frame_prompt`(若 flf) | motion prompt、seed |
| `ltx-i2v-prompt` / `ltx-flf-prompt` / `ltx-t2v-prompt` | `motion_prompt_en`, `motion_prompt_zh`, `duration_rationale`, `rolling_strategy`, `risk_watchlist`, `fallback_plan` | shot header、pipeline 决策 |
| `ltx-iteration-strategy` | 更新 `rolling_history`, `failure_log`, `seed_log` | 不改既有 Shot Deliverable 的 prompt 内容 |
| `ltx-world-bible` / 项目宪法 skill | `world_bible_anchors` 字段内容 | 不参与单镜头交付 |

---

## 应用示例

### 示例 1 · 单镜头 i2v 交付(雪林小屋静景)

````markdown
# Shot Deliverable

```yaml
shot_id: cabin-winter-cozy-001-shot-01-exterior
narrative: "雪林深处的 A 字小屋静静伫立,窗内透出温暖橙光,飘雪持续不断,烟囱细烟袅袅"
shot_role: establishing
duration: 5s
aspect_ratio: 9:16 vertical
shot_scale: wide
camera_movement: locked-off
pipeline: i2v
decision_source: "ltx-pipeline-router → scene i2v-A (纯静景微动)"
decay_score: 3 (低光++ + 暖色++,无推近无 ≥5s)
fallback_route: "i2v → flf (if 3-run decay confirmed,补几乎相同的尾帧)"
ltx_params: { N/A · i2v 无 last_strength 参数 }
```

---

## 🖼️ First Frame Prompt (Flux2)

```
A small A-frame mountain cabin nestled deep in a snowy deciduous forest, steep triangular roof clad in weathered cedar shingles heavy with thick fresh powder snow, dark cedar plank siding, a thin stone chimney releasing a delicate wisp of woodsmoke into the cold air, warm amber 2700K tungsten light glowing from the triangular front window and small upper gable window, spilling a soft orange pool onto the snow-covered wooden porch where two simple wooden chairs sit dusted with snow. Framed in the foreground by two massive bare tree trunks acting as natural side curtains, with countless slender bare branches receding into atmospheric haze behind the cabin. Heavy snowstorm in progress, fat motion-blurred snowflakes falling thickly through the entire frame. Soft diffused daylight from an overcast snowy sky, cool grey-blue ambient tone outside contrasting with the warm amber glow from inside the cabin. Cinematic cozy cabin photography, AI-generated photorealistic aesthetic, ultra-detailed, shot on Hasselblad H6D medium format, 50mm lens, vertical 9:16 portrait orientation.
```

## 🖼️ Last Frame Prompt (Flux2)

`N/A · i2v pipeline 不需要尾帧`

## 🎬 Motion Prompt (LTX 2.3)

```
Locked-off camera, the frame stays completely still throughout the entire shot. Heavy snow falls continuously across the frame in soft motion-blurred streaks, the snowflakes drifting at slightly varying speeds from upper-right to lower-left. A thin wisp of pale grey woodsmoke rises slowly and steadily from the stone chimney, curling and dissipating into the cold air. The warm amber light glowing from the cabin windows pulses with the faintest, almost imperceptible flicker, as if a fire is burning inside. The bare tree branches in the background sway minimally under the weight of fresh snow. The final frame matches the first frame in lighting, exposure, and color temperature. Ambient sound of soft wind and muffled snowfall.
```

## 🀄 中文对照

固定镜头,整个画面始终静止。大雪持续从画面飘落,雪花以柔和的运动模糊条纹下落,方向从右上向左下偏移。一缕淡灰色木烟从石砌烟囱缓慢稳定地升起,在屋顶上方卷曲消散。窗户中透出的温暖橙光带着几乎无法察觉的微弱呼吸式闪烁。背景中光秃秃的树枝在新雪重压下极轻微地摇晃。末帧的光线、曝光、色温与首帧一致。环境音是柔和的风声与被雪压低的飘雪声。

## ⏱️ Duration

**5s** — 静景 + 飘雪是 LTX 最稳的组合,5 秒能让雪花充分覆盖一轮节奏,且不踩"暗场长时长 → 末尾衰减"红线

## 🎲 Rolling Strategy

跑 3 次同 prompt 不同 seed,选末段天空亮度最接近首帧的那版,记下 seed 进黄金种子池

## 💡 Risk Watchlist

- 天空末段是否变黑(t1.mp4 老毛病的复发风险)
- 烟囱细烟是否在末段消失
- 窗光"flicker"被 LTX 误读为"逐渐熄灭"
- 雪量是否在末段减弱

## 🆘 Fallback Plan

若 3 次都明显衰减 → 改 flf,补一张"几乎相同的尾帧"(仅雪花随机性差异),进入 `ltx-flf-prompt`
````

---

### 示例 2 · 多镜头项目包(2 镜头雪林小屋成片)

````markdown
# Project Package: cabin-winter-cozy-001

## Project Overview

```yaml
project_id: cabin-winter-cozy-001
project_type: multi-shot
total_duration: 10s
shot_count: 2
aspect_ratio: 9:16 vertical
target_platform: 小红书 / 抖音 / YouTube Shorts
world_bible_skill: none (单条短视频,无系列宪法)
```

## World Bible Anchors

```yaml
character: N/A · 本项目无人物
visual_style: "A-frame mountain cabin / weathered cedar siding / heavy snowstorm in deciduous forest / cozy cabin aesthetic"
palette_and_light: "warm amber 2700K interior glow ↔ cool grey-blue snow exterior / overcast daylight ambient / film-look color grading"
world_rules: "永远飘雪 / 永远阴天白天(不是傍晚不是夜晚) / 永远是同一栋 A-frame cabin / 暖光永远从窗内透出"
story_tone: "静谧 / 温暖 / 治愈 / 隔绝感 / 慢节奏"
```

---

## Shot Manifest

### Shot 01: cabin-winter-cozy-001-shot-01-exterior

[完整 Shot Deliverable,参见示例 1]

---

### Shot 02: cabin-winter-cozy-001-shot-02-bedroom

```yaml
shot_id: cabin-winter-cozy-001-shot-02-bedroom
narrative: "阁楼三角顶下的卧室温暖静谧,蜡烛轻颤,窗外飘雪,凌乱柔软的被褥让人想钻进去"
shot_role: detail
duration: 5s
aspect_ratio: 9:16 vertical
shot_scale: medium
camera_movement: locked-off
pipeline: i2v
decision_source: "ltx-pipeline-router → scene i2v-A + i2v-G (静景微动 + 烛火动态)"
decay_score: 4 (低光++ + 暖色++,室内场景比外景略暗)
fallback_route: "i2v → flf (if 3-run decay or candle 失控 confirmed)"
ltx_params: { N/A · i2v }
```

[其余字段省略,按 Level 2 模板填]

---

## Cross-Shot Tracking

### Seed Log

```yaml
shot-01:
  flux2_first_frame: { seed: TBD, run: TBD, status: pending }
  ltx_motion: { seed: TBD, run: TBD, status: pending }
shot-02:
  flux2_first_frame: { seed: TBD, run: TBD, status: pending }
  ltx_motion: { seed: TBD, run: TBD, status: pending }
```

### Rolling History

*跑完抽卡后填入,目前 pending*

### Failure Log

*生成过程中如有失败诊断,实时填入*

### Seed Reuse

```yaml
golden_seeds:
  flux2_TBD: { used_for: ["shot-01-first-frame", "shot-02-first-frame"], note: "外景与卧室共用,保证色调统一" }
```

### Editing Notes

```yaml
shot-01 → shot-02: 硬切 (参考视频原片就是硬切)
shot-02 末尾: 可选 0.3s 黑场 fade-out 收尾
```

### Audio Strategy

```yaml
bgm:
  track: 无 / 极低音量环境氛围乐
  volume: 低
  in_out: 整段渐入渐出
sfx:
  shot-01: ["soft wind", "muffled snowfall"]
  shot-02: ["faint candle crackle", "muffled wind through window", "occasional creak of wood"]
ambient: "整体走 ASMR 治愈方向,无人声"
```
````

---

## 升级日志

| 日期 | 更新内容 | 来源对话 |
|---|---|---|
| 2026-05-26 | 初版建立,Level 1/2 双级结构 + 字段命名词典 + 2 个应用示例 | 山地小屋项目复盘 + 用户协议层需求确认 |

---

## 使用纪律

- 本 skill 是**被动参考材料**,不主动触发生成
- 其他 skill 引用本 skill 时,**只复制需要的字段**,不要把整份协议塞进每个交付物
- 字段命名词典是**硬约束**,创造同义词 = 协议失效
- 用户表示"不需要这么正式"时,可以简化输出,但**字段名仍按本协议**(只是省略部分字段)
- 协议字段不足以覆盖某个项目的需求时,**反向喂回本 skill 升级**,不要在生成型 skill 里临时造字段
