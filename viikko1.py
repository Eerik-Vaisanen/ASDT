import matplotlib.pyplot as plt
import time
import winsound
import random as rand
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button

x = 10

kuu_x = 70
kuu_y = 95

E_raketti_x, E_raketti_y = 90, 1
K_raketti_x, K_raketti_y = 30, 1

E_raketti_x_offset, K_raketti_x_offset = 0, 0

rocket_min_distance = 5  
plot_x_min, plot_x_max = 0, 100

regards_dict = {} 
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

for i in range(10):
    print(str(x) + "...")
    x -= 1
    winsound.Beep(440, 200)
    time.sleep(0.1)

if x == 0:
    winsound.Beep(600, 1000)
print("Valmista!")

def laukaisu():
    todennakoisyys = 1
    lahtolaukaisu = rand.randint(0, 100)

    if todennakoisyys == lahtolaukaisu:
        print("Launch failed! It was nice knowing you :,-)")
        return False
    else:
        print("Launch successful! Godspeed!")

        E_reached_moon = False
        K_reached_moon = False

        def ask_for_regards(astronaut_name):
            """Ask for regards from the astronaut and store it in the dictionary."""
            regard = input(f"{astronaut_name}, please enter your regards: ")
            regards_dict[astronaut_name] = regard

        def animate(frame):
            nonlocal E_reached_moon, K_reached_moon
            ax.clear()
            ax.set_xlim(0, 100)
            ax.set_ylim(0, 100)

            ax.plot(kuu_x, kuu_y, 'yo')  

            if not E_reached_moon:
                ax.plot(E_raketti_x + E_raketti_x_offset, E_raketti_y + frame, 'ko', marker='^')
                winsound.Beep(220, 100)
                ax.text(E_raketti_x + E_raketti_x_offset, E_raketti_y + frame + 5, 
                        f'({E_raketti_x + E_raketti_x_offset}, {E_raketti_y + frame})', ha='right')

            if not K_reached_moon:
                ax.plot(K_raketti_x + K_raketti_x_offset, K_raketti_y + frame, 'ko', marker='^')
                winsound.Beep(880, 100)
                ax.text(K_raketti_x + K_raketti_x_offset, K_raketti_y + frame + 5, 
                        f'({K_raketti_x + K_raketti_x_offset}, {K_raketti_y + frame})', ha='right')

         
            if not E_reached_moon and abs((E_raketti_x + E_raketti_x_offset) - kuu_x) < 1 and abs((E_raketti_y + frame) - kuu_y) < 1:
                E_reached_moon = True
                ask_for_regards("Ernesti")

           
            if not K_reached_moon and abs((K_raketti_x + K_raketti_x_offset) - kuu_x) < 1 and abs((K_raketti_y + frame) - kuu_y) < 1:
                K_reached_moon = True
                ask_for_regards("Kernesti")

           
            if E_reached_moon and K_reached_moon:
                print("Both rockets have landed.")
                print("Regards collected from the astronauts:")
                print(regards_dict)  
                plt.pause(2)
                plt.close()

       
        ax_E_left = plt.axes((0.5, 0.05, 0.1, 0.075))
        ax_E_right = plt.axes((0.61, 0.05, 0.1, 0.075))
        ax_E_up = plt.axes((0.72, 0.05, 0.1, 0.075))

        ax_K_left = plt.axes((0.1, 0.05, 0.1, 0.075))
        ax_K_right = plt.axes((0.21, 0.05, 0.1, 0.075))
        ax_K_up = plt.axes((0.32, 0.05, 0.1, 0.075))

        btn_E_left = Button(ax_E_left, 'E Left')
        btn_E_right = Button(ax_E_right, 'E Right')
        btn_E_up = Button(ax_E_up, 'E Up')

        btn_K_left = Button(ax_K_left, 'K Left')
        btn_K_right = Button(ax_K_right, 'K Right')
        btn_K_up = Button(ax_K_up, 'K Up')

        def move_E_raketti_left(event):
            global E_raketti_x_offset
            E_raketti_x_offset -= 1

        def move_E_raketti_right(event):
            global E_raketti_x_offset
            E_raketti_x_offset += 1

        def move_E_raketti_up(event):
            global E_raketti_y
            E_raketti_y += 1

        def move_K_raketti_left(event):
            global K_raketti_x_offset
            K_raketti_x_offset -= 1

        def move_K_raketti_right(event):
            global K_raketti_x_offset
            K_raketti_x_offset += 1

        def move_K_raketti_up(event):
            global K_raketti_y
            K_raketti_y += 1

        btn_E_left.on_clicked(move_E_raketti_left)
        btn_E_right.on_clicked(move_E_raketti_right)
        btn_E_up.on_clicked(move_E_raketti_up)

        btn_K_left.on_clicked(move_K_raketti_left)
        btn_K_right.on_clicked(move_K_raketti_right)
        btn_K_up.on_clicked(move_K_raketti_up)


        animation = FuncAnimation(fig, animate, frames=95, interval=100, repeat=False)
        plt.show()

        return True

laukaisu()
