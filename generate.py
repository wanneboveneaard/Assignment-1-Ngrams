def generate_sentence(ngram_model):
    n = ngram_model.n
    generated_sentence = ["<s>" * (n-1)]
    
    while True:
        prefix = generated_sentence[-(n - 1):]
        next_word = ngram_model.choose_successor(prefix)
    
        if next_word is None or "</s>":
            break
        
        generated_sentence.append(next_word)
    
    return generated_sentence
    
#Hier begint de executable sectie
if __name__ == "__main__":
    # Lees pad naar corpus en n-waarde uit command line
if len(sys.argv) > 1:
    = sys.argv[1]
        else:
        corpus_path = "./train"

    if len(sys.argv) > 2:
        n = int(sys.argv[2])
    else:
        n = 2

    # Stap 2: Lees corpus en maak model
    corpus = CorpusReader(corpus_path)
    sentences = corpus.sents()
    model = NgramModel(sentences, n)

    # Stap 3: Genereer en print twee zinnen
    print("> " + " ".join(generate))
