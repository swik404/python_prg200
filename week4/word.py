# Question 4 - Word Frequency Counter

import string

text = """
Nepal is a beautiful country. Nepal has Mount Everest.
Everest is the highest mountain in the world. Many tourists
visit Nepal every year to see Everest and other mountains.
Nepal is known for its mountains and natural beauty.
"""


def word_frequency(text):
    clean_text = text.lower()

    for punctuation_mark in string.punctuation:
        clean_text = clean_text.replace(punctuation_mark, "")

    words = clean_text.split()
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    sorted_words = sorted(
        word_counts.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return sorted_words[:3]


top_three = word_frequency(text)

print("Top 3 words:")

for word, count in top_three:
    print(f"{word} — {count} times")
