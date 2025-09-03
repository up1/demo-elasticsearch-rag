# Store PDF documents in Elasticsearch using Ollama embeddings

import os
from dotenv import load_dotenv
from pathlib import Path
from langchain_elasticsearch import ElasticsearchStore
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document
from uuid import uuid4


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

# Check if the index already exists
# res = vector_db.client.indices.exists(index=index_name)
# if res.body:
#     print(f"The index {index_name} already exists in Elasticseach")
#     exit(1)
    
print(f"Reading the PDFs in {base_path}/data")
all_products = []
doc01 = Document(
    page_content="good with fish",
    metadata={"source": "database"}
)
doc02 = Document(
    page_content="good with pork",
    metadata={"source": "database"}
)
doc03 = Document(
    page_content="good with beef",
    metadata={"source": "database"}
)
all_products.append(doc01)
all_products.append(doc02)
all_products.append(doc03)

uuids = [str(uuid4()) for _ in range(len(all_products))]

print(f"Storing data in Elasticsearch")
vector_db.add_documents(
    documents=all_products,
    ids=uuids,
    embedding=embeddings,
    es_connection=vector_db.client,
    index_name=index_name
)
print(f"Stored {len(all_products)} products")