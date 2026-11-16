import os
import book_analysis as ba
import plotting as plt

FOLDER = r"C:\Users\othom\project"


def analyse(book_name):
    path = os.path.join(FOLDER, book_name)
    with open(path, "r", encoding="utf-8") as book:
        return ba.single_book_analysis(book_name, book)


def open_compared_books(book1, book2):
    print(f"Analysing {book1} and {book2}...")
    stats1 = analyse(book1)
    stats2 = analyse(book2)
    print("Completed analysis")
    compare_menu(stats1, stats2)


def compare_menu(stats1, stats2):
    while True:
        print("Compare Books:")
        print("1. General comparison")
        print("2. Word comparison")
        print("3. Character comparison")
        print("0. Return to main menu")
        n = int(input("Enter the number of the comparison you want to see: "))

        match n:
            case 1:
                general_comparison(stats1, stats2)
            case 2:
                general_comparison(stats1, stats2)
                plt.compare_total_words_plot(stats1["total_words"], stats2["total_words"])
                plt.compare_10most_common_words_plot(stats1["most_common_words"], stats2["most_common_words"])
            case 3:
                general_comparison(stats1, stats2)
                plt.compare_total_char(stats1["total_chars"], stats2["total_chars"])
            case 0:
                return
            case _:
                print("Invalid entry, try again.")


def general_comparison(stats1, stats2):
    print(f'''
Basic Comparison
{"-" * 60}
{"":<26}{stats1["book_name"]:<17}{stats2["book_name"]:<17}
Lines:                    {stats1["number_of_lines"]:<17}{stats2["number_of_lines"]:<17}
Sentences:                {stats1["total_sentences"]:<17}{stats2["total_sentences"]:<17}
Paragraphs:               {stats1["number_of_paragraphs"]:<17}{stats2["number_of_paragraphs"]:<17}
Words:                    {stats1["total_words"]:<17}{stats2["total_words"]:<17}
Unique words:             {stats1["unique_words"]:<17}{stats2["unique_words"]:<17}
Characters (with spaces): {stats1["chars_with_spaces"]:<17}{stats2["chars_with_spaces"]:<17}
Characters (no spaces):   {stats1["total_chars"]:<17}{stats2["total_chars"]:<17}
Words per line:           {stats1["words_per_line"]:<17}{stats2["words_per_line"]:<17}
Average word length:      {stats1["chars_per_word"]:<17}{stats2["chars_per_word"]:<17}
Words per sentence:       {stats1["words_per_sentence"]:<17}{stats2["words_per_sentence"]:<17}
Readability (ARI):        {stats1["ARI"]:<17}{stats2["ARI"]:<17}
{"-" * 60}
''')


def word_comparison(stats1, stats2):
    print(f'''
Word Comparison
{"-" * 60}
{"":<26}{stats1["book_name"]:<17}{stats2["book_name"]:<17}
Words:                    {stats1["total_words"]:<17}{stats2["total_words"]:<17}
Unique words:             {stats1["unique_words"]:<17}{stats2["unique_words"]:<17}
Words appearing once:     {stats1["words_appearing_once"]:<17}{stats2["words_appearing_once"]:<17}
Average word length:      {stats1["chars_per_word"]:<17}{stats2["chars_per_word"]:<17}

Most common words:
{"-" * 60}''')
    top_words1 = stats1["most_common_words"].most_common(10)
    top_words2 = stats2["most_common_words"].most_common(10)
    for i in range(10):
        book1_entry = f"{top_words1[i][0]} | {top_words1[i][1]}"
        book2_entry = f"{top_words2[i][0]} | {top_words2[i][1]}"
        print(f"{i + 1:<4}{book1_entry:<26}{book2_entry:<26}")
    print("-" * 60)


def char_comparison(stats1, stats2):
    print(f'''
Character Comparison
{"-" * 60}
{"":<26}{stats1["book_name"]:<17}{stats2["book_name"]:<17}
Characters (no spaces):   {stats1["total_chars"]:<17}{stats2["total_chars"]:<17}
Unique characters:        {stats1["unique_chars"]:<17}{stats2["unique_chars"]:<17}
Spaces:                   {stats1["number_of_spaces"]:<17}{stats2["number_of_spaces"]:<17}
Punctuation:              {stats1["punctuation_count"]:<17}{stats2["punctuation_count"]:<17}
Uppercase letters:        {stats1["uppercase_count"]:<17}{stats2["uppercase_count"]:<17}
Lowercase letters:        {stats1["lowercase_count"]:<17}{stats2["lowercase_count"]:<17}

Most common characters:
{"-" * 60}''')
    top_chars1 = stats1["most_common_chars"].most_common(10)
    top_chars2 = stats2["most_common_chars"].most_common(10)
    for i in range(10):
        book1_entry = f"{top_chars1[i][0]} | {top_chars1[i][1]}"
        book2_entry = f"{top_chars2[i][0]} | {top_chars2[i][1]}"
        print(f"{i + 1:<4}{book1_entry:<26}{book2_entry:<26}")
    print("-" * 60)