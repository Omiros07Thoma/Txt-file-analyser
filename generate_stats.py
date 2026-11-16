def number_of_lines(text):
    return len(text.splitlines())

def number_of_paragraphs(text):
    return len([p for p in text.split("\n\n") if p.strip()])

def chars_with_spaces(text):
    return len(text)

def number_of_spaces(text):
    return text.count(" ")

def words_per_line(lines, words):
    average = words / lines
    return round(average, 2)

def words_per_sentence(sentences, words):
    average = words / sentences
    return round(average, 2)

def chars_per_word(words, chars):
    if words == 0:
        return 0
    return round(chars / words, 2)

def total_words(word_list):
    return len(word_list)

def unique_words(word_set):
    return len(word_set)

def total_chars(char_list):
    return len(char_list)

def unique_chars(char_set):
    return len(char_set)

def total_sentences(s_list):
    return len(s_list)

def longest_sentence(s_list):
    s_lenght = 0
    longest_sentence = None

    for element in s_list:
        if len(element) > s_lenght:
            s_lenght = len(element)
            longest_sentence = element
    return longest_sentence, s_lenght

def shortest_sentence(s_list):
    s_lenght = float("inf")
    shortest_sentence = None

    for element in s_list:
        if len(element) < s_lenght:
            s_lenght = len(element)
            shortest_sentence = element
    return shortest_sentence, s_lenght

def words_appearing_once(word_dict):
    words_appearing_once = 0

    for key in word_dict:
        if word_dict[key] == 1:
            words_appearing_once += 1
    return words_appearing_once

def automated_readability_index(word_list, char_list, sentence_list):
    ARI = 4.71 * (len(char_list) / len(word_list)) + 0.5 * (len(word_list) / len(sentence_list))
    return round(ARI, 2)

def sentence_length_distribution(sentence_list):
    lengths = []
    for sentence in sentence_list:
        words = sentence.split()
        lengths.append(len(words))
    return lengths
   

def most_common_words(word_list):
    from collections import Counter
    return Counter(word_list)

def most_common_chars(char_list):
    from collections import Counter
    return Counter(char_list)

def lowercase_count(char_list):
    import string
    number_lowercase = 0
    for char in char_list:
        if char in string.ascii_lowercase:
            number_lowercase += 1
    return number_lowercase

def uppercase_count(char_list):
    import string
    number_uppercase = 0
    for char in char_list:
        if char in string.ascii_uppercase:
            number_uppercase += 1
    return number_uppercase

def punctuation_count(char_list):
    import string
    punctuation_count = 0
    for char in char_list:
        if char in string.punctuation:
            punctuation_count += 1
    return punctuation_count