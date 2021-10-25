from turtle import Turtle
bob = Turtle()
bob


bob.forward(100)

bob.reset()

#then we do 4 repetitions of forward, then right
for i in range(4):
    bob.forward(100)
    bob.right(90)

# 1)
def square(t):
    for i in range(4):
        t.forward(100)
        t.right(90)
bob.reset()
square(bob)

# 2)
bob.reset()
def square_len(t, side):
    for i in range(4):
        t.forward(side)
        t.right(90)
square_len(bob, 120)

# 3)
bob.reset()
def polygon(t, n, side):
    for i in range(n):
        t.forward(side)
        t.right(360/n)
polygon(bob, 8, 120)

# 4)
bob.reset()
def circle(t, r):
    #note that for a polygon, the perimeter is n*side
    #for a circle, the circumference is pi*2*r
    #let's approximate a circle with a 360-gon.
    #for this, side length is side = 2*pi*r/n
    import math
    polygon(t, 360, 2*math.pi*r/360)
#circle(bob, 75)

# 5)
bob.reset()
def arc(t, r, angle):
    import math
    #polygon(t, 360, 2*math.pi*r/360)
    side = math.pi*r/180
    for i in range(angle):
        t.forward(side)
        t.right(1)
# arc(bob, 75, 90)
