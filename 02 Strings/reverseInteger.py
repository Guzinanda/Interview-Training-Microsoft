'''
Reverse Integer

@   Problem
    Given an integer, reverse the digits of that integer.

@   Template
  
    There are two cases: When it's 0, when it's potivie(+) and when negative(-).

    0. When it is 0:
      01. Just return '0'

    0. When it is potive(+)
      01. Separate the integers in an array:               x = 1200        ->  x = [1,2,0,0]
      02. Rotate the positions:                            x = [1,2,0,0]   ->  x = [0,0,2,1]  
      03. Iterate for 0 at the beggining deleting them:    x = [0,0,2,1]   ->  x = [2,1]  
      04. Join it                                          x = [2,1]       ->  x = 21  

    0. When it is negative(-):
      01. Separate the integers in an array:               x = -1200       ->  x = [-,1,2,0,0]
      02. Pop() the fisrt character                        x = [-,1,2,0,0] ->  x = [1,2,0,0]
      03. Rotate the positions:                            x = [1,2,0,0]   ->  x = [0,0,2,1]  
      04. Iterate for 0 at the beggining deleting them:    x = [0,0,2,1]   ->  x = [2,1]  
      04. Insert the '-' the the beggining:                x = [2,1]       ->  x = [-,2,1] 
      06. Join it                                          x = [-,2,1]     ->  x = -21  

'''

def reverseInteger(x):

    # When x = 0  -> x = 0 _____________________________________
    if x == 0:
        return '0'


    # When x = 1200  ->  x = 21 _________________________________
    elif x > 0:
        # x = ['1','2','0','0'] 
        x = list(str(x))

        # x = ['1','2','0','0']  ->  x = ['0','0','2','1']  
        i = len(x) - 1  # 2
        while i >= 0:
            character = x.pop(i)
            x.append(character)
            i -= 1
        
        # x = ['0','0','2','1']  ->  x = ['2','1']
        while x[0] == '0':
          del x[0]

        # x = ['2','1']  ->  x = 21
        x = ''.join(x)


    # When x = -120  ->  x = -21 ________________________________
    elif x < 0:
        # x = ['-','1','2','0'] 
        x = list(str(x))

        # x = ['1','2','0'] 
        del x[0]

        # x = ['1','2','0']  ->  x = ['0','2','1']  
        i = len(x) - 1  # 2
        while i >= 0:
            character = x.pop(i)
            x.append(character)
            i -= 1
        
        # x = ['0','2','1']  ->  x = ['2','1']
        
        while x[0] == '0':
          del x[0]

        # x = x = ['2','1'] ->  x = ['-','2','1']
        x.insert(0,'-')

        # x = ['-','2','1']  ->  x = -21
        x = ''.join(x)

    return x


# TEST _____________________________________________________________

x1 =  123  #  321
x2 = -123  # -321
x3 =  120  #  21
x4 =  100  #  1
x5 =  0    #  0

print(reverseInteger(x1))
print(reverseInteger(x2))
print(reverseInteger(x3))
print(reverseInteger(x4))
print(reverseInteger(x5))
