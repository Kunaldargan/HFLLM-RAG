from sentence_transformers import SentenceTransformer
import numpy as np

# Initialize the embedding model
embedding_model = SentenceTransformer('all-mpnet-base-v2')

def get_embeddings(text):
    """
    Generates embeddings for text.

    Args:
        text (str): The text to be embedded.

    Returns:
        numpy.ndarray: The text embeddings.
    """
    embeddings = embedding_model.encode(text)
    return embeddings

def build_index(chunks):
    """
    Builds an index from text chunks by generating embeddings for each.

    Args:
        chunks (list): List of text chunks.

    Returns:
        list: A list of dictionaries holding text chunks and their embeddings.
    """
    index = []
    for chunk in chunks:
        embedding = get_embeddings(chunk)
        index.append({
            "text": chunk,
            "embedding": embedding
        })
    return index

def cosine_similarity(a, b):
    """
    Computes cosine similarity between two vectors.

    Args:
        a (numpy.ndarray): First vector.
        b (numpy.ndarray): Second vector.

    Returns:
        float: Cosine similarity score.
    """
    a_norm = np.linalg.norm(a)
    b_norm = np.linalg.norm(b)
    if a_norm == 0 or b_norm == 0:
        return 0
    return np.dot(a, b) / (a_norm * b_norm)
    
def vector_search(query_embedding, index, top_k=3):
    """
    Performs a vector search on the index.

    Args:
        query_embedding (numpy.ndarray): The query vector.
        index (list): The vector index containing embeddings for document chunks.
        top_k (int): Number of top results to return.

    Returns:
        list: The top-k search results based on cosine similarity.
    """
    scores = []
    for item in index:
        score = cosine_similarity(query_embedding, item["embedding"])
        scores.append((score, item["text"]))
    # Sort results by score in descending order
    scores = sorted(scores, key=lambda x: x[0], reverse=True)
    results = [text for score, text in scores[:top_k]]
    return results

