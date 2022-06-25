#chan kin hang 20386450 khchancb@connect.ust.com
"""
    Turtle Graphics - Shooting Game
"""

import turtle
import random
from playsound import playsound

"""
    Constants and variables
"""
# General parameters
window_height = 600
window_width = 600
window_margin = 50
update_interval = 25    # The screen update interval in ms, which is the
                        # interval of running the updatescreen function

# Player's parameters
player_size = 50        # The size of the player image plus margin
player_init_x = 0
player_init_y = -window_height / 2 + window_margin
player_speed = 30       # The speed the player moves left or right

# Enemy's parameters
enemy_number = 10        # The number of enemies in the game

enemy_size = 50         # The size of the enemy image plus margin
enemy_init_x = -window_width / 2 + window_margin
enemy_init_y = window_height / 2 - window_margin
enemy_min_x = enemy_init_x
enemy_max_x = window_width / 2 - window_margin
    # The maximum x coordinate of the first enemy, which will be used
    # to restrict the x coordinates of all other enemies
enemy_hit_player_distance = 30
    # The player will lose the game if the vertical
    # distance between the enemy and the player is smaller
    # than this value

# Enemy movement parameters
enemy_speed = 2
enemy_speed_increment = 1
    # The increase in speed every time the enemies move
    # across the window and back
enemy_direction = 1
    # The current direction the enemies are moving:
    #     1 means from left to right and
    #     -1 means from right to left

# The list of enemies
enemies = []

# Laser parameter
laser_width = 2
laser_height = 15
laser_speed = 20
laser_hit_enemy_distance = 20
    # The laser will destory an enemy if the distance
    # between the laser and the enemy is smaller than
    # this value

enemy_firing_interval = 175

s = 0

A = turtle.Turtle()
A.hideturtle()
def startscreen():
    global start_button, labels, enemy_number_text, left_arrow, right_arrow, Title
    start_button = turtle.Turtle()
    # Set up the start_button
    start_button.up()
    start_button.goto(-40, -40)
    start_button.color("White", "DarkGray")
    start_button.begin_fill()
    for _ in range(2):
        start_button.forward(80)
        start_button.left(90)
        start_button.forward(25)
        start_button.left(90)
    start_button.end_fill()
    start_button.color("White")
    start_button.goto(0, -35)
    start_button.write("Start", font=("System", 12, "bold"), align="center")
    start_button.goto(0, -28)
    start_button.shape("square")
    start_button.shapesize(1.25, 4)
    start_button.color("")
    start_button.onclick(gamestart)
    # Set up other controls

    labels = turtle.Turtle()
    labels.hideturtle()
    labels.color('white')
    labels.up()
    labels.goto(-100, 0) # Put the text next to the spinner control
    labels.write("Number of Enemies:", font=("System", 12, "bold"))

    enemy_number_text = turtle.Turtle()
    enemy_number_text.hideturtle()
    enemy_number_text.color('white')
    enemy_number_text.up()
    enemy_number_text.goto(80, 0)
    enemy_number_text.write(str(enemy_number), font=("System", 12, "bold"), align="center")

    left_arrow = turtle.Turtle()
    left_arrow.shape("arrow")
    left_arrow.color("white")
    left_arrow.shapesize(0.5, 1)
    left_arrow.left(180)
    left_arrow.up()
    left_arrow.goto(60,8)
    left_arrow.onclick(decrease_enemy_number)

    right_arrow = turtle.Turtle()
    right_arrow.shape("arrow")
    right_arrow.color("white")
    right_arrow.shapesize(0.5, 1)
    right_arrow.up()
    right_arrow.goto(100,8)
    right_arrow.onclick(increase_enemy_number)

    Title = turtle.Turtle()
    Title.hideturtle()
    Title.color('white')
    Title.up()
    Title.goto(0, 200)
    Title.write("Python", font=("System", 30, "bold"), align="center")
    Title.goto(0, 150)
    Title.write("The last fight", font=("System", 30, "bold"), align="center")
    Title.goto(0,100)
    Title.write("Control Harry Potter using the arrow keys", font=("System", 17, "bold"), align="center")
    Title.goto(0,50)
    Title.write("and space bar to kill Voldemort", font=("System", 17, "bold"), align="center")
    
    turtle.update()

def decrease_enemy_number(x,y):
    global enemy_number, enemy_number_text
    if enemy_number > 1:
        enemy_number_text.clear()
        enemy_number = enemy_number - 1
        enemy_number_text.write(str(enemy_number), font=("System", 12, "bold"),align="center")

def increase_enemy_number(x,y):
    global enemy_number, enemy_number_text
    if enemy_number < 48:
        enemy_number_text.clear()
        enemy_number = enemy_number + 1
        enemy_number_text.write(str(enemy_number), font=("System", 12, "bold"),align="center")

