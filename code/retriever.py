import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL, TOP_K

class Retriever:
    def __init__(self):
        self.model = SentenceTransformer(EMBEDDING_MODEL)
        self.index = None
        self.text_chunks = []

    def build_index(self, chunks):
        self.text_chunks = [chunk.page_content for chunk in chunks]
        embeddings = self.model.encode(self.text_chunks)

        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(np.array(embeddings))

    def retrieve(self, query):
        query_embedding = self.model.encode([query])
        D, I = self.index.search(np.array(query_embedding), TOP_K)

        return [self.text_chunks[i] for i in I[0]]