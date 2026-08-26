# PHASE-5 — 阶段五：部署与收尾

> 本阶段将复审通过的 HTML 报告与素材部署到 GitHub Pages，并按规则收尾清单。

**原则：** 遇问题优先保证 HTML 报告生成，再处理部署。

## 1. 核心配置

**敏感信息一律通过环境变量 / GitHub Secret 注入，不得在仓库文件中写死明文。**

```
# 公开信息，可直接写死
REPO_URL="https://github.com/saya-ch/SayaReport.git"
BRANCH="main"
FILE="./index.html"
PAGES_URL="https://saya-ch.github.io/SayaReport/"

# 敏感信息：必须从环境变量 / Secret 读取
PAT="${SAYA_GITHUB_PAT}"          # GitHub Personal Access Token（最高机密）
USER="${SAYA_GITHUB_USER}"        # 仓库账号
EMAIL="${SAYA_GITHUB_EMAIL}"      # 提交邮箱（建议用 noreply 隐私邮箱）

COMMIT_MSG="自动更新求职信息报告 - {{当前日期时间}}"
CONFLICT="force_override"
VERIFY=true
RETRY=3
```

> ⚠️ 若环境变量未注入（为空），**不得**尝试从仓库内读取明文 token，直接报错终止部署，避免泄露。

## 2. 执行步骤

1. 完成信息验证并生成 HTML
2. 初始化 Git，配置用户信息
3. 添加远程仓库并 pull 同步（**必须先 pull，确保拿到仓库现有文件**）
4. 添加文件并提交推送
5. 验证部署并输出结果

**推送保护规则（必须遵守）：**
- **推送范围仅限网页文件与静态资源**：本次提交只允许包含 `index.html`（网页文件）及 `assets/` 静态资源文件夹中的本次素材与头图。**禁止推送、删除、覆盖或改动仓库中任何其他文件**（包括 `AGENT.md`、`PROMPT.md`、`CHECKLIST.md`、`README.md`、`LICENSE`、`PHASE-1.md` ~ `PHASE-5.md` 等所有非网页 / 非静态资源文件），这些文件在仓库中保持原样不动
- `CHECKLIST.md` 的勾选状态**仅用于本地任务跟踪**，**不得随报告提交或推送**；本次提交不得包含该文件的任何改动
- **README 头图（`assets/banner.png`）更新与推送处理（README.md 中唯一允许变动的文件内容）：**
  - **生成要求**：用图片生成模型重新绘制，风格不限，但画面必须包含 Saya 的猫娘形象，并在非主要位置（角落、边缘等次要区域）标注本次日期信息，不得占据画面主体。头图仅用于仓库主页与 README.md 顶部展示，**不属于报告页（`index.html`）内部素材，报告页不得引用它**
  - 本次图片生成成功 → 用新生成的 `assets/banner.png` 覆盖推送，README.md 头图引用保留不变
  - 本次图片生成模型调用失败、或未产出可用头图 → **必须**将 `assets/banner-default.png` 复制覆盖为 `assets/banner.png` 后推送（`banner-default.png` 是仓库内常驻的默认 README 头图，由用户指定，**禁止删除或改动**）
  - **严禁复用上一轮生成的头图**：若发现 `assets/banner.png` 仍是上一轮旧图（本次未成功生成且未用默认图覆盖），一律用 `banner-default.png` 覆盖，不得沿用
  - **除头图 `assets/banner.png` 外，不得更改 `README.md` 的任何其他内容**：其余章节一律保持原样，不得增删改
- 本次生成的 `index.html` 会**覆盖**仓库中上一次的报告页面，这是预期的定时更新行为；但内容必须基于本次全新检索独立生成，**不得参考或复用历史报告**
- **部署无法完成时（如环境变量未注入、网络失败等）**：按 `CHECKLIST.md` 10.2 规则处理——任务收尾时取消所有打勾（清空清单）；将 `index.html`、本次素材一并提交到仓库（若无法推送则保留在本地工作目录并如实记录）
- 推送前如遇冲突，使用 `CONFLICT="force_override"` 前先 `git pull --rebase` 同步，避免误伤指导文件

## 完成后

- **无论任务是否全部完成，任务收尾时一律取消所有打勾**（将 `CHECKLIST.md` 清单恢复为全部 `- [ ]` 空状态），包括全部五阶段达标完成、以及任务因环境 / 外部限制提前终止两种情况
- 重新阅读 `AGENT.md` 总纲与 `CHECKLIST.md`，确认收尾规范无误后结束任务