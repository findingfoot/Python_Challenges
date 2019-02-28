'''

Have the function LetterChanges(str) take the str parameter being passed and
modify it using the following algorithm. Replace every letter in the string with
the letter following it in the alphabet (ie. c becomes d, z becomes a). Then capitalize
 every vowel in this new string (a, e, i, o, u) and finally return this modified string.

Use the Parameter Testing feature in the box below to test your code with different arguments.

'''

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']


def LetterChanges(str):
    new = []
    for i in str:
        if i in alpha:
            if alpha[alpha.index(i) + 1] in 'aeiou':
                new.append(alpha[alpha.index(i) + 1].upper())
            else:
                new.append(alpha[alpha.index(i) + 1])
        else:
            new.append(i)

    # code goes here
    return ''.join(new)


# keep this function call here
print(LetterChanges(input()))
