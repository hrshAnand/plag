n=int(input())
while n>0:
	n-=1
	count=int(input())
	string=input()
	store=[]
	lent=[]
	i=1
	while i<count:
		if string[i]==string[0]:
			if string[0:i-1]==string[i:2*i-1]:
				store.append(string[0:i-1])
				lent.append(i)
		i+=1
	len_temp=lent
	temp=len(len_temp)
	if store==[]:
		print(string)
	else:
		len_temp.sort()
		print(store[lent.index(len_temp[temp-1])])