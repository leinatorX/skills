# GitHub 公开仓库同步说明

## 当前同步边界

本仓库同时维护两个远端：

- `origin`：内部 Gitea 仓库，保留本地正常提交历史。
- `github`：公开 GitHub 仓库，地址为 `https://github.com/leinatorX/skills.git`。

GitHub 公开仓库的 `main` 分支是为公开分享单独生成的干净历史，当前不包含历史中的 `outputs/`、打包 zip、接口响应和其他生成产物。

## 禁止操作

不要直接执行以下命令把本地完整历史推回 GitHub：

```powershell
git push github main
```

原因是本地 `main` 和 GitHub `main` 历史不同。直接普通推送可能失败；如果改成强推本地 `main`，会把旧历史重新带到公开仓库，增加泄漏生成产物、接口响应或敏感资料的风险。

## 推荐更新方式

后续更新技能内容时，先在本地正常提交并推送内部 Gitea：

```powershell
git add <需要提交的文件>
git commit -m "docs(技能仓库): 更新公开技能说明"
git push origin main
```

确认当前文件树不包含敏感内容后，再从当前 `HEAD` 导出干净文件树，生成公开单提交，并强制更新 GitHub：

```powershell
$tmp = Join-Path $env:TEMP ("skillshub-public-" + [guid]::NewGuid().ToString("N"))
$tar = Join-Path $env:TEMP ("skillshub-public-" + [guid]::NewGuid().ToString("N") + ".tar")
New-Item -ItemType Directory -Path $tmp | Out-Null

try {
  git archive --format=tar HEAD -o $tar
  tar -xf $tar -C $tmp
  git -C $tmp init -b main
  git -C $tmp add -A
  git -C $tmp commit -m "chore(公开仓库): 更新公开技能仓库"

  $files = @(git -C $tmp ls-tree -r --name-only HEAD)
  $bad = @($files | Where-Object { $_ -like "outputs/*" -or $_ -like "*.zip" })
  if ($bad.Count -gt 0) {
    $bad | Select-Object -First 20
    throw "公开提交仍包含禁止发布的文件"
  }

  git -C $tmp remote add origin https://github.com/leinatorX/skills.git
  git -C $tmp push --force origin main:main
}
finally {
  if (Test-Path -LiteralPath $tar) {
    Remove-Item -LiteralPath $tar -Force
  }
  if (Test-Path -LiteralPath $tmp) {
    Remove-Item -LiteralPath $tmp -Recurse -Force
  }
}
```

## 发布前检查

每次公开同步前至少检查：

```powershell
rg -n --hidden -g "!outputs/**" -g "!*.zip" "API_KEY|api[_-]?key|Bearer|ghp_|github_pat_|AKIA|AIza" .
npx -y skills add . --list
```

公开同步后检查 GitHub 端：

```powershell
npx -y skills add https://github.com/leinatorX/skills.git --list
git fetch github main
git ls-tree -r github/main --name-only | Select-String -Pattern "(^outputs/|\.zip$)"
```

如果最后一条命令没有输出，表示 GitHub 公开文件树中没有 `outputs/` 或 zip。
