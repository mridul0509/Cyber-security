def count():
 s=input("enter string ")
 u,l=0,0
 for i in s:
  if(i.isupper()== True):
   u=u+1
  elif(i.islower()== True):
   l=l+1
 print("upper case= ",u)
 print("lower case= ",l)
count()
 
