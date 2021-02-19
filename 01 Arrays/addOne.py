'''
Plus One

@   What I have to do?
    Given an array of digits, increment one to the last integer.

@   How I an going to do it?
    There are 3 possibilities:

    01. When the digit is == 9 and whe have an addend:
        It will set the digit place to 0 and keep the addend

    02. When the digit is < than 9 and we have an addend:
        It will add 1 to the digit in place and substract that 1 from addend

    03. When the first digit is 9 and we still have and acumulated addend:
        It will verify if the last number is a 0 and if the addend still has
        a 1, in that case add a 1 to the beggining. 

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
        
        # digits=[9,9,9] and addend=1 -> digits=[1,0,0,0] 
        if (index == 0 and addend == 1):
            digits.insert(0, 1)
        
        index -= 1
    
    return digits



# TEST ______________________________________________________________________________

digits1 = [1,3,9] # [1,4,0]
digits2 = [0,9,9] # [1,0,0]
digits3 = [9,9,9] # [1,0,0,0]

print(plusOne(digits1))
print(plusOne(digits2))
print(plusOne(digits3))
