import os
import chromadb
from sentence_transformers import SentenceTransformer

# Setup Chroma client
persist_dir = "./chroma-linux-rag"
os.makedirs(persist_dir, exist_ok=True)

# Updated client initialization for newer versions of ChromaDB
client = chromadb.PersistentClient(path=persist_dir)

# Embedder
embedder = SentenceTransformer("/home/neofto/all-MiniLM-L6-v2")

# Define a proper embedding function class that matches ChromaDB's expected interface
class SentenceTransformerEmbedder:
    def __init__(self, model_name):
        self.model = SentenceTransformer(model_name)
        
    def __call__(self, input):
        return self.model.encode(input).tolist()

# Create the embedding function instance
embedding_function = SentenceTransformerEmbedder("/home/neofto/all-MiniLM-L6-v2")

collection = client.get_or_create_collection(
    name="linux_docs",
    embedding_function=embedding_function
)

def embed_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
            if len(text.strip()) == 0:
                continue  # Skip empty files
            collection.add(
                documents=[text],
                metadatas=[{"source": filename}],
                ids=[filename]
            )
            print(f"✅ Embedded: {filename}")

if __name__ == "__main__":
    embed_folder("./data/tldr_extracted")
    embed_folder("./data/linux_books_chunks")
    print("✅ Embedding complete! Chroma will automatically persist the database.")
