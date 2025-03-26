from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from config import settings

def create_vector_store(texts: list[str]) -> FAISS:
    documents = [Document(page_content=text) for text in texts]
    text_splitter = CharacterTextSplitter(
        chunk_size=settings.CHUNK_SIZE, chunk_overlap=settings.CHUNK_OVERLAP
    )
    split_docs = text_splitter.split_documents(documents)

    vector_db = FAISS.from_documents(
        split_docs, HuggingFaceEmbeddings(model_name=settings.VECTOR_MODEL)
    )
    return vector_db
