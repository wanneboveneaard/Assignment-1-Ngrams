import os
import nltk

class CorpusReader:
    """Read the contents of a directory of files, and return the results as
    either a list of lines or a list of words.
    """

    def __init__(self, directory):
        """
        Initialize a CorpusReader object. This function stores the path to 
        the corpus directory.
        """

        self.directory = directory

        if not (os.path.isdir(directory)):
            raise ValueError(directory + " does not exist or is not a directory")

    def _get_all_text(self):
        """Read all text in the corpus and return it as one string"""
    

        all_text_list = []

        for filename in os.listdir(self.directory):
            if filename.endswith(".txt"):
                with open(self.directory + "/" + filename, 'r', encoding='utf-8') as infile:
                    file_text = infile.read()
                    all_text_list.append(file_text)

        all_text_string = "\n".join(all_text_list)

        return all_text_string

    def sents(self):
        """return the text of the corpus as a list of tokenized sentences"""

        text = self._get_all_text()

        lines = nltk.sent_tokenize(text)

        tokenized_sentences = []
        
        for line in lines:
            words = nltk.word_tokenize(line)
            tokenized_sentences.append(words)
    
        
        return tokenized_sentences
    
corpus = CorpusReader(r"C:\Users\wanne\Downloads\Computational Linguistics\small-corpus")
sentences = corpus.sents()