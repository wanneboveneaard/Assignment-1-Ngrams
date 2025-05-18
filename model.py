"""
model.py implements an N-gram language model.
authors: Mela, Wanne, Jacob
"""

import re
from corpusreader import CorpusReader
import random
import math

class NgramModel:
    """
    accepts a list of tokenized sentences and builds n-gram model, 
    and includes functions to calculate probabilities,
    and perplexity.
    """
    def __init__(self, tokenized_sentences, n):
        """
        accepts a list of tokenized sentences,
        and stores frequency tables
        """
        self.n = n
        
        self.ngram_counts = {}
        self.prefix_counts = {}
        self.tokenized_sentences = tokenized_sentences

        self.clean_sentences = []
        
        for sentence in self.tokenized_sentences:
            words_in_sentence = (n - 1) * ["<s>"]
            for word in sentence:
                if re.search(r"\b\w+\b", word):
                    words_in_sentence.append(word.lower())
            words_in_sentence.append("</s>")
            self.clean_sentences.append(words_in_sentence)

        self.vocabulary = set()
        self.context_freq = {}
        self.ngram_freq = {}
        self.maak_freq_tab()
    
    def maak_freq_tab(self):
        """ 
        creates frequency tables for n-grams
        """
        for sentence in self.clean_sentences:
            for i in range(len(sentence) - self.n + 1):
                prefix = tuple(sentence[i:i + (self.n - 1)])
                next_word = sentence[i + self.n - 1]
                ngram = prefix + (next_word,)

                self.vocabulary.add(next_word)

                self.ngram_freq[ngram] = self.ngram_freq.get(ngram, 0) + 1

                self.context_freq[prefix] = self.context_freq.get(prefix, 0) + 1

                if prefix not in self.ngram_counts:
                    self.ngram_counts[prefix] = {}
                if next_word not in self.ngram_counts[prefix]:
                    self.ngram_counts[prefix][next_word] = 0
                self.ngram_counts[prefix][next_word] += 1

                self.prefix_counts[prefix] = self.prefix_counts.get(prefix, 0) + 1
    
    def probability(self, ngram, smoothing_constant=0.0):
        """ 
        calculates the probability of a given n-gram,
        using optional add-k smoothing
        """
        if smoothing_constant == 0.0:
            for word in ngram:
                if word not in self.vocabulary:
                    return 0.0    
            
        context = tuple(ngram[:-1])
        target_word = ngram[-1]
        full_ngram = context + (target_word,)

        ngram_count = self.ngram_freq.get(full_ngram, 0)
        context_count = self.context_freq.get(context, 0)

        if context_count == 0:
            return 0.0

        if smoothing_constant == 0.0:
            return ngram_count / context_count
        else:
            k = smoothing_constant
            V = len(self.vocabulary)
            return (ngram_count + k) / (context_count + k * V)
        
    def perplexity(self, sentence, smoothing_constant=1.0):
        """
        calculates the perplexity of a given sentence,
        lower perplexity means the sentence is more likely
        """
        clean_sentence = (self.n - 1) * ["<s>"]
        for word in sentence:
            if re.search(r"\b\w+\b", word):
                clean_sentence.append(word.lower())
        clean_sentence.append("</s>")

        if len(clean_sentence) < self.n:
            return float("inf")

        log_prob_sum = 0.0
        for i in range(len(clean_sentence) - self.n + 1):
            ngram = clean_sentence[i:i + self.n]
            prob = self.probability(ngram, smoothing_constant)
            if prob == 0.0:
                return float("inf")
            log_prob_sum += -1 * (math.log(prob, 2))
        
        return 2 ** (log_prob_sum / len(clean_sentence))

    def choose_successor(self, prefix):
        """ 
        randomly select a next word, when a prefix is given,
        based on the learned frequencies
        """
        prefix_tuple = tuple(word.lower() for word in prefix)
        if len(prefix_tuple) != self.n - 1:
            raise ValueError("Prefix heeft verkeerde lengte")

        if prefix_tuple not in self.ngram_counts:
            return None
        
        successors_dict = self.ngram_counts[prefix_tuple]
        if not successors_dict:
            return None
        
        words = list(successors_dict.keys())
        weights = list(successors_dict.values())
        
        chosen_word = random.choices(words, weights=weights, k=1)[0]
        return chosen_word

corpus = CorpusReader(r"C:\Users\wanne\Downloads\Computational Linguistics\small-corpus")
lol = NgramModel(corpus.sents(), 2)
#print(lol.ngram_counts)
