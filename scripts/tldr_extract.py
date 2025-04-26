import os

def collect_tldr_texts(page_root, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    tldr_texts = []

    for root, dirs, files in os.walk(page_root):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()

                clean_lines = [line for line in content.splitlines() if not line.strip().startswith(">")]
                clean_content = "\n".join(clean_lines).strip()

                command_name = file.replace(".md", "")
                tldr_texts.append((command_name, clean_content))

                # ✅ Save each command explanation to a file
                out_path = os.path.join(output_folder, f"{command_name}.txt")
                with open(out_path, "w", encoding="utf-8") as out_f:
                    out_f.write(clean_content)

    return tldr_texts

if __name__ == "__main__":
    pages_root = "./tldr/pages/linux"
    output_folder = "./tldr_extracted"

    tldr_texts = collect_tldr_texts(pages_root, output_folder)

    for title, content in tldr_texts[:5]:
        print(f"\n=== {title} ===\n{content}\n")

