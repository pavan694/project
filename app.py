from dotenv import load_dotenv

load_dotenv()
import streamlit as st
import os
import io 

import PyPDF2 as pdf
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## gemini pro response
def get_gemini_response(input,input_prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([input,input_prompt])
    return response.text



def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)  # Initialize PdfReader
    text = ""
    for page in reader.pages:  # Iterate through the pages directly
        extracted_text = page.extract_text()
        if extracted_text:  
            text += extracted_text + "\n"
    return text

## Prompt Template
# for data science 
input_prompt1 = """
 Hey, act like a highly experienced ATS (Applicant Tracking System) specializing in the data science field.
 Your task is to evaluate the resume based on the given job description. Consider key skills such as 
 machine learning, deep learning, data analysis, big data technologies, and programming expertise
 in Python, R, or SQL. The job market is highly competitive, so provide the best assistance to improve the resume.
 Assign a percentage match based on the JD and identify missing high-impact keywords with precision.

"""
# for sd role
input_prompt2 = """
 Hey, act like a highly skilled ATS (Applicant Tracking System) with deep expertise in software development.
 Your task is to evaluate the resume based on the given job description. Consider key skills such as programming 
 languages (Python, Java, C++, JavaScript), frameworks, system design, algorithms, data structures, and software
 engineering principles. The job market is extremely competitive, so provide the best suggestions
 to optimize the resume. Assign a percentage match based on the JD and highlight missing essential keywords with
 high accuracy.


"""
# chemical engg 
input_prompt3 = """
Hey, act like an advanced ATS (Applicant Tracking System) with expertise in evaluating chemical engineering resumes.
Your task is to assess the resume based on the given job description. Consider important skills such as process
engineering, thermodynamics, reaction engineering, mass transfer, and industry-related tools like Aspen Plus,
MATLAB, or AutoCAD. The job market is competitive, so provide precise recommendations to improve the resume.
Assign a percentage match based on the JD and identify missing technical keywords with accuracy.


"""

## streamlit app

st.title("Smart ATS")

st.text("Improve Your Resume ATS")

jd = st.text_area("Paste the Job Description")

uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload pdf")


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1 = st.button("Tell Me About the Resume")

submit2 = st.button("How Can I Improvise my Skills")

submit3 = st.button("Percentage match")




if submit1:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt1,text)
        st.subheader(response)
if submit2:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt2,text)
        st.subheader(response)
if submit3:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt3,text)
        st.subheader(response)
