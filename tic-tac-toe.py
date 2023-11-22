def proof(var, git):
    #noch nicht fertig
    if git.get(1) == var and git.get(2) == var and git.get(3) == var:
        return True
    elif git.get(4) == var and git.get(5) == var and git.get(6) == var:
        return True
    elif git.get(7) == var and git.get(8) == var and git.get(9) == var:
        return True
    elif git.get(1) == var and git.get(4) == var and git.get(7) == var:
        return True
    elif git.get(2) == var and git.get(5) == var and git.get(8) == var:
        return True
    elif git.get(3) == var and git.get(6) == var and git.get(9) == var:
        return True
    elif git.get(1) == var and git.get(5) == var and git.get(9) == var:
        return True
    elif git.get(3) == var and git.get(5) == var and git.get(7) == var:
        return True
    else:
        empty = 0
        for value in git.values():
            if value == " ":
                empty+=1
            else:
                pass
        if empty == 0:
            return False
        else:
            return None

def almostWin(var, git):
    if git[1]==var and git[2]==var and git[3]==" ":
        return 3
    elif git[1]==var and git[3]==var and git[2]==" ":
        return 2
    elif git[2]==var and git[3]==var and git[1]==" ":
        return 1
    elif git[4]==var and git[5]==var and git[6]==" ":
        return 6
    elif git[4]==var and git[6]==var and git[5]==" ":
        return 5
    elif git[5]==var and git[6]==var and git[4]==" ":
        return 4
    elif git[7]==var and git[8]==var and git[9]==" ":
        return 9
    elif git[7]==var and git[9]==var and git[8]==" ":
        return 8
    elif git[1]==var and git[4]==var and git[7]==" ":
        return 7
    elif git[1]==var and git[7]==var and git[4]==" ":
        return 4
    elif git[4]==var and git[7]==var and git[1]==" ":
        return 1
    elif git[2]==var and git[5]==var and git[8]==" ":
        return 8
    elif git[2]==var and git[8]==var and git[5]==" ":
        return 5
    elif git[5]==var and git[8]==var and git[2]==" ":
        return 2
    elif git[3]==var and git[6]==var and git[9]==" ":
        return 9
    elif git[3]==var and git[9]==var and git[6]==" ":
        return 6
    elif git[6]==var and git[9]==var and git[3]==" ":
        return 3
    elif git[1]==var and git[5]==var and git[9]==" ":
        return 9
    elif git[1]==var and git[9]==var and git[5]==" ":
        return 5
    elif git[5]==var and git[9]==var and git[1]==" ":
        return 1
    elif git[3]==var and git[5]==var and git[7]==" ":
        return 7
    elif git[3]==var and git[7]==var and git[5]==" ":
        return 5
    elif git[5]==var and git[7]==var and git[3]==" ":
        return 3
    else:
        return False

def register(git):
    print(f'   {git.get(1)}   |   {git.get(2)}   |   {git.get(3)}   ')
    print("-----------------------")
    print(f'   {git.get(4)}   |   {git.get(5)}   |   {git.get(6)}   ')
    print("-----------------------")
    print(f'   {git.get(7)}   |   {git.get(8)}   |   {git.get(9)}   ')

def deleteGit(git):
    for i in git:
        git[i] = " "
    return git

