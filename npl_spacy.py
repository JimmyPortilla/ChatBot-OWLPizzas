import spacy
nlp = spacy.load("en_core_web_sm")

def spacy_info(text):
    doc = nlp(text)
    print([(w.text, w.pos_) for w in doc])
    return doc

if __name__ == '__main__':
    item = "hola como estas"
    doc = spacy_info(item)
    for w in doc:
        print(w.text, w.pos_)