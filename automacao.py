from docx import Document

doc = Document("questionario.docx")

def extract (doc):
    data = []
    for p in doc.paragraphs:
        text = p.text
        if ":" in text:
            response = text.split(":", 1)
            data.append(response)
    return data
result = extract(doc) 


def transform (data):
    cleaning = []
    for l in data:
             question = l[0].replace("\xa0", " ").strip("._ ")
             response = l[1].strip()
             cleaning.append([question,response])
    return cleaning
result = transform(result)
print(result)



        
    

