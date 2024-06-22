def add(a,b):
	return a + b
def subtract(a,b):
	return a - b
def devide(a,b):
	try:
		result = a/b
	except ZeroDivisionError:
		return "Error : Division by Zero is not possible"
	return result
