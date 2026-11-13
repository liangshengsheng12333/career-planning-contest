# -*- coding: utf-8 -*-
"""
标准 5 张高质感信息图表生成器模板 (career-planning-contest)
- 图1: 霍兰德代码(IRC)与个人综合胜任力雷达图 (极坐标正圆无畸变，下置图例防遮挡)
- 图2: 目标岗位胜任力 GAP 差距量化靶向图 (横向柱状图，X轴扩容至118，顶置图例防碰撞)
- 图3: 大学四年“阶梯赋能”实践成长行动与成果甘特图 (学历口径统一为硕士深造/秋招Offer)
- 图4: 工业端侧模型落地技术瓶颈与动态优化闭环图 (严谨工业级 INT8 PTQ/QAT 混合精度量化)
- 图5: 生涯动态进化 PDCA 机制与大四秋招熔断双轨预案树 (FancyArrowPatch顺时针弧形闭环箭头)
"""
import os
import matplotlib.pyplot as plt
import numpy as np

# 设置跨平台中文字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'DejaVu Sans', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300

def make_chart_1(output_dir="charts"):
    categories = ['数理与算法逻辑\n(Investigative)', '动手与工程实操\n(Realistic)', 
                  '规范与严谨求实\n(Conventional)', '技术攻坚与钻研\n(Specialized)', 
                  '团队协作与沟通\n(Collaborative)', '产业洞察敏锐度\n(Industry Acumen)']
    N = len(categories)
    values_student = [92, 85, 88, 90, 84, 82]
    values_target = [95, 92, 90, 94, 88, 88]
    
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    values_student += values_student[:1]
    values_target += values_target[:1]
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(6.2, 5.2), subplot_kw=dict(polar=True))
    plt.xticks(angles[:-1], categories, color='#1A365D', size=9.5, weight='bold')
    ax.tick_params(pad=14)
    ax.set_rlabel_position(30)
    plt.yticks([60, 70, 80, 90, 100], ["60", "70", "80", "90", "100"], color="#718096", size=8)
    plt.ylim(50, 100)
    
    ax.plot(angles, values_target, linewidth=2, linestyle='dashed', color='#A0AEC0', label='目标岗位胜任力基线')
    ax.fill(angles, values_target, '#CBD5E0', alpha=0.35)
    
    ax.plot(angles, values_student, linewidth=2.5, linestyle='solid', color='#2B6CB0', label='大二个人综合自评')
    ax.fill(angles, values_student, '#3182CE', alpha=0.45)
    
    plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.16), ncol=2, frameon=True, fontsize=8.5)
    plt.tight_layout()
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, "chart1_holland_competency.png"), bbox_inches='tight')
    plt.close()
    print("Chart 1 generated successfully.")

def make_chart_2(output_dir="charts"):
    dimensions = [
        '算法理论与深度学习基础',
        '模型端侧量化剪枝与轻量化 (核心突破点)',
        '嵌入式异构算力部署 (RK3588/Jetson)',
        '工业端侧实时质检项目实操',
        '工程化架构与团队协同规范'
    ]
    current = [88, 72, 68, 70, 78]
    target = [95, 92, 90, 88, 85]
    gap = [t - c for t, c in zip(target, current)]
    
    y = np.arange(len(dimensions))
    height = 0.35
    fig, ax = plt.subplots(figsize=(8.0, 3.8))
    
    ax.barh(y - height/2, current, height, label='当前大二储备水平', color='#4299E1', alpha=0.9)
    ax.barh(y + height/2, target, height, label='目标岗位胜任力要求', color='#1A365D', alpha=0.9)
    
    for i in range(len(dimensions)):
        ax.text(target[i] + 1.2, i, f'GAP: -{gap[i]}分', va='center', ha='left', 
                color='#C53030', weight='bold', fontsize=8.5,
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#FFF5F5', edgecolor='#FEB2B2', alpha=0.9))
        
    ax.set_xlabel('胜任力综合评估分 (满分100)', fontsize=9.5, weight='bold', color='#2D3748')
    ax.set_yticks(y)
    ax.set_yticklabels(dimensions, fontsize=9, weight='bold', color='#2D3748')
    ax.set_xlim(50, 118)
    ax.grid(axis='x', linestyle='--', alpha=0.5)
    ax.legend(loc='lower center', bbox_to_anchor=(0.5, 1.02), ncol=2, frameon=True, fontsize=8.5)
    plt.tight_layout()
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, "chart2_competency_gap.png"), bbox_inches='tight')
    plt.close()
    print("Chart 2 generated successfully.")

