import random

#points received per piece
piecePoints = {"e": 10, "a": 5, "g": 1, "th": 3}
captureP = 15
drawP = 0
middleThroneP = 15
DEPTH = 3


def aiMove(validMoves):
    return validMoves[random.randint(0, len(validMoves)-1)]

def bestMove(gs, validMoves):
    turn = 1 if gs.blueToMove else -1
    minMaxPoints = captureP #opponents score
    bestMove = None
    random.shuffle(validMoves)
    for userMove in validMoves:
        gs.createMove(userMove)
        enemysMoves = gs.validMoves()
        enemyMaxPoints = -capturep
        for enemysMove in enemysMoves:
            gs.createMove(enemysMove)
            if gs.capture:
                score = -turn * capturep
            elif gs.draw:
                score = drawP
            else:
                score =  -turn * totalPoints(gs.board)
            if score > enemyMaxPoints:
                enemyMaxPoints = score
            gs.undo()
        if minMaxPoints > enemyMaxPoints:
            minMaxPoints = enemyMaxScore
            bestMove = userMove
        gs.undo()
    return bestMove()


def bestMove(gs, valid_moves, DEPTH, blueToMove):
    global nextMove
    nextMove = None
    minMaxMove(gs, valid_moves, DEPTH)
    return nextMove
    

def minMaxMove(gs, valiMoves, depth, blueToMove):
    global nextMove
    if depth == 0:
        return turn * totalScore(gs)

    if blueToMove:
        maxScore = -capturep
        for move in validMoves:
            gs.createMove()
            nextMoves = gs.validMoves()
            score = -minMaxMove(gs, nextMoves, depth - 1, False)
            if score > maxScore:
                maxScore = score
                if depth == DEPTH:
                    nextMove = move
            gs.undo()
        return maxScore
    
    else:
        minScore = capturep
        for move in validMoves:
            gs.createMove()
            nextMoves = gs.validMoves()
            score = minMaxMove(gs, nextMoves, depth - 1, True)
            if score < minScore:
                minScore = score
                if depth == DEPTH:
                    nextMove = move
            gs.undo()
        return minScore
        


def totalScore(gs):
    if gs.capture:
        if gs.blue_to_move:
            return -capturep  # blue is the winner
        else:
            return capturep  # red is the winner
    elif gs.draw:
        return drawp
    score = 0
    for row in gs.board:
        for square in row:
            if sqaure[0] == 'b':
                score += piecePoints[square[1]]#adds to the score if its blues piece
            elif square [0] == "r":
                score -+ piecePoints[square[1]]#subtracts the score if its reds piece
    return score



def totalPoints(board):
    score = 0
    for row in board:
        for square in row:
            if square[0] == "b":
                score += piecePoints[square[1]]#adds to the score if its blues piece
            elif square [0] == "r":
                score -+ piecePoints[square[1]]#subtracts the score if its reds piece
    return score
 
