from langchain_community.vectorstores import FAISS
from langchain_openai import AzureOpenAIEmbeddings
from langchain_openai import AzureOpenAI, AzureChatOpenAI
import dotenv
dotenv.load_dotenv("config.env")
from fastapi import FastAPI

app = FastAPI()

class Load_query_feteher:
    def __init__(self) -> None:
        self.llm = self.load_llm()
        self.embedding = self.load_embeddings()
        self.vd = self.load_vd()


    def load_llm(self):
        llm = AzureChatOpenAI(deployment_name="gpt-4", api_version="2023-03-15-preview")
        return llm

    def load_embeddings(self):
        embeddings = AzureOpenAIEmbeddings(
                    model="text-embedding-ada-002",
            )
        return embeddings
    
    def load_vd(self):
        new_db = FAISS.load_local("faiss_index_react/", self.embedding, allow_dangerous_deserialization=True)
        return new_db

    def promt(self, context, query):
        prompt = f"""Answer the question based on the context below. If the
                question cannot be answered using the information provided answer
                with "I don't know".
                Context: {context}.
                query: {query}"""
        
        return prompt


loader = Load_query_feteher()
 
@app.get("/fetch/{query}")
async def fast_api_fetch_data(query=str, context=""):
    print(query)
    docs = loader.vd.similarity_search(query, k=5)
    for each_doc in docs:
        context += each_doc.page_content + " "
    promt = loader.promt(context, query)
    retrived_data = loader.llm.invoke(model="gpt-4", input=promt)
    return retrived_data


# loader = Load_query_feteher()
# retrived_data = loader.fast_api_fetch_data("whats inside?")

from fastapi.testclient import TestClient
client = TestClient(app)

def test_fetcher():
    query = {"question": "rect??? ...."}
    # query = "rect??"
    response = client.get(f"/fetch/{query}")
    assert response.status_code == 200



test_fetcher()
    
    
    