from collections import Counter

def bag_of_words(text):
    return Counter(text.split())
