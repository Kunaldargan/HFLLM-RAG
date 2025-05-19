# 🏥 HFLLM RAG Streamlit Med

**Health Records Management & Retrieval using Local LLM**

A secure, local-first Retrieval-Augmented Generation (RAG) application that allows wellness coaches and healthcare practitioners to:
- Upload, store, and manage medical records
- Ask personalized health-related questions
- Retrieve context-grounded answers using a Hugging Face-hosted LLaMA 3.2-Instruct model
- Minimize hallucinations and ensure clinical relevance with robust guardrails
- Highlight retrieved documents for better context understanding

![App Screenshot](assets/app_screenshot.png)

---

## 🚀 Features

- 🔍 **RAG Pipeline**: Seamlessly integrates document retrieval with a powerful language model to generate grounded responses.
- 🩺 **Personalized QA**: Ask custom questions about patient history, lab reports, and treatment summaries.
- 📁 **Medical Record Indexing**: Store structured and unstructured health records (PDFs, clinical notes, etc.).
- 🧠 **Local LLM**: Powered by Meta's LLaMA 3.2 3B-Instruct, hosted securely with Hugging Face Transformers.
- 🔒 **Privacy & Compliance**: Designed for secure handling of sensitive medical data.
- 🧰 **Guardrails**: Contextual grounding, provenance tracking, and automated reasoning checks reduce hallucinations.

---

## 🧱 Tech Stack

| Component       | Tool/Library                        |
|----------------|-------------------------------------|
| UI             | Streamlit                           |
| Language Model | Hugging Face Transformers + LLaMA 3.2 |
| Retrieval      | FAISS / Elasticsearch               |
| NLP            | LangChain + Sentence Transformers   |
| Guardrails     | NVIDIA NeMo Guardrails              |

---

## 📂 Project Structure

```
hfllm_rag_streamlit_med/
│── app.py                        # Streamlit UI
│── config/
│   ├── settings.yaml              # Configuration file
│── data/                          # Uploaded health records
│   ├── patient_records/ 
│   ├── medical_literature/
│   ├── doctor_prescriptions/
│   ├── medical_bills/
│   ├── patient_history/
│── models/
│   ├── llama-3.2-3b-instruct-medical/ # Local LLM model
│── utils/
│   ├── data_processing.py         # OCR, preprocessing, chunking
│   ├── retrieval.py               # Embedding + vector search
│── requirements.txt               # Dependencies list
│── README.md                      # Documentation
```

---

## 🛠 Installation Guide

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/your-repo/hfllm_rag_streamlit_med.git
cd hfllm_rag_streamlit_med
```

### **Step 2: Create a Virtual Environment**
```bash
python -m venv env
source env/bin/activate  # On macOS/Linux
env\Scripts\activate      # On Windows
```

### **Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 4: Setup Configuration**
Modify `config/settings.yaml` to adjust API keys, retrieval parameters, or UI configurations.

---

## 🚀 Running the Application

### **Start the Streamlit Server**
```bash
streamlit run app.py
```
This will launch the user interface in your browser.

---

## 🔍 How It Works

1. **Upload Documents**: PDFs or TXT files containing medical information.
2. **Automatic Chunking & Embedding**: Extracts relevant text and creates vector embeddings.
3. **Retrieval-Augmented Generation (RAG)**:
   - When a user inputs a query, it’s converted into an embedding.
   - A similarity search is performed using FAISS or an alternative index.
   - The most relevant document chunks are retrieved and used for the final AI-generated response.
4. **Medical Guardrails**: Ensure reliable, contextually grounded responses with minimal hallucination.

---

## ⚙️ Configuration Options

You can modify parameters inside `config/settings.yaml`, such as:
```yaml
model_name: "llama-3.2-3b-instruct-medical"
top_k_results: 5
embedding_model: "sentence-transformers/all-mpnet-base-v2"
use_faiss: true
```

---

## 🏗 Future Enhancements

- 🔥 **Enhanced PDF OCR Support**
- 🏥 **Integration with existing EHR Systems**
- 🔍 **Semantic Layer for Improved Query Interpretation**
- 🔒 **Federated Learning for Personalized Retrieval**

---

This README gives a structured overview of setting up and using the project. Let me know if you’d like any refinements or additional instructions! 🚀
