array=[1,2,3,4,5,6,7,8,9,10]
sum=0
while 6 in array:
	del array[array.index(6) : array.index(9)+1]
for i in array:
	sum=sum+i
print(sum)
