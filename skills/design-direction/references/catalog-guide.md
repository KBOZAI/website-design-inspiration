# 案例收录与筛选规范（schema_version 2）

案例的单位是网站及其页面关系，不是漂亮首屏或动效片段。展示、阅读、工具、商业页面都可以收录；行业仅辅助描述。原 README 的发现链接继续保留，进入结构化目录不代表通过整站验收。

## 记录字段

| 字段 | 含义 |
| --- | --- |
| `id`, `name`, `url` | 稳定 ID、名称、原站地址；不因排序改变 ID |
| `modes` | 候选适用的 read / operate / persuade / experience；这是匹配判断，不是原作者声明 |
| `content_types` | articles / projects / resume / photos / links / notes / data / products / forms |
| `structure_family` | 主要组织方式，例如 side-identity-flow / editorial-index；用于防止同一结构占满候选 |
| `tags.layout`, `tags.density`, `tags.mood` | 布局、密度、气质；不可用气质替代板块分析 |
| `sections` | 实际观察到的板块，按观察顺序；不补造未见内页 |
| `asset_requirement` | text-first / mixed / image-led：迁移该方向预计需要的素材量 |
| `classification_note` | 哪些标签是编辑判断、哪些是实际观察 |
| `use_when`, `do_not_copy_blindly` | 适配理由与迁移风险 |
| `evidence.observed_on`, `level`, `note`, `source` | 观察日期、范围、限制及来源；更新标签不刷新观察日期 |
| `evidence.pages` | 逐页证据，见下方 |
| `evidence.interactions` | 实际尝试的操作及结果，空数组表示没验收 |
| `evidence.screenshots`, `rights` | 已留存的图像路径/URL及复用说明；无许可时不自动公开截图 |

`pages` 每项包含 `kind`（home / inner）、`url`、`viewport`（desktop / mobile）、`extent`（full / partial / first-screen / text）、`observed_on`、`capture`（可为空）、`note`。截图要和这次观察对应，不把旧图当新站。

`interactions` 每项包含 `task`、`result`（pass / fail）、`observed_on`、`note`。例如“首页进入文章、返回列表”与实测结果。不能从有链接推断链接已测试。

## 证据分级与推荐门槛

- `text-only`：只发现内容或链接，不进入视觉候选。
- `desktop-home-only` / `desktop-partial`：仅可作为明确标记的探索候选，不能代表整站好用。
- `whole-site-reviewed`：桌面完整首页、至少一个关键内页、移动端完整页面均有图像证据，并实际通过至少一条核心导航/操作路径。

整站证据仍有时效。脚本默认使用运行日期和 90 天复核窗口；这只是本项目维护默认值，不是质量标准。可用 `--as-of` 固定评估日期，`--max-age-days` 调整窗口。缺图、过期或操作失败的记录不能作为当前已核查的整站推荐。即便结构校验通过，仍需人工打开图像/页面确认内容真实且可访问；脚本不验证网络可达性或截图真实性。

当前六条种子保持历史证据等级，新增模式等字段只是编辑分类。没有批量把它们升级成整站已验收。下次收录按真实检查补齐，不先追求数量。

## 可运行筛选

从仓库根目录运行（Python 3.9+，无第三方依赖、无网络和遥测）：

```sh
python3 skills/design-direction/scripts/catalog.py validate
python3 skills/design-direction/scripts/catalog.py shortlist --mode read --content articles
python3 skills/design-direction/scripts/catalog.py shortlist --mode read --content articles --include-partial
python3 skills/design-direction/scripts/catalog.py shortlist --mode read --content articles --content projects --density high --exclude josh-comeau --include-partial
```

默认只返回近期整站已核查的记录，所以当前严格结果为空是预期。显式 `--include-partial` 才允许有视觉观察的历史候选；`text-only` 始终排除。部分候选返回缺少的内页、手机、截图、操作证据等提示。过期条目只可作为待重新核查的候选。

筛选先应用模式、密度、排除项、内容交集等约束；有多个内容要求时，按覆盖数量排列，并明确列出未覆盖内容。相同覆盖度时，优先给不同结构留位置，再看证据和 ID 稳定排序。不会为了风格多样性牺牲更高的内容覆盖度。`--density` 是硬过滤；不满足时返回空结果。`--limit` 上限 5。

输出只负责找候选。助手仍需确认用户素材能否支持该方向，并按 `direction-workflow.md` 用用户内容制作对照方案。脚本不抓图、不评分审美、不记录用户已选中、不自动生成设计。
