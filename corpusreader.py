# -*- coding: utf-8 -*-
"""
Created on Thu May  8 12:39:27 2025

@author: wanne
"""

import os, re

class CorpusReader:
    """Read the contents of a directory of files, and return the results as
    either a list of lines or a list of words.

    The pathname of the directory to read should be passed when
    creating the class:

    >>> reader = CorpusReader(r"path/to/dir")
    """

    def __init__(self, directory): # path/to/dir wordt doorgegeven aan __init__
        """
        Initialize a CorpusReader object. This function stores the path to 
        the corpus directory.
        """

        self.directory = directory
        # self om te verwijzen naar instantie van deze klasse

        if not (os.path.isdir(directory)):
            # checken of filename bestaat
            raise ValueError(directory + " does not exist or is not a directory")

    def _get_all_text(self):
        """Read all text in the corpus and return it as one string"""

        all_text_list = [] # lijst waarvan elke tekstbestand 1 element is

        for filename in os.listdir(self.directory):
            if filename.endswith(".txt"):
                with open(self.directory + "/" + filename, 'r', encoding='utf-8') as infile:
                    file_text = infile.read()
                    all_text_list.append(file_text)

        all_text_string = "\n".join(all_text_list)

        return all_text_string

    def sents(self):
        """return the text of the corpus as a list of tokenized sentences"""

        text = self._get_all_text() # een lange string van alle files

        lines = text.splitlines()

        tokenized_sentences = []
        
        for line in lines:
            words = line.split() # elke line in woorden splitten
            tokenized_sentences.append(words) # elke gesplitte line toevoegen aan lijst
        
        return tokenized_sentences