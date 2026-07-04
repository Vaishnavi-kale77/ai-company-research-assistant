from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

def generate_pdf(content):

    filename = "company_report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    title = Paragraph(
        "<b>AI Company Research Report</b>",
        styles["Title"]
    )

    story.append(title)

    story.append(Spacer(1, 20))

    body = Paragraph(
        content.replace("\n", "<br/>"),
        styles["BodyText"]
    )

    story.append(body)

    story.append(Spacer(1, 12))

    doc.build(story)

    return filename