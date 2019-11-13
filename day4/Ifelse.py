items=['navin','prince',1,2,3,4,'shaurya']
x=0
list_int=[]
list_string=[]
for i in  items:
	if isinstance(items[x],int):
		list_int.append(items[x])
	else:
		 list_string.append(i)
	x+=1
print(list_int)
print(list_string)