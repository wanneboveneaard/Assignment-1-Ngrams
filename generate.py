
    
from corpusreader import CorpusReader
from model import NgramModel
import sys
import nltk

def generate_sentence(ngram_model):
    n = ngram_model.n
    generated_sentence = ["<s>"] * (n-1)

    while True:
        prefix = generated_sentence[-(n - 1):]
        next_word = ngram_model.choose_successor(prefix)
        if next_word is None or next_word == "</s>":
            break
        generated_sentence.append(next_word)
        
    sentence = generated_sentence[(n - 1):]
    
    if sentence:
        sentence[0] = sentence[0].capitalize()
        
    sentence[-1] = sentence[-1] + "."

    return sentence


#executable section
if __name__ == "__main__":
    # Stap 1: Lees pad naar corpus en n-waarde uit command line
    if len(sys.argv) > 1:
        corpus_path = sys.argv[1]
    else:
        corpus_path = "./train"

    if len(sys.argv) > 2:
        n = int(sys.argv[2])
    else:
        n = 2

    # Lees corpus en maak model
    corpus = CorpusReader(corpus_path)
    sentences = corpus.sents()
    model = NgramModel(sentences, n)

    # Genereer en print twee zinnen
    print("> " + " ".join(generate_sentence(model)))
    print()
    print("> " + " ".join(generate_sentence(model)))

    # Bereken perplexities van gegeven zinnen
    print("\nSentence perplexities:\n")

    test_sentences = [
        "Suggestive, Watson, is it not?",
        "It is amazing that a family can be torn apart by something as simple as a pack of wild dogs!",
        "So spoke Sherlock Holmes and turned back to the great scrapbook in which he was arranging and indexing some of his recent material.",
        "What I like best about my friends is that they are few.",
        "Friends what is like are they about I best few my that."
    ]

    for sentence in test_sentences:
        tokens = nltk.word_tokenize(sentence)
        perplexity = model.perplexity(tokens)
        print(f'"{sentence}" -> Perplexity: {perplexity}')

print(model.choose_successor(["<s>"]))  # of ["<s>", "<s>"] bij trigram