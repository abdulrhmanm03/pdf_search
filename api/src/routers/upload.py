from fastapi import APIRouter, Depends, UploadFile, HTTPException
import pymupdf
from src.assets.embed_model import get_model
from src.db.database import get_collection
from src.assets.utils import pdf_to_pages, embed_pdf_pages
from src.db.db_ops import add_to_db


upload_router = APIRouter(prefix="/upload_file")

@upload_router.post("/")
async def upload_file(file: UploadFile,
                      collection = Depends(get_collection),
                      model = Depends(get_model)):
    
    try:
        pdf_content = await file.read()
        pdf_document = pymupdf.open(stream=pdf_content, filetype="pdf")
    except Exception:
        raise HTTPException(status_code=422, detail=f"Failed to read file")
    
    pages =pdf_to_pages(pdf_document)
    embedded_pages = embed_pdf_pages(pdf_pages=pages, model=model)
    
    add_to_db(collection=collection, pdf_pages=pages,
              embedded_pages=embedded_pages, title=file.filename)
    
    return {"Success": file.filename}
