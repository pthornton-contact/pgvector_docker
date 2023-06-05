from langchain.embeddings import OpenAIEmbeddings
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.pgvector import PGVector
from langchain.document_loaders import TextLoader
from langchain.docstore.document import Document
from langchain.vectorstores.pgvector import PGVector

import os


os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')