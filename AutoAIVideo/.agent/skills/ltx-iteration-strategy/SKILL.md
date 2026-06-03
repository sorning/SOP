---
name: ltx-iteration-strategy
description: AI 视频生成失败后的诊断与重 roll 策略——把"一次出片"心态换成"三选一 + 局部 Retake + 种子管理"工作流。当用户说"生成的视频不对/有问题"、"怎么重新生成"、"哪里不好怎么改"、"动了但是怪"、"出来的不是我要的"、"重新跑一次"、"retake"、"种子"、"variation"、"换个版本"时，主动使用此技能。也在用户描述具体失败现象（脸变了 / 闪 / 抖 / 静止 / 糊 / 崩 / 漂 / 飘）时主动使用。本 skill 是 AI 视频工作流的**下游 skill**——拿到 prompt 跑出来的初版后用它诊断问题、决定救哪段、给重 roll 策略。不替代 prompt skill（ltx-t2v-prompt / ltx-i2v-prompt / ltx-flf-prompt），而是给它们提供"出错了之后怎么办"的指导。**如果用户已有 ltx-world-bible（或项目宪法 skill）产出的世界观锚点，诊断的第一步必须是对照锚点比对——脸飘了对照 Character、色调飘了对照 Palette & Light、风格飘了对照 Visual Style——锚点比"凭感觉看哪里不对"更可靠；Retake 时锚点内容不许改，只调镜头参数 / 种子 / motion 描述**。
---

# AI 视频迭代与重 roll 策略

## 本 skill 的定位

这是 AI 视频工作流的**下游 skill**——视频跑完看到结果后用它。

```
[ltx-i2v-prompt 等] 写完 prompt → 跑出来初版
                                      ↓
                                  不满意？→ [本 skill] 诊断 + 决策
                                                          ↓
                                              ┌────────────┼────────────┐
                                              ↓            ↓            ↓
                                            重 roll    局部 Retake    接受+剪辑救
                                              ↓            ↓            ↓
                                         回 prompt skill  调段     进 NLE 修
                                         调参后再跑
```

**本 skill 核心命题**：

1. **AI 视频生成本质是抽奖**——同一个 prompt 跑 5 次结果差异巨大。**不要追求"一次出片"**
2. **抽到差视频不等于 prompt 错**——可能 prompt 完全没问题，只是这次种子不好
3. **局部重生 > 整体重 roll**——LTX Retake / 模型分段 = 业界共识
4. **诊断 > 直觉调整**——先判断失败属于哪一类，再决定救法

跟其他 skill 的关系：本 skill **不写 prompt**——它产出的是"哪里出了问题、用什么策略救、要回哪个 skill 调整什么"。具体的 prompt 修改交给 prompt skill。

---

## 第一性原理：AI 视频的 3 个不可绕开的事实

### 事实 1：种子决定的随机性是主导，不是 prompt

LTX 2.3 这类 transformer 视频模型，**同一 prompt 不同 seed 的方差极大**：
- Latent diffusion 图像模型（Flux）：同 seed + 同 prompt ≈ 像素级一致
- Transformer 视频模型（LTX / Sora / Kling）：同 seed + 同 prompt = 帧级稳定，但 inter-run drift 明显
- 现实结果：**5 次跑同 prompt，可能 1 次很好、2 次能用、2 次崩**

含义：
- 看到一次失败**不要立刻改 prompt**——可能改了下次还崩
- **先用同 prompt 重 roll 2-3 次**，看是不是稳定失败
- 只有 3 次都同一种失败 → 才是 prompt 问题

### 事实 2：错误累积——"Chinese whispers"

AI 视频本质是"前一帧 → 下一帧"的逐帧生成。每帧的小漂移会**指数累积**：

- 第 10 帧：眼睛颜色微变（几乎察觉不到）
- 第 50 帧：脸型微变（开始能看出）
- 第 100 帧：完全换了一个人

这是为什么**长视频比短视频脆弱得多**。10 秒视频不是 5 秒视频质量的两倍——是**几何级数下降**。

