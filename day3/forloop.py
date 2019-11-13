items = [10,123,1121,432,12121]
print(len(items)) # This will print the length of all the items
#The below code will print all items
for i in items:
	print(i)
#the below code print the number or records in the list one by one  
j=0
for k in items:
	print("The record no. at position "+str(j+1)+" is : "+str(items[j]))
	j=j+1