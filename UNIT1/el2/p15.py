#Given a list of words, use map() to calculate the length of each word.

words =["why","common","sense","is","not","common"]
lengths = list(map(len,words))
print(lengths)

l = list(map(lambda x:len(x),words))
print(l)