含义：
- 视频越长越要分段
- 长视频出问题，**80% 都在后半段**
- 救法不是整段重 roll，是缩短时长或局部 Retake 后段

### 事实 3：失败模式有限——能分类、能诊断、能定位

虽然失败花样多，但归类只有 4 大类（见下方诊断节）。**每一类都有特定救法**——不需要漫无目的乱改 prompt。

---

## 心态切换：抽卡心态 vs 一次出片心态

| 一次出片心态（错） | 抽卡心态（对） |
|---|---|
| 跑一次看效果，不行就改 prompt | 跑 3 次同 prompt，选最佳 |
| 想一次完美 | 假设第 1 次必然有瑕疵 |
| 怕"浪费 credit"舍不得多跑 | 把 credit 预算分给 3-5 个版本 |
| 不喜欢 = 整段重新生成 | 不喜欢 = 局部 Retake 一段 |
| 把好种子忘掉 | 把好种子记下来复用 |
| 失败原因猜测 | 失败按 4 类诊断 |

**专业 AI 视频创作者的成功率公式**：

```
最终成片质量 ≈ (prompt 质量) × (种子运气) × (迭代次数) × (Retake 精度)
```

把"一次出片"换成"三选一 + 局部修"，**成功率从 30% 跳到 80%**。

---

## 失败模式诊断（4 大类）

任何 AI 视频问题先归到 4 类里——每类有明确救法，不要乱猜。

### 类型 A · Spatial 类（单帧空间问题）

**症状**：单看任一帧画面就有问题。包括：
- **Warping / Melting**（扭曲/熔化）——肢体不对、物体形变
- **Artifacts**（异物）——画面多出莫名其妙的东西
- **Identity drift**（身份漂移）——人脸变了、产品形态变了
- **Hands / fingers**（手指崩）——经典 AI 弱项
- **Text garbled**（文字糊）——必然崩

**根因**：
- 单帧的"空间正确性"问题
- 多半源于 prompt 信息密度过高 / 主体过复杂 / 首帧不合格

**救法**（按优先级）：

1. **降复杂度**：去掉 prompt 里非核心的修饰词（保留主体 + 动作，砍掉其他）
2. **改首帧**（i2v/flf）：回 `ltx-first-frame-prep` 重做首帧
3. **避开高风险元素**：手指 → 改中景、文字 → 后期叠加、复杂图案 → 简化
4. **拆短时长**：5 秒崩了 → 试 3 秒
5. **重 roll**：以上都试了还崩 → 换种子重跑 2-3 次

### 类型 B · Temporal 类（时间连续性问题）

**症状**：单帧 OK，但帧间有问题。包括：
- **Flicker**（闪烁）——画面亮度/颜色帧间跳
- **Warble**（蠕动）——本应静止的物体微微颤动
- **Frame jump**（跳帧）——某帧突然变化
- **End decay**（末尾衰减）——画面越往后越糊/变暗/物体消失
- **Static / no motion**（静止）——视频几乎不动

**根因**：
- 帧间一致性丢失
- 多半源于 motion strength 过高或过低 / 时长过长 / 光线方向不稳

**救法**（按优先级）：

1. **缩短时长**：闪烁 / 蠕动 / 衰减都和时长正相关——5 秒崩 → 试 3 秒
2. **调 motion strength**：
   - **过抖** → 降 motion strength + 加 `subtle / minimal / steady`
   - **过静** → 升 motion strength + 用强动词 / 加环境运动描述
3. **稳定光线 prompt**：加 `consistent lighting, stable exposure, single light source`
4. **末尾衰减**：加 `final frame matches first frame in lighting and color temperature`
5. **flf 场景静态输出**：调 `last_strength` 0.95 → 0.75（详见 `ltx-flf-prompt`）

### 类型 C · Sync 类（同步问题）

**症状**：视频元素之间不同步。包括：
- **Lip-sync off**（口型不对）——人物嘴动但跟台词不对位
- **Audio-visual desync**（音画不同步）——动作发生在错的音乐拍上
- **Camera-action mismatch**（镜头与动作错位）——镜头到位时动作还没完成

