import spacy
import en_core_web_sm

class KeywordExtraction:
    def __init__(self, processed_text):
        self.text = processed_text
    
    def extractKeywords(self, lowercase=True):
        nlp = en_core_web_sm.load()
        doc = nlp(self.text)
        if (lowercase):
            lower_maped = map(lambda st: str(st).lower(), doc.ents) 
            self.keywords = list(set(lower_maped))
        else:
            self.keywords = list(set(doc.ents))

    def getKeywords(self):
        return self.keywords
    

