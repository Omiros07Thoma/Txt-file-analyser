import export_report as report
import generate_stats as genstats
import create_function as createfuncs
import plotting as plt
from collections import Counter
import os

def open_single_book(selected_book):
    print(f'Analysing {selected_book}...')
    path = os.path.join(r"C:\Users\othom\project", selected_book)
    with open(path, "r", encoding="utf-8") as book:
        single_book_dict = single_book_analysis(selected_book, book)
    print("Completed analysis")
    analysis_single_book_menu(single_book_dict)

def single_book_analysis(book_name, book):
    book.seek(0)
    text = book.read()

    sentence_list = createfuncs.sentence_list(text)
    #sentence_set = createfuncs.sentence_set(book) #DELETE??
    #sentences_dict = createfuncs.sentence_dict(book) #DELETE??
    word_list = createfuncs.word_list(text)
    word_set = set(word_list)
    word_dict = dict(Counter(word_list))
    char_list = createfuncs.char_list(text)
    char_set = createfuncs.char_set(text)
    #char_dict = createfuncs.char_dict(book) 
    
    number_of_lines = genstats.number_of_lines(text)
    words_per_line = genstats.words_per_line(number_of_lines, len(word_list))
    words_per_sentence = genstats.words_per_sentence(len(sentence_list), len(word_list))
    chars_per_word = genstats.chars_per_word(len(word_list), len(char_list))
    total_words = genstats.total_words(word_list)
    unique_words = genstats.unique_words(word_set)
    total_chars = genstats.total_chars(char_list)
    total_sentences = genstats.total_sentences(sentence_list)
    unique_chars = genstats.unique_chars(char_set)
    word_appearing_once = genstats.words_appearing_once(word_dict)
    longest_sentence = genstats.longest_sentence(sentence_list)
    shortest_sentence = genstats.shortest_sentence(sentence_list)
    ARI = genstats.automated_readability_index(word_list, char_list, sentence_list)
    number_of_paragraphs = genstats.number_of_paragraphs(text)
    punctuation_count = genstats.punctuation_count(char_list)
    uppercase_count = genstats.uppercase_count(char_list)
    lowercase_count = genstats.lowercase_count(char_list)
    chars_with_spaces = genstats.chars_with_spaces(text)
    number_of_spaces = genstats.number_of_spaces(text)
    sentence_length_distribution = genstats.sentence_length_distribution(sentence_list)
    most_common_words = genstats.most_common_words(word_list)
    most_common_chars = genstats.most_common_chars(char_list)

    stats_dict = {
        "book_name": book_name,
        "number_of_lines": number_of_lines,
        "words_per_line": words_per_line,
        "words_per_sentence": words_per_sentence,
        "chars_per_word": chars_per_word,
        "total_words": total_words,
        "unique_words": unique_words,
        "total_chars": total_chars,
        "total_sentences": total_sentences,
        "unique_chars": unique_chars,
        "words_appearing_once": word_appearing_once,
        "longest_sentence": longest_sentence,
        "shortest_sentence": shortest_sentence,
        "ARI": ARI,
        "number_of_paragraphs": number_of_paragraphs,
        "punctuation_count": punctuation_count,
        "uppercase_count": uppercase_count,
        "lowercase_count": lowercase_count,
        "chars_with_spaces": chars_with_spaces,
        "number_of_spaces": number_of_spaces,
        "sentence_length_distribution": sentence_length_distribution,
        "most_common_words": most_common_words,
        "most_common_chars": most_common_chars,
    }

    return stats_dict

