list_num=[1,1,2,3,3,0,0,7,9,8]
b=0
for x in range(len(list_num)):
	if((list_num[x]==0)and(list_num[x+1]==0)and(list_num[x+2]==7)):
		print("True")
		b=1
		break
if(b!=1):
	print("False")
