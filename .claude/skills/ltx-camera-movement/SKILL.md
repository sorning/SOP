---
name: ltx-camera-movement
description: LTX Video 2.3 镜头运动（运镜）知识库与触发词词典。本 skill 是 ltx23-t2v / ltx23-i2v-prompt / ltx23-f2f-prompt 三个生成型 skill 的强制共享底座，提供 16 种电影运镜的分类、英文 LTX 触发词、易混淆对比和 LTX 难度评级。任何涉及 LTX 视频 prompt 中"镜头运动 / 运镜 / 镜头如何动 / camera movement"的描述时，都必须先加载本 skill 作为权威参考。本 skill 不主动触发生成 prompt，仅作为被动参考材料被其他 skill 引用。也可在用户直接询问"电影运镜有哪些 / 镜头运动方式 / camera movement types / dolly vs zoom / pan vs slide"时主动加载。
---

# LTX Video 2.3 镜头运动（运镜）知识库

## 本 skill 的定位

这是 `ltx23-t2v` / `ltx23-i2v-prompt` / `ltx23-f2f-prompt` 三个生成型 skill 的**强制共享底座**，专门沉淀：

1. **电影运镜分类**（16 种核心 + 特殊）
2. **每种运镜的 LTX 触发词**（实际可用的英文措辞）
3. **易混淆运镜的关键对比**
4. **LTX 处理每种运镜的难度评级**

本 skill 本身**不生成 prompt**——它是被引用的字典，不是工具。

---

## ⚠️ 验证状态标记说明

每条运镜的 LTX 触发词都标注了验证状态：

- ✅ **已验证**：在 LTX-2.3 实际跑过，触发词有效
- ⚠️ **待验证**：基于通用电影运镜知识 + LTX 训练数据推断，**未经实际测试**，使用时需注意效果
- ❌ **已证失败**：跑过但 LTX 处理不好，不推荐使用

随着项目推进，待验证条目会陆续更新为已验证或已证失败。

---

## 一、相机位移类（相机本体在移动）

这类运镜最常用，也是 LTX 处理得最好的一类。

### 1. Dolly In（推镜）⭐⭐ 难度低

相机沿光轴向前移动，整个空间朝镜头逼近。**有透视变化**——前景比后景变化幅度大。

- **情绪**：聚焦 / 进入 / 亲密 / 深入
- **触发词**：
  - ✅ `pushes in slowly along the central axis`
  - ⚠️ `dolly in / advances toward [target]`
  - ⚠️ `slowly closes in on [subject]`
- **关键搭配**：必须明确**终点构图**（推到哪、什么充满画面），否则 LTX 会自由发挥
- **常见错误**：写 `slow zoom in` —— zoom 和 dolly 是两回事（见易混淆对比节）

### 2. Dolly Out（拉镜）⭐⭐ 难度低

相机后退，空间逐渐拉开揭示全貌。

- **情绪**：抽离 / 孤独 / 揭示 / 释放
- **触发词**：
  - ⚠️ `pulls back slowly`
  - ⚠️ `dolly out / retreats from [subject]`
  - ⚠️ `the camera withdraws revealing [wider context]`
- **关键搭配**：明确**揭示了什么新内容**，否则 LTX 只是单纯后退没戏剧感
- **LTX 偏好**：对称构图首帧 + 后退指令，LTX **倾向于做后退**（多次观察到 slide 指令被 LTX 转为 dolly out）

### 3. Truck / Slide Left（左横移）⭐⭐⭐ 难度中

相机整体水平向左平移（沿轨道车）。**画面整体平移，物体保持相对位置**。

- **触发词**：
  - ⚠️ `slides horizontally from right to left`
  - ⚠️ `trucks left, moving sideways along a track`
  - ⚠️ `the camera shifts left, [right-side object] enters the frame`
- **关键搭配**：必须**明确写出物体的相对运动结果**（"X 滑出画面，Y 进入"），否则 LTX 容易把 slide 错执行为 dolly
- **常见陷阱**：写"保持中心物体居中"会触发 LTX 改做 dolly in/out

### 4. Truck / Slide Right（右横移）⭐⭐⭐ 难度中

同上，方向相反。

- **触发词**：
  - ⚠️ `slides horizontally from left to right`
  - ⚠️ `trucks right, moving sideways along a track`

#### 🟢 slide 方向稳定性实战经验（左右横移通用，2026-05 实测沉淀）

LTX 对 `left` / `right` 这类绝对方向词**执行不稳定**——多次观察到方向被反向执行（要"左→右"出来变成"右→左"）。直接靠方向词锁定不可靠。

