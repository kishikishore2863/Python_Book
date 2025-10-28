#16. Define contains_word(sentence, word) that returns how many times the word appears (case insensitive). Print message accordingly
def contains_word(sentence, word):
    words = sentence.lower().split()
    return words.count(word.lower())

sentence = input("Enter sentence: ")
word = input("Enter word to search: ")
count = contains_word(sentence, word)
print(f"{word} appears {count} time(s)")