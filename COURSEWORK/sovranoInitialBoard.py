import pygame, sys
# imports the class for the layout of the pieces on the board
import piececlass
import moveAI

# initialising pygame
pygame.init()


# variables
WIDTH = 525
HEIGHT = 665
LINE_WIDTH = 5
SQUARE_SIZE = 75
SPACE = 55
MAX_FPS = 10
# gold/brown ancient background for the board
BG_COLOR = (255, 217, 102)
LINE_COLOR = (191, 133, 67)
IMAGES = {}

# screen
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'SOVRANO' )
screen.fill( BG_COLOR )

#this function loads all possible pieces needed in each square
def loadImages():
    pieces = ['be', 're', 'ba', 'ra', 'bg', 'rg', 'th', 'mth']
    for pieces in places:
        IMAGES[pieces] = p.transform.scale(p.image.load("images/" +piece +".png"), (SQUARE_SIZE, SQUARE_SIZE))
        
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

def main():
    p.init()
    screen = p.time.Clock()
    screen.fill( BG_COLOR )
    gs = piececlass.GameState()
    validMoves = gs.validMoves()
    createMove = False#flags the variable when a move is made
    loadImages()
    running = True
    sqSelected = ()
    playerClicks = []
    gameOver = False
    userOne = True #if the user is blue then will be true, if it is the computer then false
    userTwo = False
    while running:
        userTurn = (gs.blueToMove and userOne) or (not gs.blueToMOve and userTwo)
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                if not gameOver and userTurn:
                    location = p.mouse.get.pos()
                    col = location[0]//SQUARE_SIZE
                    row = location[0]//SQUARE_SIZE
                    if sqSeleted == (row,col):
                        sqSelected = ()
                        playerClicks = []
                    else:
                        sqSelected = (row,col)
                        playerClicks.append(sqSelected)
                    if len(playerClicks)== 2:
                        move= pieceClass.Move(playerClicks[0], playerClicks[1], gs.board)
                        print(move.getNotation())
                        if move in validMoves:
                            gs.createMove(move)
                            createMove = True
                        sqSelected = ()
                        playerClicks = []
                    else:
                        playerClicks = [sqSelected]
                        
            elif e.type == p.KEYDOWN:
                if e.key == p.K_u:#allows user to undo move if 'u' is pressed on the keyboard
                    gs.undo()
                    createMove = True
                if e.type == p.K_r:#resets and clears the board to beginning state
                    gs = piececlass.GameState()
                    validMoves = gs.validMoves()
                    sqSelected = ()
                    playerClicks = []
                    createMove = False

        if not userTurn and gameOver:
            ai = moveAI.bestMove(gs, validMoves)
            if ai is None:
                ai = moveAI.aiMove(validMoves)
            gs.createMove(ai)
            createMove = True
            

        if createMove:
            validMoves = gs.validMoves()
            createMove= False

        if gs.capture:
            gameOver = True
            if gs.BlueToMove:
                drawText(screen, "RED WINS")
            else:
                drawText(screen, "BLUE WINS")
        elif gs.draw:
                gameOver = True
                drawText(screen, "DRAW")

        draw_lines(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()
        drawGameState(screen, gs, validMoves, sqSelected)

def colourSquare(screen, gs, validMoves, sqSelected):
    if sqSelected != ():#checks if the square theyve chosen is not empty
        r, c = sqSelected # refernce to the row and column of the square the user has selected
        if gs.board[r][c][0] == ('b' if gs.blueToMove else 'r'):#makes sure the player clicks on their own piece
            s = p.Surface((SQUARE_SIZE, SQUARE_SIZE))
            s.set.alpha(110)#sets the transparent colour, (255 = opaque)
            s.fill(p.color('green'))
            screen.blit(s, (c*SQUARE_SIZE, R*SQUARE_SIZE))
            s.fill(p.color('pink'))
            for move in validMoves:
                if move.startRow == r and move.startCol ==c:
                    screen.blit(s, (move.endCol*SQUARE_SIZE, move.endRow*SQUARE_SIZE))
    


def drawGameState(screen, gs, validMoves, sqSelected):
        draw_lines(screen)
        colourSquare(screen, gs, validMoves, sqSelected)
        drawPieces(screen, gs.board)

# the function outputs the pieces loaded in the correct row and collumn using the iterated for loop
def drawPieces(screen, board):
    for r in range(SQUARE_SIZE):
        for c in range(SQUARE_SIZE):
            piece = board[r][c]
            if piece!= "":
                    screen.blit(IMAGES[piece], p.Rect(c*SQUARE_SIZE, r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def drawText(screen, text):
    font = p.font.SysFont("Lucida Sans", 48, True, False)
    fontColour = font.render(text, 0, p.color('White'))
    textPosition = p.Rect(0, 0, WIDTH, HEIGHT).move(WIDTH/2 - fontColour.get_width()/2 - fontColour.get_height()/2)
    screen.blit(fontColour, textPosition)

if __name__ == "__main__":
    main()
    
pygame.quit()
