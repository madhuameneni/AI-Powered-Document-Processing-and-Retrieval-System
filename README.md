# AI-Powered-Document-Processing-and-Retrieval-System
This project reflects the key components of the project: document ingestion, vector storage, embedding generation, information retrieval, question-answering, and API integration. It highlights the use of AI and OpenAI technologies to build an advanced system for handling and querying documents. And a FastAPI for fetching the prefered information.

## Approach:  
Retrieval-Augmented Generation (RAG) is an advanced method in the field of natural language processing (NLP) that combines the strengths of retrieval-based systems and generative models to generate more accurate and contextually relevant responses.  


### Install the required libraries.
```
pip install -r requirments.txt
```

### Start the application
1. Configure the azure credentials in config.env
2. Setup the vector database.
```
python vector_data_loader.py
```
3. Start the API service.
```
python main.py
```
4. Test the serviceby running client
```
python test_client.py
```