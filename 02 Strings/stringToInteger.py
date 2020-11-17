
def myAtoi(s):

    # "hi -123" -> [-,1,2,3]
    def clean_numbers(s):
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        symbols = ['-','+']
        numList = []
        
        for i in s:
            if (i in numbers) or (i in symbols):
                numList.append(i)
        return numList

    numList = clean_numbers(s)

    # [-,1,2,3] -> -123
    def convert_to_int(numList):
        s = ''.join(map(str, numList))
        return int(s)

    result = convert_to_int(numList)

    return result



# TEST ____________________________________________________________________________________

# Example 01:
s1 = "42"
print(myAtoi(s1)) # Output: 42

s2 = "   -42"
print(myAtoi(s2)) # Output: -42

s3 = "4193 with words"
print(myAtoi(s3)) # Output: 4193

s4 = "words and 987"
print(myAtoi(s4)) # Output: 0

s5 = "-91283472332"
print(myAtoi(s5)) # Output: -2147483648

