from docx import Document


doc = Document("Test.docx")

def extractWord (doc):
    for p in doc.paragraphs:
        dados = []
        text = p.text
        if ":" in text:
            response = text.split(":", 1)
            dados.append(response)
    return dados
result = extractWord(doc)
print(result) 


    
            
