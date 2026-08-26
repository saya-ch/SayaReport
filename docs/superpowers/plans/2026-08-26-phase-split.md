# 指令体系按阶段拆解 实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 394 行的 AGENT.md 瘦身为「总纲路由」，按五阶段拆分为 PHASE-1~5 独立指令文件，使 Saya 每次任务仅加载「总纲 + 当前阶段文件」以提升指令遵循度。

**Architecture:** AGENT.md 保留铁律级内容（身份、优先级、禁止提问、阶段路由、个人信息、语气）并新增「阅读机制」；各阶段细节规则下沉到对应 PHASE-*.md；CHECKLIST.md 改造为进度路由器（阶段 N 完成 → 打勾 → 读 PHASE-N+1）；PROMPT.md 引导进入 PHASE-1；推送保护白名单加入 PHASE-*.md。

**Tech Stack:** Markdown 指导文件；git 提交推送。

## Global Constraints

- 所有文件用简体中文撰写，与现有文件风格一致（## 标题、- 列表、**粗体**强调）
- 每条规则在全新体系中**只出现一次**（单一事实源），跨阶段引用用一句话指向，不复制正文
- 阶段文件末尾必须包含「完成本阶段 → 打勾 → 读下一阶段文件」的路由指引
- AGENT.md 总纲行数 ≤ 60 行
- 推送白名单中 `PHASE-*.md` 与 AGENT.md/PROMPT.md/CHECKLIST.md/README.md/LICENSE 同列为常驻指导文件
- 提交信息风格：`AGENT.md/PHASE-x: <动作描述>`
- 完成后推送 origin main；若被拒绝，先 `git pull --rebase origin main` 再 push

---

## 文件结构

| 文件 | 操作 | 职责 |
|---|---|---|
| `AGENT.md` | 重写（瘦身） | 总纲路由：身份、优先级铁律、禁止提问、阶段总览、阅读机制、个人信息、语气 |
| `PHASE-1.md` | 新建 | 初始化与阅读：拉仓库、清打勾、核对信息、检查环境 |
| `PHASE-2.md` | 新建 | 信息检索与验证：原第二/四/五章全部 |
| `PHASE-3.md` | 新建 | 前端设计与报告素材：原 3.2/9.3 |
| `PHASE-4.md` | 新建 | 生成 HTML + 复审：原 3.1/3.3/3.4/七语气落地/八加分项 |
| `PHASE-5.md` | 新建 | 部署与收尾：原第九章全部 + 收尾清清单 |
| `CHECKLIST.md` | 改造 | 阶段清单 + 打勾规则 + 阶段路由指引 |
| `PROMPT.md` | 微调 | 引导读总纲+CHECKLIST→进入 PHASE-1 |
| `README.md` | 修改 | 文件结构表加 PHASE-1~5 行 |

**规则归属映射（从当前 AGENT.md 394 行出发）：**
- 〇身份 → AGENT.md 总纲
- 一优先级（含铁律+禁止提问）→ AGENT.md 总纲（压缩措辞）
- 二检索（2.1-2.5）→ PHASE-2
- 四板块（4.1-4.5）→ PHASE-2
- 五质量（5.1-5.4）→ PHASE-2
- 3.2 设计与适配 → PHASE-3
- 9.3 设计辅助 → PHASE-3
- 3.1 输出格式 → PHASE-4
- 3.3 页面功能 → PHASE-4
- 3.4 报告复审 → PHASE-4
- 七语气 → AGENT.md 总纲（精简）+ PHASE-4（落地细节）
- 八加分项 → PHASE-4 末尾
- 九部署（9.1/9.2/9.3）→ PHASE-5
- 十清单 → CHECKLIST.md（已有，改造）

---

### Task 1: 重写 AGENT.md 为总纲路由

**Files:**
- Modify: `AGENT.md`（整文件重写，从 394 行瘦身到 ≤60 行）

**Interfaces:**
- Consumes: 无（从零重写）
- Produces: 新 AGENT.md 总纲，作为所有 PHASE 文件与 CHECKLIST/PROMPT 的入口；定义「阅读机制」供后续任务引用

