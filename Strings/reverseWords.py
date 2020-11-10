
# What I want to do?
# I want to Slipt the array into a list of the words. 
# I want to Reverse that list of words.
# Join the list with spaces " " between words.

def reverseWords(s):

    print(s)
    # "the sky is blue"

    words = s.split()   
    # ["the", "sky", "is", "blue"] 

    words.reverse()
    # ["blue", "is", "sky", "the"]

    p = ' '.join(map(str, words))
    # "blue is sky the"
    
    return p



#! TEST __________________________________________________

s1 = "the sky is blue"
print(reverseWords(s1))     # "blue is sky the"

#s2 = "  hello world  "
#print(reverseWords(s2))     # "world hello"

#s3 = "a good   example"
#print(reverseWords(s3))     # "example good a"
