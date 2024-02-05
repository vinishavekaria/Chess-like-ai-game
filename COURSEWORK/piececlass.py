class GameState():
    def __init__(self):
        #the board is a 7x9 2d list
        #the first character illustrates the colour of the piece, either 'r' or 'b'
        #the "" empty string represents an empty space
        self.board = [
            ["","ra","rg","re","rg","ra",""],
            ["","","rg","rg","rg","",""],
            ["","","rg","rg","rg","",""],
            ["","","","","","",""],
            ["","th","","mth","","th",""],
            ["","","","","","",""],
            ["","","bg","bg","bg","",""],
            ["","","bg","bg","bg","",""],
            ["","ba","bg","be","bg","ba",""]]
        
        self.move = {"g": self.getGuardMoves, "e": self.getEmperorMoves, "a": self.getArcherMoves}
        self.blueToMove = True #the blue pieces have the first move
        self.moveLog = []
        self.blueEmperorPosition = (8, 3)
        self.redEmperorPosition = (0, 3)
        self.capture = False 
        self.draw = False


def createMove(self, move):
    self.board[move.startRow][move.startCol] = ""
    self.board[move.endRow][move.endCol] = move.piecesMoved
    #logs the move to undo it later on
    self.moveLog.append(move)
    #swaps the current players turn to the next oponent
    self.blueToMove = not self.blueToMove
    if move.piece == 'be':
        self.blueEmperorPosition = (move.endRow, move.endCol)
    elif move.piece == 're':
        self.redEmperorPosition = (move.endRow, move.endCol)

def undo(self):
    if len(self.moveLog) !=0:#ensures that there is a move to undo
        move = self.moveLog.pop()#returns the element and removes the last element of the list
        self.board[move.startRow][move.startCol] = move.pieceMoved
        self.board[move.endRow][move.endCol] = move.pieceCaptured
        self.blueToMove = not self.blueToMove #switches turns
        if move.piece == 'be':
            self.blueEmperorPosition = (move.endRow, move.endCol)
        elif move.piece == 're':
            self.redEmperorPosition = (move.endRow, move.endCol)

def validMoves(self):
    moves = self.allPossibleMoves()
    for i in range(len(moves)-1, -1):#iterate through the list backwards when removing a piece of a board
        self.createMove(moves[i])
        self.blueToMove = not self.blueToMove
        if self.check():
            moves.remove(moves[i])#if a player attacks the emperor it will be an illegal move
        self.blueToMove = not self.blueToMove
        self.undo()
    if len(moves) ==0: #if it's capture or draw
        if self.check():
            self.capture = True
        else:
            self.draw = True
    else:
        self.capture = False
        self.draw = False

    return moves
    

def check(self): #checks if theres a capture or draw
    if self.blueToMOve:
        return self.squareAttack(self.blueEmperorPosition[0], self.blueEmperorPosition[1])
    else:
        return self.squareAttack(self.redEmperorPosition[0], red.blueEmperorPosition[1])

def squareAttack(self, r, c):# checks if the opponent is able to attack a square legally
    self.blueToMove = not self.blueToMove#switch turns
    enemyMoves = self.allPossibleMoves()
    self.blueToMove = not self.blueToMove
    for move in enemyMoves:
        if move.endRow == r and move.endCol == c:
            return True
    return False


def allPossibleMoves(self):
    moves = []
    for r in range(len(self.board)):
        for c in range(len(self.board[r])):
            turn - self.board[r][c][0]
            if (turn == 'b' and self.blueToMove) or (turn == 'r' and not self.blueToMove):
                piece = self.board[r][c][1]
                self.move[piece](r, c, moves)
    return moves

def getGuardMoves(r, c, moves):
    if self.blueToMove: #blues guards turn
        if self.board[r-1][c] == "":# allows the guard to move one space up if theres an empty position
            moves.append(Move((r, c), (r-1, c), self.board))
        elif self.board[r][c-1] == "":# allows the guard to move one space to the left if theres an empty position
            moves.append(Move((r, c), (r, c-1), self.board))
        elif self.board[r][c+1] == "":# allows the guard to move one space to the right if theres an empty position
            moves.append(Move((r, c), (r, c+1), self.board))
        if c-1 >=0:#capturing a piece from the left
            if self.board[r-1][c-1][0] == 'r':
                moves.append(Move((r,c), (r-1, c-1), self.board))
        if c+1 >= 6:#capturing a piece from the right
            if self.board[r-1][c+1][0] == 'r':
                moves.append(Move((r,c), (r-1, c+1), self.board))

def getArcherMoves(r, c, moves):
    archerMoves = ((1, 0), (0, 1), (-1, 0), (0, -1), (2, 2), (2, -2), (-2, 2), (-2, -2))
    currentColour = "b" if self.blueToMOve else "r"
    for m in archerMoves:
        endRow = r+ m[0]
        endCol = c+ m[1]
        if 0<= endRow < 9 and 0<= endCol < 7:
            endPiece = self.board[endRow][endCol]
            if endPiece[0] != currentColour:
                moves.append(Move((r,c), endRow, endCol, self.board))

def getEmperorMoves(r, c, moves):
    EmperorMoves = ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))
    currentColour = "b" if self.blueToMOve else "r"
    for m in archerMoves:
        endRow = r+ m[0]
        endCol = c+ m[1]
        if 0<= endRow < 9 and 0<= endCol < 7:
            endPiece = self.board[endRow][endCol]
            if endPiece[0] != currentColour:
                moves.append(Move((r,c), endRow, endCol, self.board))
    

class Move():

    ranksToRows = {"1":8, "2":7, "3":6, "4":5, "5":4, "6":3, "7":2, "8":1, "9":0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6}
    colsToFiles = {v:k for k, v in filesToCols.items()}
    
    # stores info on a particular piece in one class
    def __init__(self, sSq, eSq, board):#tuples :sSq = start square, eSq = end square
        self.startRow = sSq[0]
        self.startCol = sSq[1]
        self.endRow = eSq[0]
        self.sendCol = eSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveID = self.startRow *1000 +self.startCol *100 + self.endCol
    

    def __eq__(self, other):#compares the object to another object
        if isinstance(other, Move):
            return self.moveID == other.moveID

    def getNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)


    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]