def make_chart_3(output_dir="charts"):
    stages = [
        "大一：通识与代码筑基期\n扎实数理 / 编程基础优异",
        "大二(当前)：工程突破与定向\n课题组助研 / 边缘部署攻坚",
        "大三：产学研融通与实战\n进驻信创联合基地 / 产线项目",
        "大四：毕设深耕与顶峰深造\n工业边缘AI毕设 / 硕士深造/算法岗"
    ]
    fig, ax = plt.subplots(figsize=(8.8, 3.8))
    ax.axis('off')
    
    ax.annotate('', xy=(8.7, 1.3), xytext=(0.3, 1.3),
                arrowprops=dict(arrowstyle="->", color="#1A365D", lw=3.0, mutation_scale=18))
    
    colors = ['#4299E1', '#3182CE', '#2B6CB0', '#1A365D']
    box_x = [1.2, 3.4, 5.6, 7.8]
    milestones = [
        "核心课高分 | 编程基础扎实\n万行代码沉淀 | 确立AI志向",
        "课题组学生助研 | 掌握TensorRT\n高阶算法研习 | 原型验证",
        "校企联合产学研基地实训\n工业多模态课题 | 产线联调",
        "端侧工业大模型软硬落地\n攻读人工智能硕士 / 核心算法Offer"
    ]
    
    for i in range(4):
        ax.plot(box_x[i], 1.3, marker='o', markersize=13, color=colors[i], markeredgecolor='white', markeredgewidth=2)
        ax.text(box_x[i], 1.3, str(i+1), color='white', weight='bold', ha='center', va='center', fontsize=8.5)
        ax.text(box_x[i], 2.1, stages[i], ha='center', va='center', fontsize=8, weight='bold', color='#1A365D',
                bbox=dict(boxstyle='round,pad=0.35', facecolor='#EBF8FF', edgecolor='#90CDF4', lw=1.2))
        ax.text(box_x[i], 0.5, milestones[i], ha='center', va='center', fontsize=7.5, color='#2D3748',
                bbox=dict(boxstyle='square,pad=0.35', facecolor='#F7FAFC', edgecolor='#E2E8F0', lw=1))
        ax.plot([box_x[i], box_x[i]], [1.65, 1.4], color=colors[i], linestyle=':', lw=1.5)
        ax.plot([box_x[i], box_x[i]], [1.2, 0.9], color=colors[i], linestyle=':', lw=1.5)

    ax.set_xlim(0, 9.2)
    ax.set_ylim(0.0, 2.7)
    plt.tight_layout()
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, "chart3_milestone_roadmap.png"), bbox_inches='tight')
    plt.close()
    print("Chart 3 generated successfully.")

