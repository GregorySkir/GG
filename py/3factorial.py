def factorial(num=1):
	"""
	Calcualtes the factorial of the integer number in num. if num is not integer, return None.
	Returns: num!
	"""

	if type(num) is not int:
		print('{} is not an integer. Please enter a \
		positive integer number'.format(num))
		return
	if num < 0:
		print('{} in negative. Please enter a positive integer number'.format(num))
		return
	total = 1
	for i in range(2, num+1):
		total *= i
	return(total)

def factorial2(num=1):
    total = 1
    if num > 1:
        total = num * factorial2(num-1)
    return(total)


x  = factorial2(5)
print(x)