from dotenv import load_dotenv

load_dotenv()
import streamlit as st
import os
import io 

import PyPDF2 as pdf
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## gemini pro response
def get_gemini_response(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
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

input_prompt = """
Hey Act Like a skilled or very experienced ATS (Application Tracking System) 
with a deep understanding of the tech field, software engineering, data science, 
data analyst, and big data engineer. Your task is to evaluate the resume based on the given job description. 
You must consider the job market is very competitive and you should provide 
the best assistance for improving the resumes. Assign the percentage Matching based 
on JD and the missing keywords with high accuracy.

resume: {text}
description: {jd}
I want the response in one single string having the structure 
{{"JD Match":"%", "MissingKeywords":[], "Profile Summary":""}}

"""

## streamlit app

st.title("Smart ATS")

st.text("Improve Your Resume ATS")

jd = st.text_area("Paste the Job Description")

uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload pdf")

submit = st.button("Submit")
if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1 = st.button("Tell Me About the Resume")

submit2 = st.button("How Can I Improvise my Skills")

submit3 = st.button("Percentage match")




if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt)
        st.subheader(response)
