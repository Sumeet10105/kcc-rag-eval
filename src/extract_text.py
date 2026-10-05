from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader


paths = [
    Path("data/raw/rbi_circular_2025-26_193.pdf"),
    Path("data/raw/rbi_circular_2024-25_59.pdf"),
    Path("data/raw/myscheme_kcc_2026-10-03.txt"),
    Path("D:\\Projects\\KCC-RAG\\data\\raw\\pib_kcc_explainer_2026-03-11.pdf")
]

docs = []

for path in paths:

    if path.suffix == ".pdf":
        pages = PyPDFLoader(str(path)).load()

    elif path.suffix == ".txt":
        pages = TextLoader(str(path), encoding="UTF-8").load()

    else:
        continue

    print(path.name, "->", len(pages), "documents")
    docs.extend(pages)

for doc in docs[9:20]:
    print(doc)