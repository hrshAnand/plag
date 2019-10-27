n=int(input())
while n>0:
	n-=1
	count=int(input())
	flag=0
	entry=input().split()
	i=0
	while i<count:
		entry[i]=int(entry[i])
		#print(i)
		i+=1
	entry.sort()
	#print("this is entry",entry)
	i=0
	while i<count:
		#print("hello world!")
		if entry[i]>i:
			break
		else:
			flag+=1
		#print("this is i",i)
		i+=1
	print(flag)