from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

## Load and Store Documents
def load_rag():
    loader=PyPDFLoader("health_docs.pdf")
    docs=loader.load()
    embeddings=HuggingFaceEmbeddings()
    db=Chroma.from_documents(docs,embeddings)
    return db
## Search relevent Info
def rag_search(query,db):
    results=db.similarity_search(query,k=2)
    return "\n".join([docs.page_content for docs in results])