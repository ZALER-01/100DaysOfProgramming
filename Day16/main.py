# from turtle import Turtle ,Screen
# import another_module
#
# print(another_module.another_module)
#
# timmy = Turtle()
# print(timmy)
# my_screen = Screen()
# print(my_screen.canvheight)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# my_screen.exitonclick()


# How to add packages in pypi

import prettytable

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Company Name", ["WondersMind Infotech","Hcl Tech","Tredence Analytics","Diebold Nixdord"])
table.add_column("Start Date" , ["01 Sep 2021" ,"07 jan 2022","01 Oct 2024" ,"04 May 2026"])
table.align["Company Name"] = "l"

print(table)

# A Class is a blueprint of any object



