"""

Integer to Binary

@   Problem
    Use a Stack dara structure to convert integer values to binary values.

@   Example
    242 = 11110010

    242 / 2 = 121  -> % 0
    121 / 2 = 60   -> % 1
    60  / 2 = 30   -> % 0
    30  / 2 = 15   -> % 0
    15  / 2 = 7    -> % 1
    7   / 2 = 3    -> % 1
    3   / 2 = 1    -> % 1
    1   / 2 = 1    -> % 1   TOP

"""

from stacks import Stack

def div_by_2(dec_num):
    s = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num


# TEST __________________________________________________________________________________________

print(div_by_2(242))