"""
    Handle the player movement
"""
# This function is run when the "Left" key is pressed. The function moves the
# player to the left when the player is within the window area
def playermoveleft():

    # Get current player position
    x, y = player.position()

    # Part 2.2 - Keeping the player inside the window
    # Player should only be moved only if it is within the window range
    if x - player_speed > -window_width / 2 + window_margin:
        player.goto(x - player_speed, y)

     # delete this line after finishing updatescreen()

# This function is run when the "Right" key is pressed. The function moves the
# player to the right when the player is within the window area
def playermoveright():

    # Get current player position
    x, y = player.position()

    # Part 2.2 - Keeping the player inside the window
    # Player should only be moved only if it is within the window range
    if x + player_speed < window_width / 2 - window_margin:
        player.goto(x + player_speed, y)

     # delete this line after finishing updatescreen()

def increase_enemy_firing_interval():
    global enemy_firing_interval
    if enemy_firing_interval < 975:
        enemy_firing_interval = enemy_firing_interval + 100

def decrease_enemy_firing_interval():
    global enemy_firing_interval
    if enemy_firing_interval > 175:
        enemy_firing_interval = enemy_firing_interval - 100

def stop():
    global s
    if s == 0:
        s = 1
    else:
        s = 0
    click()

def click():
    for enemy in enemies:
        enemy.onclick(kill)
def kill(x,y):
    A.goto(x,y)
    for enemy in enemies: 
        if enemy.isvisible() and A.distance(enemy)< laser_hit_enemy_distance:
                enemy.hideturtle()
                playsound('killed.wav')
    
              
    
"""
    Handle the screen update and enemy movement
"""

