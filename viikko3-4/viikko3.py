import tkinter as tk
from tkinter import PhotoImage
import winsound
import threading
import random
import pygame

pygame.mixer.init()
winner_sound = pygame.mixer.Sound("winner.mp3")
hit_sound = pygame.mixer.Sound("splat.wav")
throw_sound = pygame.mixer.Sound("throw.mp3")

ernestinKirjasto = {
    "eX": 1720,
    "eY": random.randint(400, 500),
    "eScore": 0
}

kernestinKirjasto = {
    "kX": 0,
    "kY": random.randint(400, 500),
    "kScore": 0
}

def checkWinner():
    if kernestinKirjasto["kScore"] > ernestinKirjasto["eScore"] + 1:
        winner_label.config(text="Kernesti voittaa!", fg="red")
        winner_label.place(x=770, y=450)  
    elif ernestinKirjasto["eScore"] > kernestinKirjasto["kScore"] + 1:
        winner_label.config(text="Ernesti voittaa!", fg="red")
        winner_label.place(x=770, y=450)
    else:
        winner_label.config(text="") 
        winner_label.place_forget()



def inviteErnesti():
    ernestinKirjasto["eY"] = random.randint(300, 500)
    ernestiKuva.place(x=ernestinKirjasto["eX"], y=ernestinKirjasto["eY"])
    simultaneousThrow.config(state=tk.NORMAL)
    ernestiThrow.config(state=tk.NORMAL)

def get_target_coordinates(widget):
    x = widget.winfo_x() + widget.winfo_width() // 2
    y = widget.winfo_y() + widget.winfo_height() // 2
    return x, y

def kthrow():
    throw_sound.play()
    tomaattix = kernestinKirjasto["kX"]
    tomaattiy = kernestinKirjasto["kY"]
    tomaattiKernesti = tk.Label(root, image=tomaatti)

    splatleima.place_forget()

    def ktomaatti():
        nonlocal tomaattix, tomaattiy
        target_x, target_y = get_target_coordinates(maalileima)
        
        if tomaattix < target_x:
            tomaattix += 10
            tomaattiKernesti.place(x=tomaattix, y=tomaattiy)
            root.after(10, ktomaatti)
        else:
            tomaattiKernesti.place_forget()
            if random.randint(1, 3) > 1:
                print("Kernesti osui")
                splatleima.place(x=target_x, y=target_y)
                hit_sound.play()
                kernestinKirjasto["kScore"] += 1
            else:
                print("Kernesti ei osunut")
                winsound.Beep(300, 300)
            updateScore()

    def kWinningThrow():
        nonlocal tomaattix, tomaattiy
        target_x, target_y = get_target_coordinates(maalileima)
        
        if tomaattix < target_x:
            tomaattix += 10
            tomaattiKernesti.place(x=tomaattix, y=tomaattiy)
            root.after(10, kWinningThrow)
        else:
            tomaattiKernesti.place_forget()
            if random.randint(1, 3) > 1:
                print("Kernesti osui Ernestiin, Kernesti voitti!")
                splatleima.place(x=tomaattix, y=tomaattiy)
                voittoK()
                winner_sound.play()
                checkWinner()
            else:
                print("Kernesti ei osunut Ernestiin")
                kernestinKirjasto["kScore"] -= 1
                winsound.Beep(300, 300)
            updateScore()

    def tarkistus():
        if kernestinKirjasto["kScore"] - ernestinKirjasto["eScore"] <= 1:
            ktomaatti()
        else:
            kWinningThrow()

    tarkistus()

