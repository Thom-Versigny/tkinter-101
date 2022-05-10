import tkinter
import time
window = tkinter.Tk()
window.geometry('300x200')
window.configure(bg='white')
window.title('clock')

klok = tkinter.Label(
    window,
    text="",
    bg="green",
    fg="black",
    font=10
)

klok.pack(
    ipadx=50,
    ipady=50,
    expand=True,
    fill='both'

)


def digitalclock():
   text_input = time.strftime("%H:%M:%S")
   klok.config(text=text_input)
   klok.after(1000, digitalclock)

digitalclock()

window.mainloop()
