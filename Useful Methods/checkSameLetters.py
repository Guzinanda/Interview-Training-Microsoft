'''
01: I want to check if both s1 and s2 are the same length:
    * If they are same length, it could be a substring.
    * If they are not same length, they don't even have possibility.
    
02: They can be same length, but don't have the same characters, so
    I want to check if both strings have the same characters:
    
    s1 = “abcd”  -> ['a', 'b', 'c', 'd'] -> ['a', 'b', 'c', 'd']
    s2 = “dabc"  -> ['d', 'a', 'b', 'c'] -> ['a', 'b', 'c', 'd']
    
    * Separate each string in a list
    * Sort the list
    * Iterate s1[0] with s2[0] and so on, if they are == continue
      if they are not, return False, if finish return True
'''

def checkInclusion(s1, s2):
        
    if len(s1) == len(s2):

        s1_list = list(s1)
        s2_list = list(s2)

        s1_sorted_list = sorted(s1_list)
        s2_sorted_list = sorted(s2_list)

        i = 0

        while i < len(s1):
            if s1_sorted_list[i] == s2_sorted_list[i]:
                i += 1
            else:
                return False

        return True

    else:
        return False


# TEST ____________________________________________________________________________________

s1 = "abcd"
s2 = "abcd"

print(checkInclusion(s1,s2))
