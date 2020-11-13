x = 123

x = list(str(x))

# x = ['1','2','3']  ->  x = ['1','2','3','3','2','1']  
i = len(x) - 1  # 2

while i >= 0:
    character = x.pop(i)
    x.append(character)
    i -= 1

print(x)