from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ("Arial", 8, "normal")


class Animal(Turtle):
    def __init__(self):
        super().__init__()

    def write_ok(self):
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


animal = Animal()
screen = Screen()
animal.write_ok()

screen.exitonclick()
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#
#     def breath(self):
#         super().breath()
#         print("the above print statement is form the super class")
#
#     def swim(self):
#         print("can swim")
#
#
# fishy = Fish()
# fishy.swim()
# fishy.breath()
# print(fishy.eye)

