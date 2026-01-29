from src.vector_store import VectorStoreBuilder
from src.recommender import Recommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

class RecommendationPipeline:
    def __init__(self, vector_store_dir: str="chroma_db"):
        try:
            logger.info("Initializing recommendation pipeline...")
            self.vector_store_builder = VectorStoreBuilder(processed_csv_path="", persist_directory=vector_store_dir)
            self.retriever = self.vector_store_builder.load_vector_store().as_retriever()
            self.recommender = Recommender(self.retriever, GROQ_API_KEY, MODEL_NAME)
            logger.info("Recommendation pipeline initialized successfully.")
        except Exception as e:
            logger.error(f"Failed to initialize recommendation pipeline: {e}")
            raise CustomException(e)

    def get_recommendations(self, query: str, top_k: int=5):
        logger.info(f"Generating recommendations for query: {query}")
        try:
            recommendations = self.recommender.get_recommendations(query)
            logger.info("Recommendations generated successfully.")
            return recommendations
        except Exception as e:
            logger.error(f"Failed to generate recommendations: {e}")
            raise CustomException(e)
