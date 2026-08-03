from docx import Document

doc = Document("Questionario.docx")

def extractWord (doc):
    dados = []
    for p in doc.paragraphs:
        text = p.text
        if ":" in text:
            response = text.split(":", 1)
            dados.append(response)
    return dados
result = extractWord(doc) 


def tranform (dados):
    limpeza = []
    for l in dados:
             question = l[0].replace("\xa0", " ").strip("._ ")
             response = l[1].strip()
             limpeza.append([question,response])
    return limpeza
resultado = tranform(result)
print(resultado)



        
    

