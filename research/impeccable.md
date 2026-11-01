# Impeccable 研究与整合决策

研究日期：2026-11-01。上游：[pbakaus/impeccable](https://github.com/pbakaus/impeccable)，固定提交 [`4f956490f0056ae1ff5ea80372cf56e83c001d3c`](https://github.com/pbakaus/impeccable/tree/4f956490f0056ae1ff5ea80372cf56e83c001d3c)。该快照的 npm shim 版本为 4.8.0，engine 为 0.1.18。以下结论绑定此版本，不保证上游以后不变。

## 研究范围与证据

本次覆盖产品定位、24 个技能动作的职责与路由、核心新建/选方向流程、上下文与设计系统、整站评审、Slop 规则目录、运行时架构、源码关键路径、案例展示与许可，并实际运行独立检测器。核心流程逐段阅读；辅助命令按职责、关键流程和验收要求检查，未逐行审计整个 Rust、浏览器扩展或所有平台实现。

| 层次 | 核查入口 | 能支持的结论 |
| --- | --- | --- |
| 产品与展示 | README、官网 Docs / Slop / Gallery、Neo Mirai case study；查看仓库中的酒店成品示例图 | 上游提供什么、示例如何展示；不等于独立效果证明 |
| 技能入口 | `skill/SKILL.src.md`、`reference/routing.md` | 页面模式、命令路由、按需加载参考 |
| 方向与实现 | `new-work.md`、`shape.md`、`visualize.md`、`region-map.md`、`component-review.md` | 方向选择、概念图/代码两条路径、构图与验收约定 |
| 上下文 | `init.md`、`document.md`、`extract.md`、`doctor.md` | 产品事实、视觉系统、页面策略分别保存 |
| 质量 | `critique.md`、`audit.md`、`craft-floor.md`、`polish.md`、`layout.md`、`typeset.md`、各模式参考 | 设计判断与机械检测区别、结构与可用性检查 |
| 局部变化 | `bolder`、`quieter`、`distill`、`colorize`、`animate`、`delight`、`clarify` 等参考 | 变化应有具体目标，并保留既有身份 |
| 适配与运行 | `adapt`、`harden`、`onboard`、`optimize`、`overdrive`、`live`、`generate`、`hooks` | 状态与设备覆盖、可比较变体、自动检测边界 |
| 代码交叉检查 | `cli/bin/cli.js`、`docs/ENGINE.md`、`crates/context/src/catalog.rs` 与 `concept_seed.rs`、`crates/detect/src/list_rules.rs` 与 `cli.rs`、`crates/foundation/src/inline_ignores.rs` | 引擎校验、案例结构/抽取、规则目录、例外过滤的实际实现 |
| 实际运行 | 官方引擎规则列表与本仓库的小型 HTML 样例 | 局部 CLI 行为；不证明端到端设计效果 |

`docs/CLI-CONTRACT.md`包含旧版本快照描述，不能单凭它推断当前实现；这次关键行为以当前代码及实测为准。

## 修正此前对项目的理解

Impeccable 已经远超“禁用紫色渐变”的规则集：有真实运行时、方向目录、可视化选择、局部实时变体、设计系统检查和截图复核。我们的“让用户选方向”与它有明显交集，不能作为已经成立的独家能力。

其目录描述的是视觉系统/构图及其迁移规则，包含 palette/material、type/composition、topology/navigation、controls/state、responsive/motion 等方面；方向流程还使用候选抽取、重选和更稳妥/更大胆的引导，降低总选同一类方案的倾向。它也允许用户已有明确方向优先。

本项目选择专注于**真实整站参考的可核查拆解**：看过哪些页面、内容量为何匹配、选中哪一部分、如何变成当前网站的板块，以及成品是否兑现。它是可以与 Impeccable 配合的方向选择层，效果和独立价值仍需验证。

## 借鉴、改造与不纳入的内容

| 上游做法 | 本项目决定 | 落地位置 |
| --- | --- | --- |
| Persuade / Operate / Read / Experience 按页面任务区分 | 借鉴；同站不同页面可以不同模式，避免把文章/工具设计成海报 | `SKILL.md`、catalog modes |
| 按需加载不同 playbook | 借鉴；入口保持短，选择/案例/复核分开加载 | Skill 的三个 references |
| 产品事实、视觉系统、页面策略分离 | 借鉴；优先沿用已有文件，不因缺文件重做品牌 | 简报模板与实现后 DESIGN.md 记录原则 |
| 方向 contract 和构图对照 | 改造为完整页面、关键内页、手机与核心任务的约定 | `direction-workflow.md` |
| 多方案和重选 | 保留真实差异、相同内容/展示规格、拒绝后调整；不强制抽签或“挑战者”仪式 | 选择流程与案例排序 |
| `critique` 与 `audit` 分工 | 保留先设计判断后机械证据，不冒称单助手检查是独立双评审 | `review.md` |
| Slop 目录与 deterministic detector | 使用可选上游检测器，不复制 Rust/WASM；报告项要核实、去重、允许窄范围例外 | 检测器适配约定 |
| 强制字体/装饰禁令、固定尺寸或数量规则 | 不照搬；普通模式信号不覆盖用户选择，不把英文字行长度直接套成中文字符数 | 去 AI 味问题表 |
| `live` / `generate` | 记录可选使用时机；现阶段不自建热替换服务 | 集成表；不宣称已实现 |
| 多轮生图、构图像素门槛、资产生产 | 暂不引入为默认依赖；真实截图与概念稿明确区分 | 默认结构/代码路径 |
| hooks、远程目录和遥测 | 不随本技能自动安装或启用；当前筛选工具纯本地 | `scripts/catalog.py` |
| 评分与复核 | 用具体证据、影响和验收结果；不制造客观“审美分” | 复核和评估方案 |

这些是有意调整。上游有部分规则比本项目更严格，本项目不声称完整兼容上游执行流程。

## 命令体系如何服务本项目

24 个动作按职责归并：`shape/init/document/extract` 用于规划与上下文；`critique/audit` 用于评审；`bolder/quieter/distill/colorize/typeset/layout/animate/delight/overdrive` 用于定向改变；`polish/harden/clarify/adapt/optimize/onboard` 用于完成度；`live/generate` 用于局部比较；`craft` 是已弃用别名。

不把这 24 个名字直接复制成我们的命令。用户仍然说“太空了”“文章不好找”“想保留颜色但别像模板”，Skill 将它转成有范围、有理由的设计操作。需要上游能力且环境已安装时，再调用对应动作。

## 实际检测结果

官方 shim 在临时目录下载 engine 0.1.18，并按上游 `engine-checksums.txt` 校验后运行。没有安装技能、hooks、浏览器扩展或修改用户全局配置。

- `detect --list-rules --json` 返回 62 条规则。官网另有人工设计评审模式；规则数不代表整站质量覆盖率。
- 含紫色渐变文字的样例返回退出码 2，涉及 `gradient-text` 和 `ai-color-palette`。`gradient-text` 在同一样例重复出现，适配时需结合位置/证据归并。
- 改为实色文字的样例返回退出码 0。
- 保留视觉选择并加入带理由的行内例外，在普通扫描下返回 0；同文件加 `--no-config` 后仍报告规则，代码确认该参数同时关闭行内例外。
- 不存在的目标返回退出码 1，stdout 仍可能是空数组；不能只看 JSON 为空就报通过。
- 探索中，未显式声明标题字号的静态 HTML 曾被按相同字号报告层级问题；这只能说明该静态扫描的推断，需要浏览器计算样式核实，不能直接认定视觉层级有误。

可复现脚本、原创样例与结果见同目录的 `run_detector_smoke.py`、`fixtures/`、`detector-smoke.json`。这些测试验证命令接口和例外边界，没有测试移动端渲染、浏览器扫描、live 回写、hooks 安装或完整设计技能效果。

## 展示案例的可借鉴与边界

官网 Gallery 说明了首轮结果、部分旧基线的生图差异、以及 Design first 样例经过选择和人工反馈的条件。因此将其作为流程示例，不作为独立随机对照实验。[Gallery](https://impeccable.style/gallery/)

Neo Mirai 案例展示概念图到整页实现，再检查裁图、导航和轮播的流程，说明视觉构图之外仍需浏览器修正。[案例说明](https://impeccable.style/cases/neo-mirai/)

查看 README 酒店图可见其强烈的插画首屏和品牌表达，适合研究展示型页面；单张图无法证明内页、预订路径或手机端好用。我们的案例库不会因此降低整站证据要求，也不会把上游生成案例冒充真实运营网站。

## 许可与归属

已读取该提交的 LICENSE（Apache-2.0）和 NOTICE.md。改写借鉴的技能内容保留来源、上游版权和修改说明，随技能分发 LICENSE 与 NOTICE.md；不搬运上游图片、远程目录、引擎或原生平台参考。本项目独立实现了案例字段和筛选脚本。详细范围见技能 [NOTICE](../skills/design-direction/NOTICE.md)。

## 下一步验证

本次完成的是研究、方法整合、结构化筛选与接口测试。案例仍为六条历史种子，不能宣称已经形成大量整站精审图库。先补齐少量多样案例的视觉证据，再按 [EVALUATION.md](../EVALUATION.md) 比较方向贴合度、修改轮次、时间成本和任务完成情况。
