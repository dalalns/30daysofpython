alist=[12,5,15,1,3,5,2]
#sort a list using sort function
alist.sort()
print(alist)
newlist = sorted(alist)
print(newlist)

stringlist=['bcd','aa','bb','ff','AD']
stringlist.sort()
print(stringlist) #sorts the list but keep the capital letters at first and than sorts the list of lower case letters
stringlist.sort(key=str.lower)
print(stringlist)

newstringlist=sorted(stringlist,key=str.lower,reverse=True)
print(newstringlist)

def mysum(mylist):
	total=0
	for i in mylist:
		if isinstance(i,int) or isinstance(i, float):
			total += i
	return total

item1 = [1,2,3,4,5,'navin','prince']
print(mysum(item1))	