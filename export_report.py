import generate_stats as genstats

def export_report(stats):
    filename = f'{stats["book_name"]}_report.txt'
    
    report = open(filename, "w")

    report.write(f'''
    Report for {stats["book_name"]}!

    Number of lines: {stats["number_of_lines"]}
    Number of words: {stats["total_words"]}
    Number of sentences: {stats["total_sentences"]}
    Number of paragraphs: {stats["number_of_paragraphs"]}
    Number of characters: {stats["total_chars"]}

    Number of words that only appear once: {stats["number_of_spaces"]}

    Average words per sentence: {stats["words_per_sentence"]}
    Average characters per word: {stats["chars_per_word"]}

    Automated Readibility Index: {stats["ARI"]}

    Longest sentence: {stats["longest_sentence"]}
    Shortest sentence: {stats["shortest_sentence"]}

    Number of uppercase letters: {stats["uppercase_count"]}
    Number of lowercase letters: {stats["lowercase_count"]}
    Number of punctuation characters: {stats["punctuation_count"]}
    Number of spaces: {stats["number_of_spaces"]}
    ''')

    report.write("Most common words:\n")
    for word, count in stats["most_common_words"].most_common(10):
        report.write(f'{word: <10}| {count}\n')

    report.write("Most common characters:\n")
    for char, count in stats["most_common_chars"].most_common(10):
        report.write(f'{char: <10}| {count}\n')

    print(f'Your report has been generated: {filename}')
    report.close()