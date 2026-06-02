# anxin-image-gen

## 功能定位

`anxin-image-gen` 用于通过安信 `gpt-image-2` 兼容图片接口生成图片，适合在 OpenClaw / Codex 工作流中生成封面、海报、公众号配图、知识图谱、信息图和参考图改图素材。

## 适用场景

- 中文海报、公众号封面、小红书封面、视频号封面、抖音封面。
- 企业汇报 PPT 的封面主视觉、架构图、生态图和场景图。
- 知识图谱、信息图、学习卡片等需要清晰排版的图片。
- 基于参考图进行重绘、局部修改或风格统一。

## 环境变量

```powershell
$env:ANXIN_API_BASE_URL = "https://your-api-host"
$env:ANXIN_API_KEY = "your-api-key"
```

不要把 API Key 写入仓库文件、提示词、日志或生成物。

## 常用命令

```powershell
cd skills/anxin-image-gen
python scripts/generate_image.py `
  --prompt "一张企业科技风的智能平台主视觉，蓝白配色，干净高级" `
  --size 1536x1024 `
  --quality high `
  --output-dir ./outputs
```

脚本默认提交异步任务并轮询结果；需要先拿到任务 ID 时使用 `--no-wait`。

## 主要文件

- `SKILL.md`：技能入口说明。
- `scripts/generate_image.py`：图片生成脚本。
- `references/api.md`：接口约束。
- `references/prompting.md`：提示词组织规范。

