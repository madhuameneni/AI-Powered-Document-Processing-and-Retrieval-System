from langchain_community.vectorstores import FAISS
import os
import dotenv
dotenv.load_dotenv("config.env")
from langchain_openai import AzureOpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

class Vector_Databade:
    def __init__(self) -> None:
        self.OPENAI_API_TYPE = os.environ["OPENAI_API_TYPE"]
        self.AZURE_OPENAI_API_KEY =  os.environ["AZURE_OPENAI_API_KEY"]
        self.AZURE_OPENAI_ENDPOINT = os.environ["AZURE_OPENAI_ENDPOINT"]
        self.embeddings = AzureOpenAIEmbeddings(
                model="text-embedding-ada-002",
        )
        
        
        
    def load_vector_database(self, pdf_path):
        self.loader = PyPDFLoader(file_path=pdf_path)
        documents = self.loader.load()
        text_splitter = CharacterTextSplitter(
            chunk_size=1000, chunk_overlap=30, separator="\n"
        )
        docs = text_splitter.split_documents(documents=documents)
        self.vector_store = FAISS.from_documents(docs, self.embeddings)
        self.vector_store.save_local("faiss_index_react")


vd = Vector_Databade("/home/mameneni/review/pwc_int/pdf_files/random machine learing pdf.pdf")
vd.load_vector_database()