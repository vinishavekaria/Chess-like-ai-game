import pygame, sys

# initialising pygame
pygame.init()

# variables
WIDTH = 555
HEIGHT = 700
LINE_WIDTH = 5
SQUARE_SIZE = 80
SPACE = 55
# golden ancient board colour
BG_COLOR = (255, 217, 102)
LINE_COLOR = (191, 133, 67)

# screen
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'SOVRANO' )
screen.fill( BG_COLOR )

# functions for a 9x7 board
def draw_lines():
	# horizontal lines (9)
	pygame.draw.line( screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH )
	pygame.draw.line( screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH )
	pygame.draw.line( screen, LINE_COLOR, (0, 3 * SQUARE_SIZE), (WIDTH, 3 * SQUARE_SIZE), LINE_WIDTH )
	pygame.draw.line( screen, LINE_COLOR, (0, 4 * SQUARE_SIZE), (WIDTH, 4 * SQUARE_SIZE), LINE_WIDTH )
	pygame.draw.line( screen, LINE_COLOR, (0, 5 * SQUARE_SIZE), (WIDTH, 5 * SQUARE_SIZE), LINE_WIDTH )
	pygame.draw.line( screen, LINE_COLOR, (0, 6 * SQUARE_SIZE), (WIDTH, 6 * SQUARE_SIZE), LINE_WIDTH )
	pygame.draw.line( screen, LINE_COLOR, (0, 7 * SQUARE_SIZE), (WIDTH, 7 * SQUARE_SIZE), LINE_WIDTH )
	pygame.draw.line( screen, LINE_COLOR, (0, 8 * SQUARE_SIZE), (WIDTH, 8 * SQUARE_SIZE), LINE_WIDTH )
	pygame.draw.line( screen, LINE_COLOR, (0, 9 * SQUARE_SIZE), (WIDTH, 9 * SQUARE_SIZE), LINE_WIDTH )

	# vertical lines (7)
	pygame.draw.line( screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH )
	pygame.draw.line( screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH )
	pygame.draw.line( screen, LINE_COLOR, (3 * SQUARE_SIZE, 0), (3 * SQUARE_SIZE, HEIGHT), LINE_WIDTH )
	pygame.draw.line( screen, LINE_COLOR, (4 * SQUARE_SIZE, 0), (4 * SQUARE_SIZE, HEIGHT), LINE_WIDTH )
	pygame.draw.line( screen, LINE_COLOR, (5 * SQUARE_SIZE, 0), (5 * SQUARE_SIZE, HEIGHT), LINE_WIDTH )
	pygame.draw.line( screen, LINE_COLOR, (6 * SQUARE_SIZE, 0), (6 * SQUARE_SIZE, HEIGHT), LINE_WIDTH )
	pygame.draw.line( screen, LINE_COLOR, (7 * SQUARE_SIZE, 0), (7 * SQUARE_SIZE, HEIGHT), LINE_WIDTH )

draw_lines()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	pygame.display.update()
pygame.quit()
