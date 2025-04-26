# Linux Tutor (Offline RAG Assistant)

This project is a lightweight offline Linux command tutor.  
It uses a local LLM (Phi-2) and a vector database (ChromaDB) to retrieve context from Linux books and TLDR command pages, and explain commands clearly.

## 📦 Setup

1. Clone this repository:


2. Create a Python environment and install dependencies:

```bash
python3 -m venv linux-tut-env
source linux-tut-env/bin/activate
pip install -r requirements.txt
```

3. Start your local Phi-2 LLM server: (Explain this)

(Assuming you have llamafile installed)


```bash
bash start-phi2.sh
```

This will run Phi-2 on http://localhost:8081.

4. Prepare the knowledge base (only needed once):
You must recreate the vector database because it is not stored in the repo.

```bash
You must recreate the vector database because it is not stored in the repo.
```

This will:

- [x] Chunk the Linux books and TLDRs

- [x] Embed them into vectors

- [x] Save into a local ChromaDB database at ./chroma-linux-rag/

✅ After this step, your retrieval database is ready.

To get a beginner-friendly explanation for any Linux command:
```bash
python3 scripts/query_command.py "your linux command here"
```

