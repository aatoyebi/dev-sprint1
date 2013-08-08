# This is where Exercise 5.4 goes
# Name: Amaka Atoyebi

def is_triangle(a, b, c):
	triangleSum = a + b
	if (triangleSum <= c):
		print "Yes"
	else:
		print "No"

def the_input():
	for value in ['a', 'b', 'c']:
		prompt = "Enter length for " + value + "\n"
		myInput = raw_input(prompt)
		intNum = int(myInput)
		exec('%s = %i' % (value, intNum))
	is_triangle(a, b, c)

the_input()	

	

		
