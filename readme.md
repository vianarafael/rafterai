# Linux Tutor (Offline RAG Assistant)

This project is a lightweight offline Linux command tutor.  
It uses a local LLM (Phi-2) and a vector database (ChromaDB) to retrieve context from Linux books and TLDR command pages, and explain commands clearly.

## 📦 Setup

1. Clone this repository and fix the paths:
search for #TODO -> change all the paths to the correct path in your machine


2. Create a Python environment and install dependencies:

```bash
python3 -m venv rafterai-env
source rafterai-env/bin/activate
pip install -r requirements.txt
```

3. Install and start your local Phi-2 LLM server:

This project uses Phi-2, a lightweight 2.7B LLM, to generate Linux command explanations.
You will need llamafile to run the model easily.

### Install llamafile
```bash
curl -LO https://huggingface.co/jartine/llamafile/resolve/main/llamafile
chmod +x llamafile
sudo mv llamafile /usr/local/bin/
```

### Download the Phi-2 model
```bash
mkdir -p ~/Projects/llms/llamafile
cd ~/Projects/llms/llamafile
curl -LO https://huggingface.co/karpathy/tinyllamas/resolve/main/phi-2.Q4_K_M.gguf
```

### start the local LLM server
```bash
bash start-phi2.sh
```

This will run a Phi-2 inference server on:
```bash
http://localhost:8081
```
Your Linux tutor scripts will send propts to this server to get explanations.

4. Prepare the knowledge base (only needed once):

You must recreate the vector database because it is not stored in the repo.

```bash
python scripts/embed_all.py
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

5. Linux tutor wrapper

```shell
function wtf() {
  #1. Run the actual command
  eval "$@"

#2. After the command runs, call the explainer
echo
echo "Explaining command $@"
python3 /add/the/path/to/rafterai/scripts/query_command.py "$@"
}
```

6. Get a beginner-friendly explanation for any Linux command
(This will embed the command you typed, retrieve related information from the Linux textbooks and TLDR vectors, and send both the command and context to Phi-2, which generates a clear explanation.)
```bash
wtf "your linux command here"
```

Example:
```bash
wtf "sudo find / -name '*.conf'"
```

