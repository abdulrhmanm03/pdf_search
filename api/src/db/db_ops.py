def add_to_db(collection , pdf_pages, embedded_pages, title):
    
    metadata = [
        {
            "page_number": page["page_number"],
            "title": title
        }
        for page in pdf_pages
    ]
    ids = [
        title + '_' + str(i)
        for i in range( len(pdf_pages) )
    ]
    documents = [page["text"] for page in pdf_pages]
    collection.add(
        documents=documents,
        embeddings=embedded_pages,
        metadatas=metadata,
        ids=ids)
    
    
def query_db(collection, model, query):
    query_embed = model.encode(query).tolist()
    
    return collection.query(
             query_embeddings=query_embed,
             n_results=1)    