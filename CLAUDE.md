# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 仓库性质

这是一个 **SOP(标准作业程序 / Standard Operating Procedure)文档仓库**,不是代码项目。内容为中文 Markdown 文档,用于记录可复用的操作流程(例如每日工作流程、内容生产流程等)。

因此:
- **没有**构建 / 编译 / 测试 / lint 流程,不存在 `package.json`、`Makefile` 等。
- 主要"产物"是 `.md` 文档。编辑后用普通 git 流程提交即可。
- 所有面向用户的文档默认用**中文**撰写。

## 文档约定

新建或修改 SOP 文档时,保持以下结构(沿用历史文档的写法):

- 顶部用一张元信息表(版本、负责人、适用范围 / 生效日期)。
- 正文按**执行时间顺序**分节,每节是动词开头、可勾选(`- [ ]`)的步骤。
- 结尾通常包含一个**复盘 / 价值衡量**环节和**修订记录**表。
- 模板类文档用 `「……」` 标记需用户替换的占位内容。

## Git

- 提交信息使用中文,简明描述本次改动。
- 推送遵循会话指定的功能分支要求(见任务说明),不要直接推 `main`。
