alist=[1,2,3,4,5,"navin","prince"]
print("Complete list \n",alist)
print("First element \n", alist[0])
print("Last element \n", alist[-1])
print("Last element \n", alist[len(alist)-1])
print("Length of list \n", len(alist))
alist.append([8,9,10]) #This will append 8,9,10 as list objects in the list so we have a list inside a list
alist.extend([10,11,12]) #This will iterate over the list and add the integer as object in the list
print("alist After append and Extend \n",alist)
alist.extend(13)# This will give error as 13 is not a iterable object , TypeError: 'int' object is not iterable
print(help(alist)) #To check what are the methods and class bluprint of list class
print(dir(alist)) #To print a list of methods and members of class alist has
