#13. Write reverse_words(sentence) that returns the sentence with words reversed but order preserved.
def reverse_words(sentence):
    return " ".join(word[::-1] for word in sentence.split())

print(reverse_words("hello world"))
