from TurtleWorld import *
world = TurtleWorld()			
bob = Turtle()				
bob.delay = .01		

def koch(t, length, angle):
	fd(t, length/3)
	lt(t, angle)
	fd(t, length/3)


def transition(t, length, angle):
	bk(t, length/3)
	rt(t, 2*angle)
	fd(t, length/3)
	lt(t, angle)

def snowflake(t, length, angle):
		koch(t, length, angle)
		rt(t, 2*angle)
		koch(t, length, angle)
		rt(t, 2*angle)
		koch(t, length, angle)
		rt(t, 2*angle)
		transition(t, length, angle)
		transition(t, length, angle)
		transition(t, length, angle)
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
		transition(t, length, angle)
		transition(t, length, angle)
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
		transition(t, length, angle)
		transition(t, length, angle)
		transition(t, length, angle)
		koch(t, length, angle)



snowflake(bob, 90, 60)


wait_for_user()