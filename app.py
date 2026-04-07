import streamlit as st
import requests
from resume_generator import create_docx, create_pdf, create_portfolio

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

experience = st.text_area("Experience (Role - Company - Description, new line)")
projects = st.text_area("Projects (Name - Description, new line)")
achievements = st.text_area("Achievements")

# ---------- HUGGING FACE API ----------
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

headers = {
    "Authorization": f"Bearer {st.secrets['HUGGINGFACE_API_KEY']}"
}

def generate_summary():
    prompt = f"""
    Write a strong professional resume summary.

    Name: {name}
    Role: {title}
    Skills: {skills}
    Experience: {experience}
    Projects: {projects}

    Keep it concise and ATS-friendly.
    """

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json={"inputs": prompt}
        )

        output = response.json()

        return output[0]["generated_text"]

    except:
        return f"Motivated individual skilled in {skills}, seeking a role as {title}."


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

        docx = create_docx(data)
        pdf = create_pdf(data)
        html = create_portfolio(data)

        st.subheader("Generated Summary")
        st.write(summary)

        with open(docx, "rb") as f:
            st.download_button("Download Resume (DOCX)", f)

        with open(pdf, "rb") as f:
            st.download_button("Download Resume (PDF)", f)

        with open(html, "rb") as f:
            st.download_button("Download Portfolio Website", f)
