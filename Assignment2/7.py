r=int(input("Enter range"))
def prime(j):
	c=0
	p="Prime"
	np="Nonprime"
	for k in range(2,j):
		if(j%k==0):
			c=c+1
	if(c==0):
		return p
	else:
		return np
l=[(i,prime(i)) for i in range(2,r+1)]
print(l)