def make_chart_4(output_dir="charts"):
    fig, ax = plt.subplots(figsize=(9.2, 2.7), dpi=300)
    ax.axis('off')
    
    ax.text(1.2, 1.0, "【初期遭遇瓶颈】\n\n• 显存受限: 边缘板卡仅8GB\n• 延迟过高: 推理耗时 >260ms\n• 精度要求: 工业容错极严苛\n• 散热功耗: 严苛车间环境", 
            ha='center', va='center', fontsize=8.5, color='#742A2A',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFF5F5', edgecolor='#FEB2B2', lw=1.5))
    
    ax.annotate('', xy=(2.7, 1.0), xytext=(2.1, 1.0),
                arrowprops=dict(arrowstyle="->", color="#E53E3E", lw=2.2))
    ax.text(2.4, 1.25, "技术反思\n方案重构", ha='center', va='center', fontsize=7.8, color='#C53030', weight='bold')

    ax.text(4.2, 1.0, "【轻量化攻坚闭环】\n\n1. 知识蒸馏 (Teacher-Student)\n2. INT8 PTQ/QAT 混合精度量化\n3. 算子融合与硬件加速编译\n4. TensorRT/ONNX 异构加速", 
            ha='center', va='center', fontsize=8.5, color='#2A4365',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#EBF8FF', edgecolor='#63B3ED', lw=1.5))

    ax.annotate('', xy=(6.3, 1.0), xytext=(5.7, 1.0),
                arrowprops=dict(arrowstyle="->", color="#3182CE", lw=2.2))
    ax.text(6.0, 1.25, "成效达成\n指标蜕变", ha='center', va='center', fontsize=7.8, color='#2B6CB0', weight='bold')

    ax.text(7.6, 1.0, "【阶段性验证成效】\n\n• 模型显存占用: 降低 72%\n• 工业端侧延迟: 压缩至 32ms\n• 缺陷检测召回率: 保持 99.6%\n• 产出: 软著在审+大创优质推进", 
            ha='center', va='center', fontsize=8.5, color='#22543D',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#F0FFF4', edgecolor='#9AE6B4', lw=1.5))

    ax.set_xlim(0, 9.0)
    ax.set_ylim(0.1, 1.9)
    plt.tight_layout()
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, "chart4_dynamic_optimization.png"), bbox_inches='tight')
    plt.close()
    print("Chart 4 generated successfully.")

def make_chart_5(output_dir="charts"):
    from matplotlib.patches import FancyArrowPatch
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 2.75), gridspec_kw={'width_ratios': [1.02, 1.15]})
    
    ax1.axis('off')
    pdca_nodes = [
        ("Plan 目标规划", "锁定工业边缘AI志向\n细化年度学业与竞赛标的", 0.5, 0.88, '#3182CE'),
        ("Do 躬行实践", "课题组助研与算法研习\n深入滨海信创生态实训", 0.88, 0.5, '#2B6CB0'),
        ("Check 反思检视", "定期对照胜任力模型评估\n查摆工程部署与算力瓶颈", 0.5, 0.12, '#D69E2E'),
        ("Act 迭代改进", "优化技术栈、重构学习路径\n产学研导师双向督导赋能", 0.12, 0.5, '#38A169')
    ]
    
    for title, desc, x, y, col in pdca_nodes:
        ax1.text(x, y, f"{title}\n{desc}", ha='center', va='center', fontsize=7.6,
                 bbox=dict(boxstyle='round,pad=0.25', facecolor='#FFFFFF', edgecolor=col, lw=1.3))
    
    ax1.text(0.5, 0.5, "生涯持续\n进化核心\n(PDCA)", ha='center', va='center', fontsize=8.5, weight='bold', color='#1A365D',
             bbox=dict(boxstyle='circle,pad=0.25', facecolor='#EDF2F7', edgecolor='#CBD5E0', lw=1))
    
    arrows_data = [
        ((0.68, 0.82), (0.85, 0.65), '#3182CE'),  # Plan -> Do
        ((0.85, 0.35), (0.68, 0.18), '#2B6CB0'),  # Do -> Check
        ((0.32, 0.18), (0.15, 0.35), '#D69E2E'),  # Check -> Act
        ((0.15, 0.65), (0.32, 0.82), '#38A169'),  # Act -> Plan
    ]
    for pA, pB, col in arrows_data:
        arrow = FancyArrowPatch(posA=pA, posB=pB, connectionstyle="arc3,rad=-0.22",
                                arrowstyle="->", mutation_scale=12, color=col, lw=1.6,
                                shrinkA=4, shrinkB=4)
        ax1.add_patch(arrow)
        
    ax1.set_xlim(-0.1, 1.1)
    ax1.set_ylim(-0.1, 1.1)

    ax2.axis('off')
    ax2.text(0.08, 0.5, "职业目标决策锚点\n【大四9月】\n推免/秋招熔断", ha='center', va='center', fontsize=7.8, weight='bold', color='#1A365D',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#E2E8F0', edgecolor='#A0AEC0', lw=1.2))
    
    ax2.annotate('', xy=(0.38, 0.78), xytext=(0.24, 0.58),
                 arrowprops=dict(arrowstyle="->", color="#3182CE", lw=1.8))
    ax2.text(0.68, 0.8, "【最优路径 A · 85%概率】\n高水平保研 / 考研深造\n进入高校智能计算重点实验室\n攻读工业具身智能与大模型硕士", 
             ha='center', va='center', fontsize=7.2, color='#1A365D',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#EBF8FF', edgecolor='#63B3ED', lw=1.2))
    
    ax2.annotate('', xy=(0.38, 0.22), xytext=(0.24, 0.42),
                 arrowprops=dict(arrowstyle="->", color="#38A169", lw=1.8, linestyle='--'))
    ax2.text(0.68, 0.2, "【稳健路径 B · 15%预案】\n9-10月秋招锁定信创SP Offer托底\n直通滨海高新区国家级信创龙头\n(飞腾/麒麟生态)任端侧算法工程师", 
             ha='center', va='center', fontsize=7.2, color='#22543D',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#F0FFF4', edgecolor='#9AE6B4', lw=1.2))

    ax2.set_xlim(0, 1.1)
    ax2.set_ylim(0, 1.0)
    plt.tight_layout()
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, "chart5_pdca_career_tree.png"), bbox_inches='tight')
    plt.close()
    print("Chart 5 generated successfully.")

if __name__ == '__main__':
    make_chart_1()
    make_chart_2()
    make_chart_3()
    make_chart_4()
    make_chart_5()
    print("All 5 standard charts generated cleanly!")
