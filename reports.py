#!/usr/bin/env python3
"""Script to generate a PDF report"""

import os
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate

def generate_report(attachment,title,paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    title = Paragraph(title, styles["h1"])
    report_info = Paragraph(paragraph, styles["BodyText"])
    empty_line = Spacer(1, 20)
    report.build([title, empty_line, report_info])
