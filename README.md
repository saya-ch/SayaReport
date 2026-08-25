<p align="center">
  <img src="assets/banner.png" alt="SayaReport Banner" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/GitHub%20Pages-自动部署-blue?style=for-the-badge">
  <img src="https://img.shields.io/github/license/saya-ch/SayaReport?style=for-the-badge">
  <img src="https://img.shields.io/github/last-commit/saya-ch/SayaReport?style=for-the-badge">
  <img src="https://img.shields.io/github/repo-size/saya-ch/SayaReport?style=for-the-badge">
</p>

<h1 align="center">SayaReport</h1>

<p align="center">面向中国石油大学（华东）理学院数据科学与大数据技术专业学生的专属求职与竞赛资讯报告，每日自动更新。</p>

## 查看报告

> **在线报告：https://saya-ch.github.io/SayaReport/**
>
> 每日定时更新，最后更新时间见报告页底部。

## 报告包含哪些内容

- **面试准备资讯**（重点板块）：面试技巧、面经、学习路径、高价值资料、讨论群组
- **学术竞赛资讯**：奖项设置、报名/截止时间、参赛要求、赛程安排
- **企业赛事资讯**：奖金、实习机会、校招绿色通道、获奖福利
- **实习招聘信息**：技能要求、申请链接、薪资待遇、专属招聘信息
- **就业辅助资讯**：行业趋势、职业认证、就业政策、简历优化、面试技巧

资讯精准匹配 AI Agent / AI 应用、算法、数据分析、大数据、后端/全栈等求职方向，所有信息均经过多轮检索与多渠道交叉验证。

## 信息质量保障

- **多轮次、多渠道检索验证**：聚焦近 7 天资讯，长周期赛事/政策在有效期内同样收录，每条信息须经至少 2 个独立权威来源核验
- **每条信息附可点击来源链接**：标题可直接跳转来源，末尾标注「信息来源」，方便你逐条核对
- **倒计时与紧急提醒**：即将截止的重要信息带红色倒计时，「急招 / 即将截止」带闪烁标签
- **独立复审**：每次报告发布前由独立 subagent 复审内容准确性与呈现质量，通过后才上线

## 项目背景

本报告由 AI 助手 **Saya** 定时运行生成，为中国石油大学（华东）理学院 2024 级数据科学与大数据技术专业学生提供个性化信息服务。

## 如何运作

1. **启动**：定时任务注入 PROMPT.md 引导词，Saya 拉取仓库并通读 AGENT.md / CHECKLIST.md
2. **检索**：多 agent 并行对五大板块执行多轮检索与多渠道交叉验证
3. **设计**：加载前端设计 skill，生成图片/视频素材（不可用时以高质量动画降级），确保报告高品位呈现
4. **生成**：产出完整响应式 HTML，由独立 subagent 复审内容与呈现质量
5. **部署**：仅推送 `index.html` 与 `assets/` 静态素材至 GitHub Pages，全程无人值守

## 文件结构

| 文件 | 说明 |
| ---- | ---- |
| AGENT.md | Saya 的完整工作规范（核心文件） |
| PROMPT.md | 精简引导提示词（定时任务入口） |
| CHECKLIST.md | 阶段工作清单（执行进度跟踪，仅本地） |
| index.html | 最新求职信息报告页面 |
| assets/ | 静态资源文件夹（报告素材 + README 头图） |
| LICENSE | MIT 开源许可 |

## 许可

本项目基于 [MIT License](LICENSE) 发布。