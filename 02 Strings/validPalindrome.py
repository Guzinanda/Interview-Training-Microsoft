# Clean the string: Lowercase everything, eliminate special characters and spaces.

# Compare: Compare the first character (index[0]) with the last character (indext[-1]).

# Two cases:
# - Pair: Compare s/2 times.
# - Odd: Compare (s - 1) times.

import re

def cleanWord(s):
	cleaned_word = s.lower()
	cleaned_word = re.sub('[^A-Za-z0-9]+', '', cleaned_word)
	return cleaned_word


def isPalindrome(s):
	word = cleanWord(s)
	
	initial = 0
	final = -1
	i = 0

	 # TODO: Pair
	if len(word) % 2 == 0:
		while i < len(word)/2:
			if word[initial] == word[final]:
				initial += 1
				final -= 1
			else:
				return False
			i += 1
		return True

 	# TODO: Odd
	else:
		while i < (len(word)-1)/2:
			if word[initial] == word[final]:
				initial += 1
				final -= 1
			else:
				return False
			i += 1
		return True


# TEST ____________________________________________________________________________________

s1 = "A man, a plan, a canal: Panama"		# True
s2 = "race a car"         			 		# False

print(isPalindrome(s1))
print(isPalindrome(s2))

'''
@   # 05

@   Instructions:
    Given a string, determine if it is a palindrome, considering only alphanumeric characters 
	and ignoring cases.

@   Example 01:
	Input: "A man, a plan, a canal: Panama"
	Output: true

@   Example 02:
	Input: "race a car"
	Output: false


@   Link:
    https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/
'''