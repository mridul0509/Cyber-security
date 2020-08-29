def unique(l):
 u=[]
 for i in l:
  if i not in u:
   u.append(i)
 return u
l=[1,1,2,3,42,12,3,3,12,12,2,4,42,1,2,3,4,1,3,23]
print(unique(l))
