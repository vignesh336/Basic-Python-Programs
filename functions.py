def add(x,y):
    c=0
    c=x+y
    print("addition",c)
def sub(x,y):
    c=0
    c=x-y
    print("subtraction",c)
def mul(x,y):
    c=0
    c=x*y
    print("multiplication",c)
def div(x,y):
    c=0
    c=x/y
    print("division",c)
a=input("enter the first value:")
b=input("enter second value:")
selection=int(input("select the mode: (1.add/2.sub/3.mul/4.div):-"))
if selection==1:
    add(10,20)
elif selection==2:
    sub(10,20)    
elif selection==3:
    mul(10,20)
else:
    div(10,20)
