import mastermind_io as io
import random as rd
import os

MAXTURNS = 10

def gameInit(debug):
    trueCode = ""
    board = []
    for i in range(4):
        x = rd.randint(0, 7)
        trueCode += str(x)
    if debug == 2:
        print("[MASTERMIND_DEBUG] Code à deviner : "+trueCode)

    for i in range(MAXTURNS):
        board.append(["", ""])
    return trueCode, board

def startUp():
    gameStatus = io.gameMenu()
    if gameStatus == -1:
        print("[MASTERMIND] Sortie...")
        return 0, 0
    elif gameStatus == 0:
        print("[MASTERMIND] "+Col.red+"ERREUR"+Col.wht)
        return 0, 0
    else:
        trueCode, board = gameInit(gameStatus)
        return trueCode, board

def occurrence(x, code):
    for i in range(len(code)):
        if x == code[i]:
            return i
    return -1

def compare(userCode, trueCode):
    comp = ""
    listComp = [False, False, False, False]
    listTrue = [False, False, False, False]

    # Cas 1 : le caractère i est il exactement bien placé?
    for i in range(len(userCode)):
        if userCode[i] == trueCode[i]:
            comp += "0"
            listComp[i] = True
            listTrue[i] = True

    # Cas 2 : le caractère i est il dans le code à deviner?
    for i in range(len(userCode)):
        for j in range(len(trueCode)):
            if (userCode[i] == trueCode[j] and listComp[j] == False and listTrue[i] == False):
                comp += "7"
                listComp[j] = True
                listTrue[i] = True

    comp += "9"*(4-len(comp))
    return comp

def turn(trueCode, iTurn, board):
    userAct = io.userInput(board)
    if userAct == -1:
        print("[MASTERMIND] Sortie...")
        return -1
    compCode = compare(userAct, trueCode)
    board[iTurn] = [userAct, compCode]
    return None

def gameCurrent(argTuple):
    trueCode = argTuple[0]
    board = argTuple[1]

    if (trueCode == 0 and board == 0):
        return None

    endState = False
    winState = False
    iTurn = 0
    while endState == False:
        if (iTurn > MAXTURNS-1 and winState == False):
            # à court d'essais + 10 essais faux
            print("[MASTERMIND] Vous avez perdu! Le code à deviner était {0}".format(trueCode))
            endState = True
            io.showBoard(board)
        elif winState:
            # on a gagné
            print("[MASTERMIND] Vous avez gagné en {0} coups!".format(iTurn))
            io.showBoard(board)
            endState = True
        else:
            x = turn(trueCode, iTurn, board)
            if x == -1:
                # fermeture anticipée
                endState = True
            if board[iTurn][0] == trueCode:
                # Si le bon code a été trouvé au tour i
                winState = True
            iTurn += 1
    return None

os.system("color") # Permet d'assurer l'affichage correct des couleurs via les codes d'échappement ANSI
gameCurrent(startUp()) # Cette ligne lance le jeu
