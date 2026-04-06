import streamlit as st
from resume_generator import create_docx, create_pdf, create_portfolio

st.set_page_config(page_title="AI Resume & Portfolio Builder", layout="centered")

st.title("📄 AI Resume & Portfolio Builder")

# ---------- INPUTS ----------
name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
links = st.text_input("Links (GitHub / LinkedIn)")

skills = st.text_area("Skills (comma separated)")
education = st.text_area("Education")
experience = st.text_area("Experience (each point on new line)")

projects = st.text_area("Projects (comma separated)")
achievements = st.text_area("Achievements (comma separated)")
summary = st.text_area("Summary (optional)")

# ---------- BUTTON ----------
if st.button("Generate"):
    if not name:
        st.error("Name is required")
    else:
        if not summary:
            summary = f"Motivated individual skilled in {skills}, with experience in {projects}."

        data = {
            "name": name,
            "email": email,
            "phone": phone,
            "links": links,
            "skills": skills,
            "education": education,
            "experience": experience,
            "projects": projects,
            "achievements": achievements,
            "summary": summary,
        }

        try:
            docx_file = create_docx(data)
            pdf_file = create_pdf(data)
            html_file = create_portfolio(data)

            st.success("Generated Successfully!")

            with open(docx_file, "rb") as f:
                st.download_button("Download Resume (DOCX)", f, file_name="resume.docx")

            with open(pdf_file, "rb") as f:
                st.download_button("Download Resume (PDF)", f, file_name="resume.pdf")

            with open(html_file, "rb") as f:
                st.download_button("Download Portfolio (HTML)", f, file_name="portfolio.html")

        except Exception as e:
            st.error(f"Error: {str(e)}")
