def validAnagram(s,t):
	
	word1 = createDictionary(s)
	word2 = createDictionary(t)
	
	if word1 == word2:
		return True
	else:
		return False

		
def createDictionary(word):
	
	dict = {}
	for character in word:
		if character not in dict:
			dict[character] = 1
		else:
			dict[character] += 1
			
	return dict




#* Test ....................................................................................

s1 = "anagram"      # True
t1 = "nagaram"

s2 = "rat"          # False
t2 = "car"

print(validAnagram(s1, t1))
print(validAnagram(s2, t2))



# Info ....................................................................................
'''
@   # 04

@   Instructions:
    Given two strings s and t , write a function to determine if t is an anagram of s.

@   Example 01:
    Input:  s = "anagram", t = "nagaram"
    Output: true

@   Example 02:
    Input:  s = "rat", t = "car"
    Output: false


@   Link:
    https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/
'''