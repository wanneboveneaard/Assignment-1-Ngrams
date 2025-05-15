# -*- coding: utf-8 -*-
"""
Created on Thu May  8 12:40:00 2025

@author: wanne
"""

import re

class NgramModel:
    def __init_(self, tokenized_sentences):
        """accepts a list of tokenized sentences and ...?"""
        self.tokenized_sentences = tokenized_sentences
        
        # [ [..., ...,...,...], [..., ...,...,...], [..., ...,...,...], ...]
        
        for sentence in tokenized_sentences:
            for word in sentence:
                if re.search(r"\b\W\b", word):
                    sentence.remove(word)
                    tokenized_sentences = word.lower()
                    
        