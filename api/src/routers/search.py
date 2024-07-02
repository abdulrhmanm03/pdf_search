from fastapi import APIRouter, Depends
from src.assets.embed_model import get_model
from src.db.database import get_collection
from src.db.db_ops import query_db

search_router = APIRouter(prefix="/search")


@search_router.get("/")
async def search(query: str, 
                 collection = Depends(get_collection),
                 model = Depends(get_model)):
    
    result = query_db(collection=collection,
                      model=model,
                      query=query)
            
    
    return {"Success": result}  