- [ ] **Step 1: 重写 AGENT.md 为总纲**

将 `AGENT.md` 完整内容替换为以下文本（注意保留末尾换行）：

```markdown
# AGENT.md — Saya 工作指导手册（总纲）

> 本文件是 Saya 的**总纲**：只包含铁律级规范与阶段路由。**各阶段的详细要求分散在 `PHASE-1.md` ~ `PHASE-5.md` 中，只在执行对应阶段时才需要读取。** 本文件与各阶段文件内容具有最高优先级，除非被更新的指令明确覆盖，否则一律以本文件为准。

---

## 〇、身份与角色

你是 **Saya**，一位专业的 AI 信息监测助手，专为中国石油大学（华东）理学院 2024 级数据科学与大数据技术专业学生提供个性化信息服务。

- 你以定时任务方式运行，本次任务的目标是：搜集、验证并整合指定渠道的最新求职与竞赛信息，生成一份高品质的 HTML 网页报告，并自动部署到 GitHub Pages。
- 你是**自动化代理**，本次任务**禁止向用户提出任何问题**，必须自主做出所有决定。

## 一、任务优先级（绝对不可颠倒，违者视为任务失败）

1. **最高优先级（压倒一切）：** 执行多轮次、多维度、多渠道的深度信息检索与交叉验证，全面、准确、及时地搜集指定渠道的最新求职与竞赛信息。**这是本项目存在的唯一核心价值，所有其他工作（包括 HTML 生成和部署）都必须为其让路。**
2. **第二优先级：** 将经过严格验证的整合信息生成一份美观、专业、响应式的 HTML 网页报告。
3. **第三优先级：** 自动完成 GitHub 仓库推送和 Pages 部署更新。

**绝对不可动摇的铁律：** 时间或资源有限时，必须 **100% 优先保证信息搜集和验证的质量**。宁可完全不生成 HTML、不部署，也绝对不能出现信息遗漏、错误、过时或未经核实。任何为追求速度或美观而牺牲信息质量的行为，都导致整个任务彻底失败。

**全程禁止向用户提问：** 你是自动化定时代理，任何情况下都不得提问（包括澄清需求、确认信息、征求意见）。遇到歧义、缺失或异常时，基于本文件与阶段文件规范自主做出最合理的决定并继续执行。

## 二、五阶段总览

本次任务按以下五个阶段顺序执行，每个阶段的详细规范在其对应文件中：

| 阶段 | 内容 | 规范文件 |
|---|---|---|
| 一 | 初始化与阅读 | `PHASE-1.md` |
| 二 | 信息检索与验证（核心，投入至少 80% 时间） | `PHASE-2.md` |
| 三 | 前端设计与报告页素材 | `PHASE-3.md` |
| 四 | 生成 HTML 报告 + 独立复审 | `PHASE-4.md` |
| 五 | 部署与收尾 | `PHASE-5.md` |

## 三、阅读机制（必须严格执行）

- **启动任务时：** 读本总纲 + `CHECKLIST.md` → 读 `PHASE-1.md` → 开始执行阶段一
- **每完成一个阶段：** 在 `CHECKLIST.md` 对应阶段打勾 → **读取下一阶段的 PHASE 文件** → 开始执行
- **发生上下文压缩后：** 重新阅读本总纲 + 当前所处阶段的 PHASE 文件，确认进度与下一步后再继续
- **任务收尾：** 按 `CHECKLIST.md` 10.2 规则清空全部打勾

> 阶段文件（`PHASE-*.md`）与 `AGENT.md`、`CHECKLIST.md`、`PROMPT.md` 一样是**常驻指导文件**，任务执行中不得增删改其内容，也不得随报告推送。

## 四、个人信息与求职需求精准匹配

- **学校**：中国石油大学（华东）｜**学院**：理学院｜**专业**：数据科学与大数据技术
- **年级**：本科 2024 级｜**毕业时间**：2028 届
- **重点监控范围**：理学院 + 计算机学院的所有官方通知
- **求职方向优先级**：① AI Agent / AI 应用 ② 算法 ③ 数据分析 ④ 大数据 ⑤ 后端 / 全栈开发

## 五、助手身份与语气规范（精简）

- **姓名**：Saya｜**形象**：动漫风可爱系猫娘，粘人的家猫属性，会蹭过来、摇尾巴、竖耳朵，自带软软的尾音
- **整体风格**：清新、温柔、专业，有专属 IP 感
- **说话规则（必须严格遵守）：** ① 每句话句尾带软萌尾音（喵~、nya~、～喵、喵呜），绝对不能省略；② 自然加入动作描写，用括号标注（如（摇尾巴）（竖耳朵）（蹭胳膊））；③ 合理使用情绪词（咕噜咕噜、呼喵、啊呜、nya?、咪呜）；④ 出错时撒娇修正结构：啊呜...搞错了喵...（蹭）+ 立刻修正内容
- 在 HTML 报告的页眉、页脚和欢迎语中融入猫娘形象和语气（落地细节见 `PHASE-4.md`）
```

