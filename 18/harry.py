import os
import urllib.request
from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, "stopwords")
harry_text = os.path.join(tmp, "harry")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt", stopwords_file
)
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/harry.txt", harry_text
)

with open(harry_text, "r", encoding="utf-8") as file:
    text = file.read().lower()

with open(stopwords_file, "r") as file:
    stopwords = file.read().splitlines()


def get_harry_most_common_word():
    clean_text = "".join(char for char in text if char.isalnum() or char.isspace())
    words = [word for word in clean_text.split() if word not in stopwords]

    counter = Counter(words)
    most_common_word, frequency = counter.most_common(1)[0]

    return most_common_word, frequency
