import pygame
import time
import math

rungame = True
Blue = (0,0,255)
Red = (255,0,0)
Black = (0,0,0)
ball_size1 = 30
ball_size2 = 30
width = 1000
height = 1000
x_1 = 500
y_1 = 500
x_2 = 100
y_2 = 350
radius = 3000
speed = 2
isCaptured = False
screen = pygame.display.set_mode((width,height))
while rungame == True:
    for event in pygame.event.get():
        if pygame.QUIT == event.type:
            rungame = False
    screen.fill(Black)
    pygame.draw.circle(screen, Blue, (x_1,y_1), ball_size1, ball_size1)
    pygame.draw.circle(screen, Red, (x_2,y_2), ball_size2, ball_size2)
    distance = math.sqrt(abs(x_2 - x_1)**2 + abs(y_2 - y_1)**2)
    if distance <= radius:
        if not isCaptured:
            x1 = x_1
            x2 = x_2
            y1 = y_1
            y2 = y_2
            isCaptured = True
        #print(distance)
        slope = abs(y2-y1)/abs(x2-x1)
        print(slope)
        if x_2 > x_1:
             x_1 = x_1 + speed
        else:
            x_1 = x_1 - speed
        
        if y_2 > y_1:
             y_1 = y_1 + speed
        else:
            y_1 = y_1 - speed
    else:
        isCaptured = False
    pygame.display.flip()