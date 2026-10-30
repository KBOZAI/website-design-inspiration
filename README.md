# 网站设计灵感库

## 设计方法参考：Impeccable

- [Impeccable 开源项目](https://github.com/pbakaus/impeccable)：面向编程助手的设计指导与审查工具；项目说明提供布局、排版、设计评审及技术审计等能力。本次仅阅读资料，未安装或实际运行。
- [AI Slop 设计问题目录](https://impeccable.style/slop/)（用户分享的[首页入口](https://impeccable.style/#slop)）：通过反例解释常见页面问题，包括同质化卡片网格、卡片套卡片、层级不清、对比度不足和过长的首屏标题。
- [案例画廊](https://impeccable.style/gallery/)：进一步查看项目提供的设计案例。

结合本站收集目标，检查网站时优先关注：内容分组和阅读路径是否清晰；标题、正文、操作入口是否有明确层级；间距是否体现内容关系；颜色和装饰是否服务于内容；手机端及实际操作是否顺畅。检测结果只是审查线索，具体设计仍须结合内容、用户和品牌判断。

---


## 补充：从推荐文章与知乎问题发现的个人网站

按你的参考方向，优先看首页与内容板块如何组织；标明实际查看范围，网站效果可能随时间变化。

| 网站 | 可参考的结构 | 核查情况 |
| --- | --- | --- |
| [Aistar](https://blog.aistar.cool/) | 首页左侧介绍和入口，右侧推荐阅读；下方串联最新文章、项目和分类，顶部导航覆盖文章、项目、关于及友链 | 来自知乎回答；已查看桌面首页，未逐项测试功能 |
| [Neil 的自留地](https://neilmin.com/zh/) | 个人简介、博客/项目/关于入口和最近文章；标题、摘要、标签、日期与阅读时间形成阅读层次 | 已查看桌面首页；文章作者的网站 |
| [Evan Luo](https://portfolio.ohevan.com/) | 个人信息、项目和摄影作品结合，观察个人介绍与不同内容的连续编排 | 来自 Neil 的文章；已读取页面内容，视觉及交互待进一步核查 |
| [Joe Coleman](https://getcoleman.com/) | 作品集、简历、奖项、文章等入口；观察个人职业信息与作品索引 | 来自 Neil 的文章；已读取页面内容，视觉及交互待进一步核查 |
| [Antoine Wodniack](https://wodniack.dev/) | About、Work、Contact 形成个人介绍到作品和联系的路径 | 来自 Neil 的文章；已读取页面内容，视觉及交互待进一步核查 |
| [Gregory Koberger](https://gkoberger.com/) | 以个人经历、所建项目、生活与时间线呈现个人信息；偏探索式，适合借鉴内容组织 | 来自 Neil 的文章；已读取页面内容，视觉及交互待进一步核查 |

来源：[我喜欢的一些个人网站](https://neilmin.com/zh/posts/favorite-personal-websites/)；[知乎：选出一个最美的个人博客&网站，你会选择哪个？](https://www.zhihu.com/question/639181262)。知乎本次仅查看页面已加载的部分回答。

### 来源中的其他候选，待验证是否适合整体布局参考

- [POETIZE](https://poetize.cn/)：知乎回答中的博客项目；当前页面内容未能通过文本方式读取，需进一步查看实际界面。
- [Alana Goyal](https://alanagoyal.com/finder)、[Sharyap](https://sharyap.com/)：文章介绍的桌面/窗口式个人站，本次未能核实当前页面。
- [Mero Dev](https://merodev.net/)、[Logartis](https://logartis.info/)：文章中的 3D 网站，当前界面待验证，偏交互探索。
- [Anime.js](https://animejs.com/)：文章中的动画库网站，并非个人站。
- [Josh Comeau](https://www.joshwcomeau.com/) 和 [Bruno Simon](https://bruno-simon.com/) 已在下方收录；后者偏游戏化互动。

---


## 个人主页精选：整体布局与板块设计

这组以真实个人网站为参考，重点看个人介绍、导航、项目、文章和链接如何组成完整页面。以下已查看桌面首页，部分还浏览了下方板块；并非移动端或完整功能测试。页面会改版，源码与线上版本不一定一致。

| 个人站 | 整体布局与值得参考的板块 | 源码或说明 |
| --- | --- | --- |
| [Zyyo 个人站](https://zyyo.net/) | 深色网格背景，大小不同的卡片把个人简介、时间、博客、笔记、照片和音乐组合在一起；顶部导航通往独立页面 | 已查看当前站；[ZYYO 开源主页](https://github.com/ZYYO666/homepage)是同作者的项目，不能认定与当前站代码相同 |
| [ZYYO 主页项目演示](https://zyyo.cc/) | 左侧头像、个人标签和时间线，右侧简介、社交链接、贡献图与项目/网站标签页；适合观察信息的左右分栏 | [源码](https://github.com/ZYYO666/homepage)；仓库也介绍了另售的后台版本，不能假设演示与免费版完全一致 |
| [Caleb XXY 个人主页](https://xuxiny.top/) | 浅色背景与白色卡片，左侧个人标签和时间线，右侧简介、社交入口和项目分类；适合看清爽的多栏组织 | [源码](https://github.com/xxynet/HomePage)，项目说明其基于 ZYYO 主页修改；版本对应关系未验证 |
| [無名の主页](https://www.imsyy.top/) | 左侧头像、简介与社交入口，右侧时间、文字与网站导航卡片；主要参考页面分区和入口排列 | [源码](https://github.com/imsyy/home)，仓库已存档；本次页面天气模块显示获取失败 |
| [Brittany Chiang](https://brittanychiang.com/) | 左侧固定身份与导航，右侧依次呈现介绍、工作经历和项目；日期、摘要和标签构成清楚的阅读层级 | 已查看首页与经历区；[旧版源码](https://github.com/bchiang7/v4)，不保证与当前页面一致 |
| [Josh Comeau](https://www.joshwcomeau.com/) | 顶部导航、文章列表与分类/热门内容侧栏组合；看内容较多时如何保持清晰与一致的视觉风格 | 已查看首页及文章列表；源码未核实 |
| [Lee Robinson](https://leerob.com/) | 左侧个人介绍与笔记链接、右侧插画，信息紧凑但留有呼吸空间 | 已查看桌面首页；源码未核实 |
| [Maggie Appleton](https://maggieappleton.com/) | 个人简介、知识花园和导航形成统一阅读站；可参考衬线标题、暖色背景和留白 | 已查看桌面首页；下方板块及完整功能待进一步检查 |

用户提供的起点：[收集全网优秀开源个人网站主页代码](https://zhuanlan.zhihu.com/p/336410564)。其中一些演示地址可能已失效或改变，请以当前项目仓库和实际访问为准。

### 同类源码候选

- [penjc/homepage](https://github.com/penjc/homepage)：README 介绍了博客、项目、书单、友链和关于页；本次演示访问未成功，视觉效果待核实。
- [poisonshell/MimicBento](https://github.com/poisonshell/MimicBento)：README 介绍可配置的多尺寸卡片与个人链接模块；本次未运行或确认演示。

---


## 视觉精选：美观、炫酷、有质感

这一组按网站本身的视觉与交互表现挑选，优先观察整体艺术指导、排版、色彩和动态体验。部分案例依赖 WebGL 或动画，建议用桌面浏览器体验；标记“资料参考”的描述来自作品介绍或设计拆解，并非本次完整实测。

| 网站 | 看什么 | 参考依据 |
| --- | --- | --- |
| [Exat Typeface](https://exat.hottype.co/) | 橙色底配超大白色字形，字体本身成为主视觉；看字重、尺度、版面与字体试用器 | 本次查看首页；[CSSDA 2025 最佳 UI](https://www.cssdesignawards.com/blog/2025-website-of-the-year-winners/430/) |
| [Heron AI](https://heronaiapp.com/) | 米色图纸、炭笔建筑、细网格与橙红标记；首页可拖拽框选图纸 | [设计拆解](https://rickcreates.com/r/2026-10-12-heron-ai)；概念展示，并非真实产品 |
| [Lando Norris](https://landonorris.com/) | 人像、头盔与荧光绿形成鲜明身份；关注光标效果和滚动转场 | [设计拆解](https://rickcreates.com/year)，资料参考 |
| [The Symphony of Vines](https://symphonyofvines.unseen.co/) | 电影式场景、空间纵深与滚动叙事，体验画面、声音和节奏的结合 | [项目介绍](https://symphonyofvines.unseen.co/)；[CSSDA 2025 年度前十](https://www.cssdesignawards.com/blog/2025-website-of-the-year-winners/430/) |
| [Dropbox Brand](https://brand.dropbox.com/) | 高饱和色彩、图形、插画和互动结合；观察品牌规范如何变成可探索的视觉体验 | [CSSDA 2025 年度网站](https://www.cssdesignawards.com/blog/2025-website-of-the-year-winners/430/) |
| [Jesper Landberg](https://jesperlandberg.com/) | 黑色空间中的弯曲作品卡片；观察滚动形变、光标反馈和黑洞式转场 | [设计拆解](https://rickcreates.com/r/2026-09-29-jesper-landberg)，资料参考 |
| [Sleep Well Creatives](https://sleep-well-creatives.com/) | 米白与蓝色统一三维插画和文字；观察场景如何像绘本一样衔接 | [设计拆解](https://rickcreates.com/r/2026-02-07-sleep-well-creative)，资料参考 |
| [Igloo Inc](https://igloo.inc/) | 冰雪世界、三维场景和极简线框标签；看滚动镜头与材质氛围 | [设计拆解](https://rickcreates.com/r/2024-07-23-igloo-inc)；文本检索无法读取动态画面 |
| [Lusion](https://lusion.co/) | 三维空间、材质与细致互动；适合研究沉浸式视觉叙事 | 已在旧清单收录；[Lusion v3 拆解](https://rickcreates.com/year)，网站可能已改版 |
| [Bruno Simon](https://bruno-simon.com/) | 把作品集做成可驾驶探索的三维世界；观察场景、镜头与交互 | 已在旧清单收录；[CSSDA 2025 最佳作品集](https://www.cssdesignawards.com/blog/2025-website-of-the-year-winners/430/) |
| [Active Theory](https://activetheory.net/) | 数字空间、三维、动效与沉浸式项目展示 | [案例介绍](https://webcity.design/articles/best-agency-websites)；文本检索提示需要 JavaScript |
| [BASIC/DEPT®](https://www.basicagency.com/) | 大字、作品画面与品牌化编辑版式的组合 | [案例介绍](https://webcity.design/articles/best-agency-websites)，资料参考 |
| [BUCK](https://buck.co/) | 动画、插画与品牌视觉作品的表达 | [案例介绍](https://webcity.design/articles/best-agency-websites)，资料参考 |
| [COLLINS](https://wearecollins.com/) | 品牌故事、排版和精选项目的编辑式呈现 | [案例介绍](https://webcity.design/articles/best-agency-websites)，资料参考 |

> 视觉精选是审美参考，不代表直接照搬整站。优先借鉴具体的配色、构图、字体、动效节奏和交互逻辑，再结合目标网站实际需求调整。

---


收集日期：2026-10-30。用于查找视觉、信息组织和交互方面的参考；网站可能随时间改版，具体效果以当前页面为准。以下是建议观察的方向，并非可用性或无障碍验收结论。

## 产品与工具网站

| 网站 | 类型 | 值得观察 |
| --- | --- | --- |
| [Stripe](https://stripe.com/) | 金融产品 | 信息层级、复杂产品的模块化介绍、开发者内容与营销页面的衔接 |
| [Linear](https://linear.app/) | 项目管理 | 深色界面、文字层级、产品画面与功能叙述 |
| [Vercel](https://vercel.com/) | 开发工具 | 黑白基调、网格、技术信息的呈现方式 |
| [Notion](https://www.notion.com/) | 知识与协作 | 多使用场景组织、产品演示与插画的结合 |
| [Figma](https://www.figma.com/) | 设计协作 | 色彩、品牌表达及产品功能展示 |
| [Framer](https://www.framer.com/) | 网站制作 | 产品能力的直观展示、交互与页面节奏 |
| [Supabase](https://supabase.com/) | 开发者平台 | 技术产品页面、代码与功能卡片的组合 |
| [Anthropic](https://www.anthropic.com/) | AI | 温暖的中性色、编辑式排版及品牌表达 |
| [Apple](https://www.apple.com/) | 消费电子 | 产品摄影、大标题、内容分区与行动入口 |

## 内容、阅读与品牌

| 网站 | 类型 | 值得观察 |
| --- | --- | --- |
| [Making Software](https://www.makingsoftware.com/) | 技术内容 | 长文与图解结合，适合知识内容的组织参考；本次检索访问受限 |
| [The Pudding](https://pudding.cool/) | 数据故事 | 图文叙事和数据可视化的衔接 |
| [Pentagram](https://www.pentagram.com/) | 设计机构 | 项目网格、案例内容和图像编排 |
| [Wolff Olins](https://www.wolffolins.com/) | 品牌设计 | 编辑式布局和品牌案例叙述 |
| [Readymag](https://readymag.com/) | 创意工具 | 版式表达及创意案例展示 |
| [Aperture](https://aperture.org/) | 摄影与出版 | 图片、文章与出版内容的组织 |
| [Walker Art Center](https://walkerart.org/) | 艺术机构 | 展览、活动和编辑内容的组织 |
| [Dezeen](https://www.dezeen.com/) | 设计媒体 | 多栏目内容、文章列表和图片密集型页面 |

## 创意与互动展示

| 网站 | 类型 | 值得观察 |
| --- | --- | --- |
| [Lusion](https://lusion.co/) | 创意工作室 | 沉浸式视觉和互动呈现；参考时留意加载和性能成本 |
| [Bruno Simon](https://bruno-simon.com/) | 个人作品集 | 游戏化交互与作品展示；参考时留意操作门槛 |
| [Locomotive](https://locomotive.ca/) | 数字创意工作室 | 动效、作品集和页面转场 |
| [Spring/Summer](https://springsummer.dk/) | 创意机构 | 编辑式视觉、案例列表和排版 |

## 持续发现参考的网站

- [Siteinspire](https://www.siteinspire.com/)：按风格、类型和主题查找网站。
- [Lapa Ninja](https://www.lapa.ninja/)：按行业、颜色和页面类型寻找落地页。
- [Awwwards](https://www.awwwards.com/)：查找获奖网站、创意交互和设计案例。
- [CSS Design Awards](https://www.cssdesignawards.com/)：查看网站设计奖项与案例。
- [A1 Gallery：编辑式设计](https://www.a1.gallery/style/editorial)：查找内容型和杂志式页面。
- [TypeScale](https://typescale.app/typescales)：参考网站字号层级及字体系统；具体数据需要在目标页面重新核实。

## 参考来源

- [软件网站设计案例](https://rankite.com/blog/best-software-company-websites)
- [网站设计语言参考库](https://styles.talkdedsec.com/en/references)
- [编辑式网站案例](https://upvote.seojack.net/style/editorial)
- [创意网站示例](https://www.youtube.com/watch?v=RGWXVbkrYKM)

使用时优先根据项目内容、受众和功能选择参考，关注可读性、移动端、性能与键盘操作；视觉形式需要结合实际体验判断。


## 扩充：科研与单细胞

| 网站 | 适合参考的方向 |
| --- | --- |
| [Human Cell Atlas](https://www.humancellatlas.org/) | 跨机构研究计划的介绍、社区和资源入口；适合单细胞项目参考 |
| [Broad Institute](https://www.broadinstitute.org/) | 大型研究机构如何组织研究方向、成果和新闻 |
| [Allen Institute](https://alleninstitute.org/) | 科研团队、开放科学资源与研究故事的组织 |
| [EMBL-EBI](https://www.ebi.ac.uk/) | 生物信息资源门户的搜索、数据入口与分类 |
| [NHGRI](https://www.genome.gov/) | 基因组研究、科普与资源入口；可观察阅读辅助选项 |
| [eLife](https://elifesciences.org/) | 学术文章列表、检索和研究内容阅读入口 |
| [Nature](https://www.nature.com/) | 期刊栏目、论文、新闻和搜索入口的组织 |

## 扩充：数据可视化与互动叙事

| 网站 | 适合参考的方向 |
| --- | --- |
| [Our World in Data](https://ourworldindata.org/) | 按主题组织数据、文章和图表；适合数据密集型知识站 |
| [Gapminder](https://www.gapminder.org/) | 用互动工具和教学内容解释宏观数据 |
| [Observable](https://observablehq.com/) | 数据笔记本、可视化案例与代码的结合 |
| [FlowingData](https://flowingdata.com/) | 图表故事、案例索引和可视化学习资源 |
| [Information is Beautiful](https://informationisbeautiful.net/) | 信息图表、视觉化专题和项目归档 |
| [Neal.fun](https://neal.fun/) | 独立互动作品的入口、趣味叙事与参与感 |

## 扩充：科学写作与阅读

| 网站 | 适合参考的方向 |
| --- | --- |
| [Distill](https://distill.pub/) | 机器学习文章中的图解、正文与交互式解释；历史文章可作为参考 |
| [Quanta Magazine](https://www.quantamagazine.org/) | 科学报道的主题导航、插图和长文叙事 |
| [Aeon](https://aeon.co/) | 长文阅读、封面图片与专题栏目组织 |
| [Readwise](https://readwise.io/) | 阅读内容、摘录和产品介绍之间的关系 |
| [It's Nice That](https://www.itsnicethat.com/) | 创意媒体的多栏目导航、文章列表和图片编排 |
| [Are.na](https://www.are.na/) | 跨媒介素材收藏、内容集合及发现路径 |

## 扩充：产品与开发工具

| 网站 | 适合参考的方向 |
| --- | --- |
| [Raycast](https://www.raycast.com/) | 通过键盘视觉与功能示例传达效率工具的特点 |
| [Resend](https://resend.com/) | 开发者产品的功能说明、代码与文档入口 |
| [Attio](https://attio.com/) | 复杂 SaaS 产品的功能导航、演示和场景组织 |
| [Cursor](https://cursor.com/) | 开发工具的产品叙述、下载入口和技术内容 |

## 扩充：电商与生活方式

| 网站 | 适合参考的方向 |
| --- | --- |
| [Peak Design](https://www.peakdesign.com/) | 产品分类、使用场景、产品内容与品牌故事 |
| [Aesop](https://www.aesop.com/) | 商品分类、文字风格和品牌呈现；本次检索显示部分功能受限 |
| [Patagonia](https://www.patagonia.com/) | 商品目录、户外故事与品牌议题的衔接 |
| [MUJI](https://www.muji.com/) | 多品类商品、导航和产品列表的信息组织 |
| [Allbirds](https://www.allbirds.com/) | 商品分类、图片、材质说明与品牌内容 |
| [HAY](https://www.hay.com/) | 家居产品、设计师与品牌内容的呈现 |

## 扩充：文化与展览

| 网站 | 适合参考的方向 |
| --- | --- |
| [MoMA](https://www.moma.org/) | 展览、藏品、活动和访问入口的组织 |
| [Rijksmuseum](https://www.rijksmuseum.nl/) | 博物馆藏品、参观信息和内容探索 |

## 本轮发现来源与使用说明

- [SaaS 网站设计参考](https://www.regards.design/websites/saas)：查找产品展示和 SaaS 网站案例。
- [Web Stylebook](https://webstylebook.com/references)：按产品、技术、内容、电商等类别查找案例。
- [Framer Gallery](https://www.framer.com/community/gallery/)：按行业与页面类型查找网站。
- [编辑与出版网站案例](https://websitedesignawards.com/category/editorial)：继续查找内容和出版设计。
- [交互新闻案例清单](https://github.com/wbkd/awesome-interactive-journalism)：查找数据叙事和交互报道。

本轮主要通过公开页面和检索资料筛选；以上为具体观察方向，不代表已逐项完成视觉、移动端、性能、无障碍或交互体验验收。网站可能改版或存在地区、脚本限制。
