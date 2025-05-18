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
        
        self.ngram_counts = {}
        self.prefix_counts = {}
        self.clean_sentences 
        self.tokenized_sentences = tokenized_sentences #  property

        self.clean_sentences = []
        self.maak_freq_tab()

 #       for sentence in tokenized_sentences:
            # Verwijder tokens die alleen interpunctie zijn, zet om naar kleine letters
#            sentence = [token.lower() for token in sentence if token not in string.punctuation]

            # Voeg n-1 <s> tokens toe aan het begin en </s> aan het eind
 #           padded = ['<s>'] * (n - 1) + sentence + ['</s>']
  #          self.vocab.update(padded)  # Voeg tokens toe aan de woordenschat

            # Tel alle n-grammen en hun context
 #           for i in range(len(padded) - n + 1):
  #              prefix = tuple(padded[i:i + n - 1])  # de eerste n-1 tokens (prefix)
  #              word = padded[i + n - 1]  # het n-de token (het woord dat volgt op de prefix)
  #              self.ngram_counts[prefix][word] += 1
    #            self.context_counts[prefix] += 1
        
        # test


        for sentence in self.tokenized_sentences:
            self.words_in_sentence = (n-1) *["<s>"]
            for word in sentence:
                if re.search(r"\b\w*\b", word): # \W stat voor letters
                    self.words_in_sentence.append(word.lower())
        self.words_in_sentence.append("</s>")
        self.clean_sentences.append(self.words_in_sentence)
            
    
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
        
        #V = len(set(clean_sentences)) # verzameling unieke woorden (voor smoothing)

        for word in ngram:
            if word not in self.vocabulary:
                return 0.0
        
        # Extract context (first n-1 words) and target word (last word)
        context = ngram[:-1]
        target_word = ngram[-1]
        
        # Get counts
        ngram_count = self.ngram_freq.get(ngram, 0)
        context_count = self.context_freq.get(context, 0)
        
        # Handle case where context was never seen
        if context_count == 0:
            return 0.0
        
        # Calculate probability based on smoothing
        if smoothing_constant == 0.0:
            # Raw probability: P(target | context) = count(ngram) / count(context)
            return ngram_count / context_count
        else:
            # Add-k smoothed probability: P(target | context) = (count(ngram) + k) / (count(context) + k * V)
            k = smoothing_constant
            V = len(self.vocabulary)
            return (ngram_count + k) / (context_count + k * V)

        

corpus = CorpusReader(r"C:\Users\wanne\Downloads\Computational Linguistics\small-corpus")
                  
lol = NgramModel(corpus.sents())
print(lol.clean_sentences[-100:])
print(lol.maak_freq_tab(lol.clean_sentences))