'''

You are given a string  and width .
Your task is to wrap the string into a paragraph of width .

Input Format

The first line contains a string, .
The second line contains the width, .

Constraints

Output Format

Print the text wrapped paragraph.

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

'''

import textwrap


def wrap(string, max_width):
    # return '\n'.join(string[i:i+max_width] for i in range(0, len(string), max_width)) #solution 1
    return '\n'.join(textwrap.wrap(string, max_width))  # solution 2 using inbuilt methods


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
