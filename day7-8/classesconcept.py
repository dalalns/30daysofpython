class Animal:
	name ='Amy'
	color='brown'
	noise='Grunt'
	def get_color(self):
	    return self.color
	
	def change_color(self, col):
		self.color=col
		return self.color
	@property	# used to define the method as a property and than we can call the funtion without parantheses Animal().make_noice
	def make_noice(self):
		return self.noise
#inheirtance Dog class inheiret the feature of animal class
class Dog(Animal):
	name='john'
	
			
instace = Dog() #instance or object of class type Dog
obj = Dog() ##instance or object of class type Dog with instance name as obj	
obj.name # this will print john
instace.name # this will also print john

obj.name = 'navin' # we have changed the attribute of class dog which  have obj object or instance
obj.color='red'
print(obj.name) # this will print navin
print(instace.name) #this will print john as it is not changed
print(obj.get_color())
print(instace.get_color())

object=Animal()
print(object.change_color('green'))
print('function noise',object.make_noice)
#positional arg like arg1 are declared ahead of keyword argument like keyarg
def some_func(arg1,arg2,keyarg=None,keyarg2=None):
	print(arg1,arg2)

some_func("navin","prince")	

