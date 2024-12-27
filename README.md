# Summarizer and Question Answering Application
The PDF/Text Summarization and Question Answering App is an interactive web application that allows users to upload PDF documents or enter plain text for summarization and question answering. The app leverages state-of-the-art natural language processing (NLP) models to provide concise summaries of long documents and answer questions related to the text, all within a user-friendly interface built with Streamlit.

### Key Features:
<li> Text Summarization: Automatically generates a brief summary of large PDF documents or entered text, making it easier to extract key information quickly.
<li> Question Answering: Allows users to ask questions related to the content of the uploaded PDF or entered text and receive accurate, context-aware answers.
<li>File Upload and Text Input: Supports both PDF file uploads and direct text input, giving users flexibility in how they interact with the app.

## Models Used (from Hugging Face)
#### BART (Bidirectional and Auto-Regressive Transformers)
Used for text summarization. BART is a powerful transformer model trained for both sequence-to-sequence tasks (like summarization) and denoising tasks. The model is fine-tuned on large-scale datasets to generate coherent and concise summaries of long texts or documents.

#### DistilBERT
Used for question answering. DistilBERT is a smaller, faster variant of the BERT model, which retains much of its accuracy while being computationally more efficient. It is fine-tuned for the task of question answering using the SQuAD dataset, enabling it to understand and extract answers from the provided text based on the user's questions.
