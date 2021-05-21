#import the system and pygame library
import sys, pygame, random

#Initialize pygame
pygame.init()

#Settinng Window Size
size = width, height = 650,350

#Creating a display
display = pygame.display.set_mode(size)

# Loading a ball image
ball = pygame.image.load("intro_ball.gif")

# Measure the ball size in rectangle
ballrect = ball.get_rect()

# Setting the ball speed
speed = [1,1]
# Setting color (black; 0,0,0)
black = 0,0,0
randcol = random.randint(0,255), random.randint(0,255), random.randint(0,255)
# Makes the game repeating
count = 0
while (True):
	for event in pygame.event.get():
		if (event.type == pygame.QUIT):
			sys.exit()
	# Changing ball direction after bouncing
	ballrect = ballrect.move(speed)
	if (ballrect.left < 0 or ballrect.right > width):
		speed[0] *= -1
	if (ballrect.top < 0 or ballrect.bottom > height):
		speed[1] *= -1
	
	# Setting Background color
	display.fill(randcol)
	if (count == 25):
		randcol = random.randint(0,255), random.randint(0,255), random.randint(0,255)
		count = 0

	count += 1
	# Updating the screen and ball position
	display.blit(ball, ballrect)
	pygame.display.flip()