def kihard(git, symbol, notSymbol):
    import random
    setSymbol=False
    while setSymbol==False:
        if symbol=="X" and git[3]==" ":
            input("Die KI hat ein Feld gefunden...")
            git[3]=symbol
            setSymbol=True
        elif symbol=="O" and git[1]=="X" and git[5]==" ":
            input("Die KI hat ein Feld gefunden...")
            git[5]=symbol
            setSymbol=True
        elif symbol=="O" and git[3]=="X" and git[5]==" ":
            input("Die KI hat ein Feld gefunden...")
            git[5]=symbol
            setSymbol=True
        elif symbol=="O" and git[7]=="X" and git[5]==" ":
            input("Die KI hat ein Feld gefunden...")
            git[5]=symbol
            setSymbol=True
        elif symbol=="O" and git[9]=="X" and git[5]==" ":
            input("Die KI hat ein Feld gefunden...")
            git[5]=symbol
            setSymbol=True
        elif almostWin(symbol,git)!=False:
            input("Die KI hat ein Feld gefunden...")
            git[almostWin(symbol, git)]=symbol
            setSymbol=True
        elif almostWin(notSymbol,git)!=False:
            input("Die KI hat ein Feld gefunden...")
            git[almostWin(notSymbol, git)]=symbol
            setSymbol=True
        elif symbol=="X" and git[2]=="O" and git[9]==" ":
            input("Die KI hat ein Feld gefunden...")
            git[9]=symbol
            setSymbol=True
        elif symbol=="X" and git[6]=="O" and git[1]==" ":
            input("Die KI hat ein Feld gefunden...")
            git[1]=symbol
            setSymbol=True
        elif symbol=="X" and git[8]=="O" and git[9]==" ":
            input("Die KI hat ein Feld gefunden...")
            git[9]=symbol
            setSymbol=True
        elif symbol=="X" and git[4]=="O" and git[1]==" ":
            input("Die KI hat ein Feld gefunden...")
            git[1]=symbol
            setSymbol=True
        elif symbol=="X" and git[7]==" ":
            input("Die KI hat ein Feld gefunden...")
            git[7]=symbol
            setSymbol=True
        elif symbol=="X" and git[1]==" ":
            input("Die KI hat ein Feld gefunden...")
            git[1]=symbol
            setSymbol=True
        elif symbol=="X" and git[9]==" ":
            input("Die KI hat ein Feld gefunden...")
            git[9]=symbol
            setSymbol=True
        else:
            kiSet = random.randint(1,9)
            if git[kiSet] == " ":
                input("Die KI hat ein Feld gefunden...")
                git[kiSet] = symbol
                setSymbol=True
            else:
                pass
    return git

def kimedium(git, symbol, notSymbol):
    import random
    setSymbol=False
    while setSymbol==False:
        if symbol=="X" and git[1]==" ":
            input("Die KI hat ein Feld gefunden...")
            git[1]=symbol
            setSymbol=True
        elif almostWin(notSymbol,git)!=False:
            input("Die KI hat ein Feld gefunden...")
            git[almostWin(notSymbol, git)]=symbol
            setSymbol=True
        else:
            kiSet = random.randint(1,9)
            if git[kiSet] == " ":
                input("Die KI hat ein Feld gefunden...")
                git[kiSet] = symbol
                setSymbol=True
            else:
                pass
    return git

def kilight(git, symbol):
    import random
    setSymbol=False
    while setSymbol==False:
        kiSet = random.randint(1,9)
        if git[kiSet] == " ":
            input("Die KI hat ein Feld gefunden...")
            git[kiSet] = symbol
            setSymbol=True
        else:
            pass
    return git

def playerO(nm, git):
    setSymbol=False
    while setSymbol==False:
        try:
            scnd = int(input(f"{nm}, in welches Feld setzt du Dein O (Zahl): "))
            if scnd in git.keys():
                if git[scnd] == " ":
                    git[scnd]="O"
                    setSymbol=True
                elif git[scnd] == "O":
                    print(f"{nm}, sieh genau hin! An Stelle {scnd} hast Du schon gesetzt!")
                    pass
                elif git[scnd] =="X":
                    print(f"{nm}, spiele fair! An Stelle {scnd} hat Dein Gegner schon gesetzt!")
                    pass
                else:
                    print("Fehler")
                    pass
            else:
                print(f"{nm}, die Zahl {scnd} ist nicht auf dem Tik-Tak-Toe-Brett zu sehen!")
                pass
        except:
            print("Fehler: Deine Eingabe ist ungültig.")
    return git

def playerX(nm, git):
    setSymbol=False
    while setSymbol==False:
        try:
            frst = int(input(f"{nm}, in welches Feld setzt du Dein X (Zahl): "))
            if frst in git.keys():
                if git[frst] == " ":
                    git[frst]="X"
                    setSymbol=True
                elif git[frst] == "X":
                    print(f"{nm}, sieh genau hin! An Stelle {frst} hast Du schon gesetzt!")
                    pass
                elif git[frst] =="O":
                    print(f"{nm}, spiele fair! An Stelle {frst} hat Dein Gegner schon gesetzt!")
                    pass
                else:
                    print("Fehlermeldung.")
                    pass
            else:
                print(f"{nm}, die Zahl {frst} ist nicht auf dem Tik-Tak-Toe-Brett zu sehen!")
                pass
        except:
            print("Fehler: Deine Eingabe ist ungültig.")
    return git

