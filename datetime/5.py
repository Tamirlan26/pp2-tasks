w=input()
l={}
for i in w:
    if i in l:
        l[i]+=1
    else:
        l[i]=1
print(l)