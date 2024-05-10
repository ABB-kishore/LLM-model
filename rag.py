# Importing the necessary module for prompts
from langchain.retrievers import BM25Retriever, EnsembleRetriever
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_openai import AzureChatOpenAI
from langchain_openai import AzureOpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
import os
from langchain.prompts import PromptTemplate

# Setting up the Azure GPT-4 Turbo API credentials
openai_api_key = "ab98620d70c446b2aae75ee7835902f9"
openai_api_endpoint = "https://rfq-traffic-3.openai.azure.com/"
openai_api_version = "2023-07-01-preview"
openai_api_deployment = "gpt-4-Turbo"
openai_embeddings_deployment = "rfq-embeddings-traffic3"

# Creating an instance of AzureOpenAIEmbeddings for text embeddings
embedding = AzureOpenAIEmbeddings(
    openai_api_key=openai_api_key,
    azure_deployment=openai_embeddings_deployment,
    openai_api_version=openai_api_version,
    azure_endpoint=openai_api_endpoint
)

# Path to the PDF file
path = "uploaded.pdf"

# Creating an instance of AzureChatOpenAI for chat-based language model
llm = AzureChatOpenAI(
    deployment_name=openai_api_deployment,
    openai_api_key=openai_api_key,
    openai_api_version=openai_api_version,
    azure_endpoint=openai_api_endpoint,
    temperature=0.1,
    max_tokens=4096
)

# Function to process the PDF file and return BM25Retriever and FAISS vectorstore
def file_processing(pdf_path):
    # Loading the PDF file
    loader = PyPDFLoader(pdf_path)
    data = loader.load()

    # Splitting the text into chunks
    text_splitter = CharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=200,
    )
    splits = text_splitter.split_documents(data)

    # Creating FAISS vectorstore from the text chunks
    vectordb = FAISS.from_documents(documents=splits, embedding=embedding)
    vectordb = vectordb.as_retriever(search_kwargs={"k": 20})

    # Creating BM25Retriever from the text chunks
    bm25_retriever = BM25Retriever.from_documents(splits)
    bm25_retriever.k = 20

    return bm25_retriever, vectordb

# Function to implement the RAG approach for query answering
def rag_approach(query):
    # Processing the PDF file
    bm25_retriever, vectordb = file_processing(path)

    # Creating an ensemble retriever with BM25Retriever and FAISS vectorstore
    ensemble_retriever = EnsembleRetriever(retrievers=[bm25_retriever, vectordb], weights=[0.5, 0.5])

    # Getting relevant documents using the ensemble retriever
    ensemble_docs = ensemble_retriever.get_relevant_documents(query)

    # Template for the prompt
    prompt_template = """Assume the role of an ABB Budgetary Bid Engineer. Your task is to assist the Bid Team by extracting relevant information from the provided document as a vendor. If the information is not available or unknown, simply state that you do not know.

    {context}

    Question: {question}

    Answer:"""

    # Creating a PromptTemplate instance
    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    # Generating the response using the language model
    return llm.predict(text=PROMPT.format_prompt(
        context=ensemble_docs,
        question=query
    ).text)

# Function to get the results for a given query
def results(query_str):
    query_results = rag_approach(query_str)
    return str(query_results)
