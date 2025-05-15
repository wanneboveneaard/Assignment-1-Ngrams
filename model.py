# -*- coding: utf-8 -*-
"""
Created on Thu May  8 12:40:00 2025

@author: wanne
"""

import re
from corpusreader import CorpusReader

class NgramModel:
    
    def __init__(self, tokenized_sentences, n):
        """accepts a list of tokenized sentences and ...?"""
        self.tokenized_sentences = tokenized_sentences #  property
    
        self.clean_sentences = []

        for sentence in self.tokenized_sentences:
            self.words_in_sentence = [n*"<s>"]
            for word in sentence:
                if re.search(r"\b\w*\b", word): # \W stat voor letters
                    self.words_in_sentence.append(word.lower())
            self.words_in_sentence.append("</s>")
            self.clean_sentences.append(self.words_in_sentence)
            
    
    def maak_freq_tab(self, clean_sentences): # maakt een frequency tabel
        freq_dict = dict()
        for sentence in clean_sentences:
            for i in range(n-1, len(sentence)):
                if word in freq_dict:
                    freq_dict[word] += 1
                else:
                    freq_dict[word] = 1
        return freq_dict
    
        
                    
corpus = CorpusReader(r"C:\Users\wanne\Downloads\Computational Linguistics\small-corpus") 
                  
lol = NgramModel(corpus.sents())
print(lol.clean_sentences[-100:])
print(lol.maak_freq_tab(lol.clean_sentences))