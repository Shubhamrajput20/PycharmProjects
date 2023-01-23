n=int(input())
a=[]
for i in range(0,n):
    a.append(int(input())

l=[]
for i in a:
    if i in l:
        continue
    else:
        l.append(i)
print(l)