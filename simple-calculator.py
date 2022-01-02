def add(a,b):
    result=a+b
    print(result)
def sub(a,b):
    result=a-b
    print(result)
def mul(a,b):
    result=a*b
    print(result)
def div(a,b):
    result=a/b
    print(result)
a=int(input("enter the value of a : "))
b=int(input("enter the value of b : "))
o=input("enter the operator : ")

if o=="+":
    add(a,b)
elif o=="-":
    sub(a,b)
elif o=="*":
    mul(a,b)
elif o=="/":
    div(a,b)
else:
    print("invalid")
