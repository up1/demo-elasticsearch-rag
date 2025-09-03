# Simple RAG architecture using LangChain, Ollama and Elasticsearch

import os
from dotenv import load_dotenv
from pathlib import Path

from langchain_elasticsearch import ElasticsearchStore
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.documents import Document
from langgraph.graph import START, StateGraph
from typing_extensions import List, TypedDict

# Disable LangChain tracing
#os.environ["LANGCHAIN_TRACING_V2"] = "false"

# Load and chunk contents of the PDF
base_path = Path(__file__).resolve().parent
  
# Index the chunks in Elasticsearch
dotenv_path = Path(base_path / "elastic-start-local/.env")
if not dotenv_path.is_file():
    print("Error: it seems Elasticsearch has not been installed")
    print("using start-local, please execute the following command:")
    print("curl -fsSL https://elastic.co/start-local | sh")
    exit(1)
    
load_dotenv(dotenv_path=dotenv_path)
index_name="products"

# Embeddings
embeddings = OllamaEmbeddings(
    model="llama3.2:1b",
)

vector_db  = ElasticsearchStore(
    es_url=os.getenv('ES_LOCAL_URL'),
    es_api_key= os.getenv('ES_LOCAL_API_KEY'),
    embedding=embeddings,
    index_name=index_name
)

# LLM
llm = ChatOllama(model="llama3.2:1b", temperature=0.0000000001)


# Define state for application
class State(TypedDict):
    question: str
    context: List[Document]
    answer: str

# Define application steps
def retrieve(state: State):
    retrieved_docs = vector_db.similarity_search(state["question"], k=5)
    print(f"Retrieved {len(retrieved_docs)} documents from Elasticsearch")
    return {"context": retrieved_docs}


question = "Wine for seafood"
print("==== Question:====")
print(question)

results = retrieve({"question": question})
print("\n==== Results:====")
for doc in results["context"]:
    print(doc)