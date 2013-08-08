from TurtleWorld import *
world = TurtleWorld()			
bob = Turtle()				
bob.delay = .01		

def koch(t, length, angle):
	'''if n == 0:
		return'''
	fd(t, length/3)
	lt(t, angle)
	fd(t, length/3)
	rt(t, 2*angle)
	fd(t, length/3)
	lt(t, angle)
	fd(t, length/3)	

def snowflake(t, length, angle):
	koch(t, length, angle)
	rt(t, angle*2)
	koch(t, length, angle)
	rt(t, angle*2)
	koch(t, length, angle)
	rt(t, angle*2)
	koch(t, length, angle)
	rt(t, angle*2)
	koch(t, length, angle)
	rt(t, angle*2)
	koch(t, length, angle)

snowflake(bob, 90, 60)		

wait_for_user()