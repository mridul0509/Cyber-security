a=int(input())
b=int(input())
c=int(input())
sum=a+b+c
if(sum<=21):
	print(sum)
else:
	if(a==11 or b==11 or c==11):
		sum=sum-10
	if(sum>21):
		print("Bust")
	else:
		print(sum)
