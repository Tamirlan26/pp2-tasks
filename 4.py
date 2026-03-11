grades = {
    "математика": 5,
    "русский": 4,
    "информатика": 5
}
s=0
m=0
for i in grades:
    s+=grades[i]
    if grades[i]>0:
        m=grades[i]
print(s//3,m)
