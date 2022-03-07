class Col:
    red = "\033[31m"
    ylw = "\033[93m"
    blu = "\033[36m"
    org = "\033[33m"
    grn = "\033[92m"
    ppl = "\033[35m"
    pnk = "\033[96m"
    wht = "\033[97m"

    clist = [red, ylw, blu, org, grn, ppl, pnk, wht]

def colorCodes():
    """
    Choix des indices pour les couleurs basés sur Col.clist
    """
    strCodes = """
    ╔═══╤═══╦═══╤═══╗
    ║ 0 │{0}║ 1 │{1}║
    ╟───┼───╫───┼───╢
    ║ 2 │{2}║ 3 │{3}║
    ╟───┼───╫───┼───╢
    ║ 4 │{4}║ 5 │{5}║
    ╟───┼───╫───┼───╢
    ║ 6 │{6}║ 7 │{7}║
    ╚═══╧═══╩═══╧═══╝
    """.format(Col.red+" █ "+Col.wht, Col.ylw+" █ "+Col.wht, Col.blu+" █ "+Col.wht, Col.org+" █ "+Col.wht, Col.grn+" █ "+Col.wht, Col.ppl+" █ "+Col.wht, Col.pnk+" █ "+Col.wht, Col.wht+" █ "+Col.wht)
    return print(strCodes)

def helper():
    return print("""
    COMMANDE\t\tDESCRIPTION\t\t\t\tALIAS
    board\t\taffiche le tableau de jeu\t\tb
    colors\t\taffiche les codes couleurs\t\tc
    rules\t\taffiche les règles du jeu\t\tr
    quit\t\tferme le jeu sans sauvegarde\t\tstop, q, s, exit
    """)

def gameRules():
    f = open("mastermind_rules.txt", 'r')
    rules = f.readlines()
    f.close()

    for line in rules:
        if line.strip('\n') == "-BR-":
            print(Col.ylw+"q pour quitter, entrée pour la suite des règles"+Col.wht)
            choice = input(Col.org+"règles>"+Col.wht)
            if choice.lower() == "q":
                return None
        else:
            print(line.strip('\n'))
    return None

def gameCredits():
    print("""
    * Truong Tommy
    * Merci Wilson Crochet!
    """)
    return None

def showBoard(board):
    """
    - Définir board         # Done (cf mastermind_structs.txt)
    - Coder cette fonction  # TODO
    Attention : le format de board est primordial pour le bon fonctionnement de
    cette fonction!
    """
    print("     C O D E     C O M P")
    for i in range(len(board)):
        strRow = str(i+1) + " "*(2-len(str(i+1)))
        print("{0} : {1}".format(strRow, showLine(board[i])))
    return None

def showLine(line):
    """
    - Définir line          # Done (cf mastermind_structs.txt)
    - Coder cette fonction  # TODO
    Attention : le format de line est primordial pour le bon fonctionnement de
    cette fonction!
    """
    lineStr = ""
    for elt in line:
        for chr in elt:
            x = int(chr)
            if x > 7:
                lineStr += Col.wht+"░ "
            else:
                lineStr += Col.clist[x]+"█ "+Col.wht
        lineStr += " "*4
    return lineStr

def userInput(board):
    print("[MASTERMIND] Veuillez entrer un code à 4 chiffres ou une commande.")
    print("[MASTERMIND] helpme permet d'afficher les commandes")
    code = input(">>> ")
    if code.lower() in ["colors", "c"]:
        colorCodes()
        return userInput(board)
    elif code.lower() in ["board", "b"]:
        showBoard(board)
        return userInput(board)
    elif code.lower() in ["helpme", "help"]:
        helper()
        return userInput(board)
    elif code.lower() in ["rules", "r"]:
        gameRules()
        return userInput(board)
    elif code.lower() in ["quit", "exit", "q", "s"]:
        return -1
    else:
        try:
            int(code)
        except ValueError:
            print(Col.red+"Entrée invalide! (TYPE != ENTIER)"+Col.wht)
            return userInput(board)

        if len(code) != 4:
            print(Col.red+"Entrée invalide! (NB_PIONS != 4)"+Col.wht)
            return userInput(board)

        else:
            if ("8" in code) or ("9" in code):
                print(Col.red+"Entrée invalide! (PION INCONNU)"+Col.wht)
                return userInput(board)
            return code

def gameMenuChoice():
    choice = input(">>> ")
    if choice.lower() == "j":
        return 1
    elif choice.lower() == "d":
        return 2
    elif choice.lower() == "r":
        gameRules()
        x = gameMenuChoice()
        return x
    elif choice.lower() == "q":
        return -1
    elif choice.lower() == "m":
        x = gameMenu()
        return x
    elif choice.lower() == "c":
        gameCredits()
        x = gameMenuChoice()
        return x
    else:
        print("[MASTERMIND] Entrée non reconnue.")
        x = gameMenuChoice()
        return x
    return "Ceci ne devrait jamais s'afficher."

def gameMenu():
    print("""
    ╔═════════════════════╦════╗
    ║ M A S T E R M I N D ║v1.2║
    ╠═════════════════════╬════╣
    ║ règles              ║ R  ║
    ║ jouer               ║ J  ║
    ║ menu                ║ M  ║
    ║ crédits             ║ C  ║
    ║ quitter             ║ Q  ║
    ╚═════════════════════╩════╝
    """)
    gameStatus = gameMenuChoice()
    return gameStatus
