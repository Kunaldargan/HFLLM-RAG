import io
import os

def process_document(file):
    """
    Processes a document using OCR, preprocessing, and chunking.

    Args:
        file (file): The uploaded file object.

    Returns:
        list: A list of text chunks.
    """
    print(f"Processing document: {file.name}")
    # Simulate OCR logic, preprocessing, chunking
    chunks = []
    try:
        # Get the file extension
        file_ext = os.path.splitext(file.name)[1]
        if file_ext == '.txt':
            # Read and process text files directly
            stringio = io.StringIO(file.getvalue().decode("utf-8"))
            text = stringio.read()
            chunks = chunk_text(text)
        elif file_ext == '.pdf':
            # Here you would do PDF extraction, OCR etc, but for now we just display that the file is of PDF type
            chunks = [f"This file is a PDF file named: {file.name}, You would normally do OCR and PDF extraction, if the correct libs were available"]
        else:
            chunks = ["Unsupported file type."]
    except Exception as e:
        chunks = [f"An error has occured: {e}"]
    return chunks

def chunk_text(text, chunk_size=500, overlap=50):
    """
    Chunks the text into smaller segments.

    Args:
        text (str): The text to be chunked.
        chunk_size (int): The maximum size of each chunk.
        overlap (int): The amount of overlap between chunks.

    Returns:
        list: A list of text chunks.
    """
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        if end > len(text):
            end = len(text)
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

# More document processing functions
