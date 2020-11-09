list=[1,1,2,3,3]
b=0
for x in list:
    if ((list[x]==3)and(list[x+1]==3)):
        print("True")
        b=1
        break
if(b!=1):
	print("False")
