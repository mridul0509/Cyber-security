num=int(input("Enter upper bound : "))
for j in range(num+1):
   if (j > 1):
      k=0
      for i in range(2,j):
          if (j % i) == 0:
              k=1
              break
      if(k!=1):
           print(j,"is a prime number")
