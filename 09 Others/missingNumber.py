'''
Missing Number

@ What I have to do?
  Find the missing number in the sequence nums = [3,0,1]

@ Who I am going to do it?

  With the "Summation Formula":

  01. The length of the array is:                   l =  len(nums)
                                                    l =  3

  02. The sum of all elements is:                   s =  l * (l+1)/2
                                                    s =  3 * (3+1)/2
                                                    s =  6

  03. Subtract from the sum of first n natural      m =  s - sum(nums)
      numbers, it will be the value of the          m =  6 - 4
      missing element whitch is:                    m =  2 


sum(sum)     its going to sume all numbers inside nums : sum(3,0,1) = 4
l * (l+1)/2  its going to make a sume of all sequential numbers till 'l' : 1+2+3 = 6

'''


def missingNumber(nums):
    n = len(nums)
    return n * (n+1) / 2 - sum(nums)


# TEST ________________________________________________________________________________

nums = [3,0,1]
print(missingNumber(nums))