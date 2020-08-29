s=input("Enter the srting ")
def palin(s):
 s1=s[::-1]
 if(s == s1):
  return 1;
 else:
  return 0
a=palin(s)
if(a==1):
 print("palindrome")
else:
 print("not plaindrome")
