import os
 

from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import TextLoader
from  langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

def main():
    print("Hello from rag-with-vector-datbase!")
    loader = TextLoader("../Resources/mediumblog1.txt")
    document =loader.load()




if __name__ == "__main__":
    main()
