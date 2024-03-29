adict={0:"navin",1:"prince"}
adict[0]="navin singh dalal"
adict[2]=[1,2,3] # value can be a iterable like list
adict[3]=(4,5,6) # value can be a iterable like tuple
adict[4]={'abc':'abcd1','efgh':'efgh1'} # value can be iterable like dict inside a dict. key can be integer or can be a string
adict[[5,6]]=[7,8,9] # this is not possible as the key can not be unhasble type like list ,TypeError: unhashable type: 'list'
'''
Anything that is not mutable (mutable means, likely to change) can be hashed. Besides the hash function to look for, if a class has it, by eg. dir(tuple) and looking for the __hash__ method, here are some examples

#x = hash(set([1,2])) #set unhashable
x = hash(frozenset([1,2])) #hashable
#x = hash(([1,2], [2,3])) #tuple of mutable objects, unhashable
x = hash((1,2,3)) #tuple of immutable objects, hashable
#x = hash()
#x = hash({1,2}) #list of mutable objects, unhashable
#x = hash([1,2,3]) #list of immutable objects, unhashable
List of immutable types:

int, float, decimal, complex, bool, string, tuple, range, frozenset, bytes
List of mutable types:

list, dict, set, bytearray, user-defined classes #These could not be used as key of dict
'''
adict[True]=[7,8,9] # This is possible and it will update the dict key 1
adict[False]='xyz' # This is also possible and it will update the record at key 0

adict[('a','b')]='tuple of a and b' # this is also possible as tuple is immutable