# This function is run in a fixed interval. It updates the position of all
# elements on the screen, including the player and the enemies. It also checks
# for the end of game conditions.
def updatescreen():
    # Use the global variables here because we will change them inside this
    # function
    global enemy_direction, enemy_speed, bullet, enemy_firing_interval,s

    # Move the enemies depending on the moving direction

    # The enemies can only move within an area, which is determined by the
    # position of enemy at the top left corner, enemy_min_x and enemy_max_x

    # x and y displacements for all enemies
    dx = enemy_speed * enemy_direction
    dy = 0

    # Part 3.3
    # Perform several actions if the enemies hit the window border
    x0 = enemies[0].xcor()
    if enemy_number//6 > 0:
        xLast = enemies[5].xcor()
    else:
        xLast = enemies[-1].xcor()
    if xLast + dx > enemy_max_x or x0 + dx < enemy_min_x:
        # Switch the moving direction
        enemy_direction = -enemy_direction
        # Bring the enemies closer to the player
        dy = -enemy_size / 2
        # Increase the speed when the direction switches to right again
        if enemy_direction == 1:
            enemy_speed = enemy_speed + enemy_speed_increment
    # Move the enemies according to the dx and dy values determined above
    if  s == 0:
        for enemy in enemies:
            x, y = enemy.position()
            enemy.goto(x + dx, y + dy)
            if y > 0:
                if (x // 20) % 2 == 0 :
                    enemy.shape("V.gif")
                else:
                    enemy.shape("V2.gif")
            else:
                if (x // 20) % 2 == 0 :
                    enemy.shape("V3.gif")
                else:
                    enemy.shape("V2.gif")
    # Part 4.3 - Moving the laser
    # Perfrom several actions if the laser is visible
    if laser.isvisible():
        # Move the laser
        laser.goto(laser.xcor(),laser.ycor()+ laser_speed)
        # Hide the laser if it goes beyong the window
        if laser.ycor() > window_height / 2:
            laser.hideturtle()
        # Check the laser against every enemy using a for loop
    if laser.isvisible():
        for enemy in enemies: 
            # If the laser hits a visible enemy, hide both of them
            if enemy.isvisible() and laser.distance(enemy)< laser_hit_enemy_distance:
                # Stop if some enemy is hit
                enemy.hideturtle()
                laser.hideturtle()
                playsound('killed.wav')
                break

    if bullet.isvisible() and s == 0:
        # Move the laser
        bullet.goto(bullet.xcor(),bullet.ycor()- laser_speed)
        # Hide the laser if it goes beyong the window
        if bullet.ycor() < -(window_height / 2):
            bullet.hideturtle()
            turtle.ontimer(enemy_bullet, enemy_firing_interval)
        if bullet.distance(player) < laser_hit_enemy_distance:
                # Stop if some enemy is hit
                bullet.hideturtle()
                player.hideturtle()
                gameover("You Lose!")
                return
    
    # Part 5.1 - Gameover when one of the enemies is close to the player

    # If one of the enemies is very close to the player, the game will be over
    for enemy in enemies:        
        if enemy.ycor()-player.ycor() < enemy_hit_player_distance and enemy.isvisible():
            # Show a message
            gameover("You Lose!")
            # Return and do not run updatescreen() again
            return

    # Part 5.2 - Gameover when you have killed all enemies
    
    # Set up a variable as a counter
    count = 0
    # For each enemy
    for enemy in enemies:
        if enemy.isvisible():
        # Increase the counter if the enemy is visible
            count = count + 1
    # If the counter is 0, that means you have killed all enemies
    if count == 0:
        # Perform several gameover actions
        gameover("You Won!")
        return
    # Part 3.1 - Controlling animation using the timer event
    turtle.update()
    turtle.ontimer(updatescreen, update_interval)
    #
    # Add code here
    #
    
"""
    Shoot the laser
"""

# This function is run when the player presses the spacebar. It shoots a laser
# by putting the laser in the player's current position. Only one laser can
# be shot at any one time.
def shoot():

     # delete this line after completing the function

    # Part 4.2 - the shooting function
    # Shoot the laser only if it is not visible
    if not laser.isvisible():
        laser.showturtle()
        playsound('shoot.wav')
        laser.goto(player.position())
        
    #
    # Add code here
    #
def enemy_bullet():
    for enemy in enemies:
        if enemy.isvisible() and random.randint(0,1) == 0:
            bullet.showturtle()
            x, y = enemy.position()
            bullet.goto(enemy.position())
"""
    Game start
"""
# This function contains things that have to be done when the game starts.
  
def gamestart(x, y):
    start_button.clear()
    start_button.hideturtle()

    labels.clear()
    labels.hideturtle()

    enemy_number_text.clear()
    enemy_number_text.hideturtle()

    left_arrow.clear()
    left_arrow.hideturtle()

    right_arrow.clear()
    right_arrow.hideturtle()

    Title.clear()
    Title.hideturtle()
    # Use the global variables here because we will change them inside this
    # function
    global player, laser,bullet, enemy_firing_interval

    ### Player turtle ###

    # Add the spaceship picture
    turtle.addshape("Harry_Potter.gif")

    # Create the player turtle and move it to the initial position
    player = turtle.Turtle()
    player.shape("Harry_Potter.gif")
    player.up()
    player.goto(player_init_x, player_init_y)

    # Part 2.1
    # Map player movement handlers to key press events
    turtle.onkeypress(playermoveleft, "Left")
    turtle.onkeypress(playermoveright, "Right")
    turtle.listen()
    #
    # Add code here
    #
    turtle.onkeypress(decrease_enemy_firing_interval, "comma")
    turtle.onkeypress(increase_enemy_firing_interval, "period")
    ### Enemy turtles ###

    # Add the enemy picture
    turtle.addshape("Voldemort1.gif")
    turtle.addshape("Voldemort2.gif")
    turtle.addshape("Voldemort3.gif")

    for i in range(enemy_number):
        # Create the turtle for the enemy
        enemy = turtle.Turtle()
        enemy.shape("Voldemort1.gif")
        enemy.up()

        # Move to a proper position counting from the top left corner
        enemy.goto(enemy_init_x + enemy_size * (i % 6), enemy_init_y - enemy_size * (i // 6))

        # Add the enemy to the end of the enemies list
        enemies.append(enemy)
    ### Laser turtle ###

    # Create the laser turtle using the square turtle shape
    laser = turtle.Turtle()
    turtle.addshape("shooting_laser.gif")
    laser.shape("shooting_laser.gif")

    # Change the size of the turtle and change the orientation of the turtle
    
    
    laser.up()

    # Hide the laser turtle
    laser.hideturtle()

    # Part 4.2 - Mapping the shooting function to key press event
    turtle.onkeypress(shoot, "space")
    #
    # Add code here
    #
    turtle.onkeypress(stop, "s")

    #Enemy_enemy_bullet
    bullet = turtle.Turtle()
    turtle.addshape("enemy_bullet.gif")
    bullet.shape("enemy_bullet.gif")
    
    
    bullet.up()
    bullet.hideturtle()
    
    
    turtle.update()

    # Part 3.1 - Controlling animation using the timer event
    turtle.ontimer(updatescreen, update_interval)
    #
    # Add code here
    #
    turtle.ontimer(enemy_bullet, 200)
"""
    Game over
"""

# This function shows the game over message.
def gameover(message):

    # Part 5.3 - Improving the gameover() function
    message_turtle = turtle.Turtle()
    if message == 'You Won!':
        message_turtle.color("yellow")
        playsound('winning.wav')
    if message == 'You Lose!':
        message_turtle.color("red")
        playsound('gameover.wav')
    message_turtle.write(message, align='center', font=("System", 30, "bold"))
    turtle.hideturtle()
    turtle.uplate()
    print(message) # delete this line after completing the function

"""
    Set up main Turtle parameters
"""

# Set up the turtle window
turtle.setup(window_width, window_height)
turtle.addshape("Harry_Potter_cover.gif")
cover = turtle.Turtle()
cover.goto(0,0)
cover.shape("Harry_Potter_cover.gif")
turtle.up()
turtle.hideturtle()
turtle.tracer(False)

# Start the game
startscreen()

# Switch focus to turtle graphics window
turtle.done()
