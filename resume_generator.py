from docx import Document
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


# ---------- DOCX ----------
def create_docx(data):
    doc = Document()

    doc.add_heading(data["name"], 0)
    doc.add_paragraph(f"{data['email']} | {data['phone']}")
    doc.add_paragraph(f"{data['linkedin']} | {data['github']}")

    doc.add_heading("Summary", 1)
    doc.add_paragraph(data["summary"])

    doc.add_heading("Skills", 1)
    for s in data["skills"].split(","):
        if s.strip():
            doc.add_paragraph(s.strip(), style="List Bullet")

    doc.add_heading("Experience", 1)
    for e in data["experience"].split("\n"):
        if e.strip():
            doc.add_paragraph(e.strip(), style="List Bullet")

    doc.add_heading("Projects", 1)
    for p in data["projects"].split("\n"):
        if p.strip():
            doc.add_paragraph(p.strip(), style="List Bullet")

    doc.add_heading("Education", 1)
    doc.add_paragraph(data["education"])

    doc.add_heading("Achievements", 1)
    doc.add_paragraph(data["achievements"])

    doc.save("resume.docx")
    return "resume.docx"


# ---------- PDF ----------
def create_pdf(data):
    doc = SimpleDocTemplate("resume.pdf")
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph(f"<b>{data['name']}</b>", styles["Title"]))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph(data["summary"], styles["Normal"]))
    elements.append(Spacer(1, 10))

    for section in ["skills", "experience", "projects"]:
        elements.append(Paragraph(f"<b>{section.title()}</b>", styles["Heading2"]))
        for item in data[section].split("\n"):
            if item.strip():
                elements.append(Paragraph(f"• {item}", styles["Normal"]))
        elements.append(Spacer(1, 10))

    doc.build(elements)
    return "resume.pdf"


# ---------- PORTFOLIO ----------
def create_portfolio(data):
    html = f"""
<html>
<head>
<style>
body {{
    font-family: Arial;
    margin: 0;
    background: #121212;
    color: white;
}}
.hero {{
    text-align: center;
    padding: 60px;
    background: #1e2d24;
}}
.section {{
    padding: 40px;
}}
.card {{
    background: #1e1e1e;
    padding: 20px;
    margin: 15px 0;
    border-radius: 10px;
}}
h1, h2 {{
    color: #d6e5b1;
}}
</style>
</head>

<body>

<div class="hero">
    <h1>{data['name']}</h1>
    <h2>{data['title']}</h2>
    <p>{data['email']} | {data['phone']}</p>
    <p>{data['linkedin']} | {data['github']}</p>
</div>

<div class="section">
    <h2>About</h2>
    <p>{data['summary']}</p>
</div>

<div class="section">
    <h2>Projects</h2>
    {"".join([f"<div class='card'>{p}</div>" for p in data['projects'].split("\\n") if p.strip()])}
</div>

<div class="section">
    <h2>Experience</h2>
    {"".join([f"<div class='card'>{e}</div>" for e in data['experience'].split("\\n") if e.strip()])}
</div>

</body>
</html>
"""

    with open("portfolio.html", "w", encoding="utf-8") as f:
        f.write(html)

    return "portfolio.html"