**经验 1：靠"物体进出方向"锁定，不靠 left/right 单词**
镜头向右走 = 画面内容向左流 = **左侧物体从左缘滑出 + 右侧物体从右缘进入**。把这套物理逻辑明写进 prompt，比反复说"to the right"更能锁住方向：
```
scene flowing leftward across the frame as a result,
[left-side object] slides out through the left edge of the frame,
new space keeps entering from the right edge as the camera travels
```
（向左走则全部反向。）这是 LTX 在物理上"无法理解错"的描述方式。

**经验 2：防 slide 被偷偷转成 dolly（推近亮元素）**
首帧里如果有强亮/强吸引元素（巨型吊灯、亮屏 TV、明亮窗景），LTX 容易把 slide 偷偷做成 dolly in 推近它——尤其当 prompt 里给了它任何"focus / center / view"暗示时。**必须三连防御**：

```
[the bright element] simply drifts across the frame as the camera passes it,
never becoming the center of focus, just one element sliding by among others,
the camera never pushes forward or zooms, it only translates sideways, holding the same distance throughout
```

第一句让亮元素降格成"路过的一个"；第二句明确否定"聚焦中心"；第三句明确否定"推近/变焦"——三连组合实测能稳住 slide 不被偷换成 dolly。

**经验 3：方向若仍被反向执行（最暴力解）**
如果上述措辞都没救回方向，**别和 LTX 较劲改 prompt** —— 直接把首帧图**水平镜像翻转**（左右翻转），让"想揭示的右侧内容"翻到左边，再用同 prompt 跑，等于用图片翻转强制锁方向。这是对付 LTX 方向不听话最可靠的兜底。

#### 共用陷阱（左右横移通用）

- **关键搭配**：必须**明确写出物体的相对运动结果**（"X 滑出画面，Y 进入"），否则 LTX 容易把 slide 错执行为 dolly
- **常见陷阱**：写"保持中心物体居中"会触发 LTX 改做 dolly in/out
- **聚焦陷阱**：给任何亮元素加 `focus / center / full view / fills the frame` 等措辞 → LTX 会把 slide 转成 dolly 推近它（见经验 2 的三连防御）

### 5. Pedestal / Boom Up（升镜）⭐⭐⭐ 难度中

相机整体上升（如同站起来或被吊起）。跟 tilt up 的区别：**相机本体在上升，视线高度变了**。

- **触发词**：
  - ⚠️ `booms up / rises vertically`
  - ⚠️ `the camera ascends, revealing the upper part of the space`
- **用例**：从地面升起揭示场景全貌、从前景升起越过遮挡物

### 6. Pedestal / Boom Down（降镜）⭐⭐⭐ 难度中

相机整体下降。

- **触发词**：
  - ⚠️ `booms down / descends slowly`
  - ⚠️ `the camera lowers toward [subject]`

### 7. Tracking / Following Shot（跟拍）⭐⭐⭐⭐ 难度高

相机跟随移动的主体，保持相对距离不变。可侧跟、前跟、后跟。

- **触发词**：
  - ⚠️ `tracks alongside [subject]`
  - ⚠️ `parallel tracking shot following [subject]`
  - ⚠️ `the camera follows behind [subject]`
- **LTX 注意**：需要主体本身在动，**静景里没法用**
- **限制**：跟拍人物时容易出现身份漂移（脸/服装变化）

### 8. Arc / Orbit（弧线/环绕）⭐⭐⭐⭐⭐ 难度极高

相机围绕中心点做弧线或环形运动。

- **触发词**：
  - ⚠️ `orbits around [subject]`
  - ⚠️ `arcs around the central object`
- **LTX 注意**：**3D 一致性是 AI 视频模型的弱项**——绕半圈，背面就开始崩。建议幅度控制在 45° 以内
- **替代方案**：如需 360° 环绕，拆成多段拼接

### 9. Crane / Jib（吊臂复合）⭐⭐⭐⭐⭐ 难度极高

升降 + 推进 + 横移的复合运动，通常是大幅度俯瞰式开场镜头。

- **触发词**：
  - ⚠️ `craning down and forward / sweeping aerial descent`
- **LTX 强烈建议**：**拆成多段单一运镜**。让 LTX 一次做三种复合运动出片率极低。

---

## 二、相机原地转动类（相机不动，只转方向）

### 10. Pan Left / Pan Right（横摇）⭐⭐ 难度低

相机基座不动，镜头水平转向。**跟 slide 的根本区别：画面在旋转，边缘物体比中央走得快**。

- **触发词**：
  - ⚠️ `pans horizontally from left to right`
  - ⚠️ `the camera rotates horizontally on its axis`