def ethrow():
    throw_sound.play()
    tomaattix = ernestinKirjasto["eX"]
    tomaattiy = ernestinKirjasto["eY"]
    tomaattiErnesti = tk.Label(root, image=tomaatti)

    splatleima.place_forget()

    def etomaatti():
        nonlocal tomaattix, tomaattiy
        target_x, target_y = get_target_coordinates(maalileima)
        
        if tomaattix > target_x:
            tomaattix -= 10
            tomaattiErnesti.place(x=tomaattix, y=tomaattiy)
            root.after(10, etomaatti)
        else:
            tomaattiErnesti.place_forget()
            if random.randint(1, 3) > 1:
                print("Ernesti osui maalitauluun!")
                splatleima.place(x=tomaattix, y=tomaattiy)
                hit_sound.play()
                ernestinKirjasto["eScore"] += 1
            else:
                print("Ernesti ei osunut")
                winsound.Beep(300, 300)
            updateScore()

    def eVoittoheitto():
        nonlocal tomaattix, tomaattiy
        target_x, target_y = get_target_coordinates(maalileima)
        
        if tomaattix > 0:
            tomaattix -= 10
            tomaattiErnesti.place(x=tomaattix, y=tomaattiy)
            root.after(10, eVoittoheitto)
        else:
            tomaattiErnesti.place_forget()
            if random.randint(1, 3) > 1:
                print("Ernesti osui Kernestiin, Ernesti voitti!")
                splatleima.place(x=tomaattix, y=tomaattiy)
                voittoE()
                winner_sound.play()
                checkWinner()
            else:
                print("Ernesti heitti ohi Kernestistä")
                ernestinKirjasto["eScore"] -= 1
                winsound.Beep(300, 300)
            updateScore()

    def tarkistus():
        if ernestinKirjasto["eScore"] - kernestinKirjasto["kScore"] <= 1:
            etomaatti()
        else:
            eVoittoheitto()

    tarkistus()

def saikeKHeitto():
    kahvaHeittoK = threading.Thread(target=kthrow)
    kahvaHeittoK.start()

def saikeEHeitto():
    kahvaHeittoE = threading.Thread(target=ethrow)
    kahvaHeittoE.start()

def updateScore():
    points.config(text=f'Kernesti: {kernestinKirjasto["kScore"]} - Ernesti: {ernestinKirjasto["eScore"]}')

def reset():
    ernestinKirjasto["eScore"] = 0
    kernestinKirjasto["kScore"] = 0
    updateScore()
    splatleima.place_forget()
    ernestiKuva.place_forget()
    winner_label.config(text="")
    kutsuErnesti.config(state=tk.NORMAL)
    kernestiThrow.config(state=tk.NORMAL)
    ernestiThrow.config(state=tk.DISABLED)
    simultaneousThrow.config(state=tk.DISABLED)

def voittoK():
    kutsuErnesti.config(state=tk.DISABLED)
    kernestiThrow.config(state=tk.DISABLED)
    ernestiThrow.config(state=tk.DISABLED)
    simultaneousThrow.config(state=tk.DISABLED)

def voittoE():
    kutsuErnesti.config(state=tk.DISABLED)
    kernestiThrow.config(state=tk.DISABLED)
    ernestiThrow.config(state=tk.DISABLED)
    simultaneousThrow.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Heittokisa")
root.geometry("1920x1080")


tomaatti = PhotoImage(file="tomaatti.png")
kernesti = PhotoImage(file="kerne.png")
ernesti = PhotoImage(file="erne.png")
splat = PhotoImage(file="splat.png")
maalitaulu = PhotoImage(file="maalitaulu.png")


maalileima = tk.Label(root, image=maalitaulu)
ernestiKuva = tk.Label(root, image=ernesti)
kernestiKuva = tk.Label(root, image=kernesti)
splatleima = tk.Label(root, image=splat)


maalileima.place(x=700, y=300)
kernestiKuva.place(x=kernestinKirjasto["kX"], y=kernestinKirjasto["kY"])


kutsuErnesti = tk.Button(root, text="Kutsu Ernesti", command=inviteErnesti)
kutsuErnesti.place(x=897, y=775)

kernestiThrow = tk.Button(root, text="Kernesti heittää tomaatin", command=saikeKHeitto)
kernestiThrow.place(x=kernestinKirjasto["kX"], y=kernestinKirjasto["kY"] + kernesti.height() + 10)

ernestiThrow = tk.Button(root, text="Ernesti heittää tomaatin", command=saikeEHeitto, state=tk.DISABLED)
ernestiThrow.place(x=ernestinKirjasto["eX"], y=ernestinKirjasto["eY"] + ernesti.height() + 10)

simultaneousThrow = tk.Button(root, text="Yhteisheitto", command=lambda: [kthrow(), ethrow()], state=tk.DISABLED)
simultaneousThrow.place(x=900, y=750)

resetButton = tk.Button(root, text="Reset", command=reset)
resetButton.place(x=915, y=275)

points = tk.Label(root, text=f'Kernesti: {kernestinKirjasto["kScore"]} - Ernesti: {ernestinKirjasto["eScore"]}')
points.place(x=877, y=250)

winner_label = tk.Label(root, text="", font=("Arial", 36), fg="red")
winner_label.place(x=770, y=450)



updateScore()
root.mainloop()