**根因**：
- 时间分配问题
- prompt 里没明确每个事件发生的时刻

**救法**：

1. **加时间分配指令**（来自 `ltx-camera-movement` 原则 3）：
   - `completing by the Xth second, then holds steady`
   - `she finishes the gesture by the 4th second`
2. **拆短台词**（来自 `ltx-flf-prompt` Dialogue 写法）：短句 + 表演指示穿插
3. **降低同时发生的事件数**：3 件事并行 → 拆成 2 段独立镜头
4. **lip-sync 不准**：LTX 2.3 Pro 有 LipDub 专门 pipeline，普通 i2v 不擅长长台词

### 类型 D · Intent 类（意图错位）

**症状**：技术上没问题，但**不是用户想要的**。包括：
- 风格不对（想要电影感，出来像广告）
- 节奏不对（想要慢，出来太快）
- 情绪不对（想要悲伤,出来平淡）
- 内容偏离（想要 A 动作,模型自由发挥成 B）

**根因**：
- prompt 缺乏关键意图锚点
- LTX 默认填空：缺什么模型自己编

**救法**：

1. **风格不对**：补**电影/质感锚点词**——`35mm film grain, anamorphic lens flare, shallow depth of field, cinematic color grading`
2. **节奏不对**：用时间分配 + audio 节奏控制——audio 描述会反向影响运动节奏（详见 `ltx-flf-prompt` Audio 节）
3. **情绪不对**：用物理线索代替情绪标签（详见 `ltx-flf-prompt`）——`her eyes lower, jaw tightens` 而不是 `she looks sad`
4. **内容偏离**：用因果链强化主线——`as A happens, B follows, because C`

---

## 决策树：拿到失败视频该怎么办

```
看到失败视频
    ↓
Step 1: 这是单次失败还是稳定失败？
    └─ 用同 prompt 重 roll 2 次
        ├─ 3 次结果差异大 → 单次抽卡问题
        │     └─ 选最好那次，或继续 roll 1-2 次取最佳
        └─ 3 次同一种失败 → 稳定失败，进 Step 2

Step 2: 失败属于哪一类？
    ├─ 类型 A（Spatial） → 用 A 救法
    ├─ 类型 B（Temporal） → 用 B 救法
    ├─ 类型 C（Sync） → 用 C 救法
    └─ 类型 D（Intent） → 用 D 救法

Step 3: 是整段救还是局部救？
    ├─ 失败覆盖整段 → 回 prompt skill 改后整段重 roll
    ├─ 失败集中在某一段（如末尾 2 秒崩了）
    │     └─ 用 LTX Retake / 模型局部重生
    └─ 失败在 1-2 帧瞬间 → 接受 + NLE 后期遮盖（速度块、模糊、剪掉）
```

---

## 三选一原则（核心工作流）

**永远跑 3 个版本，不要只跑 1 个。**

具体操作：

1. **第 1 版**：默认 seed（让模型自由发挥）
2. **第 2 版**：换 seed（同 prompt 再跑一次）
3. **第 3 版**：换 seed（同 prompt 第三次跑）

如果你的工具支持 batch generation，**同时提交 3 个** —— 等待时间一样，credit 翻 3 倍但成功率从 30% 跳到 80%。

如果不支持 batch，**串行跑 3 次** —— 总时间 ×3 但仍比"跑 1 次失败 + 改 prompt 再跑 1 次失败 + 再改 1 次"快。

**选择标准（不只是"哪个好看"）**：

| 维度 | 怎么看 |
|---|---|
| 主线动作是否到位 | 用户最想看到的那个动作有没有发生 |
| 身份是否稳定 | 全程人脸/产品是同一个 |
| 帧间是否连续 | 拖时间轴扫一遍，有没有闪烁/跳变 |
| 末尾是否衰减 | 看最后 1 秒画质 vs 第 1 秒 |
| 是否符合意图 | 风格、节奏、情绪是否匹配 |

**选定后必做**：把胜出版本的 **seed 记下来**——下次同角色/同场景跑变体时复用。

---

## 种子管理（IP / 系列必须）