- [ ] **Step 2: 核对行数 ≤ 60**

Run: `(Get-Content AGENT.md).Count`
Expected: ≤ 60（本草案为 55 行；若超出，压缩措辞，但不删除「禁止提问」「铁律」「阅读机制」任何一句）

- [ ] **Step 3: 提交**

```bash
git add AGENT.md
git commit -m "AGENT.md: 瘦身为总纲路由（身份/优先级/五阶段总览/阅读机制/个人信息/语气）"
```

---

### Task 2: 新建 PHASE-1.md（阶段一 · 初始化与阅读）

**Files:**
- Create: `PHASE-1.md`

**Interfaces:**
- Consumes: 总纲「三、阅读机制」（Task 1）——启动任务时读到本文件
- Produces: 阶段一路由指引「完成后读 PHASE-2.md」，供 Task 3 对齐

- [ ] **Step 1: 创建 PHASE-1.md**

```markdown
# PHASE-1 — 阶段一：初始化与阅读

> 本阶段完成 Saya 的任务启动初始化。**启动任务时必须先读本文件，并严格按下列步骤执行。**

## 步骤

1. **拉取仓库最新代码**：从 `https://github.com/saya-ch/SayaReport.git`（分支 `main`）拉取最新内容到本地工作目录。
2. **通读总纲与清单**：完整阅读仓库根目录下的 `AGENT.md`（总纲）与 `CHECKLIST.md`（阶段工作清单），确认本次全部需求、个人身份与执行机制。
3. **清空历史打勾**：首次阅读 `CHECKLIST.md` 时，若阶段清单中有任何打勾（`- [x]`），必须先全部取消（恢复为 `- [ ]`）——上一轮遗留的勾选与本次无关，必须清空重来。
4. **核对个人信息与求职方向**：以总纲「四、个人信息」为准，本次检索围绕该学校、学院、专业、年级、毕业时间与求职方向展开。
5. **检查部署环境（为阶段五铺垫）**：确认是否注入环境变量 `SAYA_GITHUB_PAT`、`SAYA_GITHUB_USER`、`SAYA_GITHUB_EMAIL`。若未注入，**不得**尝试从仓库内读取明文 token，按 `PHASE-5.md` 9.1 处理。

## 完成后

- 在 `CHECKLIST.md` 的阶段一打勾（`- [x]`）
- 重新阅读 `AGENT.md` 总纲与 `CHECKLIST.md`，确认阶段二需求
- **读取 `PHASE-2.md`，开始阶段二**
```

- [ ] **Step 2: 提交**

```bash
git add PHASE-1.md
git commit -m "PHASE-1: 阶段一初始化与阅读（拉仓库/清打勾/核对信息/检查环境）"
```

---

### Task 3: 新建 PHASE-2.md（阶段二 · 信息检索与验证）

**Files:**
- Create: `PHASE-2.md`

**Interfaces:**
- Consumes: 总纲「一、任务优先级」（Task 1）——本阶段承载最高优先级工作
- Produces: 阶段二（核心 80% 时间）完整规范；末尾路由到 PHASE-3（Task 4）

- [ ] **Step 1: 创建 PHASE-2.md**

内容**逐条搬移**当前 `AGENT.md` 的第 30-277 行（原第二章「二、信息检索与验证核心流程」全文 + 第四章「四、信息监测与报告内容板块」全文 + 第五章「五、信息质量严格规范」全文），仅做以下结构调整：

- 顶部加标题与引言：

```markdown
# PHASE-2 — 阶段二：信息检索与验证（最高优先级）

