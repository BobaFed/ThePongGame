from turtle import Screen, Turtle
from paddle import Paddle
from ball import Pallo
from scoreboard import Scoreboard
import time
from map import Kartta

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_maila = Paddle((350, 0))
l_maila = Paddle((-350, 0))
balls = Pallo()
score_l = Scoreboard((-100, 350))
score_r = Scoreboard((100, 350))
arena = Kartta()


screen.listen()
screen.onkey(r_maila.go_up, "Up")
screen.onkey(r_maila.go_down, "Down")
screen.onkey(l_maila.go_up, "w")
screen.onkey(l_maila.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(balls.move_speed)
    screen.update()
    balls.move()

    #Detect collision with wall
    if balls.ycor() > 280 or balls.ycor() < -280:
        balls.bounce_y()

    #Detect collision with paddle
    if balls.distance(r_maila) < 50 and balls.xcor() > 320 or balls.distance(l_maila) < 50 and balls.xcor() < -320:
        balls.bounce_x()

    # Check if ball misses, reset and add score to left side player
    if balls.xcor() > 380:
        balls.huti()
        score_l.lisaa_piste()

    # Check if ball misses, reset and add score to right side player
    if balls.xcor() < -380:
        balls.huti()
        score_r.lisaa_piste()

screen.exitonclick()