import tkinter
import time
import random
kleur = ["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta"]
breedte = 50
hoogte = 50
window = tkinter.Tk()


for x in range(6,0,-1):
    breedte += 50
    hoogte += 50
    nukleur = random.choice(kleur)
    window.geometry(f'{breedte}x{hoogte}')
    window.configure(bg=nukleur)
    window.update()
    print(x)
    time.sleep(2)


window.mainloop()


