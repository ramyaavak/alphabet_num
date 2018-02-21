a=raw_input()
n=len(a)
r=0
k=0
for i in range(0,n):
	if(a[i]>='a' and a[i]<='z'):
		r=r+1
	if(a[i]>='0' and a[i]<='9'):
		k=k+1
if((r and k)>0):
	print("yes")
else:
	print("no")
