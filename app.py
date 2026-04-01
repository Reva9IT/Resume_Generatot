import streamlit as st
from resume_generator import create_docx, create_pdf

st.set_page_config(page_title="AI Resume Builder", layout="centered")

st.title("📄 AI Resume Builder")
st.write("Fill in your details and generate your resume.")

# --- INPUTS ---
name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
links = st.text_input("Links (GitHub / LinkedIn)")
skills = st.text_area("Skills (comma separated)")
education = st.text_area("Education")
experience = st.text_area("Experience (each point on new line)")

# --- BUTTON ---
if st.button("Generate Resume"):
    if not name:
        st.error("Name is required")
    else:
        data = {
            "name": name,
            "email": email,
            "phone": phone,
            "links": links,
            "skills": skills,
            "education": education,
            "experience": experience,
        }

        try:
            docx_file = create_docx(data)
            pdf_file = create_pdf(data)

            with open(docx_file, "rb") as f:
                st.download_button("Download DOCX", f, file_name="resume.docx")

            with open(pdf_file, "rb") as f:
                st.download_button("Download PDF", f, file_name="resume.pdf")

            st.success("Resume generated successfully!")

        except Exception as e:
            st.error(f"Error: {str(e)}")
