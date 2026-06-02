# anxin-video-aduit

## 功能定位

`anxin-video-aduit` 用于通过安信 Gemini 兼容多模态接口审核短视频发布素材，输出适合微信视频号和抖音发布前检查的风险判断和修改建议。

## 适用场景

- 审核短视频、口播稿、字幕稿、文稿、分镜图、封面图和截图。
- 判断内容是否存在平台合规风险、夸大宣传、敏感表达或不适合发布的问题。
- 发布前生成结构化审核结果、Markdown 报告和接口原始响应。

## 环境变量

```powershell
$env:ANXIN_API_BASE_URL = "https://your-api-host"
$env:ANXIN_API_KEY = "your-api-key"
```

环境变量约定复用 `anxin-image-gen`，Base URL 不要包含末尾 `/v1/chat/completions`。

## 常用命令

```powershell
cd skills/anxin-video-aduit
python scripts/audit_video.py `
  --video "D:\videos\demo.mp4" `
  --title "一分钟了解家庭消防隐患" `
  --description "用于微信视频号和抖音发布的安全科普短视频" `
  --platform both `
  --output-dir .\outputs
```

## 主要文件

- `SKILL.md`：技能入口说明。
- `scripts/audit_video.py`：短视频和素材审核脚本。
- `references/api.md`：接口说明。
- `references/rules.md`：平台规则审核口径。

## 注意事项

审核结果只作为发布前风险评估，不等同于微信视频号或抖音平台的最终审核结论。