def analysis_single_book_menu(single_book_dict):
    print("Single Book Analysis:")
    print("1. General Statistics")
    print("2. Word Analysis")
    print("3. Character Statistics")
    print("4. Sentence Statistics")
    print("5. Export Summary")
    print("0. Return to main menu")
    n = int(input("Enter the number of the analysis you want to see: "))

    match n:
        case 1:
            general_stats(single_book_dict)
            plt.plot_text_composition(single_book_dict["number_of_lines"], single_book_dict["number_of_paragraphs"], single_book_dict["total_sentences"], single_book_dict["total_words"], single_book_dict["unique_words"])
            plt.plot_character_types_pie(single_book_dict)
            analysis_single_book_menu(single_book_dict)
        case 2:
            word_stats(single_book_dict)
            plt.single_total_words(single_book_dict["total_words"])
            plt.unique_words(single_book_dict["total_words"], single_book_dict["unique_words"])
            plt.plot_10_most_common_words(single_book_dict["most_common_words"], single_book_dict["book_name"])
            plt.plot_word_length_histogram(single_book_dict["most_common_words"], single_book_dict["book_name"])
            analysis_single_book_menu(single_book_dict)
        case 3:
            char_stats(single_book_dict)
            plt.plot_character_types_pie(single_book_dict)
            plt.plot_10_most_common_chars(single_book_dict["most_common_chars"], single_book_dict["book_name"])
            analysis_single_book_menu(single_book_dict)   
        case 4:
            sentence_stats(single_book_dict)
            plt.plot_sentence_length_histogram(single_book_dict["sentence_length_distribution"], single_book_dict["book_name"])
            plt.plot_common_sentence_lengths(single_book_dict["sentence_length_distribution"])
            analysis_single_book_menu(single_book_dict)
        case 5:
            report.export_report(single_book_dict)
            analysis_single_book_menu(single_book_dict)
        case 0:
            return 
        case _:
            print("Invalid entry, try again.")
            analysis_single_book_menu(single_book_dict)

def general_stats(stats):
    print(f'''
Basic Statistics for {stats["book_name"]}
{"-" * 45}
Lines: {stats["number_of_lines"]}
Sentences: {stats["total_sentences"]}
Paragraphs: {stats["number_of_paragraphs"]}
Words: {stats["total_words"]}
Unique words: {stats["unique_words"]}
Characters (with spaces): {stats["chars_with_spaces"]}
Characters (without spaces): {stats["total_chars"]}
Average words per line: {stats["words_per_line"]}
Average word length: {stats["chars_per_word"]}
Average words per sentence: {stats["words_per_sentence"]}
Automated Readability Index: {stats["ARI"]}
{"-" * 45}
''')

def word_stats(stats):
    print(f'''
Word Analysis for {stats["book_name"]}
{"-" * 45}
Most common words:   ''')
    for word, count in stats["most_common_words"].most_common(10):
        print(f'{word: <10}| {count}')
    print(f'''
Word statistics:

Average word lenght: {stats["chars_per_word"]}
Unique words: {stats["unique_words"]}
Words only appearing once: {stats["words_appearing_once"]}    
''')

def char_stats(stats):
    print(f'''
Character Analysis for {stats["book_name"]}
{"-" * 45}
Most common characters:   ''')
    for char, count in stats["most_common_chars"].most_common(10):
        print(f'{char: <10}| {count}')
    print(f'''  
Character statistics:

Total Characters: {stats["chars_with_spaces"]}

Total Spaces: {stats["number_of_spaces"]} ({stats["number_of_spaces"] / stats["chars_with_spaces"] * 100}%)
Total Puncuation: {stats["punctuation_count"]} ({stats["punctuation_count"] / stats["chars_with_spaces"] * 100}%)
Total uppercase letters: {stats["uppercase_count"]} ({stats["uppercase_count"] / stats["chars_with_spaces"] * 100}%)
Total lowercase letters: {stats["lowercase_count"]} ({stats["lowercase_count"] / stats["chars_with_spaces"] * 100}%)
''')

def sentence_stats(stats):
    lengths = stats["sentence_length_distribution"]   
    longest_text, longest_chars = stats["longest_sentence"]
    shortest_text, shortest_chars = stats["shortest_sentence"]

    length_counts = {}
    for length in lengths:
        if length in length_counts:
            length_counts[length] += 1
        else:
            length_counts[length] = 1
    most_common_length = max(length_counts, key=length_counts.get)

    
    if len(longest_text) > 200:
        longest_text = longest_text[:200] + "..."

    print(f'''
Sentence Analysis for {stats["book_name"]}
{"-" * 45}
Total sentences: {stats["total_sentences"]}
Average words per sentence: {stats["words_per_sentence"]}
Most common sentence length: {most_common_length} words ({length_counts[most_common_length]} sentences)
Longest sentence: {max(lengths)} words ({longest_chars} characters)
Shortest sentence: {min(lengths)} words ({shortest_chars} characters)
Automated Readability Index: {stats["ARI"]}

Longest sentence starts:
    {longest_text}

Shortest sentence:
    {shortest_text}
{"-" * 45}
''')