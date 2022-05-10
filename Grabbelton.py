import tkinter
import random
grabbeldingen = ['ps4', 'pc', 'boek', 'muis', 'oortjes', 'hoet', 'shirt', 'tv', 'cocktail', 'rgb', ]
window = tkinter.Tk()
window.geometry('300x200')
window.configure(bg='white')
window.title('grabbel ton')

gegrabbeld = tkinter.Label(window,text="",bg="green",fg="black",)
gegrabbeld.pack(ipadx=50,ipady=50,expand=True,fill='both')


def grabbelen():
    if len(grabbeldingen) > 0:
        GegrabbeldDingen = random.choice(grabbeldingen)
        grabbeldingen.remove(GegrabbeldDingen)
        gegrabbeld.config(text=f'Gefeliciteerd, je hebt een {GegrabbeldDingen} gegrabbeld!')
        window.update()
    else:
        gegrabbeld.config(text=f'U heeft een alle dingen gegrabbeld')

button = tkinter.Button(
    window,
    text='grabbel',
    command = grabbelen
)

button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

window.mainloop()
