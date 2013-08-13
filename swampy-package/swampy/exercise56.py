from TurtleWorld import *
world = TurtleWorld()			
bob = Turtle()				
bob.delay = .01		

def koch(t, length):
	if (length<3):
		fd(t, length)
		return
	koch(t, length/3)
	lt(t, 60)
	koch(t, length/3)
	rt(t, 120)
	koch(t, length/3)
	lt(t, 60)
	koch(t, length/3)


'''def transition(t, length, angle):
	for i in range(4):
		bk(t, length/3)
		rt(t, 2*angle)
		fd(t, length/3)
		lt(t, angle)'''

def snowflake(t, length):
	for i in range(3):
		koch(t, length)
		rt(t, 120)
		'''koch(t, length, angle)
		rt(t, 2*angle)
		koch(t, length, angle)
		rt(t, 2*angle)
		koch(t, length, angle)
		rt(t, 2*angle)
		transition(t, length, angle)
		koch(t, length, angle)
		rt(t, 2*angle)
		koch(t, length, angle)
		rt(t, 2*angle)
		koch(t, length, angle)
		rt(t, 2*angle)
		koch(t, length, angle)
		rt(t, 2*angle)
		transition(t, length, angle)
		rt(t, 6*angle)
		koch(t, length, angle)
		rt(t, 2*angle)
		koch(t, length, angle)
		rt(t, 2*angle)
		koch(t, length, angle)
		rt(t, 2*angle)
		koch(t, length, angle)
		rt(t, 2*angle)
		transition(t, length, angle)
		koch(t, length, angle)'''



snowflake(bob, 300)


wait_for_user()