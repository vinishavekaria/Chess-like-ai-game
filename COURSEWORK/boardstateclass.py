class GameState():
    def __init__(self):
        #the board is a 7x9 2d list
        #the first character illustrates the colour of the piece, either 'r' or 'b'
        #the "" empty string represents an empty space
        self.board = [
            ["","rA","rG","rE","rG","rA",""],
            ["","","rG","rG","rG","",""],
            ["","","rG","rG","rG","",""],
            ["","","","","","",""],
            ["","throne","","throne","","throne",""],
            ["","","","","","",""],
            ["","","bG","bG","bG","",""],
            ["","","bG","bG","bG","",""],
            ["","bA","bG","bE","bG","bA",""]]
        self.blueToMove = True
        self.moveLog = []

import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 7, 9
SQUARE_SIE = WIDTH//COLS

RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
        
            
            
        
