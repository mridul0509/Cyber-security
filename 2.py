low=int(input("enter low value "))
high=int(input("enter high value "))
def check(low,high):
 n=float(input("Enter number to be checked "))
 if(n>=low and n<=high):
  print("In range")
 else:
  print("Not in range")
check(low,high)
