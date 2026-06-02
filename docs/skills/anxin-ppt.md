# anxin-ppt

## 功能定位

`anxin-ppt` 用于生成蓝白企业汇报风 HTML PPT，适合公司介绍、解决方案汇报、项目路演、业务复盘、产品矩阵、技术架构和安全应急领域材料。

## 适用场景

- 安信科创、安全应急、安责险、危化、消防、城市安全等业务汇报。
- 企业介绍、解决方案、项目复盘、路演材料。
- 需要封面主视觉、方案图、架构图和生态图的成品级 HTML PPT。

## 配图关系

需要封面图、场景图、架构图或生态图时，优先调用同级 `anxin-image-gen` 生成图片资产。页面文案默认使用简体中文，不做不必要的英文或中英混排。

## 常用命令

生成整套配图资产：

```powershell
cd skills/anxin-ppt
powershell -ExecutionPolicy Bypass -File scripts/generate-deck-assets.ps1 `
  -Theme "安信科创安全应急数智化解决方案"
```

校验 HTML 结构：

```powershell
node skills/anxin-ppt/scripts/validate-blue-deck.mjs --strict --require-images outputs/anxin-company-ppt/index.html
```

截图预览：

```powershell
powershell -ExecutionPolicy Bypass -File skills/anxin-ppt/scripts/capture-deck-screenshots.ps1 `
  -InputHtml outputs\anxin-company-ppt\index.html `
  -OutputDir outputs\anxin-company-ppt\screenshots `
  -Slides 1,2,6
```

## 主要文件

- `SKILL.md`：技能入口说明。
- `assets/template-blue.html`：HTML PPT 模板。
- `assets/example-full-deck.html`：完整示例。
- `references/layouts.md`：版式说明。
- `references/image-prompts.md`：配图提示词。
- `references/checklist.md`：交付检查清单。

