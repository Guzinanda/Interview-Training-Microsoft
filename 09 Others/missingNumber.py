'''
Missing Number

@ What I have to do?
  Find the missing number in the sequence nums = [3,0,1,4]

@ How I am going to do it?

  By substracting the current value of nums to the "Summation Formula":
  n * (n+1) / 2  -  sum(nums)


  01. The length of the array is 'n':               n =  len(nums)
                                                    n =  4

  02. The sum of all elements is:                   s =  n * (n+1)/2
                                                    s =  4 * (4+1)/2
                                                    s =  10

  03. Subtract from the sum of first n natural      r =  s - sum(nums)
      numbers, it will be the value of the          r =  10 - 8
      missing element whitch is:                    r =  2 


sum(sum)     its going to sume all numbers inside nums : sum(3,0,1) = 4
n * (n+1)/2  its going to make a sume of all sequential numbers till 'n' : 1+2+3 = 6
'''


def missingNumber(nums):
    n = len(nums)
    return n * (n+1) / 2 - sum(nums)



# TEST ________________________________________________________________________________

nums = [3,0,1,4]
print(missingNumber(nums))