from docx import Document
from docx.shared import Pt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


# ---------- DOCX ----------
def create_docx(data):
    doc = Document()

    # Name
    doc.add_heading(data.get("name", ""), 0)

    # Contact
    contact = f"{data.get('email','')} | {data.get('phone','')}"
    if data.get("links"):
        contact += f" | {data.get('links')}"
    doc.add_paragraph(contact)

    # Skills
    doc.add_heading("Skills", level=1)
    for skill in data.get("skills", "").split(","):
        if skill.strip():
            doc.add_paragraph(skill.strip(), style="List Bullet")

    # Education
    doc.add_heading("Education", level=1)
    doc.add_paragraph(data.get("education", ""))

    # Experience
    doc.add_heading("Experience", level=1)
    for line in data.get("experience", "").split("\n"):
        if line.strip():
            doc.add_paragraph(line.strip(), style="List Bullet")

    file_path = "resume.docx"
    doc.save(file_path)
    return file_path


# ---------- PDF ----------
def create_pdf(data):
    doc = SimpleDocTemplate("resume.pdf")
    styles = getSampleStyleSheet()
    elements = []

    # Name
    elements.append(Paragraph(f"<b>{data.get('name','')}</b>", styles['Title']))
    elements.append(Spacer(1, 10))

    # Contact
    contact = f"{data.get('email','')} | {data.get('phone','')}"
    if data.get("links"):
        contact += f" | {data.get('links')}"
    elements.append(Paragraph(contact, styles['Normal']))
    elements.append(Spacer(1, 12))

    # Skills
    elements.append(Paragraph("<b>Skills</b>", styles['Heading2']))
    for skill in data.get("skills", "").split(","):
        if skill.strip():
            elements.append(Paragraph(f"• {skill.strip()}", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Education
    elements.append(Paragraph("<b>Education</b>", styles['Heading2']))
    elements.append(Paragraph(data.get("education",""), styles['Normal']))
    elements.append(Spacer(1, 12))

    # Experience
    elements.append(Paragraph("<b>Experience</b>", styles['Heading2']))
    for line in data.get("experience","").split("\n"):
        if line.strip():
            elements.append(Paragraph(f"• {line.strip()}", styles['Normal']))

    doc.build(elements)
    return "resume.pdf"
