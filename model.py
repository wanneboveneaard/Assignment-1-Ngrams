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
            
        self.ngram_counts = {}
        self.prefix_counts ={}
        
        self.maak_freq_tab()
        
            
    
    def maak_freq_tab(self, clean_sentences): 
        """
        Create freq table and ?
        """
        freq_dict = dict()
        for sentence in clean_sentences:
            for i in range(len(sentence) - self.n - 1):
                prefix = tuple(sentence[i:i+ (self.n - 1)])
                next_word = sentence[i+self.n - 1]
                #ngram = tuple(sentence[i:i+self.n])
                if prefix not in self.ngram_counts:
                    self.ngram_counts[prefix] = {}
                
                if next_word not in self.ngram_counts[prefix]:
                    self.ngram_counts[prefix][next_word] = 0
                
                self.ngram_counts[prefix][next_word] += 1
                
                if prefix not in self.prefix_counts:
                    self.prefix_counts[prefix] = 0
                
                self.prefix_counts[prefix] += 1
                
        return freq_dict
    
   
corpus = CorpusReader(r"C:\Users\wanne\Downloads\Computational Linguistics\small-corpus") 
                  
lol = NgramModel(corpus.sents(), 3)
#print(lol.clean_sentences[-1:])
print(lol.maak_freq_tab(lol.clean_sentences))