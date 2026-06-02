# SkillsHub

这是一个公开 OpenClaw / Codex 技能仓库，当前包含六个核心技能：

- `anxin-image-gen`：通过安信 `gpt-image-2` 兼容接口生成图片。
- `anxin-ppt`：生成企业科技风 HTML PPT，并结合 `anxin-image-gen` 生成封面、方案图、生态图和图标组等视觉资产。
- `anxin-video-aduit`：通过安信 Gemini 多模态接口审核短视频、文稿和分镜图是否适合发布到微信视频号和抖音。
- `emergency-wechat-writer`：创作应急、消防、危化、安全生产等领域微信公众号文章和选题策划。
- `wechat-article-html-style`：将公众号文章整理成统一风格的本地 HTML 排版页，便于复制到微信公众平台。
- `yingji-linglingqi-knowledge-graph`：完成应急凌凌漆知识图谱从立项、调研、提示词、出图复核到发布文案的闭环。

## 技能文档

| 技能 | 说明 | 文档 |
| --- | --- | --- |
| `anxin-image-gen` | 安信图片生成、封面、海报、知识图谱和信息图 | [docs/skills/anxin-image-gen.md](docs/skills/anxin-image-gen.md) |
| `anxin-ppt` | 蓝白企业汇报风 HTML PPT | [docs/skills/anxin-ppt.md](docs/skills/anxin-ppt.md) |
| `anxin-video-aduit` | 微信视频号和抖音发布前短视频素材审核 | [docs/skills/anxin-video-aduit.md](docs/skills/anxin-video-aduit.md) |
| `emergency-wechat-writer` | 应急安全类微信公众号写作、策划和发布前自检 | [docs/skills/emergency-wechat-writer.md](docs/skills/emergency-wechat-writer.md) |
| `wechat-article-html-style` | 公众号文章本地 HTML 排版和微信复制样式 | [docs/skills/wechat-article-html-style.md](docs/skills/wechat-article-html-style.md) |
| `yingji-linglingqi-knowledge-graph` | 应急凌凌漆知识图谱闭环：立项、调研、提示词、成图复核和发布文案 | [docs/skills/yingji-linglingqi-knowledge-graph.md](docs/skills/yingji-linglingqi-knowledge-graph.md) |

## 目录结构

```text
.
├── skills/                   # 可被 skills CLI 识别的技能集合
│   ├── anxin-image-gen/      # 安信图片生成技能
│   ├── anxin-ppt/            # 安信企业 PPT 生成技能
│   ├── anxin-video-aduit/    # 安信短视频审核技能
│   ├── emergency-wechat-writer/
│   ├── wechat-article-html-style/
│   └── yingji-linglingqi-knowledge-graph/
├── docs/
│   └── skills/               # 每个技能的独立说明文档
├── CLAUDE.md                 # Claude Code 使用说明
└── README.md
```

查看仓库内可安装的技能：

```powershell
npx -y skills add . --list
```

## 安装方法

本仓库公开地址：

```text
https://github.com/leinatorX/skills.git
```

查看远端仓库可安装的技能：

```powershell
npx -y skills add https://github.com/leinatorX/skills.git --list
```

安装单个技能到 Codex：

```powershell
npx -y skills add https://github.com/leinatorX/skills.git --skill anxin-ppt -g -a codex
```

把 `--skill anxin-ppt` 替换为上方表格中的任意技能名即可安装指定技能。

安装全部技能到 Codex：

```powershell
npx -y skills add https://github.com/leinatorX/skills.git --skill '*' -g -a codex
```

安装到 OpenClaw 时把 `-a codex` 改为 `-a openclaw`：

```powershell
npx -y skills add https://github.com/leinatorX/skills.git --skill anxin-ppt -g -a openclaw
```

### CC Switch

在 CC Switch 的“管理技能仓库”里添加：

- 仓库 URL：`leinatorX/skills` 或 `https://github.com/leinatorX/skills`
- 分支：`main`

不要填写 `https://github.com/leinatorX/skills/tree/main/skills` 这类子目录地址；CC Switch 的仓库 URL 校验只接受 `owner/name` 或 GitHub 仓库根地址。技能目录由工具在仓库内递归识别。

## 环境变量

图片生成、短视频审核和需要调用安信接口的内容生产任务，需要在当前终端配置以下环境变量：

```powershell
$env:ANXIN_API_BASE_URL = "https://your-api-host"
$env:ANXIN_API_KEY = "your-api-key"
```

不要把 API Key 写入仓库文件、命令历史说明或生成的 HTML PPT。

## 交付标准

- 正式企业 PPT 必须使用真实图片资产，不能只依赖 CSS 占位图。
- 首页需要有成品级主视觉，默认优先调用 `anxin-image-gen` 生成。
- 每页使用清晰版式、标题、品牌位和页码。
- 结构校验通过后，还需要打开截图人工检查首页、目录页和至少一页密集内容页。
- 公众号文章必须先核实事实依据；涉及法规、标准、事故、新闻和数据时，不凭记忆编写。
- 公众号 HTML 排版页必须能本地打开，正文图片使用相对路径，并保留复制到微信公众平台的按钮。
- 知识图谱内容必须先核验具体答案；成图后检查中文、画幅、知识准确性、收藏点和互动门槛。

## 安全边界

- 仓库不保存真实 API Key。
- `outputs/`、打包 zip、接口响应、客户资料和未脱敏业务内容不提交到公开仓库。
- 生成失败时优先检查环境变量、Base URL、尺寸合法性和接口原始响应。
- 短视频审核结果只作为发布前风险评估，不等同于微信视频号或抖音平台的最终审核结论。
- 公开分享前应重新扫描密钥、环境变量文件、生成产物和历史提交，避免把敏感内容带入公共仓库。
