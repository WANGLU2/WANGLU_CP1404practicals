"""
CP1404/CP5632 Practical
Write a program to count the occurrences of words in a string.
"""
text = input('Text:')
words = text.split()
word_to_count = {}
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

words = list(word_to_count.keys())
words.sort()


for word in words:
    max_len = max(len(word) for word in words)
    print('{0:{1}} : {2}'.format(word, max_len, word_to_count[word]))


