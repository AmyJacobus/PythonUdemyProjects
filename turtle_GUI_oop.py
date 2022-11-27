# import turtle as tr, requires you to use tr infront of object creation or when calling method or attribute
import second_module_gui_oop as second
from turtle import Turtle, Screen

print(second.variable) #print variable from second module

Pet = Turtle() # Create new turtle object  - Construct new object

print(Pet) # Just shows you where its being saved

my_screen = Screen()  # Create an object
print(my_screen.canvheight)  # Attribute associated with that screen
my_screen.exitonclick()  # Call a method



