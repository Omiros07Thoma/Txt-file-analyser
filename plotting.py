import matplotlib.pyplot as plt
import create_function as cf
import generate_stats as gn

def compare_total_words_plot(total_words_book1, total_words_book2):
    plt.bar(["Book 1", "Book 2"], [total_words_book1, total_words_book2] , color=['blue', 'orange'])
    plt.xlabel("Books")
    plt.ylabel("Total Words")
    plt.title("Comparison of Total Words")
    plt.show()

def compare_unique_words_plot(unique_words_book1, unique_words_book2,total_words_book1, total_words_book2):
    plt.pie([unique_words_book1, total_words_book1], labels=["Unique Words", "Total Words"], autopct='%1.1f%%', colors=['blue', 'orange'], explode=(0.1, 0))
    plt.title("Unique Words Book 1")
    plt.show()
    plt.pie([unique_words_book2, total_words_book2], labels=["Unique Words", "Total Words"], autopct='%1.1f%%', colors=['blue', 'orange'], explode=(0.1, 0))
    plt.title("Unique Words Book 2")

def compare_10most_common_words_plot(most_common_words1, most_common_words2):
    for number, counter in ((1, most_common_words1), (2, most_common_words2)):
        top = counter.most_common(10)
        words = [pair[0] for pair in top]
        counts = [pair[1] for pair in top]

        plt.figure()
        plt.bar(words, counts)
        plt.title(f"Most Common Words - Book {number}")
        plt.xlabel("Words")
        plt.ylabel("Frequency")
        plt.show()

def single_total_words(total_words):
    print(f"Total Words:{total_words}")
    plt.bar(["Book"], [total_words] , color=['blue'])
    plt.xlabel("Books")
    plt.ylabel("Total Words")
    plt.title("Total Words")
    plt.show()

def unique_words(total_words,unique_words):
    print(f"Unique Words:{unique_words}")
    plt.pie([unique_words, total_words], labels=["Unique Words", "Total Words"], autopct='%1.1f%%', colors=['blue', 'orange'], explode=(0.1, 0))
    plt.title("Unique Words")
    plt.show()    

def compare_total_char(total_char_book1 , total_char_book2):
    print(f"Total Characters:Book 1: {total_char_book1}, Book 2: {total_char_book2}")
    plt.bar(["Book 1", "Book 2"], [total_char_book1, total_char_book2] , color=['blue', 'orange'])
    plt.xlabel("Books")
    plt.ylabel("Total Characters")
    plt.title("Comparison of Total Characters")
    plt.show()

def single_book_total_char(total_char):
    print(f"Total Characters:{total_char}")
    plt.bar(["Book"], [total_char] , color=['blue'])
    plt.xlabel("Books")
    plt.ylabel("Total Characters")
    plt.title("Total Characters")
    plt.show()

def plot_10_most_common_words(most_common_words, book_name=""):
    top_10 = most_common_words.most_common(10)
    words = [pair[0] for pair in top_10]
    counts = [pair[1] for pair in top_10]

    plt.figure(figsize=(10, 5))
    plt.bar(words, counts, color="steelblue")
    plt.title(f"10 most common words {book_name}".strip())
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def plot_text_composition(lines, paragraphs, sentences, words, unique_words):
    labels = ["Lines", "Paragraphs", "Sentences", "Words", "Unique words"]
    values = [lines, paragraphs, sentences, words, unique_words]
 
    plt.bar(labels, values , )
    plt.title("Text composition")
    plt.ylabel("Count")
    plt.show()


def plot_10_most_common_chars(most_common_chars, book_name=""):
    top_10 = most_common_chars.most_common(10)
    chars = [pair[0] for pair in top_10]
    counts = [pair[1] for pair in top_10]

    plt.figure(figsize=(10, 5))
    plt.bar(chars, counts, color="seagreen")
    plt.title(f"10 most common characters {book_name}".strip())
    plt.xlabel("Characters")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()


def plot_character_types_pie(stats):
    lower = stats["lowercase_count"]
    upper = stats["uppercase_count"]
    punct = stats["punctuation_count"]
    spaces = stats["number_of_spaces"]
    labels = ["Lowercase", "Uppercase", "Punctuation", "Spaces"]
    values = [lower, upper, punct, spaces]
    colors = ["steelblue", "orange", "seagreen", "lightgray"]

    total = sum(values)
    legend_labels = [f"{l}: {v / total * 100:.1f}%" for l, v in zip(labels, values)]

    plt.pie(values, colors=colors)
    plt.legend(legend_labels, loc="center left", bbox_to_anchor=(1, 0.5))
    plt.title("Character types")
    plt.tight_layout()
    plt.show()


def plot_word_length_histogram(word_counts, book_name=""):
    length_counts = {}
    for word, count in word_counts.items():
        length_counts[len(word)] = length_counts.get(len(word), 0) + count

    lengths = sorted(length_counts)
    counts = [length_counts[n] for n in lengths]

    plt.figure(figsize=(10, 5))
    plt.bar(lengths, counts, color="indianred", edgecolor="white")
    plt.title(f"Word lengths {book_name}".strip())
    plt.xlabel("Word length (letters)")
    plt.ylabel("Number of words")
    plt.xticks(lengths)
    plt.tight_layout()
    plt.show()


def plot_sentence_length_histogram(lengths, book_name=""):
    plt.figure(figsize=(10, 5))
    plt.hist(lengths, bins=range(0, 61, 2), color="mediumpurple", edgecolor="white")
    plt.title(f"Sentence lengths {book_name}".strip())
    plt.xlabel("Words per sentence")
    plt.ylabel("Number of sentences")
    plt.tight_layout()
    plt.show()

def plot_common_sentence_lengths(lengths):
    counts = {}
    for length in lengths:
        if length in counts:
            counts[length] += 1
        else:
            counts[length] = 1

    top = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)[:10]
    top.sort()

    sizes = [str(pair[0]) for pair in top]
    amounts = [pair[1] for pair in top]

    plt.bar(sizes, amounts)
    plt.title("Most common sentence lengths")
    plt.xlabel("Words per sentence")
    plt.ylabel("Number of sentences")
    plt.show()


def plot_most_common_letters(char_list):
    common = gn.most_common_chars(char_list)
    chars = [pair[0] for pair in common]
    counts = [pair[1] for pair in common]
 
    plt.bar(chars, counts, color="skyblue")
    plt.title("Most common characters")
    plt.xlabel("Character")
    plt.ylabel("Count")
    plt.show()