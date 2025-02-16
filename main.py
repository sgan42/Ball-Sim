import pygame
import time
import math
import tkinter as tk

root = tk.Tk()
def on_slider_change(oo):
    label.config(text=f"Speed: {oo}")
label = tk.Label(root, text="Speed = 0", font=("Times New Roman", 20))
label.pack(pady=10)

# Create the slider (from 0 to 100)
slider_value = tk.DoubleVar(value=0)
slider = tk.Scale(root, from_=0, to=100, orient="horizontal", command=on_slider_change, variable=slider_value)
slider.pack(padx=100)
rungame = True
Blue = (0,0,255)
Red = (255,0,0)
Black = (0,0,0)
ball_size1 = 30
ball_size2 = 30
width = 1000
height = 1000
blueX = 500
blueY = 500
redX = 1
redY = 350
radius = 3000
speed = 2
isCaptured = False
screen = pygame.display.set_mode((width,height))
while rungame == True:
    for event in pygame.event.get():
        if pygame.QUIT == event.type:
            rungame = False
    root.update()
    root.update_idletasks()
    screen.fill(Black)
    pygame.draw.circle(screen, Blue, (blueX,blueY), ball_size1, ball_size1)
    pygame.draw.circle(screen, Red, (redX,redY), ball_size2, ball_size2)
    distance = math.sqrt(abs(redX - blueX)**2 + abs(redY - blueY)**2)
    speed = slider_value.get()/5
    print(speed)
    if distance <= radius:
          # Calculate direction vector (dx, dy)
        dx = redX - blueX
        dy = redY - blueY

        # Normalize the direction vector (to avoid speeding up as the balls get closer)
        length = math.sqrt(dx**2 + dy**2)
        dx /= length
        dy /= length
        
        # Move the blue ball towards the red one
        blueX += dx * speed
        blueY += dy * speed
    else:
        isCaptured = False

# Start the Tkinter event loop
    pygame.display.flip()
    pygame.time.Clock().tick(60)
