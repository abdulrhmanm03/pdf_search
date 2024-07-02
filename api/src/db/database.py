import chromadb

client = chromadb.PersistentClient(path="database")

def get_collection():
    return client.get_or_create_collection(name="pdf_collection",
                                            metadata={"hnsw:space": "cosine"})
