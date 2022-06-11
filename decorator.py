#This is my own decorator function
def mydecorator(any_function):
#This decorator func will take ur any custom func as an argument

	#This is a wrapper function that will get called when the decorator will get called!
	def wrapper(*args, **kwargs):
	#*args so that this wrapper func will become generic and will take any arguments
		print("I am decorating ur function! ")
		any_function(*args, **kwargs)
		#As we want to make it generic any function can have any number of args hence *args here too!
	
	#returning the output of the wrapper function
	return wrapper

@mydecorator
def hello(person):
	print(f"Hello {person}! ")

hello("Chinya")

#Output
#I am decorating ur function!
#Hello Chinya!
