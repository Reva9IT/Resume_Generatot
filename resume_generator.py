from docx import Document
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

    # Summary
    doc.add_heading("Summary", level=1)
    doc.add_paragraph(data.get("summary", ""))

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

    # Projects
    doc.add_heading("Projects", level=1)
    for project in data.get("projects", "").split(","):
        if project.strip():
            doc.add_paragraph(project.strip(), style="List Bullet")

    # Achievements
    doc.add_heading("Achievements", level=1)
    for ach in data.get("achievements", "").split(","):
        if ach.strip():
            doc.add_paragraph(ach.strip(), style="List Bullet")

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

    # Summary
    elements.append(Paragraph("<b>Summary</b>", styles['Heading2']))
    elements.append(Paragraph(data.get("summary",""), styles['Normal']))
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
    elements.append(Spacer(1, 12))

    # Projects
    elements.append(Paragraph("<b>Projects</b>", styles['Heading2']))
    for p in data.get("projects","").split(","):
        if p.strip():
            elements.append(Paragraph(f"• {p.strip()}", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Achievements
    elements.append(Paragraph("<b>Achievements</b>", styles['Heading2']))
    for a in data.get("achievements","").split(","):
        if a.strip():
            elements.append(Paragraph(f"• {a.strip()}", styles['Normal']))

    doc.build(elements)
    return "resume.pdf"


# ---------- PORTFOLIO ----------
def create_portfolio(data):
    html_content = f"""
    <html>
    <head>
        <title>{data.get("name","")} Portfolio</title>
        <style>
            body {{
                font-family: Arial;
                background-color: #1e2d24;
                color: #f5f5dc;
                padding: 40px;
            }}
            h1, h2 {{
                color: #d6e5b1;
            }}
        </style>
    </head>
    <body>

    <h1>{data.get("name","")}</h1>
    <p>{data.get("email","")} | {data.get("phone","")}</p>
    <p>{data.get("links","")}</p>

    <h2>Summary</h2>
    <p>{data.get("summary","")}</p>

    <h2>Skills</h2>
    <ul>
        {''.join([f"<li>{s.strip()}</li>" for s in data.get("skills","").split(",") if s.strip()])}
    </ul>

    <h2>Projects</h2>
    <ul>
        {''.join([f"<li>{p.strip()}</li>" for p in data.get("projects","").split(",") if p.strip()])}
    </ul>

    <h2>Experience</h2>
    <ul>
        {''.join([f"<li>{e.strip()}</li>" for e in data.get("experience","").split("\\n") if e.strip()])}
    </ul>

    <h2>Achievements</h2>
    <ul>
        {''.join([f"<li>{a.strip()}</li>" for a in data.get("achievements","").split(",") if a.strip()])}
    </ul>

    </body>
    </html>
    """

    file_path = "portfolio.html"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    return file_path
