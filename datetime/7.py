text = "привет как дела привет мир как дела привет"
a=text.split(" ")
c={}
for i in a:
    if i in c:
        c[i]+=1
    else:
        c[i]=1