- **常见错误**：用户说"横摇"时经常其实想要 slide。**先确认是不是真的要原地转头**
- **对称构图警告**：对称首帧做 pan 会破坏构图平衡，慎用

### 11. Tilt Up（上摇）⭐⭐ 难度低

相机原地仰头。跟 pedestal up 区别：**视线高度不变，只是抬头看**。

- **触发词**：
  - ⚠️ `tilts upward gradually`
  - ⚠️ `the camera angles up, ending framed on [upper element]`
- **用例**：从床扫到屋顶到雪山顶、从脚扫到头介绍人物

### 12. Tilt Down（下摇）⭐⭐ 难度低

相机原地俯头。

- **触发词**：
  - ⚠️ `tilts downward / cranes down (note: this is rotation, not pedestal)`

### 13. Roll / Dutch Tilt（横滚/倾斜）❌ LTX 几乎必崩

画面沿光轴旋转，地平线倾斜。

- **触发词**：⚠️ `rolls slowly / dutch angle rotation`
- **强烈不推荐**：LTX 处理画面旋转时几乎必出畸形和形变。**用静态 Dutch tilt 首帧 + 静止镜头**作为替代方案。

---

## 三、镜头光学类（相机不动，焦距/焦点变）

### 14. Zoom In / Zoom Out（变焦）⭐ 难度极低但效果平

焦距变化导致画面缩放。**和 dolly 的关键区别：没有透视变化，整体均匀放大/缩小**。

- **触发词**：
  - ⚠️ `zooms in / focal length narrows`
  - ⚠️ `zooms out / pulls back via focal length`
- **重要**：观众心理感受跟 dolly 完全不同——dolly 是"走过去"，zoom 是"用望远镜看"。**如果要"接近感"，永远用 dolly，不用 zoom**
- **LTX 实测**：zoom 容易被 LTX 转为 dolly（模型偏好后者）

### 15. Dolly Zoom / Vertigo Shot（眩晕变焦）❌ LTX 做不出

同时反向 dolly 和 zoom，制造希区柯克式心理冲击。

- ❌ **LTX 完全做不出来，不要尝试**

### 16. Rack Focus（拉焦/变焦点）⭐⭐⭐ 难度中

焦点从一处转移到另一处，前后景虚实切换。相机不动、焦距不动。

- **触发词**：
  - ⚠️ `focus shifts from foreground to background`
  - ⚠️ `rack focus from [near subject] to [far subject]`
- **限制**：简单场景能做，复杂场景容易整体糊

---

## 四、特殊运镜

### 17. Static / Locked-off（固定镜头 + 微动）⭐ 难度极低

相机完全不动，只有画面内的事物在动（火苗、雪花、热气）。**i2v 静景微动的默认选择**。

- **触发词**：
  - ✅ `locked-off camera, only [element] moves`
  - ✅ `static frame, everything else stays still`
- **常用搭配**：明确写出"哪些东西在动 + 哪些东西不动"

### 18. Handheld（手持）⭐⭐⭐ 难度中

镜头有自然抖动，纪实/紧张/临场感。

- **触发词**：
  - ⚠️ `handheld camera with subtle natural shake`
  - ⚠️ `documentary-style handheld movement`
- **LTX 注意**：默认会**过度抖动**，必须加 `subtle / minimal shake` 限制幅度

### 19. Steadicam / Gimbal（稳定器跟拍）⭐⭐ 难度低

流畅跟拍，无抖动，漂浮般跟着主体。

- **触发词**：
  - ✅ `smooth gimbal-stabilized shot`
  - ⚠️ `steadicam tracking shot`
- **本项目已验证**：在山地小屋客厅横扫场景中触发词 `smooth gimbal-stabilized pan` 配合"前 X 秒摇 + 后 Y 秒定格"结构有效

### 20. POV（主观镜头）⭐⭐⭐⭐ 难度高

模拟某个角色的视角，等同于"主体的眼睛在看"。

- **触发词**：
  - ⚠️ `POV shot / first-person perspective`
- **限制**：LTX 处理 POV 时容易丢失"持镜者"的代入感，画面跟普通广角差别不大

---

## 五、易混淆运镜对比

这一节专门解决今天反复踩坑的根源——**用户说一个词，LTX 理解成另一个**。

### Dolly vs Zoom

| 维度 | Dolly | Zoom |
|---|---|---|
| 相机位置 | 相机在移动 | 相机不动 |
| 透视 | 有透视变化（前景比后景变化大） | 无透视变化（整体均匀缩放） |
| 心理感 | "走过去" | "望远镜看" |
| 用例 | 接近主体、揭示空间 | 强调细节、戏剧性放大 |

