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
        """self.tokenized_sentences = tokenized_sentences #  property
    
        self.clean_sentences = []

        for sentence in self.tokenized_sentences:
            self.words_in_sentence = [n*"<s>"]
            for word in sentence:
                if re.search(r"\b\w*\b", word): # \W stat voor letters
                    self.words_in_sentence.append(word.lower())
            self.words_in_sentence.append("</s>")
            self.clean_sentences.append(self.words_in_sentence)""" "even comment van gemaakt"

        self.n = n  # grootte van de ngram
        self.vocab = set()  # verzameling unieke woorden (voor smoothing)
        
        self.ngram_counts = {}
        self.prefix_counts ={}
       
        self.maak_freq_tab()

        for sentence in sentences:
            # Verwijder tokens die alleen interpunctie zijn, zet om naar kleine letters
            sentence = [token.lower() for token in sentence if token not in string.punctuation]

            # Voeg n-1 <s> tokens toe aan het begin en </s> aan het eind
            padded = ['<s>'] * (n - 1) + sentence + ['</s>']
            self.vocab.update(padded)  # Voeg tokens toe aan de woordenschat

            # Tel alle n-grammen en hun context
            for i in range(len(padded) - n + 1):
                prefix = tuple(padded[i:i + n - 1])  # de eerste n-1 tokens (prefix)
                word = padded[i + n - 1]  # het n-de token (het woord dat volgt op de prefix)
                self.ngram_counts[prefix][word] += 1
                self.context_counts[prefix] += 1
            
    
    def maak_freq_tab(self, clean_sentences): # maakt een frequency tabel
        freq_dict = dict()
        
        for sentence in self.clean_sentences:
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

    def probability(self, ngram, smoothing_constant=0.0):

        if len(ngram) != self.n:
            raise ValueError(f"Ngram moet lengte {self.n} hebben")

        prefix = tuple(ngram[:-1])  # eerste n-1 woorden
        
        word = ngram[-1]  # het woord dat we willen voorspellen
        if prefix not in self.context_counts:
            return 0.0  # prefix onbekend => kans is 0

        prefix_count = self.context_counts[prefix]  # aantal keer dat de prefix voorkomt
        word_count = self.ngram_counts[prefix].get(word, 0)  # aantal keer dat het woord volgde op die prefix

        V = len(self.vocab)  # grootte van de woordenschat, voor smoothing

        if smoothing_constant == 0.0:
            if word_count == 0:
                return 0.0
            return word_count / prefix_count
        else:
            # add-k smoothing
            return (word_count + smoothing_constant) / (prefix_count + smoothing_constant * V)
        

corpus = CorpusReader(r"C:\Users\wanne\Downloads\Computational Linguistics\small-corpus")
                  
lol = NgramModel(corpus.sents())
print(lol.clean_sentences[-100:])
print(lol.maak_freq_tab(lol.clean_sentences))