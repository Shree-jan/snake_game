from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

scoreboard = Scoreboard()
food = Food()
snake = Snake()
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake_Game")
screen.tracer(0)  # This code is used to stop the animation on the screen. This is because, if the code isn't used then
# we can see the movement of each blocks in the snake body. However, if we stop the animation now and resume the
# animation later when a certain block of code is executed than the whole snake body moves simultaneously.


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()  # resumes the animation
    time.sleep(0.08)  # delays the screen by given time
    snake.move()

    # Detecting collision with food
    if snake.head.distance(food) < 15:  # turtle.distance(x,y) detects the distance of one turtle with the another. Here
        # (x,y) is the x and y coordinate of the another turtle. Here, food
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # DETECT COLLISION WITH WALL
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # DETECT SELF COLLISION
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass  # Difference between pass and continue. continue forces the loop to start at the next iteration
        #     # whereas pass means "there is no code to execute here" and will continue through the remainder of the loop
        #     # body.
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
