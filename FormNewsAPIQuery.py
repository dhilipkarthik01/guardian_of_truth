class FormNewsAPIQuery:
    
    def process(self, keywords):
        st = ""
        for word in keywords:
            st += " \"" + word + "\" "
        st = st.strip()
        self.query = st
        return self

    def getQuery(self):
        if len(self.query) == 0:
            return None
        return self.query