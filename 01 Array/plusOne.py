'''
Plus One

@ What I have to do?
  Given an array of digits, increment on to the integer.

@ How I an going to do it?
  
'''

def plusOne(digits):
    
    # digits = [1,3,9] 

    addend = 1
    index = len(digits) - 1  #2

    while index >= 0:
        
        # digits=[1,2,9] and addend=1 -> digits=[1,2,0] and keep addend=1
        if digits[index] == 9 and addend == 1:
            digits[index] = 0
        
        # digits=[1,2,3] and addend=1 -> digits=[1,2,4] and addend=0
        elif digits[index] < 9 and addend == 1:
            digits[index] += 1
            addend -= 1
        
        # digits=[9,0,0] and addend=1 -> digits=[1,0,0,0] 
        if (index == 0 and addend == 1):
            digits.insert(0, 1)
        
        index -= 1
    
    return digits



# TEST _____________________________________________________________________

digits1 = [1,3,9] # [1,4,0]
digits2 = [0,9,9] # [1,0,0]
digits3 = [9,9,9] # [1,0,0,0]

print(plusOne(digits1))
print(plusOne(digits2))
print(plusOne(digits3))
