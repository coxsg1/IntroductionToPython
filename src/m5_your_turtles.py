"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Sarah Cox.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
import rosegraphics as rg

window = rg.TurtleWindow()

purple_turtle = rg.SimpleTurtle('turtle')
purple_turtle.pen_up()
purple_turtle.go_to(rg.Point(100,30))
purple_turtle.pen_down()
purple_turtle.pen = rg.Pen('purple', 3)
purple_turtle.speed = 100  # Fast
size = 100
for k in range(20):

    purple_turtle.draw_square(size)

    purple_turtle.pen_up()
    purple_turtle.right(45)
    purple_turtle.forward(20)
    purple_turtle.left(45)

    purple_turtle.pen_down()
    size = size - 8

blue_turtle = rg.SimpleTurtle('turtle')
blue_turtle.pen_up()
blue_turtle.go_to(rg.Point(-100,-60))
blue_turtle.pen_down()
blue_turtle.pen = rg.Pen('blue',3)
blue_turtle.speed = 100
size = 20
for k in range(11):

    blue_turtle.draw_regular_polygon(size, size)

    blue_turtle.pen_up()
    blue_turtle.right(45)
    blue_turtle.forward(8)
    blue_turtle.left(45)

    blue_turtle.pen_down()
    size = size - 2



#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
