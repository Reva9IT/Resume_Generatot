import streamlit as st
import google.generativeai as genai
from resume_generator import create_docx, create_pdf, create_portfolio

if st.button("Show Available Models"):
    models = [m.name for m in genai.list_models()]
    st.write(models)

# ---------- API CONFIG ----------
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

st.set_page_config(page_title="AI Resume & Portfolio Builder", layout="centered")

st.title("🚀 AI Resume & Portfolio Builder")

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

experience = st.text_area("Experience (Role - Company - Description)")
projects = st.text_area("Projects (Name - Description)")
achievements = st.text_area("Achievements")

# ---------- LLM ----------
def generate_summary():
    prompt = f"""
    Create a strong professional resume summary.

    Name: {name}
    Role: {title}
    Skills: {skills}
    Experience: {experience}
    Projects: {projects}

    Make it ATS-friendly and impactful.
    """

    model = genai.GenerativeModel("models/gemini-1.5-flash")
    response = model.generate_content(prompt)

    return response.text


# ---------- BUTTON ----------
if st.button("Generate"):
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

        docx = create_docx(data)
        pdf = create_pdf(data)
        html = create_portfolio(data)

        st.subheader("Generated Summary")
        st.write(summary)

        with open(docx, "rb") as f:
            st.download_button("Download Resume DOCX", f)

        with open(pdf, "rb") as f:
            st.download_button("Download Resume PDF", f)

        with open(html, "rb") as f:
            st.download_button("Download Portfolio Website", f)
