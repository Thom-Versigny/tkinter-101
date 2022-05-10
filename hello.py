import tkinter as tk
window = tk.Tk()
window.geometry('300x200')
window.configure(bg='blue')
window.title('hello')

box1 = tk.Label(
    window,
    text="Hello tkinter!",
    bg="green",
    fg="black",
    font=10
)

box1.pack(
    ipadx=50,
    ipady=50,
    expand=True
    
)

window.mainloop()
