import streamlit as st
from nlp_utils import extract_text_from_pdf, summarize_long_text, answer_question

st.title("PDF/Text Summarization and Question Answering App")

# User selects input method
input_option = st.radio(
    "Choose input method:",
    ("Upload PDF", "Enter Text")
)

if input_option == "Upload PDF":
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if uploaded_file is not None:
        # Extract text from the uploaded PDF
        pdf_text = extract_text_from_pdf(uploaded_file)
        st.subheader("Extracted Text")
        st.write(pdf_text[:1000])  # Display only the first 1000 characters

        # Summarize the text
        if st.button("Summarize PDF"):
            summary = summarize_long_text(pdf_text)
            st.subheader("Summary")
            st.write(summary)

        # Ask a question
        question = st.text_input("Ask a question about the PDF content:")
        if question:
            answer = answer_question(pdf_text, question)
            st.subheader("Answer")
            st.write(answer)

elif input_option == "Enter Text":
    user_text = st.text_area("Enter text to summarize and ask questions:")
    if st.button("Summarize Text"):
        # Summarize the entered text
        summary = summarize_long_text(user_text)
        st.subheader("Summary")
        st.write(summary)

    # Ask a question
    question = st.text_input("Ask a question about the text:")
    if question:
        answer = answer_question(user_text, question)
        st.subheader("Answer")
        st.write(answer)
