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

    for sentence in clean_sentences:
        prefix = (sentence[i], sentence[i+1])
    
    def probability(self, ngram, smoothing_constant=0.0):
        if smoothing_constant == 0.0:

            return P_raw
    
                    
corpus = CorpusReader(r"C:\Users\wanne\Downloads\Computational Linguistics\small-corpus") 
                  
lol = NgramModel(corpus.sents())
print(lol.clean_sentences[-100:])
print(lol.maak_freq_tab(lol.clean_sentences))