如果在做系列内容（连续短剧、产品广告系列、IP 角色），种子管理是**专业 vs 业余的分水岭**。

### 三级种子档案

| 种子级别 | 用途 | 记录位置 |
|---|---|---|
| **黄金种子**（gold seed） | 同一角色 / 同一产品的"基础形态"种子，反复复用 | 项目宪法 skill（如 `cuojia-longgu`）顶端 |
| **场景种子**（scene seed） | 某个场景（光线/色调/构图）的稳定种子 | 镜头清单备注 |
| **试验种子**（trial seed） | 当次抽卡选中的最佳种子 | 单次输出备注 |

### 黄金种子如何建立

1. 用同一 prompt 跑 10-20 个 seed
2. 标注每个出片质量（1-5 分）
3. 把 5 分的 seed 编号记下，叫"黄金种子池"
4. 之后这个角色/产品的视频，**优先用黄金种子池里的种子起手**

### Batch-Seed 协议（跨镜头一致性）

同一角色出现在 5 个镜头里——不要每个镜头从随机 seed 起。**用同一个黄金种子起 5 个镜头**：

- 镜头 1：seed_gold + prompt_1
- 镜头 2：seed_gold + prompt_2
- 镜头 3：seed_gold + prompt_3
- ...

这样身份漂移概率显著下降。

**和 `ltx-first-frame-prep` 的衔接**：first-frame-prep skill 里已经有 Batch-Seed 协议讲首帧出图——视频生成阶段同理。

---

## LTX 局部重生工具：Retake 和 Extend

LTX 2.3 Pro 提供两个**段级**工具，比整段重 roll 高效得多：

### Retake（段级替换）

**原理**：选中视频中的一个时间段（通常 2-16 秒），让模型只重新生成这段，其余保持不变。

**用法场景**：
- 视频中段动作不对，其余都好 → Retake 这一段
- 末尾衰减但前半段好 → Retake 最后 2 秒
- 想试不同情绪/节奏的同段 → Retake 出多个变体

**Retake prompt 写法**：
- 必须**清楚描述这段要发生什么**（不能太抽象，否则会漂离原视频太远）
- 加**承接前段** + **接续后段**的描述（保持连续性）
- 时长精确到秒：`from second 3 to second 5: ...`

### Extend（前后接续）

**原理**：在现有视频前后接续一段新生成的内容。

**用法场景**：
- 5 秒视频很好但太短 → Extend 接 3 秒到 8 秒
- 想加一个开场 → Extend 在前面接 2 秒
- 长视频拆成 5+5+5 三段拼接 → Extend 链式

**Extend 注意**：
- 接续段的**起始帧 = 原视频末帧**——所以原视频末帧质量决定接续质量
- Extend 比从头生成更稳定（有锚点），但也容易累积漂移
- 链式 Extend 超过 3 段后画质明显下降——这时改剪辑拼接更好

### 决策：Retake vs Extend vs 重 roll vs 拼接

| 问题 | 推荐 |
|---|---|
| 中段动作不对 | Retake 中段 |
| 末尾崩了 | Retake 末段 |
| 整段都不对 | 改 prompt + 整段重 roll |
| 段对但太短 | Extend |
| 想做 10 秒+ 长视频 | **拆成多个 5 秒段独立生成 + NLE 拼接**（比 Extend 链式更稳）|

---

## 何时该放弃 AI、改剪辑救

不是所有失败都要继续 roll AI。有些时候**接受瑕疵 + 后期处理**才是最优解：

| 瑕疵 | 后期救法 |
|---|---|
| 末尾 0.5 秒崩 | 剪掉这 0.5 秒——视频时长变短 |
| 中间某帧异物 | 速度块（quick speed up）盖过去 |
| 末尾衰减 | 加淡出转场（fade out）盖住 |
| 一闪而过的扭曲 | 加动态模糊或叠加字幕盖住 |
| 一个 5 秒视频 80% 时间好 | 截取那 80%，剩下 20% 不要 |

**判断标准**：roll 5 次都没救 → 接受当前最好版本 + 进 NLE 修。AI 视频是**生成 + 编辑**的联合艺术，不是纯生成。