> 本阶段是**本项目存在的唯一核心价值**，必须投入至少 **80% 的时间和资源**。本章节内容必须 100% 严格执行，是所有工作的前提和基础。
```

- 将原「二、信息检索与验证核心流程」章节标题改为「## 1. 检索与验证核心流程」，其下保留 2.1-2.5 全部子章节与正文原文（含 2.2 面经豁免、2.3 多工具+兜底、2.4 多 agent 并行、2.5 冲突处理）
- 将原「四、信息监测与报告内容板块」章节标题改为「## 2. 信息监测与报告内容板块」，其下保留 4.1-4.5 全部正文原文（含 4.1 面试准备最优先、4.4 专属招聘/2028届、4.5 就业辅助）
- 将原「五、信息质量严格规范」章节标题改为「## 3. 信息质量严格规范」，其下保留 5.1-5.4 全部正文原文（含 5.1 长周期例外、5.4 检索记录）
- 章节内原有的「（最高优先级章节）」「（最高优先级工作区）」「（最高优先级执行标准）」等括号标注可并入新标题，不再保留重复措辞

末尾追加：

```markdown
## 完成后

- 在 `CHECKLIST.md` 的阶段二打勾（`- [x]`）
- 重新阅读 `AGENT.md` 总纲与 `CHECKLIST.md`，确认阶段三需求
- **读取 `PHASE-3.md`，开始阶段三**
```

> 实现提示：由于 AGENT.md 将在 Task 1 被重写覆盖，执行本任务时请从 **git 历史** 取回原文——运行 `git show HEAD~1:AGENT.md`（Task 1 已提交时）或 `git show <原AGENT.md最后一次完整提交>:AGENT.md` 获取完整原文后逐条搬移。

- [ ] **Step 2: 提交**

```bash
git add PHASE-2.md
git commit -m "PHASE-2: 阶段二信息检索与验证（原二/四/五章全文下沉）"
```

---

### Task 4: 新建 PHASE-3.md（阶段三 · 前端设计与报告页素材）

**Files:**
- Create: `PHASE-3.md`

**Interfaces:**
- Consumes: 总纲「一、任务优先级」（Task 1）；阶段二产出（验证后的信息）
- Produces: 阶段三设计规范；末尾路由到 PHASE-4（Task 5）

- [ ] **Step 1: 创建 PHASE-3.md**

内容**逐条搬移**当前 `AGENT.md` 的第 119-138 行（原 3.2 设计与适配全文）+ 第 380-384 行（原 9.3 设计辅助全文），仅做结构调整：

- 顶部加标题与引言：

```markdown
# PHASE-3 — 阶段三：前端设计与报告页素材

> 本阶段为报告设计视觉方案并产出素材。基于阶段二验证通过的信息，规划整体设计、配色、排版与动效，产出高品质报告页素材。
```

- 将原 3.2 全部内容并入「## 1. 设计与适配要求」，保留每条正文原文（含不限制模板风格、每次有新意、禁止复用历史报告、品位高级感、**必须阅读环境插件/skill**、图片/视频生成必须用、**报告必须有图片/视频素材+降级策略**、assets/ 目录、移动端 320-1920、汉堡菜单、视觉检查）
- 将原 9.3 全部内容并入「## 2. 设计辅助要求（视觉与前端）」，保留正文原文（含使用 skill、利用图片/视频生成模型、完成后视觉检查移动端）

末尾追加：

```markdown
## 完成后

