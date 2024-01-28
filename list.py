a=[1,2,3,4,5]
for i in a:
    print(i)
print()
print("indexing",a[-1])
print("repilition",a*2)
b=[6,7]
print("concat",a+b)
#adding
a.append(8)
print(a)
a.extend(b)
print(a)
a.insert(5,7)
print(a)
a.insert(2,b)
print(a)
print(a[2][0])
#removing
a.remove(7)
print(a)
a.pop()
print(a)
a.clear()
print(a)
del a 
print(a)