import os
import sys
import chromadb
import requests
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

def call_phi2(prompt, max_tokens=300):
    response = requests.post(
        "http://localhost:8081/completion",
        json={
            "prompt": prompt,
            "n_predict": max_tokens,
            "temperature": 0.7,
            "stop": ["<|endoftext|>"]
        }
    )  
    response.raise_for_status()
    return response.json()["content"]


# 1. Setup ChromaDB connection
persist_dir = "./chroma-linux-rag"
client = chromadb.Client(Settings(persist_directory=persist_dir))
collection = client.get_or_create_collection("linux_docs")

# 2. Load the embedding model (for command query)
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# 3. Load local LLM (Phi-2 or substitute model)
# You can replace this model with Phi-2 when available locally
print("\U0001F50D Loading local model...")

# 4. Define the explanation generator
def explain_command(command_text, top_k=3):
    print("\n\U0001F4C8 Retrieving relevant context from ChromaDB...")
    query_embedding = embedder.encode(command_text).tolist()
    
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    context_docs = results["documents"][0]
    
    combined_context = "\n\n".join(context_docs)

    # Build prompt for the local LLM
    prompt = (
        "You are a helpful Linux tutor.\n"
        f"Command: {command_text}\n"
        f"Context:\n{combined_context}\n"
        "Explain the command to a beginner user in a clear and simple way."
    )

    print ("\n Sending prompt to Phi-2 server...")
    output = call_phi2(prompt, max_tokens=300)

    print("=== Explanation ===")
    print(output)

# 5. CLI Entry
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python query_command.py '<your linux command>'")
        sys.exit(1)

    command_input = " ".join(sys.argv[1:])
    explain_command(command_input)

