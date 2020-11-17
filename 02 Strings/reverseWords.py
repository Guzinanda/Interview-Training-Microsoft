'''
Reverse Words

@   What I have to do?
    Reverse the words in a string

@   Example:
    s = "the sky is blue"
    s = "blue is sky the"

@   How I am going to do it?
    01. I want to s.slipt() the array into a list of words. 
    02. I want to words.reverse() that list of words.
    03. ' '.join() the list with spaces ' ' between words.
'''


def reverseWords(s):

    # "the sky is blue"
    print(s)
    
    # ["the", "sky", "is", "blue"] 
    words = s.split()   
    
    # ["blue", "is", "sky", "the"]
    words.reverse()

    # "blue is sky the"
    p = ' '.join(map(str, words))
    #p = ' '.join(words)
    
    return p



# TEST ____________________________________________________________________________________

#s1 = "the sky is blue"
#print(reverseWords(s1))     # "blue is sky the"

#s2 = "  hello world  "
#print(reverseWords(s2))     # "world hello"

s3 = "a good   example"
print(reverseWords(s3))     # "example good a"
