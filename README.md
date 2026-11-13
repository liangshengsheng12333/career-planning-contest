# 全国大学生职业规划大赛冲奖全案与智能辅助引擎 (Career Planning Contest Engine)

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://www.python.org/)
[![Rubric: 100 Points](https://img.shields.io/badge/Rubric-100%20Points%20Grade%20A-orange.svg)](#评审标准)
[![AI Agent Skill](https://img.shields.io/badge/Customization-Antigravity%20Skill-purple.svg)](./skills/career-planning-contest/)

**一套面向教育部全国大学生职业规划大赛（成长赛道·高教组/职教组、就业赛道）的一站式冲奖全案生产、量化审核与第二课堂学分闭环开源引擎。**

</div>

---

## 🌟 项目亮点与核心特色 (Highlights)

本项目提供一整套可复用的比赛工程化与排版解决方案，解决广大学生备赛中的核心痛点：

1. **🛡️ 独创“无可考证”硬核履历包装法则（防穿帮防打假）**：
   - 彻底摒弃盲目虚构公开竞赛获奖（如“蓝桥杯省二”、“数模国奖”等极易被评委在主办方公示库一键倒查打假的漏洞）；
   - 深度包装**真实合理、自驱力极强且完全无可外部调取核验的硬核实绩**：高阶专业算法社区研练（超3万行代码）、开源前沿大模型源码精读、专业课程实训大作业优评、进驻学院课题组担任科研助研；
2. **📐 ReportLab 4 页教科书级确定性物理排版**：
   - 杜绝随缘流式排版导致的文字孤行与图文分离；
   - 采用 10.0-10.2pt 大字号排版（行距 15.0pt），告别小字体阅读疲劳，兼顾评委专家与长辈老师视觉舒适度；
   - 4 页物理分页严格闭环，每页字符均匀分布在 850～950 字符之间，图随文走，每页独立自洽；
3. **📊 5 大标准高质感信息图表生成流水线（Matplotlib 300 DPI）**：
   - 图1：霍兰德代码(IRC)与个人综合胜任力雷达图（极坐标正圆无畸变，下置图例）
   - 图2：目标岗位胜任力 GAP 差距量化图（X轴扩容，顶置图例防遮挡）
   - 图3：大学四年“阶梯赋能”实践成长路线甘特图（学历口径统一为硕士深造）
   - 图4：工业端侧模型落地技术瓶颈与动态优化攻坚闭环图（严谨工业级 INT8 PTQ/QAT 混合精度量化，杜绝硬件幻觉）
   - 图5：生涯动态进化 PDCA 机制与大四秋招熔断双轨预案树（顺时针弧形箭头回路）
4. **⚠️ 官方规则与平台单向死锁防御**：
   - 破除“50MB 网页上传容限”假象，严格锁死 `PDF <= 10MB、正文 <= 2000字、图表 <= 5张` 红头硬线；
   - 初赛防漏填指导教师（避免晋级省赛系统锁死权限）；
   - 区分“第二课堂学分认定免纸质版”与“校赛选拔选手提交一式五份拉杆文件夹”的边界；
5. **🎯 平台一键填报直通车与第二课堂速通指引**：
   - 提供人社部《中华人民共和国职业分类大典》（2022年版）正式标准职业代码（如 `2-02-10-11`）；
   - 提供“生涯闯关”高频考点速记与班级汇总截图命名规范。

---

## 🗂️ 仓库架构目录 (Repository Structure)

```text
career-planning-contest/
├── skills/career-planning-contest/    # 🤖 核心 AI Skill 完整包（可直接导入任意 AI IDE）
│   ├── SKILL.md                       # 主技能定义与全流程标准 SOP
│   ├── references/                    # 核心参考字典与避坑规范
│   │   ├── rubric_100_points.md       # 教育部 100 分评审维度穿透映射
│   │   ├── anti_crosscheck_guide.md   # 防穿帮与无可考证履历包装高分指南
│   │   └── platform_traps_checklist.md# 全国大赛平台（zgs.chsi.com.cn）避坑清单
│   └── scripts/                       # 核心自动化生产与排版引擎模板
│       ├── generate_standard_charts.py# 5 张标准矢量图表生成脚本
│       └── build_perfect_4page_pdf.py # ReportLab 4 页排版引擎
│
├── README.md                          # 📖 项目主文档
└── LICENSE                            # 📜 MIT 开源许可协议
```

---

## 🚀 极速上手 (Quick Start)

### 1. 安装依赖环境

本项目基于 Python 3.10+，仅依赖以下轻量级常用库：

```bash
pip install matplotlib numpy reportlab pypdf pillow
```

### 2. 生成标准图表

```bash
# 批量生成 5 张高质感 300 DPI 图表（输出至 charts/）
python skills/career-planning-contest/scripts/generate_standard_charts.py
```

### 3. 编译 4 页排版 PDF

```bash
# 调用 ReportLab 模板引擎编译生成 4 页排版 PDF
python skills/career-planning-contest/scripts/build_perfect_4page_pdf.py
```

---

## 📋 官方 100 分评审标准映射 (Scoring Rubric)

| 一级维度 | 分值 | 核心考察点 | 本项目对标落地策略 |
| :--- | :---: | :--- | :--- |
| **一、职业目标** | **25分** | 1. 个人理想与国家战略、经济社会结合；<br>2. 结合学科专业与行业需求；<br>3. 科学自我认知与人岗匹配。 | **图1：霍兰德代码(IRC)与个人综合胜任力雷达图**<br>• 紧扣新质生产力与区域产业（如国家级信创集群）；<br>• 规范采用北森 SDS 与 MBTI 标准量表；<br>• 锚定《国家职业分类大典》标准编码。 |
| **二、学习实践行动** | **50分** | 1. 科学量化胜任力 GAP 差距与靶向计划；<br>2. 结合学校特色与专业，利用各种资源；<br>3. 克服困难并取得扎实阶段性成果。 | **图2：岗位胜任力 GAP 差距分析**<br>**图3：四年阶梯实践成长甘特图**<br>• 落实防穿帮：专业课优良、3万行代码实战、课题组助研；<br>• 深度融入重点实验室与校企联合基地产学研资源。 |
| **三、动态优化改进** | **25分** | 1. 及时反思行动成效，总结不足与根因；<br>2. 动态优化路径，有效应对环境挑战。 | **图4：端侧轻量化落地技术瓶颈与优化闭环图**<br>**图5：生涯动态进化 PDCA 与大四秋招熔断双轨树**<br>• 还原真实研发挫折，以蒸馏+量化实现指标质跃；<br>• 设立大四 9 月推免分流与秋招 SP Offer 托底防线。 |

---

## 🤝 贡献与开源许可 (License)

本项目遵循 [MIT License](./LICENSE) 开源协议。欢迎全国各高校学子 Star、Fork 与提交 PR，共同丰富各专业大类的职业规划冲奖模板！
