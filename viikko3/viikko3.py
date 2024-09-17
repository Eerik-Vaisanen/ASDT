import tkinter as tk
from PIL import Image, ImageTk
import math
import random as rand
import pygame

pygame.mixer.init()
winner_sound = pygame.mixer.Sound("winner.mp3")

competition = {
    'Kerne': {'player': "Kerne", 'score': 0},
    'Erne': {'player': "Erne", 'score': 0}
}

root = tk.Tk()
root.title("Heittokisa")

root.geometry("1440x900")
root.resizable(False, False)

image1 = Image.open("kerne.png")
image2 = Image.open("erne.png")
image3 = Image.open("maalitaulu.png")
image4 = Image.open("tomaatti.png")
image5 = Image.open("splat.png")
image6 = Image.open("tomaatti1.png")
image7 = Image.open("splat1.png")

tk_image1 = ImageTk.PhotoImage(image1)
tk_image2 = ImageTk.PhotoImage(image2)
tk_image3 = ImageTk.PhotoImage(image3)
tk_image4 = ImageTk.PhotoImage(image4.resize((100, 100)))
tk_image5 = ImageTk.PhotoImage(image5.resize((50, 50)))
tk_image6 = ImageTk.PhotoImage(image6.resize((100, 100)))
tk_image7 = ImageTk.PhotoImage(image7.resize((50, 50)))

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

label1 = tk.Label(root, image=tk_image1)
label1.grid(row=0, column=0, sticky="e")

label3 = tk.Label(root, image=tk_image3)
label3.grid(row=0, column=1)

label2 = tk.Label(root, image=tk_image2)

moving_label = tk.Label(root, image=tk_image4)
moving_label.place(x=-100, y=-100)

moving_label_erne = tk.Label(root, image=tk_image6)
moving_label_erne.place(x=-100, y=-100)

splat_label = tk.Label(root, image=tk_image5)
splat_label.place(x=-200, y=-200)

splat_label_erne = tk.Label(root, image=tk_image7)
splat_label_erne.place(x=-200, y=-200)

score_label = tk.Label(root, text="Kerne: 0  Erne: 0")
score_label.grid(row=3, column=1)

def update_scores():
    score_label.config(text=f"Kerne: {competition['Kerne']['score']}  Erne: {competition['Erne']['score']}")
    if competition['Kerne']['score'] >= competition['Erne']['score'] + 2:
        button_special_kerne.config(state=tk.NORMAL)
    else:
        button_special_kerne.config(state=tk.DISABLED)

    if competition['Erne']['score'] >= competition['Kerne']['score'] + 2:
        button_special_erne.config(state=tk.NORMAL)
    else:
        button_special_erne.config(state=tk.DISABLED)

def reset_scores():
    competition['Kerne']['score'] = 0
    competition['Erne']['score'] = 0
    update_scores()


def check_victory():
    if abs(competition['Kerne']['score'] - competition['Erne']['score']) >= 2:
        winner_sound.play()
        pygame.time.wait(2000)
        
        button.grid_forget()
        button_move_arc.grid_forget()
        button_move_arc2.grid_forget()
        button_yhteissheitto.grid_forget()
        button_special_erne.grid_forget()
        button_special_kerne.grid_forget()

        root.destroy()
        
        return True
    return False

def show_image2():
    label2.grid(row=0, column=2, sticky="w")
    button_move_arc2.grid(row=1, column=2)
    button_yhteissheitto.grid(row=2, column=1)

