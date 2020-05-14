l=[]
print(l)

l=[10,20,30,'pranay',40,50,54]
print(l)
print(l[3])
print(l[3:5])
print(len(l))
print(l*4)


l.append(40)
print(l)
l.remove('pranay')
print(l)
del(l[3])
print(l)

print(max(l))
print(min(l))

l.insert(3,99)
print(l)

l.sort()
print(l)

l.sort(reverse=True)
print(l)

l.append("Japan")
l[3]
print(l)