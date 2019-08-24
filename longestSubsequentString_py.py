s=input("enter string")
l=[]
n=int(input("how many ?"))
for i in range(n):
	l.append(str(input()))
ch=[]
ch.append(s[0])
j=0
for i in range(1,len(s)):
	if(ch[j-1] == s[i]):
		continue
	else:
		ch.append(s[i])
		j =j+1


for i in range(len(l)):
	for j in range(i,len(l)):
		if len(l[i])<len(l[j]):
			x= l[i]
			y=l[j]
			del l[i]
			l.insert(i,y)
			del l[j]
			l.insert(j,x)
			
print(l)
for i in range(len(l)):
	j=0
	sp=0
	print(l[i])
	while(j<len(l[i])):
		print(l[i][j])
		if(l[i][j]==ch[sp]):
			j=j+1
		elif l[i][j]!=ch[sp]:
			sp=sp+1
		if(sp>=len(ch)):
			break
	if(j==len(l[i]) ):
		print(l[i])
		break

		