**结论**：要"接近感"永远用 dolly。

### Slide / Truck vs Pan

| 维度 | Slide / Truck | Pan |
|---|---|---|
| 相机位置 | 相机在水平移动 | 相机原地不动 |
| 画面变化 | 整体水平平移 | 画面在旋转 |
| 物体相对运动 | 物体保持相对位置 | 边缘物体走得比中央快 |
| 用例 | 横扫房间（@relaxinoffgrid 同款）、跟拍移动主体 | 环视空间、跟随转头 |

**结论**：今天用户多次说"横摇"实际是想要 slide。**先问清楚是相机移动还是原地转头**。

### Pedestal vs Tilt

| 维度 | Pedestal | Tilt |
|---|---|---|
| 相机位置 | 相机整个升降（视线高度变） | 相机原地仰俯（视线高度不变） |
| 用例 | 站起来看、蹲下看 | 抬头看天花板、低头看地板 |

### Dolly Out vs Zoom Out

| 维度 | Dolly Out | Zoom Out |
|---|---|---|
| 揭示感 | 强（空间被打开） | 弱（画面变小但不揭示新内容） |
| LTX 偏好 | LTX 偏好 dolly out | zoom out 经常被 LTX 转为 dolly out |

---

## 六、写 LTX 运镜 prompt 的核心原则

### 原则 1：必须有"任务感"

LTX 的运镜表现取决于是否给了**明确的起点和终点**。

- ❌ 弱：`the camera pans` —— 不知道摇到哪
- ✅ 强：`the camera pans from the fireplace, ending framed on the triangular window` —— 终点明确

### 原则 2：用"动作的结果"描述运动

LTX 对"运动结果"比"运动本身"响应更好。

- ❌ 弱：`slides horizontally to the right`
- ✅ 强：`slides right; the left-side stove exits the frame, the right-side lantern enters the view`

### 原则 3：速度词不如时间分配

"慢"这个形容词 LTX 经常忽略。**改用时间分配指令**。

- ❌ 弱：`very slowly pans` —— LTX 经常仍然较快
- ✅ 强：`pans, completing by the seventh second, then holds steady` —— 强制 7 秒走完

### 原则 4：避免"反指令"

不要在运镜指令里加"保持 X 居中"这类约束——LTX 会优先满足约束，破坏运镜本身。

- ❌ 错误：`slides right while keeping the central window centered` —— LTX 改做 dolly
- ✅ 正确：`slides right; the camera moves, the window naturally shifts to the left of the frame`

### 原则 5：避免否定描述运动方向

LTX 对否定句弱。

- ❌ 弱：`pans left, not right`
- ✅ 强：`pans from right to left`

---

## 七、本项目已验证的有效配置

以下是 2026-05 山地小屋项目跑通的真实配置：

| 场景 | 运镜 | 有效触发词组 | LTX 参数 |
|---|---|---|---|
| 客厅黄昏横扫 | smooth pan left-to-right | `pans smoothly from left to right at a natural cinematic pace, starting on the fireplace and ending framed on the window, completes in the first 3 seconds then holds steady` | 5 秒，CFG 4.0，enhance off |
| 卧室对称构图后退 | LTX 自动选 dolly out | （prompt 写的是 slide，LTX 实际给了 dolly out）—— **教训：对称构图 + 保持中心居中指令 → LTX 改 dolly out** | 9 秒，CFG 4.5 |

---

## 八、附：LTX 末尾衰减问题的应对（运镜相关部分）

运镜越长，LTX 越容易在末尾发生"画面变暗 / 雪量减弱 / 火焰熄灭"等衰减。运镜相关的应对：

1. **时长不要超过 7 秒**（低光场景）
2. **明确写"末帧匹配首帧"**：`the final frame matches the first frame in lighting, exposure, color temperature`
3. **避免用 dusk / blue hour 等隐含时间流逝的词**作首帧描述
4. **运镜结束后保留 2-3 秒定格**——让 LTX 在定格期"稳定下来"而不是继续自由发挥

更完整的反衰减经验，待沉淀到独立 skill（暂时分散在本 skill 第七节"已验证配置"中）。

---

## 九、更新日志

| 日期 | 更新内容 | 来源对话 |
|---|---|---|
| 2026-05-25 | 初版建立，16 种运镜分类 + 3 条已验证经验 | 山地小屋项目 |

未来每次新跑出运镜效果，请把"待验证"升级为"已验证"或"已证失败"，并补充触发词措辞。
