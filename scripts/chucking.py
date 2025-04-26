import os

def chunk_text(text, max_length=400):
    sentences = text.split('. ')
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) < max_length:
            current_chunk += sentence + ". "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + ". "
    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def chunk_folder(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            with open(os.path.join(input_folder, filename), "r") as f:
                text = f.read()

            chunks = chunk_text(text)

            for idx, chunk in enumerate(chunks):
                chunk_filename = f"{filename.replace('.txt','')}_chunk_{idx}.txt"
                with open(os.path.join(output_folder, chunk_filename), "w", encoding="utf-8") as cf:
                    cf.write(chunk)

            print(f"Chunked {filename} into {len(chunks)} pieces.")

# Example usage:
chunk_folder("./data/linux_books_txt", "./data/linux_books_chunks")

