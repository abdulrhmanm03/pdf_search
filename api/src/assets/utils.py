import re


def pdf_to_pages(pdf):
    pages = []
    for page_number, page in enumerate(pdf):
        text = page.get_text()
        text = text.replace("\n", " ")
        text = re.sub(r'\uf761|\uf774|\uf76e|\uf764|\uf76b|\uf769|\uf779|\uf777|\uf76f|\uf766|\uf772|\uf769|\uf765|\uf773', '', text)
        text = re.sub(r'\s+', ' ', text) 
        text = text.strip()
        page_number += 1
        pages.append({"page_number": page_number,
                      "text": text})
    return pages    


def embed_pdf_pages(pdf_pages, model):
    
    pages_text = [page["text"] for page in pdf_pages]
    embedded_pages = model.encode(pages_text)
    
    return embedded_pages