---

## 输出格式

```
## 失败诊断

**失败现象**：[用户描述 + 你观察]

**重 roll 验证**：[是否已重 roll 验证稳定失败？没有 → 先跑 2 次同 prompt]

---

### 失败分类

**类型**：A（Spatial）/ B（Temporal）/ C（Sync）/ D（Intent）

**具体子类**：[Warping / Identity drift / Flicker / End decay / ...]

**根因分析**：[一句话说明]

---

### 救法决策

**策略**：
- [ ] 重 roll（换种子）
- [ ] 改 prompt + 重 roll
- [ ] LTX Retake 段级重生
- [ ] LTX Extend 前后接续
- [ ] 接受 + 后期剪辑救
- [ ] 改首帧（回 ltx-first-frame-prep）

**具体步骤**：
1. ...
2. ...
3. ...

---

### prompt 调整建议（如果要回 prompt skill）

回到 [ltx-i2v-prompt / ltx-flf-prompt / ltx-t2v-prompt]，做以下调整：

- [具体调整 1]
- [具体调整 2]

---

### 种子记录建议

[如果当前有可用的版本，提醒用户记录 seed 到哪一级档案]
```

---

## 应用示例

### 示例 1：人物视频末尾脸崩了

**用户输入**："5 秒视频，女主从沉思到微笑，但最后 1 秒她的脸完全变了，像换了个人"

```
**失败现象**：5 秒人物视频，前 4 秒一致，末 1 秒身份漂移

**重 roll 验证**：未验证。先跑 2 次同 prompt——但根据描述判断这是典型的"末尾累积漂移"，大概率稳定失败。

---

### 失败分类
**类型**：B（Temporal）+ A（Spatial）双重
**具体子类**：End decay + Identity drift
**根因分析**：人脸特写 5 秒到达 LTX 身份稳定的临界点，错误累积在最后阶段爆发。

---

### 救法决策
**策略**：
- [x] LTX Retake 段级重生（针对末 1 秒）
- [x] 备选方案：缩短整段到 4 秒
- [x] 改首帧（如果尾帧也是输入）

**具体步骤**：
1. 先把当前视频前 4 秒裁出来留作锚点
2. 用 Retake 重生末 1 秒，prompt 强调"承接前段表情发展，末帧光线匹配开头"
3. 若 Retake 仍崩 → 直接剪到 4 秒，接受这个时长
4. 长期方案：以后人脸近景视频默认上限 4 秒，不要冲 5 秒

---

### prompt 调整建议（如果整段重 roll）
回到 ltx-flf-prompt 或 ltx-i2v-prompt：
- 加 "her facial features remain consistent throughout, no morphing"
- 加 "the final frame matches the first frame in face geometry and lighting"
- 时长从 5 秒降到 4 秒
- 检查首帧是否合格（回 ltx-first-frame-prep）

---

### 种子记录建议
当前视频虽然末尾崩，但前 4 秒角色形态对吗？如果对——这个 seed 进"黄金种子池"，下次同角色复用。
```

### 示例 2：产品旋转视频几乎不动

**用户输入**："想让陶瓷杯旋转 360 度，5 秒，跑出来杯子只动了几度"

```
**失败现象**：i2v 产品旋转视频，目标 360°，实际旋转幅度极小

**重 roll 验证**：建议先跑 2 次同 prompt 验证。

---

### 失败分类
**类型**：B（Temporal）
**具体子类**：Static / no motion（运动不足）
**根因分析**：LTX i2v 默认 motion strength 偏保守 + 首帧"运动种子"不足。

---

### 救法决策
**策略**：
- [x] 改首帧（首帧不暗示运动 → 模型不动）
- [x] 改 prompt（加强运动动词 + 时间分配指令）
- [x] 改用 flf（首帧静止杯把朝右、尾帧旋转后杯把朝左——锁住起止）

**具体步骤**：
1. 优先级 1：改用 flf 而不是 i2v——一张图让 AI 猜旋转方向是低成功率任务
2. 出尾帧：用 flux2-prompt-generator 生成"杯把朝左"的版本（其他保持一致）
3. 用 ltx-flf-prompt 写 flf prompt：
   - first_strength=1.0 / last_strength=0.9（强锁起止）
   - 时间分配：`rotates 360° clockwise, completing by the 4th second, then holds steady`
   - 加环境运动种子：`subtle steam continuously rising during rotation`

---

### prompt 调整建议（如果坚持 i2v）
回到 ltx-i2v-prompt：
- 加强运动动词：`rotates fully` 而不是 `slowly rotates`
- 加时间分配：`completes one full rotation by the 4th second`
- 加首帧约束：回 `ltx-first-frame-prep` 检查首帧"运动种子"——杯把方向、是否有水蒸气暗示

---

### 种子记录建议
i2v 静止失败几乎都是首帧问题，不是 seed 问题——不需要为这次失败记 seed。等改用 flf 跑通后，那个 seed 才值得记录。
```

