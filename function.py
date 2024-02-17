#WITHOUT ARGUMENT WITHOUT RETURN VALUE
def add():
    a=int(input("enter a no"))
    b=int(input("enter b no"))
    print("sum of 2 no",a+b)
    add()


#without argument with return value
def add():
    a=int(input("enter a no"))
    b=int(input("enter a no"))
    return a+b
print("add of 2 no",add())
print("total",add())


#with argument withount return value
def add(a,b):
    print(a+b)
add(10,20) 
add(10,40)   


#with argument with return value
def add(a,b):
    return a+b
print("sum of 2 no",add(10,20))

def name(a,b):
    print("the name is",a," ","the age is",b)
name("anbu",21)

def sum(a,b):
    return a+b
c=int(input("A"))
d=int(input("B"))
print(sum(c,d))


#variable length argument
def my(name):
    print(name)
my("vasanth")


#key word argument
def my(name,age):
    print(name,age)
    my(age=21,name="vasanth")


#default
def color(a="orange"):
    print(a)
color()
color("blue")    


#recursive
print(pow(2,3))

def pow1(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    else:
        return a*pow1(a,b-1)
    print(pow1(2,2))


#Try exception
try:
    a=4
    b=0
    print(a+b)
except:
    print("Error accored")
#finally exception
finally:
    print("finish")

from formulas import cyrcle
print(cyrcle.area(8))
from formulas import triangle
print(triangle.area(3,5))