import os
from langchain_comminity.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from langchain_openai import ChatOpenAIEmbeddings
from langchain_comminity.vectorstores import Chroma
from langchain_chains import RetrievalQA
from src.core.llm_factory import get_llm

def run_rag_pipeline(query: str):
    # 1. Load Data 
    loader = PyPDFLoader("/data/input_docs/sample.pdf")
    documents = loader.load()

    # 2. Chunking (Splitting large text into readable pieces)
    text_splitters = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_documents(documents)

    # 3. Embedding & Vector Store (Saving text as numbers for search)
    vector_db = Chroma.from_documents(
        documents=texts,
        embedding=ChatOpenAIEmbeddings(),
        persistent_directory="data/vector_store"
    )

    # 4. Retrieval & Generation (Find relevant info + Answer)
    qa_chain = RetrievalQA.from_chain_type(
        llm=get_llm(),
        chain_type="stuff",
        retriever=vector_db.as_retriever()
    )

    return qa_chain.invoke()


