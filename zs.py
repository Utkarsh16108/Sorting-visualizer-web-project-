from collections import Counter
import re

def count_word_frequency(string):
    words = re.findall(r'\w+', string.lower())
    word_counts = Counter(words)
    return word_counts

# Example usage
input_string = input("Enter a string: ")
word_frequency = count_word_frequency(input_string)

print("Word frequency:")
for word, count in word_frequency.items():
    print(f"{word}: {count}")