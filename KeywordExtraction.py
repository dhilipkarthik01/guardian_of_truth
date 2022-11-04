import spacy
import en_core_web_sm

class KeywordExtraction:
    def __init__(self):
        self.nlp = en_core_web_sm.load()
    
    def extractKeywords(self, processed_text, lowercase=True):
        self.text = processed_text
        doc = self.nlp(self.text)
        if lowercase:
            lower_maped = map(lambda st: str(st).lower(), doc.ents) 
            self.keywords = list(set(lower_maped))
        else:
            self.keywords = list(set(doc.ents))
        return self

    def getKeywords(self):
        return self.keywords

if __name__ == "__main__":
    st = "My name is Rizwan Mohamed Kareem. I am from Chennai. I study at VIT."
    keyword_extraction = KeywordExtraction().extractKeywords(st).getKeywords()
    print(keyword_extraction)
