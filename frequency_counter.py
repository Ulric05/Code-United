def count_words(sentence):
    # Remove punctuation and convert the sentence to lowercase
    sentence = sentence.lower().replace(",", "").replace(".", "").replace("!", "").replace("?", "")
    
    # Split the sentence into words using whitespace as the delimiter
    words = sentence.split()
    print(f"The split words are {words}")
    
    # Initialize an empty dictionary to store word counts
    word_count = {}
    
    # Loop through each word in the list and count occurrences
    for w in words:
        if w in word_count:
            word_count[w] += 1
        else:
            word_count[w] = 1
    
    return word_count