def move_arc_kerne():
    start_x = 350
    start_y = 200

    target_center_x = 720
    target_center_y = 200

    variance_x = 50
    variance_y = 50

    end_x = target_center_x - (tk_image5.width() // 2) + rand.randint(-variance_x, variance_x)
    end_y = target_center_y - (tk_image5.height() // 2) + rand.randint(-variance_y, variance_y)

    steps = 100
    delay = 20

    def animate(step):
        if step <= steps:
            t = step / steps
            x = start_x + t * (end_x - start_x)
            y = start_y + (math.sin(-(t * math.pi)) * 100)

            moving_label.place(x=x, y=y)
            root.after(delay, animate, step + 1)
        else:
            moving_label.place_forget()
            if rand.random() > 0.5:
                splat_label.place(x=end_x, y=end_y)
                competition['Kerne']['score'] += 1
            else:
                splat_label.place_forget()

            update_scores()

    animate(0)

def move_arc_erne():
    start_x = 1050
    start_y = 175

    target_center_x = 720
    target_center_y = 200

    variance_x = 50
    variance_y = 50

    end_x = target_center_x - (tk_image7.width() // 2) + rand.randint(-variance_x, variance_x)
    end_y = target_center_y - (tk_image7.height() // 2) + rand.randint(-variance_y, variance_y)

    steps = 100
    delay = 20

    def animate(step):
        if step <= steps:
            t = step / steps
            x = start_x - t * (start_x - end_x)
            y = start_y + (4 * (t - 0.5) ** 2 - 1) * 150  

            moving_label_erne.place(x=x, y=y)
            root.after(delay, animate, step + 1)
        else:
            moving_label_erne.place_forget()

            if rand.random() > 0.5:
                splat_label_erne.place(x=end_x, y=end_y)
                competition['Erne']['score'] += 1
            else:
                splat_label_erne.place_forget()

            update_scores()

    animate(0)


def move_special_kerne():
    button_special_kerne.config(state=tk.DISABLED)
    
    number = rand.random() 
    if number > 0.5:
        special_throw_kerne()
        competition['Kerne']['score'] += 1
        update_scores()
        if check_victory():
            return
    else:
        print("Kerne's special throw missed.")
        button_special_kerne.config(state=tk.NORMAL)

    update_scores()  
    

def special_throw_kerne():
    start_x = 350
    start_y = 200

    target_center_x = 720
    target_center_y = 200

    end_x = target_center_x - (tk_image5.width() // 2) + rand.randint(-50, 50)
    end_y = target_center_y - (tk_image5.height() // 2) + rand.randint(-50, 50)

    steps = 100
    delay = 20

    def animate(step):
        if step <= steps:
            t = step / steps
            x = start_x + t * (end_x - start_x)
            y = start_y + (math.sin(-(t * math.pi)) * 100)
            moving_label.place(x=x, y=y)
            root.after(delay, animate, step + 1)
        else:
            moving_label.place_forget()
            if rand.random() > 0.5:
                splat_label.place(x=end_x, y=end_y)
            else:
                splat_label.place_forget()

    animate(0)
    

def move_special_erne():
    button_special_erne.config(state=tk.DISABLED)

    number = rand.random()
    if number > 0.5:
        special_throw_erne()
        competition['Erne']['score'] += 1
        update_scores()
        if check_victory():
            return
    else:
        print("Erne's special throw missed.")
        button_special_erne.config(state=tk.NORMAL)

    update_scores()  

def special_throw_erne():
    start_x = 1050
    start_y = 175

    target_center_x = 720
    target_center_y = 200

    end_x = target_center_x - (tk_image7.width() // 2) + rand.randint(-50, 50)
    end_y = target_center_y - (tk_image7.height() // 2) + rand.randint(-50, 50)

    steps = 100
    delay = 20

    def animate(step):
        if step <= steps:
            t = step / steps
            x = start_x - t * (start_x - end_x)
            y = start_y + (4 * (t - 0.5) ** 2 - 1) * 150
            moving_label_erne.place(x=x, y=y)
            root.after(delay, animate, step + 1)
        else:
            moving_label_erne.place_forget()
            if rand.random() > 0.5:
                splat_label_erne.place(x=end_x, y=end_y)
            else:
                splat_label_erne.place_forget()

    animate(0)  


button = tk.Button(root, text="Kutsu Erne", command=show_image2)
button.grid(row=1, column=1)  #

button_move_arc = tk.Button(root, text="Kernen heitto", command=move_arc_kerne)
button_move_arc.grid(row=1, column=0) 

button_move_arc2 = tk.Button(root, text="Ernen heitto", command=move_arc_erne)
button_move_arc2.grid(row=1, column=2)  
button_move_arc2.grid_forget()  

button_yhteissheitto = tk.Button(root, text="Yhteisheitto", command=lambda: [move_arc_kerne(), move_arc_erne()])
button_yhteissheitto.grid(row=2, column=1)
button_yhteissheitto.grid_forget() 

button_reset = tk.Button(root, text="Nollaa", command=reset_scores)
button_reset.grid(row=4, column=1)

button_special_kerne = tk.Button(root, text="Kerne Special Throw", command=move_special_kerne, state=tk.DISABLED)
button_special_kerne.grid(row=2, column=0)

button_special_erne = tk.Button(root, text="Erne Special Throw", command=move_special_erne, state=tk.DISABLED)
button_special_erne.grid(row=2, column=2)


update_scores()
root.mainloop()
