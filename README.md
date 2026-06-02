# SkillsHub Skills

这是一个纯 skills 源仓库，面向 CC Switch、OpenClaw 和 `skills CLI` 使用。仓库只维护原始 skill 内容，不包含 Codex plugin marketplace 包装结构。

## 技能列表

- `anxin-image-gen`：通过安信 `gpt-image-2` 兼容接口生成图片。
- `anxin-ppt`：生成企业科技风 HTML PPT，并结合 `anxin-image-gen` 生成封面、方案图、生态图和图标组等视觉资产。
- `anxin-video-aduit`：通过安信 Gemini 多模态接口审核短视频、文稿和分镜图是否适合发布到微信视频号和抖音。
- `emergency-wechat-writer`：创作应急、消防、危化、安全生产等领域微信公众号文章和选题策划。
- `wechat-article-html-style`：将公众号文章整理成统一风格的本地 HTML 排版页，便于复制到微信公众平台。
- `yingji-linglingqi-knowledge-graph`：完成应急凌凌漆知识图谱从立项、调研、提示词、出图复核到发布文案的闭环。

## 目录结构

```text
skills/       # 可被 skills CLI 和 CC Switch 识别的技能集合
docs/         # 每个技能的说明文档
CLAUDE.md     # Claude Code 使用说明
```

## 安装

查看仓库内可安装的技能：

```powershell
npx -y skills add . --list
```

安装单个技能到 Codex：

```powershell
npx -y skills add . --skill anxin-ppt -g -a codex
```

安装全部技能到 Codex：

```powershell
npx -y skills add . --skill '*' -g -a codex
```

安装到 OpenClaw 时把 `-a codex` 改为 `-a openclaw`。

## CC Switch

在 CC Switch 的“管理技能仓库”里添加仓库根地址和分支即可。不要填写 `/tree/main/skills` 这类子目录地址；技能目录由工具在仓库内递归识别。

## 环境变量

图片生成、短视频审核和需要调用安信接口的内容生产任务，需要在当前终端配置：

```powershell
$env:ANXIN_API_BASE_URL = "https://your-api-host"
$env:ANXIN_API_KEY = "your-api-key"
```

不要把 API Key 写入仓库文件、命令历史说明或生成产物。
