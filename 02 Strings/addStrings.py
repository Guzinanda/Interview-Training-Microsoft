'''
Add Strings

@ Problem Link
  https://leetcode.com/problems/add-strings/
    
@ Problem
  Given two arrays of digits add them.
    
  aU  =   123 
  aD  =  4567
        ------ +
  sum =  4690

'''

def addStrings(num1: str, num2: str) -> str:
    
    num1 = num1[::-1]
    num2 = num2[::-1]
    num3 = ''

    carry = 0
    i = 0
    
    l1 = len(num1)
    l2 = len(num2)
    l3 = max(l1, l2)

    while i < l3 or carry:
        dig1  = int(num1[i]) if i < l1 else 0
        dig2  = int(num2[i]) if i < l2 else 0
        dig3  = (dig1 + dig2 + carry) % 10
        carry = (dig1 + dig2 + carry) // 10
        num3 += str(dig3)
        i    += 1
    
    return num3[::-1]


# TEST ______________________________________________________________________________

num1 = "123"
num2 = "4567"

print(addStrings(num1, num2)) # 4690
