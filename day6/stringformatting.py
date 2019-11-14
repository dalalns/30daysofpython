abc = "this is a line\'s"
print(abc)
abcd ="this is a string"
print(abcd.split()) #split the string based on the delimeter single space
print("this is a {var} string".format(var="really really cool"))
print("My name is {name1} and my guruji name is {name2}".format(name1="navin singh dalal",name2="prince Misra"))# string formating using variable name
name1="navin singh dalal"
name2="prince Misra"
print("My name is {0} and my guruji name is {1}".format(name1,name2)) # string formatting using indexing
print("My name is %s and my guruji name is %s" %("navin singh dalal","prince misra")) # string formatting with substitution
print("10 decimal places : %.10f" %(20)) #10 decimal places after 20
print("2 decimal places : %.2f" %(20)) #2 decimal places after 20
print("0 decimal places : %.0f" %(20)) #0 decimal places after 20
print("400 decimal places : %.400f" %(20)) #400 decimal places after 20


import datetime


default_names = ["Justin", "john", "Emilee", "Jim", "Ron", "Sandra", "veronica", "Whitney"]
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]

unf_message = """Hi {name}! 
Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!
Team CFE
"""


def make_messages(names, amounts):
    messages = []
    if len(names) == len(amounts):
        i = 0
        today = datetime.date.today()
        text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        for name in names:
            new_amount = "%.2f" %(amounts[i])
            new_msg = unf_message.format(
                    name=name,
                    date=text,
                    total=new_amount
                )
            i += 1
            print(new_msg)



make_messages(default_names, default_amounts)