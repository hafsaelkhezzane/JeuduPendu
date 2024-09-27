import tkinter as tk

mot = ""
lettre = ""
invalides = ""
incomplet = ""

def init_matrice():
    global mat
    mat = [
        ["A", "B", "C","D", "E", "F", "G",],
        ["H", "I", "J","K", "L", "M", "N",],
        ["O", "P", "Q","R", "S", "T", "U",],
        ["V", "W", "X","Y", "Z", "'", "-",]
    ] 

def drawMat():
    print("")
    for ligne in mat:
        print(ligne)

def cls():
    print("\n"*100)

def choix(): 
    global lettre
    lettre = input("veuillez entrer une lettre:").upper()
    for i in range(0,3): #parcourri la matrice
        for j in range(0,6):
            if lettre == mat[i][j]:
                mat[i][j]=" " #remplacer un lettre qu'on a choisit par " " 
    return lettre

def points_communs(): 
    global incomplet
    tmp = list(incomplet)
    x=""
    if mot.count(lettre) == 1:
        i = mot.find(lettre)
        tmp[i] = lettre
    else:
        for i, char in enumerate(list(mot)):
            if char == lettre:
                tmp[i] = lettre #remplace la lettre correspondant dans tmp
    incomplet = x.join(tmp) # pour rejoindre les caractére de tmp à une chaine de caractére et met à jour à la variable incomlet
    return incomplet

def saisir_mot():
    global mot
    mot = input("Entrez le mot à trouver : ").upper()
    init()

def init():
    global incomplet
    for i in range(len(mot)):
       incomplet += "_" 

def update_word_display(word):
    word_label.configure(text=word)

def update_lives_display(vie):
    lives_label.configure(text=f"Lives: {vie}")

def update_hangman_display(vie):
    if vie == 8:
        L =[ """
            +---+
                |
                |
                |
                |
            ========"""] 
        hangman_canvas.delete("all")
        hangman_canvas.create_text(100, 100, text=L, font=("Courier", 14)),
    elif vie == 7:
        L =[ """
            +---+
                |
                |
                |
                |
            ========"""] 
        hangman_canvas.delete("all")
        hangman_canvas.create_text(100, 100, text=L, font=("Courier", 14)),
    elif vie == 6:
        L=[ """
            +---+
            |   |
            O   |
                |
                |
            ========"""]
        hangman_canvas.delete("all")
        hangman_canvas.create_text(100, 100, text=L, font=("Courier", 14)),
    elif vie == 5:
        L=[  """
            +---+
            |   |
            O   |
            |   |
                |
            ========"""]
        hangman_canvas.delete("all")
        hangman_canvas.create_text(100, 100, text=L, font=("Courier", 14)),
    elif vie == 4:
        L=[  """
            +---+
            |   |
            O   |
           -|   |
                |
            ========"""]
        hangman_canvas.delete("all")
        hangman_canvas.create_text(100, 100, text=L, font=("Courier", 14)),
    elif vie == 3:
        L= [ """
            +---+
            |    |
            O    |
           -|-   |
                 |
            ========"""]
        hangman_canvas.delete("all")
        hangman_canvas.create_text(100, 100, text=L, font=("Courier", 14)),
    elif vie == 2:
        L=[  """
            +---+
            |    |
            O    |
            -|-  |
            /    |
            ========"""]
        hangman_canvas.delete("all")
        hangman_canvas.create_text(100, 100, text=L, font=("Courier", 14)),
    else:
        L=[ """
            +---+
            |    |
            O    |
            -|-  |
            | |  |
            ========"""]
        hangman_canvas.delete("all")
        hangman_canvas.create_text(100, 100, text=L, font=("Courier", 14))

# Create the main window
window = tk.Tk() #creation de l'interface
window.title("   ☠  WELCOME TO HANGMAN GAME ☠") #titre 


# Word display label
word_label = tk.Label(window, text="Word")
word_label.pack()

# Lives display label
lives_label = tk.Label(window, text="Lives")
lives_label.pack()

# Hangman display canvas
hangman_canvas = tk.Canvas(window, width=200, height=200)
hangman_canvas.pack()
def update_hangman_displayM():
    M=["""
        ____________________________________
        |                                   |
        |        1- START                   |
        |        2- EXIT                    |
        |                                   |
        |___________________________________|
        """]
    hangman_canvas.delete("all")
    hangman_canvas.create_text(100, 100, text=M, font=("Courier", 14))

    message=input_entry.get()
input_entry = tk.Entry(window)
input_entry.pack()
submit_button = tk.Button(window, text="Valider", command=update_hangman_displayM())
submit_button.pack()


def pendu():
    global invalides
    saisir_mot()
    tentatives = 8
    init_matrice()
    while tentatives > 0 and "_" in incomplet:
        print("\n")
        print("*******************************")
        print(incomplet)
        drawMat()
        choix()
        if lettre in mot:
            print(points_communs())
        else:
            print("\n")
            invalides += lettre + ", "
            print("lettres invalides : ", invalides)
            tentatives = tentatives - 1
            print("tentatives restantes : ", tentatives)
            update_hangman_display(tentatives)
    if tentatives == 0:
        print("Vous avez perdu !")
    else:
        print("Vous avez gagné !")


def main():
    print("   ☠  WELCOME TO HANGMAN GAME ☠")
    print("____________________________________")
    print("|                                   |")
    print("|        1- START                   |")
    print("|        2- EXIT                    |")
    print("|                                   |")
    print("|___________________________________|")
    x = int(input("ENTER YOUR CHOICE: "))

    if x == 1:
        pendu()
        window.mainloop()
    elif x == 2:
        print("PLAY AGAIN?")
        w = int(input("[YES:1/NO:0]: "))
        if w == 1:
            main()            
        else:
            exit(0)            
    else:
        exit(0)
main()

