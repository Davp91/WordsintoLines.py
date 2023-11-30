def sort_words_into_lines(text, words_per_line=5):
    """
    Sorts words in the given text alphabetically and groups them into lines.

    :param text: The text containing the words to be sorted.
    :param words_per_line: Number of words to include in each line.
    :return: A string with words sorted and grouped into lines.
    """
    words = sorted(text.split())
    lines = []

    for i in range(0, len(words), words_per_line):
        line = ' '.join(words[i:i + words_per_line])
        lines.append(line)

    return '\n'.join(lines)

# Example usage
example_text = "create a program in python that sorts words into lines"
sorted_text = sort_words_into_lines(example_text, 4)
print(sorted_text)
