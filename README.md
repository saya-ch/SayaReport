<p align="center">
  <img src="assets/banner.png" alt="SayaReport Banner" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/GitHub%20Pages-自动部署-blue?style=for-the-badge">
  <img src="https://img.shields.io/github/license/saya-ch/SayaReport?style=for-the-badge">
  <img src="https://img.shields.io/github/last-commit/saya-ch/SayaReport?style=for-the-badge">
  <img src="https://img.shields.io/github/repo-size/saya-ch/SayaReport?style=for-the-badge">
</p>

# SayaReport

Saya 专属自动化资讯监测系统，面向中国石油大学（华东）理学院 2024 级数据科学与大数据技术专业学生。由 AI 助手 Saya 定时运行，权威整合求职、竞赛、实习、就业等资讯，精准匹配 AI Agent / AI 应用、算法、数据分析、大数据、后端/全栈等求职方向，并自动生成高品质 HTML 网页报告，部署到 GitHub Pages 每日定时更新。

在线报告：<https://saya-ch.github.io/SayaReport/>

## 功能特点

- 自动化定时运行，全程无需人工干预
- 多轮次、多渠道深度检索，每条信息至少 2 个独立权威源交叉验证
- 五大信息板块：
  - 面试准备资讯（重点板块）：面试技巧、面经、学习路径、高价值资料、讨论群组
  - 学术竞赛资讯：完整奖项、报名/截止时间、参赛要求、赛程安排
  - 企业赛事资讯：奖金、实习机会、校招绿色通道、获奖福利
  - 实习招聘信息：技能要求、申请链接、薪资待遇、专属招聘信息
  - 就业辅助资讯：行业趋势、职业认证、就业政策、简历优化、面试技巧
- 精准匹配求职方向：AI Agent/AI 应用、算法、数据分析、大数据、后端/全栈
- 高品质响应式 HTML 报告，适配 320px-1920px 移动端
- GitHub Pages 自动部署

## 文件结构

| 文件 | 说明 |
| ---- | ---- |
| AGENT.md | Saya 的完整工作规范（核心文件），定义身份角色、任务优先级、信息检索验证流程、报告输出设计规范、内容板块、信息质量规范、语气规范与自动部署流程 |
| PROMPT.md | 精简引导提示词，引导 Saya 拉取仓库、读取 AGENT.md 并严格执行 |
| index.html | 每次任务生成的求职信息报告页面，自动覆盖更新 |
| assets/ | 静态资源文件夹，存放头图及本次生成的图片、视频等素材 |
| README.md | 项目说明 |

## 快速开始

Saya 以定时任务方式运行，引导流程如下：

1. 拉取本仓库最新代码
2. 读取根目录下的 AGENT.md
3. 严格按照 AGENT.md 各章节规范执行信息检索、HTML 生成与部署
4. 全程自动化，不向用户提问

### 环境变量

部署环节所需敏感信息通过环境变量或 GitHub Secret 注入，不在仓库中写死明文：

```
SAYA_GITHUB_PAT      # GitHub Personal Access Token
SAYA_GITHUB_USER     # 仓库账号
SAYA_GITHUB_EMAIL    # 提交邮箱（建议使用 noreply 隐私邮箱）
```

## 技术栈

- HTML / CSS / JavaScript：报告前端
- Git / GitHub：版本管理与部署
- GitHub Pages：静态站点托管
- 图片 / 视频生成模型：辅助前端设计（可选）

## 维护说明

- 每次提交仅添加本次生成的报告文件（index.html 及 assets/ 中的素材），不删除、覆盖或改动 AGENT.md、PROMPT.md 指导文件
- 每次报告均基于全新检索独立生成，不参考或复用历史报告
- 信息检索与验证质量优先于一切，宁可不出报告也不输出错误、过时或未经核实的信息

## 许可

本项目基于 [MIT License](LICENSE) 发布。
