import streamlit as st
import fitz  # PyMuPDF
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key='OPENAIAPIKEY')

def pdf_to_text(uploaded_file):
    # Upload to streamlit
    # Read the PDF file into bytes
    pdf_bytes = uploaded_file.getvalue()
    # Open the PDF with PyMuPDF (fitz) using the bytes
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def simplify_text(text):
    response = client.chat.completions.create(
      model="gpt-4",  # Consider using the latest model that best fits your needs
      messages=[
        {"role": "system", "content": "You are a helpful assistant that simplifies the given educational text for a student. Highlight the Chapter details as Title:, Summary: Simplified summary:"},
        {"role": "user", "content": text}
      ]
    )
    simplified_text = response.choices[0].message.content
    # Assuming the last message from the assistant is the simplified text
    #simplified_text = response['choices'][0]['message']['content'] if response['choices'] else "Could not simplify the text."
    return simplified_text

st.title('Learning Made Easy')

pdf_file = st.file_uploader("Upload a PDF", type=["pdf"])
if pdf_file is not None:
    text = pdf_to_text(pdf_file)
    if st.button('Simplify Content'):
        simplified_text = simplify_text(text)
        st.write(simplified_text)
