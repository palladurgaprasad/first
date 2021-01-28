n=int(input('enter the value of sorting:'))
l=[]
for i in range(0,n):
    l.append(int(input('the value of'+str(i)+':')))
print(l)
for  k in range(0,n):
    for j in range(0,n,1):
        if l[k]>l[j]:
            l[k],l[j]=l[j],l[k]
print(l)            
