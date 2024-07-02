from sentence_transformers import SentenceTransformer
from src.config import config

model_id =config["MODEL_ID"]
device = config["DEVICE"]
        
def get_model(): 
    return SentenceTransformer(model_id, device = device)       

