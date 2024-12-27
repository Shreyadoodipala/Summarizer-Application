from PyPDF2 import PdfReader
from transformers import BartForConditionalGeneration, BartTokenizer

# Load summarization model and tokenizer
model_name = "facebook/bart-large-cnn"
model = BartForConditionalGeneration.from_pretrained(model_name)
tokenizer = BartTokenizer.from_pretrained(model_name)

# Load question-answering model and pipeline
qa_model_name = "deepset/roberta-base-squad2"
qa_pipeline = pipeline("question-answering", model=qa_model_name, tokenizer=qa_model_name)

def extract_text_from_pdf(pdf_file):
    """Extracts text from an uploaded PDF file."""
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def summarize_text(text, max_length=130, min_length=30, length_penalty=2.0, num_beams=4):
    """Summarizes a single chunk of text."""
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(
        inputs,
        max_length=max_length,
        min_length=min_length,
        length_penalty=length_penalty,
        num_beams=num_beams,
        early_stopping=True,
    )
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

def summarize_long_text(text, chunk_size=1024):
    """Handles long text by breaking it into chunks and summarizing each."""
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    summaries = [summarize_text(chunk) for chunk in chunks]
    return " ".join(summaries)

def answer_question(text, question):
    """Answer a question based on the provided context text."""
    result = qa_pipeline(question=question, context=text)
    return result['answer']
