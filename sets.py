
l=[4,4,5,6,0,7]


a= set (l)
a.add(8)

print(a)
print()
b=list(a)
print(b)
print()
m=[2,3,4,5,6,11,12]

n= set (m)
print(n)
print()

c=n.union(l)
print(c)
print()

d=n.intersection(l)
print(d)
print()
e=n.difference(l)
print(e)