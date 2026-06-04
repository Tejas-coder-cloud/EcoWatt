from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import (
    getSampleStyleSheet
)
def generate_report(
    filename,
    result
):
    doc = SimpleDocTemplate(
        filename
    )
    styles = getSampleStyleSheet()
    content = []
    content.append(
        Paragraph(
            "EcoWatt AI Energy Report",
            styles["Title"]
        )
    )
    content.append(
        Spacer(1, 20)
    )
    content.append(
        Paragraph(
            f"Monthly Consumption: {result['Total']} kWh",
            styles["BodyText"]
        )
    )
    content.append(
        Paragraph(
            f"Estimated Bill: ₹{result['Bill']}",
            styles["BodyText"]
        )
    )
    doc.build(content)