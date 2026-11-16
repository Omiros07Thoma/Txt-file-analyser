import string
 
 
def word_list(text):
    word = ""
    word_list = []
 
    for char in text:
        if char in string.ascii_letters or char == "'":
            word = word + char
        else:
            word = word.strip("'")
            if word != "":
                word_list.append(word.lower())
            word = ""
    # the last word, in case the text doesn't end with a space or punctuation
    word = word.strip("'")
    if word != "":
        word_list.append(word.lower())
    return word_list
 
 
def word_set(text):
    word_set = set()
    for word in word_list(text):
        word_set.add(word)
    return word_set
 
 
def word_dict(text): #creates a dictionary with unique words in the book as the key and number of times that word appears as the value
    word_dict = dict()
    for word in word_list(text):
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict
 
 
def sentence_list(text):
    sentence = ""
    sentence_list = []
 
    for char in text:
        if char not in ".!?":
            sentence = sentence + char
        else:
            sentence = " ".join(sentence.split())  # removes newlines and extra spaces
            if sentence != "":
                sentence_list.append(sentence)
            sentence = ""
    # the last sentence, in case the text doesn't end with . ! or ?
    sentence = " ".join(sentence.split())
    if sentence != "":
        sentence_list.append(sentence)
    return sentence_list
 
 
def sentence_set(text):
    sentence_set = set()
    for sentence in sentence_list(text):
        sentence_set.add(sentence)
    return sentence_set
 
 
def sentence_dict(text):
    sentence_dict = dict()
    for sentence in sentence_list(text):
        if sentence in sentence_dict:
            sentence_dict[sentence] += 1
        else:
            sentence_dict[sentence] = 1
    return sentence_dict
 
 
def char_list(text):
    char_list = []
 
    for char in text:
        if char not in string.whitespace:
            char_list.append(char)
    return char_list
 
 
def char_set(text):
    char_set = set()
 
    for char in text:
        if char not in string.whitespace:
            char_set.add(char)
    return char_set
 
 
def char_dict(text):
    char_dict = dict()
 
    for char in text:
        if char not in string.whitespace:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict
 