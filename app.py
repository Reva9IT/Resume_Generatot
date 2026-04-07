import streamlit as st
from resume_generator import create_docx, create_pdf, create_portfolio

st.set_page_config(page_title="Resume & Portfolio Builder", layout="centered")

st.title("🚀 Resume & Portfolio Builder")

# ---------- INPUTS ----------
name = st.text_input("Full Name")
title = st.text_input("Professional Title")

email = st.text_input("Email")
phone = st.text_input("Phone")

linkedin = st.text_input("LinkedIn")
github = st.text_input("GitHub")
website = st.text_input("Website")

skills = st.text_area("Skills (comma separated)")
education = st.text_area("Education")

experience = st.text_area("Experience (Role - Company - Description, new line)")
projects = st.text_area("Projects (Name - Description, new line)")
achievements = st.text_area("Achievements")

# ---------- SUMMARY ----------
def generate_summary():
    skills_list = [s.strip() for s in skills.split(",") if s.strip()]
    top_skills = ", ".join(skills_list[:4])

    first_project = ""
    if projects:
        first_project = projects.split("\n")[0]

    return f"""{title} with strong expertise in {top_skills}.
Experienced in building projects such as {first_project}.
Passionate about solving real-world problems and delivering scalable solutions."""

# ---------- BUTTON ----------
if st.button("Generate Resume & Portfolio"):
    if not name or not skills:
        st.error("Fill required fields")
    else:
        summary = generate_summary()

        data = {
            "name": name,
            "title": title,
            "email": email,
            "phone": phone,
            "linkedin": linkedin,
            "github": github,
            "website": website,
            "skills": skills,
            "education": education,
            "experience": experience,
            "projects": projects,
            "achievements": achievements,
            "summary": summary,
        }

        # Generate files
        create_docx(data)
        create_pdf(data)
        create_portfolio(data)

        st.subheader("Generated Summary")
        st.write(summary)

        # ---------- DOWNLOAD BUTTONS (FIXED MIME ISSUE) ----------
        with open("resume.docx", "rb") as f:
            st.download_button(
                label="Download Resume (DOCX)",
                data=f,
                file_name="resume.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

        with open("resume.pdf", "rb") as f:
            st.download_button(
                label="Download Resume (PDF)",
                data=f,
                file_name="resume.pdf",
                mime="application/pdf"
            )

        with open("portfolio.html", "rb") as f:
            st.download_button(
                label="Download Portfolio Website",
                data=f,
                file_name="portfolio.html",
                mime="text/html"
            )
