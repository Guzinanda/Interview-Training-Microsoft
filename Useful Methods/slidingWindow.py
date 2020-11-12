'''
Sliding Window is a common technique por iterate an array using a set (conjunto)
it is like using a window for just evaluate some of the elements.

win = 2
arr = [1,2,3,4,5,6]
         ___ 1,2
           ___ 2,3
             ___ 3,4
               ___ 4,5
                 ___ 5,6
'''


def sliding_window(win,arr):
  
    list_of_num = []

    pi = 0    # 0
    pf = win  # 2

    # [[],[],[],[],[]]
    for i in range(len(arr) - win + 1):
        list_of_num.append(arr[pi:pf])
        pi += 1
        pf += 1

    return list_of_num
    


# TEST ____________________________________________________________________________________

win = 2
arr = [1,2,3,4,5,6]
print(sliding_window(win,arr))


