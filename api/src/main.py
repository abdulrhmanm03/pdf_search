from fastapi import FastAPI
from src.routers import search, upload


app = FastAPI()

app.include_router(upload.upload_router)
app.include_router(search.search_router)