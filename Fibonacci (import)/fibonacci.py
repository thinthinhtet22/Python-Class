#Fibonacci
fibonacci.py

# Fibonacci numbers module

#n = int(input('Please enter a number: '))

def fib(n):   #write Fibonacci series up
	a, b = 0, 1
	while a < n:
		print(a, end='')
		a, b = b, a+b
		print()

# Go to Fibonacci Powerpoint

def fib2(n):   # return Fibonacci series uo
	result = []
	a, b =  0, 1
	while x < n:
		result,append(a)
		a, b = b, a+b
		return result