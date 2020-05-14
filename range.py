#Range type
r=range(6)
for i in r :
   print(i)
   
   
   
r=range(1,15,5)
for i in r :
   print(i) 
   
   
#bytes and bytearray
l=[10,20,30,40,50,]
print(type(l))
print(l)

b=bytes(l)
print(type(b))
print(b)

b1=bytearray(l)
print(type(b1))
b1[2]=33
print(b1)




#dictionary
dict={1:"p",2:"r",3:"a"}
print(dict)

#to access both key & value
print(dict.items())
# to access only keys
k=dict.values()
for i in k : print(i)
print(dict[3])
del(dict[2])
print(dict)