def playAgain():
    print("\n1: Noch einmal, 2: Beenden")
    setAgaian=False
    while setAgaian==False:
        try:
            again=int(input(""))
            if again==1:
                setAgaian=True
                main()
            elif again==2:
                setAgaian=True
            else:
                print(f"Die Zahl {again} ist keine Eingabemöglichkeiten.")
                pass
        except:
            print("Fehler: Gib bitte eine Zahl (1 oder 2) ein!")
    return True
            

def main():
    git={1:"1", 2:"2", 3:"3",
    4:"4", 5:"5", 6:"6",
    7:"7", 8:"8", 9:"9"}
    
    try:
        modus = int(input("\n1: Singleplayer, 2: Multiplayer\n"))

        # Einzelplayer gegen KI
        if modus == 1:
            nmOne = input("Dein Name: ")            
            nmTwo = input("\nAls KI spiele ich gegen Dich! Wie schwer soll ich sein? \n('+' bis '+++'): ")

            # KI light
            if nmTwo == "+":
                register(git)
                git = deleteGit(git)

                select=False
                while select==False:
                    selectSymbol = input(f"{nmOne}, wähle zwischen X oder O!\n")

                    if selectSymbol == "X":
                        select=True
                        kiSymbol = "O"

                        close=False
                        while close==False:
                            git = playerX(nmOne, git)
                            register(git)
                            if proof(selectSymbol, git) == True:
                                print(f"{nmOne}, Du hast tatsächlich gewinnen können, Herzlichen Glückwunsch!")
                                close = playAgain()
                            elif proof(selectSymbol, git) == False:
                                print(f"Unentschieden! {nmOne}, Du kannst der KI virtuell die Hände schütteln.")
                                close = playAgain()
                            else:
                                pass
                            
                            if close==False:
                                git = kilight(git, kiSymbol)
                                register(git)

                                if proof(kiSymbol, git) == True:
                                    print(f"Die KI hat Dich abgezogen, versuch es doch noch einmal!")
                                    close = playAgain()
                                else:
                                    pass
                            else:
                                pass

                    elif selectSymbol == "O":
                        select=True
                        kiSymbol = "X"

                        close=False
                        while close==False:
                            git = kilight(git, kiSymbol)
                            register(git)
                            if proof(kiSymbol, git) == True:
                                print(f"Die KI hat Dich abgezogen, versuch es doch noch einmal!")
                                close = playAgain()
                            elif proof(kiSymbol, git) == False:
                                print(f"Unentschieden! {nmOne}, Du kannst der KI virtuell die Hände schütteln.")
                                close = playAgain()
                            else:
                                pass

                            if close==False:
                                git = playerO(nmOne, git)
                                register(git)
                                if proof(selectSymbol, git) == True:
                                    print(f"{nmOne}, Du hast tatsächlich gewinnen können, Herzlichen Glückwunsch!")
                                    close = playAgain()
                                else:
                                    pass
                            else:
                                pass
                    else:
                        print("Fehler: Bitte wähle zwischen den Antwortmöglichkeiten! Achte auf Großschreibung beim X und O!")

            # KI medium
            elif nmTwo == "++":
                register(git)
                git = deleteGit(git)

                select=False
                while select==False:
                    selectSymbol = input(f"{nmOne}, wähle zwischen X oder O!\n")

                    if selectSymbol == "X":
                        select=True
                        kiSymbol = "O"

                        close=False
                        while close==False:
                            git = playerX(nmOne, git)
                            register(git)
                            if proof(selectSymbol, git) == True:
                                print(f"{nmOne}, Du hast tatsächlich gewinnen können, Herzlichen Glückwunsch!")
                                close = playAgain()
                            elif proof(selectSymbol, git) == False:
                                print(f"Unentschieden! {nmOne}, Du kannst der KI virtuell die Hände schütteln.")
                                close = playAgain()
                            else:
                                pass
                            
                            if close==False:
                                git = kimedium(git, kiSymbol, selectSymbol)
                                register(git)

                                if proof(kiSymbol, git) == True:
                                    print(f"Die KI hat Dich abgezogen, versuch es doch noch einmal!")
                                    close = playAgain()
                                else:
                                    pass
                            else:
                                pass

                    elif selectSymbol == "O":
                        select=True
                        kiSymbol = "X"

                        close=False
                        while close==False:
                            git = kimedium(git, kiSymbol, selectSymbol)
                            register(git)
                            if proof(kiSymbol, git) == True:
                                print(f"Die KI hat Dich abgezogen, versuch es doch noch einmal!")
                                close = playAgain()
                            elif proof(kiSymbol, git) == False:
                                print(f"Unentschieden! {nmOne}, Du kannst der KI virtuell die Hände schütteln.")
                                close = playAgain()
                            else:
                                pass

                            if close==False:
                                git = playerO(nmOne, git)
                                register(git)
                                if proof(selectSymbol, git) == True:
                                    print(f"{nmOne}, Du hast tatsächlich gewinnen können, Herzlichen Glückwunsch!")
                                    close = playAgain()
                                else:
                                    pass
                            else:
                                pass
                    else:
                        print("Fehler: Bitte wähle zwischen den Antwortmöglichkeiten! Achte auf Großschreibung beim X und O!")

            # KI hard
            elif nmTwo == "+++":
                register(git)
                git = deleteGit(git)

                select=False
                while select==False:
                    selectSymbol = input(f"{nmOne}, wähle zwischen X oder O!\n")

                    if selectSymbol == "X":
                        select=True
                        kiSymbol = "O"

                        close=False
                        while close==False:
                            git = playerX(nmOne, git)
                            register(git)
                            if proof(selectSymbol, git) == True:
                                print(f"{nmOne}, Du hast tatsächlich gewinnen können, Herzlichen Glückwunsch!")
                                close = playAgain()
                            elif proof(selectSymbol, git) == False:
                                print(f"Unentschieden! {nmOne}, Du kannst der KI virtuell die Hände schütteln.")
                                close = playAgain()
                            else:
                                pass
                            
                            if close==False:
                                git = kihard(git, kiSymbol, selectSymbol)
                                register(git)

                                if proof(kiSymbol, git) == True:
                                    print(f"Die KI hat Dich abgezogen, versuch es doch noch einmal!")
                                    close = playAgain()
                                else:
                                    pass
                            else:
                                pass

                    elif selectSymbol == "O":
                        select=True
                        kiSymbol = "X"

                        close=False
                        while close==False:
                            git = kihard(git, kiSymbol, selectSymbol)
                            register(git)
                            if proof(kiSymbol, git) == True:
                                print(f"Die KI hat Dich abgezogen, versuch es doch noch einmal!")
                                close = playAgain()
                            elif proof(kiSymbol, git) == False:
                                print(f"Unentschieden! {nmOne}, Du kannst der KI virtuell die Hände schütteln.")
                                close = playAgain()
                            else:
                                pass

                            if close==False:
                                git = playerO(nmOne, git)
                                register(git)
                                if proof(selectSymbol, git) == True:
                                    print(f"{nmOne}, Du hast tatsächlich gewinnen können, Herzlichen Glückwunsch!")
                                    close = playAgain()
                                else:
                                    pass
                            else:
                                pass
                    else:
                        print("Fehler: Bitte wähle zwischen den Antwortmöglichkeiten! Achte auf Großschreibung beim X und O!")
            
            # kein Schwierigkeitslevel ausgewählt
            else:
                print("Gib bitte ein Schwierigkeitslevel durch das '+'-Symbol ein!")
                main()
        
        # Multiplayer offline
        elif modus == 2:
            nmOne = input("\nPlayer 1: ")
            nmTwo = input("Player 2: ") 
            
            register(git)
            editGit = deleteGit(git)

            close=False
            while close == False:
                editGit = playerX(nmOne, editGit)
                register(editGit)
                
                if proof("X", editGit) == True:
                    print(f"{nmOne} hat gewonnen, Herzlichen Glückwunsch.")
                    close = playAgain()
                elif proof("X", editGit) == False:
                    print(f"Unentschieden! {nmOne} und {nmTwo}, ihr könnt euch die Hände schütteln!")
                    close = playAgain()
                else:
                    pass

                if close == False:
                    editGit = playerO(nmTwo, editGit)
                    register(editGit)

                    if proof("O", editGit) == True:
                        print(f"{nmTwo} hat gewonnen, Herzlichen Glückwunsch.")
                        close = playAgain()
                    else:
                        pass
                else:
                    pass
        
        # Zahlenangaben not 1 or 2
        else:
            print("Wähle eine der vorgegebenen Möglichkeiten aus.")
            main()
    
    except:
        print("Gib bitte eine Zahl ein!")
    count=+1
    input(f"Bis zum nächsten Mal! {count} Please press Enter...")

if __name__=="__main__":
    print("---------- Herzlich Willkommen zum Tik-Tak-Toe-Spiel! ---------- \nDies ist Tik-Tak-Toe nach originalen Regeln.\nWähle als Erstes deinen Modi!")
    main()