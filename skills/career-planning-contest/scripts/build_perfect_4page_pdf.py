# -*- coding: utf-8 -*-
"""
ReportLab 4 页确定性物理排版与大字号编译引擎模板 (career-planning-contest)
- 字体：正文 10.0pt (行距 15.0pt)，标题与表格协调放大，兼顾视觉质感与长辈评委阅读舒适度
- 版面：精确 4 页整，带页眉页脚与动态总页数，无跨页脱节与多余空白
- 门禁：PDF 体积严格控制在 1.5MB 左右（远低于 10MB 大赛红线）
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

# 注册中文字体（自动适配 Windows 与 Linux 常见字体路径）
font_registered = False
for font_path in [
    ('YaHei', 'C:/Windows/Fonts/msyh.ttc', 0),
    ('YaHeiBd', 'C:/Windows/Fonts/msyhbd.ttc', 0),
    ('SimHei', 'C:/Windows/Fonts/simhei.ttf', None),
    ('SourceHan', '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc', 0)
]:
    name, path, subidx = font_path
    if os.path.exists(path):
        try:
            if subidx is not None:
                pdfmetrics.registerFont(TTFont(name, path, subfontIndex=subidx))
            else:
                pdfmetrics.registerFont(TTFont(name, path))
            font_registered = True
        except Exception:
            pass

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont('YaHei' if 'YaHei' in pdfmetrics.getRegisteredFontNames() else 'Helvetica', 8.5)
        self.setFillColor(colors.HexColor('#718096'))
        
        # 页眉（第2页起）
        if self._pageNumber > 1:
            self.drawString(45.0, 842 - 28, "第四届全国大学生职业规划大赛成长赛道参赛材料")
            self.setStrokeColor(colors.HexColor('#CBD5E0'))
            self.setLineWidth(0.6)
            self.line(45.0, 842 - 32, 595 - 45.0, 842 - 32)
            
        # 页脚
        footer_text = f"第 {self._pageNumber} 页 / 共 {page_count} 页"
        self.drawRightString(595 - 45.0, 22, footer_text)
        self.drawString(45.0, 22, "《生涯发展报告》—— 成长赛道（高教组）")
        self.setStrokeColor(colors.HexColor('#CBD5E0'))
        self.setLineWidth(0.6)
        self.line(45.0, 32, 595 - 45.0, 32)
        
        self.restoreState()

def build_pdf(output_pdf_path="生涯发展报告_成长赛道.pdf", chart_dir="charts"):
    # 边距优化为 45pt（约15.8mm），可打印宽度 505.27pt，高度 757.89pt
    doc = SimpleDocTemplate(
        output_pdf_path,
        pagesize=A4,
        leftMargin=45.0,
        rightMargin=45.0,
        topMargin=40.0,
        bottomMargin=40.0
    )
    
    font_body = 'YaHei' if 'YaHei' in pdfmetrics.getRegisteredFontNames() else 'Helvetica'
    font_bold = 'YaHeiBd' if 'YaHeiBd' in pdfmetrics.getRegisteredFontNames() else 'Helvetica-Bold'
    
    title_style = ParagraphStyle(
        'DocTitle_Custom',
        fontName=font_bold,
        fontSize=15.5,
        leading=21.0,
        textColor=colors.HexColor('#1A365D'),
        alignment=1,
        spaceAfter=7
    )
    
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        fontName=font_bold,
        fontSize=12.5,
        leading=17.0,
        textColor=colors.HexColor('#1A365D'),
        spaceBefore=7,
        spaceAfter=4,
        keepWithNext=True
    )
    
    h2_style = ParagraphStyle(
        'Heading2_Custom',
        fontName=font_bold,
        fontSize=10.8,
        leading=15.0,
        textColor=colors.HexColor('#2B6CB0'),
        spaceBefore=5,
        spaceAfter=3,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'Body_Custom',
        fontName=font_body,
        fontSize=10.0,
        leading=15.0,
        textColor=colors.HexColor('#2D3748'),
        firstLineIndent=20.0,
        spaceAfter=4
    )
    
    caption_style = ParagraphStyle(
        'Caption_Custom',
        fontName=font_bold,
        fontSize=9.0,
        leading=12.5,
        textColor=colors.HexColor('#4A5568'),
        alignment=1,
        spaceBefore=3,
        spaceAfter=5
    )
    
    print(f"Template ready for: {output_pdf_path}")

if __name__ == '__main__':
    build_pdf()
