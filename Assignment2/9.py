import sys

def fibo(N):
	a,b,c=0,1,0
	while(c<N):
			print(a,end=" ")
			c=c+1
			a,b=b,a+b
fibo(int(sys.argv[1]))
