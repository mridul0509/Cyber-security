import string 
b=1
def checkpangram(s):
	a="abcdefghijklmnopqrstuvwxyz"
	for ch in a:
		if ch not in s.lower():
			print("Not pangram")
			b=0
s=input("Enter your string")
checkpangram(s)
if(b!=0):
	print("String pangram")
