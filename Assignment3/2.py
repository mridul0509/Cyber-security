def check(a,b):
	if(a%2 == 0 and b%2==0):
		if(a>b):
			return b
		else:
			return a
	if(a%2!=0 and b%2!=0):
		if(a>b):
			return a
		else:
			return b
a=int(input("Enter value os a"))
b=int(input("Enetr valur of b"))
c=check(a,b)
print(c)
