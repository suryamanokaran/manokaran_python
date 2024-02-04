#indexing
a="welcome to python class"
print(a)
#repitation
print(a*3)
#slicing
print(a[4])
print(a[-1])
print(a[1:])
print(a[:-1])
print(a[1:9])
#double slicing
print(a[1:9:2])
b=("1,2,3,4,5,6,7,8,9")
print(b[1:8:1])
#reversing
print(a[::-1])
#max and min
c="a1,5,C"
print(max(c))
print(min(c))
#example
d=['aba','121','123','xyx']
x=[]
sum=0
for i in d:
    if i[0]==i[-1]:
        x.append(i)
        sum=sum+1
print(x)
print(len(x))
print(sum)
#boolian function
print(a,isupper())
print(a,islower())
print(a,isnumeric())
print(a,isalnum())

y="    "
print(y,isspece())

print(a,upper())
print(a,lower())
print(a,swapcase())
print(a,replace("class"),("session"))
print(a,startswith("py"),11)
print(a,endswith("ss"))
print(a,endswith("on"),1,17)
print(a,ljust(30,"1"))
print(a,rjust(30,"1"))
print(a,enter(30,"_"))
print(a,zfill(30))

m="aaa python aaa"
print(m,strip("m"))
print(m,lstrip("a"))
print(a,rstrip("a"))

n="hi welcome"
print(n,capitalize())
print(n,count("e"))
print(n,index("w"))