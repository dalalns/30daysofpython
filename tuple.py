atuple = (1,2,3)
atuple = (1,2,3,["navin","prince"],{"0":"navin","1":"prince"}) # we can add a list or dictionary or simple integer or string to tuple
atuple[3] = ['abcd','efgh'] #This is not supported in tuple as tuple is immutable, Error TypeError: 'tuple' object does not support item assignment
atuple[3][0] = "navin sing dalal" # This is ok as the list present in tuple is mutable so the tuple can be updated here.
atuple[4]["0"]="navin singh dalal" # This is also ok as dict present in tuple is mutable so tuple can be updated here.
