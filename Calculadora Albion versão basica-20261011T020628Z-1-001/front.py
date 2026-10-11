from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("Albion Gerenciador")

icon = PhotoImage(file='assets/albion-logo.png')
window.iconphoto(True,icon)
window.config(background="#023857")
label = Label(window,text="Albion Gerenciador",
              font=('Arial'),
              fg='white',
              bg='#023857')
#label.place(x=0,y=0)
label.pack()

window.mainloop()
