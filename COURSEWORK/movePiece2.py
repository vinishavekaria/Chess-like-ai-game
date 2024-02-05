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

#this function loads all possible pieces needed in each square
def loadImages():
    pieces = ['be', 're', 'ba', 'ra', 'bg', 'rg', 'th', 'mth']
    for pieces in places:
        IMAGES[pieces] = p.transform.scale(p.image.load("images/" +piece +".png"), (SQUARE_SIZE, SQUARE_SIZE))

def main():
    p.init()
    screen = p.time.Clock()
    screen.fill( BG_COLOR )
    gs = piececlass.GameState()
    loadImages()
    running = True
    sqSelected = ()
    playerClicks = []
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                # gets the mouses coordinates in terms of (x,y)
                location = p.mouse.get.pos()
                col = location[0]//SQAURE_SIZE
                row = loaction[1]//SQUARE_SIZE
                # allows the user to double click
                if sqSelected == (row, col):
                    # helps the user to redo their select move
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)
                if len(playerClicks) == 2:
                    #allows the pice to move once the user has double clicked
                    move = pieceClass.Move(playerClicks[0], playerClicks[1], gs.board)
                
        draw_lines(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

# functions for a 9x7 board
def draw_lines(screen):
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

draw_lines(screen)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	pygame.display.update()

def drawGameState(screen, gs):
        draw_lines(screen)
        drawPieces(screen, gs.board)

# the function outputs the pieces loaded in the correct row and collumn using the iterated for loop
def drawPieces(screen, board):
    for r in range(SQUARE_SIZE):
        for c in range(SQUARE_SIZE):
            piece = board[r][c]
            if piece!= "":
                    screen.blit(IMAGES[piece], p.Rect(c*SQUARE_SIZE, r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

if __name__ == "__main__":
    main()
    
pygame.quit()

