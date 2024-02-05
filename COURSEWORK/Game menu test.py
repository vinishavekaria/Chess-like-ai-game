import pygame
import sys


# initializing the constructor
pygame.init()

# screen resolution
res = (720,720)

# opens up a window
screen = pygame.display.set_mode(res)

# black color
color = (0,0,0)

# peach color of the button
color_light = (0,112,192)

# blue colour when the button is pressed
color_dark = (244,177,131)

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

#created the main menu screen
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

# defining a font
smallfont = pygame.font.SysFont('Calibri (Body)',45)

# rendering a text written in
# this font
text = smallfont.render('QUIT' , True , color)

while True:
	
	for ev in pygame.event.get():
		
		if ev.type == pygame.QUIT:
			pygame.quit()
			
		#checks if a mouse is clicked
		if ev.type == pygame.MOUSEBUTTONDOWN:
			
			#if the mouse is clicked on the
			# button the game is terminated
			if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
				pygame.quit()
				
	# fills the screen with a color
	screen.fill((255,217,102))
	
	# stores the (x,y) coordinates into
	# the variable as a tuple
	mouse = pygame.mouse.get_pos()
	
	# if mouse is hovered on a button it
	# changes to lighter shade
	if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
		pygame.draw.rect(screen,color_light,[width/2,height/2,140,40])
		
	else:
		pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])
	
	# superimposing the text onto our button
	screen.blit(text , (width/2+50,height/2))
	
	# updates the frames of the game
	pygame.display.update()






