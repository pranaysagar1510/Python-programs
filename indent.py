x =int(input("enter min numbr"))
y =int(input("enter max number"))
i=x
if i%2 ==0: i=x+1
while i<=y:
    print(i)
    i+=2
    print(i)