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
        self.clean_sentences # is dit nodig?
        self.tokenized_sentences = tokenized_sentences #  property

        self.clean_sentences = []
        
        self.maak_freq_tab() # is dit nodig?

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
        
    def perplexity(self, sentence, smoothing_constant=1.0):
        
        clean_sentence = (self.n - 1) * [n-1]
        
        for word in clean_sentence:
            if re.search(r"\b\w*\b", word): # \W stat voor letters
                self.clean_sentence.append(word.lower())
                self.clean_sentence.append("</s>")
                
        if len(cleaned_sentences) < self.n:
            return float("inf")
        
        for i in range(len(cleaned_sentences) - self.n +1):
            ngram = tuple(cleaned_sentences[i:i + self.n])
        
        prob = self.probability(list(ngram), smoothing_constant)
        
        if prob == 0.0:
            return float("inf")
        
    def choose_succesor(self, prefix):
        prefix_tuple = tuple(word.lower() for word in prefix)
        if len(prefix_tuple) != self.n - 1:
            raise ValueError(f"Prefix heeft verkeerde lengte")

        if prefix_tuple not in self.ngram:
            return None
        
        successors_dict = self.ngram[prefix_tuple]
        if not successors_dict:
            return None
        
        words = list(successors_dict.keys())
        weights = list(successors_dict.values())
        
        chosen_word = random.choices(words, weights=weights, k=1)[0]
        return chosen_word
                
corpus = CorpusReader(r"C:\Users\wanne\Downloads\Computational Linguistics\small-corpus")
                  
lol = NgramModel(corpus.sents())
print(lol.clean_sentences[-100:])
print(lol.maak_freq_tab(lol.clean_sentences))