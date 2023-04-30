import requests
import string

book1_url = "http://www.gutenberg.org/files/84/84-0.txt"
book1_text = requests.get(book1_url).text

book2_url = "http://www.gutenberg.org/files/11/11-0.txt"
book2_text = requests.get(book2_url).text

book1_text = book1_text.translate(str.maketrans('', '', string.punctuation)).lower()
book2_text = book2_text.translate(str.maketrans('', '', string.punctuation)).lower()

book1_words = book1_text.split()
book2_words = book2_text.split()

book1_unique_words = set(book1_words)
book2_unique_words = set(book2_words)

print("The first book has", len(book1_unique_words), "unique words.")
print("The second book has", len(book2_unique_words), "unique words.")

if len(book1_unique_words) > len(book2_unique_words):
    print("The first book has more unique words.")
elif len(book1_unique_words) < len(book2_unique_words):
    print("The second book has more unique words.")
else:
    print("Both books have the same number of unique words.")

