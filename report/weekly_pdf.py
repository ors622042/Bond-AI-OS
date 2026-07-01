# Bond AI OS V7 - Weekly PDF Report Generator
# Requires reportlab

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
from config import ETFS
from indicators.score import etf_score


def generate_weekly_pdf(filename="weekly_report.pdf"):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    story = []

    title = Paragraph("Bond AI OS Weekly Investment Report", styles['Title'])
    story.append(title)
    story.append(Spacer(1, 12))

    date = Paragraph(f"Generated: {datetime.now()}", styles['Normal'])
    story.append(date)
    story.append(Spacer(1, 12))

    for etf in ETFS:
        r = etf_score(etf)

        content = f"""
        <b>ETF:</b> {r['etf']}<br/>
        Price: {r['price']}<br/>
        Score: {r['score']:.2f}<br/>
        Risk: {r['risk_level']}<br/>
        Action: {r['action']}<br/><br/>
        """

        story.append(Paragraph(content, styles['BodyText']))
        story.append(Spacer(1, 10))

    doc.build(story)

    return filename