---

## 常见错误

### 错误 1：跑 1 次失败立刻改 prompt

最常见的错。1 次失败可能是抽卡运气——**先重 roll 2 次同 prompt 验证**再说。

### 错误 2：一改就大改

prompt 改了 5 处 → 不知道哪处起作用。**每次只改 1-2 处**，且记下改了什么。

### 错误 3：整段重 roll 解决局部问题

末尾 1 秒崩 → 整段重 roll 8 秒？浪费。**用 Retake 救末段**。

### 错误 4：忘记记录好 seed

跑出来神作 → 没记 seed → 下次永远找不回来。**好版本必记 seed**。

### 错误 5：把 AI 视频当一次性消费

跑完看一眼觉得不行就删 → 错过可以剪辑救的片段。**保留所有跑过的版本**，最后挑剪辑素材。

### 错误 6：拒绝接受 AI 瑕疵

5% 的瑕疵都要重 roll → 永远跑不完。**专业创作者用 NLE 修小瑕疵，不用 AI 救**。

### 错误 7：长视频从头到尾用一个 prompt 跑

10 秒视频用一个 prompt 跑 → 后半段必然漂。**拆成 5+5 两段独立生成 + 拼接**。

---

## 跟其他 skill 的协作

| 上游（prompt 跑完出问题） | 本 skill | 下游（按建议回上游或进剪辑） |
|---|---|---|
| `ltx-t2v-prompt` 跑完 | 本 skill 诊断 | 改 prompt 重 roll / Retake / 剪辑救 |
| `ltx-i2v-prompt` 跑完 | | 改 prompt / 改首帧（回 first-frame-prep）|
| `ltx-flf-prompt` 跑完 | | 改 prompt（调 strength）/ 改首尾帧 |
| `gpt-image2-seedance-storyboard` 跑完 | | 改九宫格分镜 / 改 motion prompt |

**和上游 skill 的反馈循环**：

```
prompt skill 写 → 跑 → 不满意 → 本 skill 诊断
                                    ↓
                            回 prompt skill 调整
                                    ↓
                                  重跑
                                    ↓
                                  ... 循环 ...
                                    ↓
                            满意 → 记录黄金种子
```

**和 `ltx-shot-planning` 的协作**：如果某个镜头反复抽卡失败（5 次都崩），可能不是 prompt 问题，是**镜头本身 AI 做不出来**——回到 shot-planning 重新评估这个镜头的可生成性（Step 7），考虑替代方案（真拍 / 拆短 / 改构图）。

**和项目宪法（如 `cuojia-longgu`）的协作**：黄金种子池**记录在项目宪法 skill 顶端**，跨剧集复用。

---

## 写作风格

- 输出始终中文（除非用户明确要英文）
- 诊断必须分类（A/B/C/D），不要笼统说"有问题"
- 救法必须给优先级（不只是列方案）
- 应用示例里**先用决策树走一遍**再给具体步骤

## 输出纪律

- 不写 prompt（那是上游 skill 的事，本 skill 给"调什么"的指导）
- 不评价用户的审美（"那个视频其实挺好的啊" → 错。用户说不好就是不好）
- 不调用 storage
- 不生成反馈 Artifact
- 输出完即停
