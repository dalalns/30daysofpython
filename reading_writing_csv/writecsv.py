import csv

'''Writing to a csv file'''

list1=[1, 2, 3]
list2=['navin','vikas' , 'vikas G']
list3=[84, 90, 92]
nms=[]
for i in range(len(list1)):
    nms.append(list((list1[i],list2[i],list3[i])))
with open('numbers3.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["sr no", "name", "marks"])
    writer.writerows(nms)

''' Reading a csv file'''
fields = []
rows = []
with open('data.csv', 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	fields = csvreader.__next__()
	print(type(csvreader))
	for row in csvreader:
		rows.append(row)
		
	#get total number of rows
	print("The total number of rows in csv is ",csvreader.line_num)
	
print("field name of csv "," ".join(fields))

for row in rows[0:2]:
	print(row[0])

''' Writing a csv file using a dictionary'''
# importing the csv module 
import csv 
  
# my data rows as dictionary objects 
mydict =[{'id': '9', 'name': 'navin', 'email': 'navin@gmail.com', 'amount': '200', 'sent':'yes'}, 
         {'id': '10', 'name': 'prince', 'email': 'prince@gmail.com', 'amount': '100', 'sent':'no'}, 
         ]
# field names 
fields = ['id', 'name', 'email', 'amount', 'sent'] 
  
# name of csv file 
filename = "data.csv"
  
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv dict writer object 
    writer = csv.DictWriter(csvfile, fieldnames = fields) 
      
    # writing headers (field names) 
    writer.writeheader() 
      
    # writing data rows 
    writer.writerows(mydict) 