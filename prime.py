n=int(input("enter the value:"))
for i in range(1,n+1,1):
    c=0
    for x in range(1,i,1):
      if i%x==0:
          c=c+1
    if c==1:
        print(i)
          
        
