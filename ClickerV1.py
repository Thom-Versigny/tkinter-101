import tkinter
window = tkinter.Tk()
nummer = 0
window.geometry('200x200')
window.configure(bg='grey')
window.title('grabbel ton')

def up():
    global nummer
    nummer = nummer + 1
    buttonmiddle.config(text=nummer)
def down():
    global nummer
    nummer = nummer - 1
    buttonmiddle.config(text=nummer)

def achtergrond():
    if nummer <= -1:
        window.configure(bg='red')
    elif nummer >= 1:
        window.configure(bg='green')
    else:
        window.configure(bg='grey')


buttonup = tkinter.Button(window, text='up', command=lambda: [up(), achtergrond()])
buttonmiddle = tkinter.Button(window, text='0',)
buttondown = tkinter.Button(window, text='down', command=lambda: [down(), achtergrond()])

buttonup.pack(ipadx=5,ipady=5,expand=True)
buttonmiddle.pack(ipadx=5, ipady=5, expand=True)
buttondown.pack(ipadx=5, ipady=5, expand=True)

window.mainloop()
