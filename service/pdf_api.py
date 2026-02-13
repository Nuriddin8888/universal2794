# service/pdf_api.py

import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import A4


def create_pdf(file_name: str, title: str, content_list: list):

    if not file_name.endswith(".pdf"):
        file_name += ".pdf"

    # Uzbek font (arial.ttf project ichida bo‘lishi kerak)
    pdfmetrics.registerFont(TTFont("Arial", "arial.ttf"))

    doc = SimpleDocTemplate(file_name, pagesize=A4)
    elements = []

    title_style = ParagraphStyle(
        name="TitleStyle",
        fontName="Arial",
        fontSize=20,
        leading=24,
        textColor=colors.black,
        spaceAfter=20
    )

    normal_style = ParagraphStyle(
        name="NormalStyle",
        fontName="Arial",
        fontSize=12,
        leading=15,
        textColor=colors.black
    )

    bold_style = ParagraphStyle(
        name="BoldStyle",
        fontName="Arial",
        fontSize=14,
        leading=18,
        textColor=colors.black
    )

    elements.append(Paragraph(f"<b>{title}</b>", title_style))
    elements.append(Spacer(1, 0.4 * inch))

    for item in content_list:
        if item["type"] == "text":
            elements.append(Paragraph(item["data"], normal_style))
            elements.append(Spacer(1, 0.3 * inch))

        elif item["type"] == "image":
            img = Image(item["data"])
            img.drawHeight = 3 * inch
            img.drawWidth = 3 * inch
            elements.append(img)
            elements.append(Spacer(1, 0.3 * inch))

    elements.append(Spacer(1, 0.5 * inch))
    elements.append(Paragraph("<b>PDF tayyorla</b>", bold_style))

    doc.build(elements)

    return file_name