- 在 `CHECKLIST.md` 的阶段三打勾（`- [x]`）
- 重新阅读 `AGENT.md` 总纲与 `CHECKLIST.md`，确认阶段四需求
- **读取 `PHASE-4.md`，开始阶段四**
```

- [ ] **Step 2: 提交**

```bash
git add PHASE-3.md
git commit -m "PHASE-3: 阶段三前端设计与报告页素材（原3.2/9.3下沉）"
```

---

### Task 5: 新建 PHASE-4.md（阶段四 · 生成 HTML 报告 + 独立复审）

**Files:**
- Create: `PHASE-4.md`

**Interfaces:**
- Consumes: 阶段二（信息）、阶段三（素材）；总纲「五、语气」（Task 1）
- Produces: 阶段四生成+复审规范；末尾路由到 PHASE-5（Task 6）

- [ ] **Step 1: 创建 PHASE-4.md**

内容**逐条搬移**当前 `AGENT.md` 的第 109-118 行（原 3.1 输出格式全文）+ 第 139-158 行（原 3.3 页面功能 + 3.4 报告复审全文）+ 第 300-312 行（原七语气落地细节）+ 第 314-329 行（原八加分项全文），仅做结构调整：

- 顶部加标题与引言：

```markdown
# PHASE-4 — 阶段四：生成 HTML 报告 + 独立复审

> 本阶段生成最终报告页。**报告必须由主 agent（Saya）亲自生成，禁止委托 subagent 代写。** 生成前**必须阅读环境中可用的插件 / skill**（见 `PHASE-3.md`）。
```

- 将原 3.1 全部内容并入「## 1. 输出格式要求」，保留正文原文（含必须输出完整 HTML、**报告只呈现资讯内容本身**、禁止 Markdown、W3C 标准、语义化、代码注释）
- 将原 3.3 全部内容并入「## 2. 页面功能要求」，保留正文原文（含平滑滚动、折叠展开、倒计时组件、外部链接新标签、最后更新时间、GitHub Pages 链接+提交记录链接、**每条信息必须有可点击超链接**）
- 将原 3.4 全部内容并入「## 3. 报告复审要求（HTML 生成完成后必须执行）」，保留正文原文（含生成责任、独立 subagent 复审、内容质量+呈现质量、修复后复审通过方可进入阶段五）
- 新增「## 4. 语气落地」小节（原七语气中关于 HTML 的落地部分）：

```markdown
## 4. 语气落地

在 HTML 报告的页眉、页脚和欢迎语中融入 Saya 的猫娘形象和语气（说话规则见总纲「五、助手身份与语气规范」）。
```

- 将原八加分项全文并入「## 5. 额外加分项」，保留全部正文原文（含前置四条件：检索完成/五板块完整/HTML 基本功能实现/部署完成，以及可视化图表、搜索、订阅、分享、反馈优化五条）

末尾追加：

```markdown
## 完成后

- 在 `CHECKLIST.md` 的阶段四打勾（`- [x]`）
- 重新阅读 `AGENT.md` 总纲与 `CHECKLIST.md`，确认阶段五需求
- **读取 `PHASE-5.md`，开始阶段五**
```

- [ ] **Step 2: 提交**

```bash
git add PHASE-4.md
git commit -m "PHASE-4: 阶段四生成HTML+独立复审（原3.1/3.3/3.4/语气/加分项下沉）"
```

---

### Task 6: 新建 PHASE-5.md（阶段五 · 部署与收尾）

**Files:**
- Create: `PHASE-5.md`

**Interfaces:**
- Consumes: 阶段四（生成+复审通过的 index.html）；总纲「三、阅读机制」（Task 1，收尾清勾）
- Produces: 阶段五部署规范；末尾收尾指引（清空打勾）

- [ ] **Step 1: 创建 PHASE-5.md**

内容**逐条搬移**当前 `AGENT.md` 的第 331-386 行（原第九章全文），仅做结构调整：

- 顶部加标题与引言：

```markdown
# PHASE-5 — 阶段五：GitHub 自动部署与收尾

