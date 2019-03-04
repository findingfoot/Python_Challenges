'''

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.



Your task is to determine the winner of the game and their score.

Input Format

A single line of input containing the string .
Note: The string  will contain only uppercase letters: .

Constraints



Output Format

Print one line: the name of the winner and their score separated by a space.

If the game is a draw, print Draw.


Sample Input

BANANA
Sample Output

Stuart 12

'''


def minion_game(beginning_word):
    # your code goes here
    vow = 'AEIOU'
    kev = 0
    stu = 0

    for i in range(len(beginning_word)):
        if beginning_word[i] in vow:
            kev += len(s) - i
        else:
            stu += len(s) - i
    if kev > stu:
        print('Kevin', kev)
    elif kev < stu:
        print('Stuart', stu)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
