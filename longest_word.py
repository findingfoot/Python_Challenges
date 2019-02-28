def longest_word(sentence):
    sentence = ''.join(char for char in sentence if char.isalnum() or char.isspace()).split()

    maxlen = max(len(w) for w in sentence)
    for i in sentence:
        if len(i) == maxlen:
            return (i)
    return -1


print(longest_word(input()))
