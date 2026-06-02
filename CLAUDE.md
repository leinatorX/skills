# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 仓库概述

SkillsHub 是 OpenClaw / Codex 技能仓库，技能统一放在 `skills/` 目录下：

- `skills/anxin-image-gen/`：安信 `gpt-image-2` 兼容接口的图片生成技能。
- `skills/anxin-ppt/`：基于 `anxin-image-gen` 生成企业科技风 HTML PPT 的技能。
- `skills/anxin-video-aduit/`：安信 Gemini 多模态短视频素材审核技能。
- `skills/emergency-wechat-writer/`：应急安全类微信公众号写作、策划和发布前自检技能。
- `skills/wechat-article-html-style/`：公众号文章本地 HTML 排版和微信复制样式技能。
- `skills/yingji-linglingqi-knowledge-graph/`：应急凌凌漆知识图谱闭环技能，覆盖立项、调研、提示词、成图复核和发布文案。

各技能都可以独立使用；`anxin-ppt` 在生成配图时会调用同级的 `anxin-image-gen`，`wechat-article-html-style` 默认承接 `emergency-wechat-writer` 产出的公众号正文，`yingji-linglingqi-knowledge-graph` 默认面向图文平台知识图谱内容包。

## 环境变量

图片生成需要配置以下环境变量（不要写入仓库文件）：

```powershell
$env:ANXIN_API_BASE_URL = "https://your-api-host"
$env:ANXIN_API_KEY = "your-api-key"
```

## 常用命令

### anxin-image-gen

```powershell
cd skills/anxin-image-gen
python scripts/generate_image.py --prompt "中文提示词" --size 1024x1024 --quality high --output-dir ./outputs
```

异步提交不等待：`--no-wait`，之后再用 `--task-id <id>` 查询。

### anxin-ppt

生成整套配图资产：
```powershell
cd skills/anxin-ppt
powershell -ExecutionPolicy Bypass -File scripts/generate-deck-assets.ps1 -Theme "解决方案主题"
```

校验 HTML 结构：
```powershell
node skills/anxin-ppt/scripts/validate-blue-deck.mjs --strict --require-images outputs/anxin-company-ppt/index.html
```

截图预览（需本机 Chrome/Edge）：
```powershell
powershell -ExecutionPolicy Bypass -File scripts/capture-deck-screenshots.ps1 -InputHtml path\to\deck.html -OutputDir path\to\screenshots -Slides 1,2,6
```

## 架构要点

- `skills/anxin-ppt/assets/template-blue.html`：HTML PPT 模板，每个 `<section class="slide" data-layout="...">` 为一页。
- 版式固定为 10 种（cover / agenda / problem / solution / architecture / product-grid / metrics / roadmap / case-study / closing），不得临时发明复杂结构。
- 配图提示词模板见 `skills/anxin-ppt/references/image-prompts.md`，尺寸规范：全幅封面/架构图用 `2048x1152` 或 `1536x1024`，局部插图用 `1024x1024`。
- 图片生成走异步轮询，脚本默认 600 秒超时，用 `--no-wait` 可先返回 task_id 避免 OpenClaw 外层超时。
- 应急公众号写作先使用 `skills/emergency-wechat-writer/` 做选题、核实、正文和配图方案，再用 `skills/wechat-article-html-style/` 整理为本地 HTML 排版页。
- 应急凌凌漆知识图谱任务使用 `skills/yingji-linglingqi-knowledge-graph/`，按立项、资料核验、分图方案、逐图提示词、成图复核、发布文案的闭环推进。

## 安全边界

- 不将 API Key 写入代码、SKILL.md、HTML 或日志。
- 生成内容不涉及违法、侵权、隐私泄露。
- 交付前需截图检查首页、目录页和密集内容页，不能仅靠结构校验通过就交付。
