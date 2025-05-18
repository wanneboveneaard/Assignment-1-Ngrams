import re
from corpusreader import CorpusReader

class NgramModel:
    
    def __init__(self, tokenized_sentences, n):
        """accepts a list of tokenized sentences and ...?"""
        self.tokenized_sentences = tokenized_sentences #  property
        self.n = n # hiermee kan n ook in andere functiedefinities kunnen worden geimplementeerd direct
    
        self.clean_sentences = []

        for sentence in self.tokenized_sentences:
            self.words_in_sentence = (n-1) * ["<s>"]
            for word in sentence:
                if re.search(r"\b\w*\b", word): # \W stat voor letters
                    self.words_in_sentence.append(word.lower())
            self.words_in_sentence.append("</s>")
            self.clean_sentences.append(self.words_in_sentence)
            
    
    def maak_freq_tab(self, clean_sentences): 
        """
        Create freq table and ?
        """
        freq_dict = dict()
        for sentence in clean_sentences:
            for i in range(len(sentence) - self.n + 1):
                ngram = tuple(sentence[i:i+self.n])
                if ngram in freq_dict:
                    freq_dict[ngram] += 1
                else:
                    freq_dict[ngram] = 1
                    
        return freq_dict
    
    def probability(self, ngram, smoothing_constant=0.0):
        prefix = tuple(ngram[:-1]) # Ik houd van pizza, n=3, prefix: houd van pizza / houd van whatever
        word = ngram[-1]
        
        prefix_count =  self.freq_dict.get(prefix, 0)
        word_count = self.freq_dict.get(word, 0)
        
        if word_count == 0:
            P_raw = 0
        
        if smoothing_constant == 0.0:
            P_raw = prefix_count / word_count
        else: 
            # met add-k smoothing
           
        return P_raw
                    
corpus = CorpusReader(r"C:\Users\wanne\Downloads\Computational Linguistics\small-corpus") 
                  
lol = NgramModel(corpus.sents(), 3)
#print(lol.clean_sentences[-1:])
print(lol.maak_freq_tab(lol.clean_sentences))