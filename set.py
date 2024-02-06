#inbuild numeric function
import math
print(math.sqrt(145))
print(math.pow(2,7))
print(math.exp(0))
print(math.ceil(3.2))
print(math.floor(6.9))
print(math.fabs(-4.6))
print(round(6.7))
print(min(32,98,87,65))

a=12345678
count=0
while a!=0:
    a=a//10
    count+=1
print(count)
b=987987
c=str(b)
print(len(c))

print(a)
#set
a={'red','blue','green'}
print(a)
a.add("yellow")
print(a)
b={'wehite','black'}
print(a.update(b))
print(a)
#set operation
c={'sql','wd','python'}
d={'sql','wd','java'}
e=c&d
e=c|d
e=c-d
e=d-c
e=c^d
print(e)

#quesion
w=[1,2,1,5,2,8]
k=[]
for i in w:
    if i not in k:
        k.append(i)
print(k)

p=[1,2,1,5,2,8]
o=sorted(list(set(p)))
print(o)

v={"id":1,"name":"abc"}
print(v["name"])
v["id"]=33
print(v)
r={"age":33,"course":"python"}
v.update(r)
print(v)
print(v.values())
print(v.keys())
print(v.items())
print(v.pop("id"))
print(v.popitem())
del a["name"]
print(v)
