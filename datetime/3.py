numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
z={}
for i in numbers:
    if i in z:
        z[i]+=1
    else:
        z[i] = 1
