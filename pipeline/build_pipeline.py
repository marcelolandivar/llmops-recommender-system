from src.data_loader import DataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()
logger = get_logger(__name__)

def main():
    """Build the recommendation system pipeline by loading data and creating the vector store."""
    try:
        logger.info("Starting data loading process...")
        data_loader = DataLoader(original_csv_path="data/anime_with_synopsis.csv", 
                                      processed_csv_path="data/processed_data.csv")
        processed_csv = data_loader.load_data()

        logger.info("Data loaded successfully.")

        vector_store_builder = VectorStoreBuilder(processed_csv_path=processed_csv)
    
        logger.info("Creating vector store...")
        vector_store = vector_store_builder.create_vector_store()
        logger.info("Vector store created successfully.")

        logger.info("Pipeline built successfully.")

    except Exception as e:
        logger.error(f"Failed to build pipeline: {e}")
        raise CustomException(e)
    
if __name__ == "__main__":
    main()