from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv
load_dotenv()

"""
    Loads processed data from a CSV file, splits the text into manageable chunks,
    and creates a Chroma vector store for efficient retrieval.
"""

class VectorStoreBuilder:
    def __init__(self, processed_csv_path: str, persist_directory: str="chroma_db"):
        self.processed_csv_path = processed_csv_path
        self.persist_directory = persist_directory
        self.embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    def create_vector_store(self) -> Chroma:
        """Create a Chroma vector store from the processed CSV data."""
        # Load documents from the processed CSV file
        loader = CSVLoader(file_path=self.processed_csv_path, encoding='utf-8', metadata_columns=[])
        documents = loader.load()

        # Split documents into smaller chunks
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        split_documents = text_splitter.split_documents(documents)

        # Create and persist the Chroma vector store
        vector_store = Chroma.from_documents(
            documents=split_documents,
            embedding=self.embedding_model,
            persist_directory=self.persist_directory
        )
        return vector_store

    def load_vector_store(self) -> Chroma:
        """Load the Chroma vector store from disk."""
        return Chroma(persist_directory=self.persist_directory, embedding_function=self.embedding_model)