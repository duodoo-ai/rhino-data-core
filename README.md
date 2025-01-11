# OpenCoze，中文名称开源扣子。

#### 介绍
OpenCoze，中文名称开源扣子。一个开源的企业 ERP + MES 系统。

借助开源手段，通过一站式数字化套件系统，助力企业实现内外部管理各环节、各用户之间的紧密协作。

项目开源方式：

#### tone_master  外部开源模块

#### tone_good    内部开源模块

#### tone_better  待开源模块（MES核心模块、数采核心模块、WMS核心模块，客户供应商门户）

项目构成：供应链（采购、销售、库存），WMS模块、MES模块、供应商平台、财务模块

项目底座版本Odoo18.0。

#### 软件架构（多层架构模式）

 **展现层** ：负责与用户直接交互，提供直观友好的操作界面。它涵盖了丰富多样的前端组件，基于现代 Web 技术构建，如 HTML5、CSS3 和 JavaScript 框架（通常为 Vue.js 或 React 等），确保用户在使用诸如销售管理、库存监控、财务管理等模块时，能够流畅地进行数据录入、查询与业务流程操作，适配不同终端设备，无论是桌面电脑还是移动设备，都能提供一致且便捷的体验。

 **业务逻辑层** ：犹如 Odoo 的 “大脑中枢”，承载着核心业务规则与流程处理逻辑。这里运用 Python 语言编写大量业务代码，紧密围绕企业运营各环节，像订单处理流程从生成、审核到发货的一系列复杂逻辑，以及库存自动补货规则的精准运算等，通过精心设计的模块与类，将业务流程转化为可执行、可管理的代码单元，协调展现层与数据持久层的数据交互，保障系统运行符合企业实际业务流程。

 **数据持久层** ：负责与数据库打交道，确保数据的安全存储与高效检索。Odoo 18 支持多种主流数据库，如 PostgreSQL（与前文 OpenCoze 所选用数据库相同，以其强大事务处理和扩展性备受青睐），数据持久层利用 SQLAlchemy 等 ORM（对象关系映射）工具，将 Python 对象与数据库表结构无缝映射，开发人员无需编写繁琐原生 SQL 语句，就能便捷地进行数据的增删改查操作，比如快速保存新客户信息、更新销售订单状态、查询库存数量等，为上层业务逻辑提供坚实的数据支撑。

 **核心模块** ：涵盖了企业基本管理功能，如人力资源管理（员工信息、考勤、薪资核算）、财务管理（总账、应收应付、财务报表生成）、销售与采购管理（客户订单管理、供应商采购流程）等，这些模块构成企业运营管理的 “骨架”，彼此通过标准接口交互，例如销售订单确认后自动触发库存模块的预留与财务模块的应收款项记录生成。

 **行业特定模块** ：针对不同行业特性，Odoo 18 拓展出一系列专用模块，制造业有生产管理模块（生产排程、物料需求计划、质量控制与追溯），类似于 OpenCoze 聚焦 MES 功能；对于电商行业则配备电商平台对接模块（网店订单同步、线上支付集成、物流信息跟踪），满足特定行业精细化管理需求，企业可按需选择、安装与定制这些模块，无缝融入现有核心系统，快速搭建适配自身行业的信息化解决方案。

 **第三方插件与社区模块** ：Odoo 开放的架构吸引全球开发者社区贡献海量第三方插件，进一步丰富功能生态。这些插件从增强用户界面交互效果到拓展新业务功能，如客户关系管理的高级营销自动化插件、物流配送优化插件等，企业可通过 Odoo 官方应用商店或社区论坛轻松获取并集成，以低成本实现系统功能的个性化升级。


#### 安装教程

1.  xxxx
2.  xxxx
3.  xxxx

#### 使用说明

1.  xxxx
2.  xxxx
3.  xxxx

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)


#### 微信群运营：【OpenCoze开源俱乐部】
![contect.jpg](contect.jpg)
