from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


paths = [
    Path("D:\\Projects\\KCC-RAG\\data\\raw\\pib_kcc_explainer_2026-03-11.pdf")
]


pages = PyPDFLoader(str(paths[0])).load()
pages.extend(PyPDFLoader(str(paths[0])).load())

print(pages)

pages.find("available")