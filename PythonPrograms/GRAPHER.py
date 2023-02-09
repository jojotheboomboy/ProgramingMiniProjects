# import the pygame module
import pygame
import math

func_general = input("What function would you like evaluated? ")

def transform(x):
    return ((x - HEIGHT/2)/100)

def untransform(x):
    return int(100*x + HEIGHT/2)
  
# Define the background colour
# using RGB color coding.
background_color = (255, 255, 255)
  
# Define the dimensions of
# screen object(width,height)
HEIGHT = 1000
WIDTH = 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
color_line = (100,100,100) 

# Set the caption of the screen
pygame.display.set_caption('Math_Graph')
  
# Fills the background color to the screen and sets up x and y axis
screen.fill(background_color)
pygame.draw.line(screen, color_line,(0, HEIGHT/2 + 1), (WIDTH, HEIGHT/2 + 1))
pygame.draw.line(screen, color_line,(0, HEIGHT/2 - 1), (WIDTH, HEIGHT/2 - 1))
pygame.draw.line(screen, color_line,(WIDTH/2 + 1, 0), (WIDTH/2 + 1, HEIGHT))
pygame.draw.line(screen, color_line,(WIDTH/2 - 1, 0), (WIDTH/2 - 1, HEIGHT))

# Sets up value grid
for i in range(int(HEIGHT/100)):
    value = int((i+1)*(HEIGHT/10))
    pygame.draw.line(screen, color_line,(0, value), (WIDTH, value))   
    pygame.draw.line(screen, color_line,(value, 0), (value, HEIGHT))   

pygame.display.update() 

# plots points for each pixel on the graph
for i in range(WIDTH+1):
    val = "({})".format(str(transform(i)))
    func_specfic = func_general.replace("x", val)
    if 5 >= eval(func_specfic):
        cached_untransform = HEIGHT - untransform(eval(func_specfic))
        pygame.draw.circle(screen, "blue",(i, cached_untransform), 1)


pygame.display.update()      

# Variable to keep our game loop running
running = True
  
# game loop
while running:
    
# for loop through the event queue  
    for event in pygame.event.get():
      
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False