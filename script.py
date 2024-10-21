import os
import socket
import re
from collections import Counter

def count_words(filename):
    with open(filename, 'r') as f:
        text = f.read()
    words = re.findall(r'\b\w+\b', text.lower())  
    return len(words), Counter(words)

def handle_contractions(text):
    contractions = {
        "I'm": "I am", "can't": "cannot", "don't": "do not", "you'll": "you will",
        "I'll": "I will", "It's": "It is", "that's": "that is", "wasn't": "was not",
        "weren't": "were not", "hasn't": "has not", "haven't": "have not",
        "didn't": "did not", "doesn't": "does not", "won't": "will not",
        "wouldn't": "would not", "isn't": "is not", "ain't": "am not",
        "I'm": "I am", "couldn't": "could not", "shouldn't": "should not", 
        "doesn't": "does not", "wasn't": "was not", "weren't": "were not"
    }
    for contraction, full in contractions.items():
        text = text.replace(contraction, full)
    return re.findall(r'\b\w+\b', text.lower())  

if_word_count, if_word_counter = count_words("IF.txt")

with open("AlwaysRememberUsThisWay.txt", 'r') as f:
    text = f.read()
text_words = handle_contractions(text)
always_remember_count = len(text_words)
always_remember_counter = Counter(text_words)

ip_address = socket.gethostbyname(socket.gethostname())

os.makedirs("output", exist_ok=True)

with open("output/result.txt", 'w') as output_file:
    output_file.write(f"IF.txt Word Count: {if_word_count}\n")
    output_file.write(f"AlwaysRememberUsThisWay.txt Word Count: {always_remember_count}\n")
    output_file.write(f"Total Word Count of both text files: {if_word_count + always_remember_count}\n")
    output_file.write(f"Top 3 Words in IF.txt: {if_word_counter.most_common(3)}\n")
    output_file.write(f"Top 3 Words in AlwaysRememberUsThisWay.txt: {always_remember_counter.most_common(3)}\n")
    output_file.write(f"Container IP Address: {ip_address}\n")

with open("output/result.txt", 'r') as output_file:
    print(output_file.read())
