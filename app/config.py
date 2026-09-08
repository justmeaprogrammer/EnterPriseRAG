import os
import sys
from dotenv import load_dotenv
load_dotenv()

from utils.exception import CustomException
from utils.logger import get_logger
logger = get_logger(__name__)

class Settings:
    try:
        GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")    
        GROQ_API_KEY=os.getenv("GROQ_API_KEY")
        QDRANT_API_KEY=os.getenv("QDRANT_API_KEY")
        QDRANT_CLUSTER_ENDPOINT=os.getenv("QDRANT_CLUSTER_ENDPOINT")
        QDRANT_COLLECTION = os.getenv("QDRANT_COLLECTION")
        
        
    
    except Exception as e:
        logger.error("Failed to fetch API keys")
        raise CustomException(e,sys)
    
settings = Settings()