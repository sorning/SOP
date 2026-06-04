# Sources（来源清单）

本 skill 的所有 references 文件均为 Lightricks 官方资源的本地副本，**正文一字不改**。
列出每个文件的原始来源，方便未来核对、更新、追溯。

---

## references/prompting-guide-official-readme.md

- **来源**：https://github.com/Lightricks/LTX-2/blob/master/README.md（第 85-101 行 "Prompting for LTX-2" 章节 + "Automatic Prompt Enhancement" 章节）
- **抓取方式**：`git clone --depth 1 https://github.com/Lightricks/LTX-2.git`
- **抓取日期**：2026-05-18
- **抓取 commit**：master 分支最新（depth=1）
- **原协议**：参见 repo LICENSE
- **说明**：这是 GitHub repo 自带的简洁版 prompting 指南，README 在结尾推荐用户去 blog 查阅完整版。

## references/prompting-guide-blog.md

- **来源**：https://ltx.io/model/model-blog/prompting-guide-for-ltx-2
- **备用 URL**：https://ltx.video/blog/how-to-prompt-for-ltx-2（GitHub README 推荐的官方 URL，但抓取时返回 403，使用 ltx.io 备用源）
- **抓取方式**：web_fetch
- **抓取日期**：2026-05-18
- **作者**：LTX Team
- **发布日期**：February 17, 2026（blog 元数据）
- **说明**：完整官方 prompting 指南，含 12 个官方示范 prompt。Lightricks 在 LTX-2.3 的 HuggingFace model card 中也将本 blog 作为 prompting 官方指南，意味着本 blog 同样适用于 LTX-2.3。

## references/pipelines-overview.md

- **来源**：https://github.com/Lightricks/LTX-2/blob/master/packages/ltx-pipelines/README.md
- **抓取方式**：`git clone --depth 1`
- **抓取日期**：2026-05-18
- **原行数**：497 行
- **说明**：ltx-pipelines 包的完整技术文档，含 10 个 pipeline 类的对比、参数推荐、CLI 用法。

## references/pipelines-claude-md.md

- **来源**：https://github.com/Lightricks/LTX-2/blob/master/packages/ltx-pipelines/CLAUDE.md
- **抓取方式**：`git clone --depth 1`
- **抓取日期**：2026-05-18
- **原行数**：88 行
- **说明**：Lightricks 在 ltx-pipelines 包中专门为 Claude/AI agents 编写的架构参考文档。本文件正文一字不改照搬。

## references/model-spec.md

- **来源**：https://huggingface.co/Lightricks/LTX-2.3（model card README）
- **辅助来源**：HuggingFace LTX-2.3 仓库的关键技术规范段落（之前的搜索结果中已捕获）
- **抓取日期**：2026-05-18
- **说明**：LTX-2.3 当前最新版的硬性技术约束（分辨率必须被 32 整除、帧数必须 8n+1、推荐分辨率上限等）。

---

## 删除/未复制的官方文件

为避免冗余和污染，**未复制**以下官方文件：

- `packages/ltx-trainer/AGENTS.md` 和 trainer 目录下的 docs/——这些是 LoRA 训练相关文档，**不影响 prompt 写作**，与本 skill 用途无关
- `packages/ltx-core/README.md`——核心模型实现文档，开发者用，**与 prompt 写作无关**
- GitHub repo 中的 LICENSE、CONTRIBUTING.md 等元文件

如未来需要这些内容，可重新 `git clone` 原 repo 查阅。

---

## 使用原则

1. **本 skill 的所有 references 内容均为官方一手资料的本地副本，可信度最高**
2. **如本 skill 内容与 Claude 训练记忆冲突，永远以本 skill 为准**
3. **本 skill 内容如与 https://docs.ltx.video 或 https://ltx.io 的最新版本冲突，以官方网站最新版本为准**
4. **如果用户描述了与本 skill 内容不符的 LTX 行为，先查证是不是用户用的 LTX 版本与本 skill 覆盖版本不同**
