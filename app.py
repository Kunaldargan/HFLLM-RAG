import streamlit as st
import yaml
from utils.data_processing import process_document
from utils.retrieval import get_embeddings, vector_search, build_index  # Updated import

st.title("🏥 HFLLM RAG Streamlit Med")
st.write("Welcome to the Health Records Management & Retrieval app!")

# Load settings from the config file
try:
    with open("config/settings.yaml", "r") as f:
        settings = yaml.safe_load(f)
except FileNotFoundError:
    st.error("Error: 'settings.yaml' file not found. Please create the file in the 'config/' directory.")
    st.stop()
except yaml.YAMLError as e:
    st.error(f"Error reading 'settings.yaml': {e}")
    st.stop()

# Display Configuration Settings
st.sidebar.header("Configuration Settings")
for key, value in settings.items():
    st.sidebar.write(f"**{key}:** {value}")

# File upload section
uploaded_files = st.file_uploader("Upload medical documents", type=["pdf", "txt"], accept_multiple_files=True)

# Collect all text chunks from the uploaded files
all_chunks = []

if uploaded_files:
    st.write("Uploaded files:")
    for file in uploaded_files:
        st.write(f"- {file.name}")
        try:
            chunks = process_document(file)  # Process the file to produce chunks
            # Optionally, show a preview for each chunk:
            for chunk in chunks:
                st.write(f"*Preview:* {chunk[:100]}{'...' if len(chunk) > 100 else ''}")
            all_chunks.extend(chunks)
        except Exception as e:
            st.error(f"Error processing document {file.name}: {e}")

# If we have processed text, build an embedding index for retrieval
if all_chunks:
    st.write("Building document index for retrieval...")
    index = build_index(all_chunks)  # Compute embeddings for every chunk
else:
    index = None

# Query interface for RAG
if index:
    st.subheader("Query Your Data")
    query = st.text_input("Enter your query for medical analysis:")
    if st.button("Search") and query:
        query_embedding = get_embeddings(query)
        results = vector_search(query_embedding, index)
        st.write("Search Results:")
        for res in results:
            st.write(res)
else:
    st.write("Upload documents to build the index and enable querying.")

# Placeholder: additional application features can be integrated here.
st.write("Other RAG integration features will be added in further iterations!")