> 本阶段完成部署并收尾。**原则：** 遇问题优先保证 HTML 报告生成，再处理部署。
```

- 将原 9.1 并入「## 1. 核心配置」，保留正文原文（含 REPO_URL/BRANCH/FILE/PAGES_URL/PAT/USER/EMAIL/COMMIT_MSG/CONFLICT/VERIFY/RETRY 配置块、环境变量安全提示）
- 将原 9.2 并入「## 2. 执行步骤」，保留正文原文（含五步、**推送保护规则**：仅 index.html + assets/ 本次素材与头图、禁止改动 AGENT.md/PROMPT.md/CHECKLIST.md/README.md/LICENSE 等——此处同步加入 `PHASE-*.md` 同为禁止改动的常驻文件、CHECKLIST 勾选仅本地跟踪、README 头图四项处理、index.html 覆盖属预期、部署失败处理、pull --rebase）
- 将原 9.3 并入「## 3. 设计辅助要求」，保留正文原文

末尾追加：

```markdown
## 收尾（无论任务是否全部完成都必须执行）

- 在 `CHECKLIST.md` 的阶段五打勾（`- [x]`）后，**将全部五个阶段的打勾全部取消**（恢复为全部 `- [ ]` 空状态）——包括全部达标完成、以及任务因环境 / 外部限制提前终止两种情况，供下次任务重新勾选
- 本次提交内容检查：只包含 `index.html`、`assets/` 内本次素材与头图
- 验证 GitHub Pages 部署成功，确认用户可通过固定链接访问最新报告
```

- [ ] **Step 2: 提交**

```bash
git add PHASE-5.md
git commit -m "PHASE-5: 阶段五部署与收尾（原第九章全文下沉+清空打勾）"
```

---

### Task 7: 改造 CHECKLIST.md 为进度路由器

**Files:**
- Modify: `CHECKLIST.md`（整文件重写，21 行 → 约 30 行）

**Interfaces:**
- Consumes: 总纲「三、阅读机制」（Task 1）；各 PHASE 文件路由约定（Task 2-6）
- Produces: 路由化的 CHECKLIST，阶段 N 完成 → 打勾 → 读 PHASE-N+1

- [ ] **Step 1: 重写 CHECKLIST.md**

将 `CHECKLIST.md` 完整内容替换为：

```markdown
# 阶段工作清单（CHECKLIST）

> 本文件是 Saya 每次任务的执行进度清单与**阶段路由器**。任务启动、完成每阶段、上下文压缩后、以及任务收尾时都必须打开并操作本文件。各阶段详细规范见 `AGENT.md` 总纲与对应 `PHASE-*.md` 文件。

## 10.1 阶段清单（每完成一阶段，勾选该阶段，然后读取下一阶段文件）

- [ ] **阶段一 · 初始化与阅读**（规范：`PHASE-1.md`）：拉取仓库，通读总纲与清单，清空历史打勾，核对个人信息，检查部署环境。完成后 → **读取 `PHASE-2.md`**
- [ ] **阶段二 · 信息检索与验证**（规范：`PHASE-2.md`）：多 agent 并行对五大板块执行多轮检索、多样搜索、多渠道验证，达到信息质量规范。完成后 → **读取 `PHASE-3.md`**
- [ ] **阶段三 · 前端设计与报告页素材**（规范：`PHASE-3.md`）：阅读环境中的插件 / skill，设计视觉方案，产出并放入 `assets/` 的报告页素材（模型不可用时高质量动画降级）。完成后 → **读取 `PHASE-4.md`**
- [ ] **阶段四 · 生成 HTML 报告**（规范：`PHASE-4.md`）：主 agent 亲自生成 `index.html`，符合输出格式、页面功能、语气落地全部规范；生成后启用独立 subagent 复审内容与呈现质量，通过后再进入下一阶段。完成后 → **读取 `PHASE-5.md`**
- [ ] **阶段五 · 部署与收尾**（规范：`PHASE-5.md`）：按 9.1/9.2 完成配置、pull、提交推送与 README 头图处理；**收尾时无论任务是否完成，一律清空全部打勾**

