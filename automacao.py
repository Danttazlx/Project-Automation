from docx import Document

doc = Document("")

def extract (doc):
    dataRaw = []
    for p in doc.paragraphs:
        text = p.text
        if ":" in text:
            response = text.split(":", 1)
            dataRaw.append(response)  
    return dataRaw
result = extract(doc) 


def transform (result):
    cleaning = []
    for l in result:
             question = l[0].replace("\xa0", " ").strip("._ ")
             response = l[1].strip()
             cleaning.append([question,response])
    return cleaning
result_transform = transform(result)
print(result)   


def load (result_transform):
     with open("Questionario_padronizado.txt", "w", encoding="utf-8") as file:
          for l in result_transform:
               file.write(f"{l[0]}:{l[1]}\n")
result_load = load(result_transform)
print(result_load)


     



        
    

