#import another_module
#print(another_module.another_variable)
from turtle import Turtle, Screen

# jacek = Turtle()
# #print(jacek)
# jacek.shape("turtle")
# jacek.color("red")
# jacek.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu","Electric"])
table.add_row(["Squirtle","Water"])
table.add_row(["Charmander","Fire"])
# table.align = 'l'

print(table)