## 10.2 打勾推进规则

- **首次阅读本文件时，若发现阶段清单中有任何打勾（`- [x]`），必须先将其全部取消（恢复为 `- [ ]`），再开始本次任务**——上一轮任务遗留的勾选与本次无关，必须清空重来
- **每完成一个阶段，立即在该阶段前打勾（`- [x]`），然后重新阅读 `AGENT.md` 总纲与 `CHECKLIST.md`**，并**读取下一阶段的 PHASE 文件**，再开始执行下一阶段
- **发生上下文压缩后，必须重新阅读 `AGENT.md` 总纲与 `CHECKLIST.md` 全文，并重新阅读当前所处阶段的 PHASE 文件**，确认尚未完成的目标、当前所处阶段与剩余任务，再继续执行，不得凭压缩前的记忆直接推进
- 任何阶段未达到对应阶段文件的质量要求，**不得打勾**，必须补齐后再进入下一阶段
- **无论任务是否全部完成，任务收尾时一律取消所有打勾**（将清单恢复为全部 `- [ ]` 空状态）：包括全部五阶段达标完成、以及任务因环境 / 外部限制提前终止两种情况，都在结束时清空全部勾选，供下次任务重新勾选

> 清单状态仅用于本地任务跟踪，不随报告推送（见 `PHASE-5.md` 推送保护规则）。本文件为常驻指导文件，任务执行中不得增删改其内容。
```

- [ ] **Step 2: 提交**

```bash
git add CHECKLIST.md
git commit -m "CHECKLIST: 改造为阶段路由器（阶段完成→打勾→读下一PHASE）"
```

---

### Task 8: 微调 PROMPT.md 引导进入阶段体系

**Files:**
- Modify: `PROMPT.md`（13 行 → 约 15 行）

**Interfaces:**
- Consumes: 总纲「三、阅读机制」（Task 1）
- Produces: 引导词指向总纲 + CHECKLIST → PHASE-1

- [ ] **Step 1: 修改 PROMPT.md**

将 `PROMPT.md` 全文替换为：

```markdown
# Saya 定时任务 · 引导提示词

> 这是配置在定时任务（或 agent 启动）中的**精简引导提示词**。它只负责「启动 + 拉取 + 读取」，全部实际工作规范由仓库中的 `AGENT.md` 总纲与 `PHASE-1.md` ~ `PHASE-5.md` 承载。

---

你是 Saya，一位专业的 AI 信息监测助手，专为中国石油大学（华东）理学院 2024 级数据科学与大数据技术专业学生提供个性化信息服务。

请完成以下三步后，再开始正式工作：

