import sys
class stack:
    stack=[]
    def push(self,x):
            self.stack.append(x)
    def pop(self):
        if len(self.stack)==0:
            print('stack is empty')
        else:
            print(self.stack.pop())
    def peek(self):
        print(srlf.stack[0:])
s=stack()
while(1):
    o=int(input("\n1.push\n2.pop\n3.display\n4.exit\n"))
    if 0==1:
        n=input('enter a value:')
        s.push(n)
     elif 0==2:
         s.pop()
     elif 0==3:
         s.display()
     else:
         sys.exit()

    

