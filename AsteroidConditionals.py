# ***********
# Asteroid Conditionals
# ES2 Homework Assignment HW3
# ************************************************************
# Adapter from Tiny Asteroids with exploding ship for Microbit
# Original created by deejaygraham
# https://gist.github.com/deejaygraham
# ************************************************************


# FILL THESE COMMENTS IN
#*****************************************
# YOUR NAME:
# NUMBER OF HOURS TO COMPLETE:  
# YOUR COLLABORATION STATEMENT(s):
#
#
#*****************************************

# Run this code in micro:bit mode

# The following is code for a mini-version of the classic game Asteroids for micro:bit.
# Feel free to read over the following functions to understand what they do,
# they should not need any modification. 
# Around line 108 you will find the start of the "main script"
# The main script is the code that makes the game work. It is missing two critical 
# conditional statements. Please fill them in.


from microbit import *
import random #This library allows us to create random numbers.

# board dimensions
pixel_width, pixel_height = 4, 4    #The micro:bit has a 5 x 5 grid of pixels
                                    #The top left position is (0,0)
                                    #The bottom right position is (4, 4)
                                    
Frame_Rate_In_Milliseconds = 500    #Speed of screen updates
                                    #smaller delay = faster = harder

ship_Y = 4  #Ship is drawn in bottom row

# ********************************
# General Game Functions -  You do not need to edit these, but you script will use them!
# ********************************

def display_start():
    #Diplay "Ready? Go!" then wait a half second
    display.scroll("Ready? Go!")
    sleep(500)

def display_game_over(ship_X, score):
    # Display a sad face, wait, then show the final score.
    hide_ship(ship_X)
    display.show(Image.SAD)
    sleep(500)
    display.scroll("Score: " + str(score))

# **************************************
# Ship functions - You do not need to edit these, but you script will use them!
# **************************************

def create_ship():
    # Return the x value for a new ship at position 2
    ship_X = 2 # Middle of screen
    return ship_X

def hide_ship(ship_X):
    # Turn off pixel at a given ship_X position
    display.set_pixel(ship_X, ship_Y, 0) #turn ship pixel off

def draw_ship(ship_X):
    # Turn on pixal at a given ship_X position
    display.set_pixel(ship_X, ship_Y, 9) #turn ship pixel on

def move_ship_left(ship_X):
    # Take a ship_X value, and reduce it by one to move left.
    # If the new value would be less than 0, return 0
    ship_X = max(ship_X - 1, 0) #return either ship_X or 0 whichever is larger
    return ship_X

def move_ship_right(ship_X):
    # Take a ship_X value, and increase it by one to move right.
    # If the new value would be more than the screen width, return the max screen width
    ship_X = min(ship_X + 1, pixel_width) #return either ship_X or pixel_width whichever is smaller
    return ship_X

# **************************************
# Asteroid Functions -  You do not need to edit these, but you script will use them!
# **************************************

def hide_asteroid(asteroid_x, asteroid_y):
    display.set_pixel(asteroid_x, asteroid_y, 0)

def draw_asteroid(asteroid_x, asteroid_y):
    display.set_pixel(asteroid_x, asteroid_y, 3)

def create_asteroid():
    asteroid_x = random.randint(0, pixel_width)
    asteroid_y = 0
    return [asteroid_x, asteroid_y]
  
def move_asteroid(asteroid_y):
    asteroid_y += 1
    return asteroid_y


# ***********************************
# Main Script  --- This will part should be modified for Homework 3
# See STEP 1 and STEP 2 below
# Once you complete them, try flashing the program to your micro:bit to test the game.
# ***********************************

score = 0

ship_X = create_ship()
[asteroid_x, asteroid_y] = create_asteroid()

# Game Start
display_start() 
display.clear()

# Main Game Loop
while True:

    draw_ship(ship_X) #Draw the first ship
    draw_asteroid(asteroid_x, asteroid_y) #Draw the first asteroid

    sleep(Frame_Rate_In_Milliseconds) #Delay between animations

    if False :  #Test to see if the ship has hit an asteroid
        # STEP 1 ##########################################################
        # Write a logical expression (replace the "False") above to determine 
        # if the ship and asteroid are at the same location
        # That is to say, that they have the same X and Y postion
        display_game_over(ship_X , score)
        break

    hide_ship(ship_X)
    hide_asteroid(asteroid_x, asteroid_y)

    if False:   #Test to see if the current asteroid is at the bottom
        # STEP 2 ###########################################################
        # Write a logical expression (replace the "False") above to determine
        # if the asteroid is at the bottom of the screen. That is if asteroid_y
        # is equal to 4
        score += 1
        [asteroid_x, asteroid_y] = create_asteroid()
    else:
        # Check for button pushes, and move ship appropriately
        if button_a.was_pressed():
            ship_X = move_ship_left(ship_X)
        elif button_b.was_pressed():
            ship_X = move_ship_right(ship_X)
        asteroid_y = move_asteroid(asteroid_y)