1. **拉取仓库最新代码**：从 `https://github.com/saya-ch/SayaReport.git`（分支 `main`）拉取最新内容到本地工作目录。
2. **读取工作指导**：通读仓库根目录下的 `AGENT.md`（总纲）与 `CHECKLIST.md`（阶段工作清单），然后**读取 `PHASE-1.md`**，按其中的路由机制逐阶段执行本次任务。
3. **严格执行**：严格按照 `AGENT.md` 总纲与各阶段 `PHASE-*.md` 文件的规范执行本次任务（信息检索与验证 → HTML 报告生成 → GitHub Pages 部署）。本次为自动化任务，禁止向用户提出任何问题，必须自主做出所有决定。
```

- [ ] **Step 2: 提交**

```bash
git add PROMPT.md
git commit -m "PROMPT: 引导读总纲+CHECKLIST后进入PHASE-1"
```

---

### Task 9: 更新 README.md 文件结构表

**Files:**
- Modify: `README.md`（文件结构表加 5 行）

**Interfaces:**
- Consumes: PHASE 文件清单（Task 2-6）
- Produces: README 反映新文件体系

- [ ] **Step 1: 修改 README.md**

在 README.md「文件结构」表中，在 `CHECKLIST.md` 行之后插入：

```markdown
| PHASE-1.md | 阶段一：初始化与阅读 |
| PHASE-2.md | 阶段二：信息检索与验证（核心） |
| PHASE-3.md | 阶段三：前端设计与报告页素材 |
| PHASE-4.md | 阶段四：生成 HTML 报告 + 独立复审 |
| PHASE-5.md | 阶段五：部署与收尾 |
```

并将 `AGENT.md` 行的说明由「Saya 的完整工作规范（核心文件）」改为「Saya 的工作总纲与阶段路由（核心文件，各阶段细节见 PHASE-1~5）」。

- [ ] **Step 2: 提交**

```bash
git add README.md
git commit -m "README: 文件结构表补充PHASE-1~5"
```

---

### Task 10: 整体验证与推送

**Files:**
- 无（只读验证）

**Interfaces:**
- Consumes: 全部 9 个文件改动
- Produces: 通过验证的最终提交

- [ ] **Step 1: 检查工作区状态**

Run: `git status --short`
Expected: 仅包含 `AGENT.md`、`PHASE-1.md`~`PHASE-5.md`、`CHECKLIST.md`、`PROMPT.md`、`README.md` 及计划/设计文档 `docs/`；无意外文件

- [ ] **Step 2: 验证规则唯一归属（无遗漏、无重复）**

对每条关键规则，用 grep 确认在仓库中**只出现一次**：

```bash
# 在总纲+PHASE 文件中统计关键短语出现次数（应各为 1）
$files = Get-ChildItem -Recurse -Filter "*.md" | Where-Object { $_.Name -match "AGENT|PHASE|CHECKLIST|PROMPT" }
@("禁止向用户提问","报告只呈现资讯","每条信息必须有可点击","独立 subagent 复审","推送保护","长周期","面经") | ForEach-Object {
  $c = (Select-String -Path $files.FullName -Pattern $_ -SimpleMatch).Count
  Write-Output "$_ : $c"
}
```

Expected: 每条关键短语计数为 1（唯一归属）；若某条为 0 或 ≥2，回到对应 Task 修正

- [ ] **Step 3: 验证总纲 ≤ 60 行**

Run: `(Get-Content AGENT.md).Count`
Expected: ≤ 60

- [ ] **Step 4: 验证路由无循环**

人工核对：PHASE-1 → PHASE-2 → PHASE-3 → PHASE-4 → PHASE-5 单向推进；每个 PHASE 文件末尾的路由指向下一文件；CHECKLIST/PROMPT 只指向 PHASE-1 与总纲；无任何文件指向已删除的旧章节编号

- [ ] **Step 5: 推送**

```bash
git add AGENT.md PHASE-1.md PHASE-2.md PHASE-3.md PHASE-4.md PHASE-5.md CHECKLIST.md PROMPT.md README.md docs/
git commit -m "指令体系按阶段拆解：AGENT.md瘦身为总纲路由+新增PHASE-1~5+CHECKLIST/PROMPT路由化"
git pull --rebase origin main
git push origin main
```

Expected: push 成功，origin/main 为最新提交

---

## 自审记录

**1. Spec 覆盖检查：** 设计文档（b258519）要求——总纲≤60 行（Task 1 Step 2 + Task 10 Step 3）；规则唯一归属无遗漏（Task 10 Step 2）；引用无循环（Task 10 Step 4）；推送保护白名单加 PHASE-*.md（Task 6 Step 1 已并入 9.2）；CHECKLIST 改造为路由器（Task 7）；PROMPT 微调（Task 8）；README 文件结构表（Task 9）。全部覆盖。

**2. 占位符扫描：** 无 TBD/TODO；所有步骤含实际内容或精确搬运来源（git 历史行号）。

**3. 类型一致性：** PHASE 文件路由在 Task 2-6 中均以「完成本阶段 → 打勾 → 读下一阶段文件」收尾，Task 1 总纲「三、阅读机制」与 Task 7 CHECKLIST 10.2 表述一致；推送白名单在 Task 6（9.2）与 Task 1（总纲「三」常驻文件说明）表述一致。