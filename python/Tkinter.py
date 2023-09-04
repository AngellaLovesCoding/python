from tkinter import *

window=Tk()
window.geometry("320x320")

i = 5
def close():
    global i
    i-=1
    if i is 4:
        label.config(text="i told you not to press it :<")
    if i is 3:
        label.config(text="bruhhhhhh i told you >:(")
    if i is 2:
        label.config(text=".........")
    if i is 1:
        label.config(text="this is the last warning!!!!!!!!!")
    if i is 0:
        label.config(text="NOOooooooooooooooooooo..........")
    esc_btn.config(text=i)
    if i<0:
        window.quit()

label=Label(window, text="dont press the button!!!")
label.pack()

esc_btn =Button(window,text="close",padx=50, pady=20,command=close)
esc_btn.place(relx=0.5,rely=0.5,anchor=CENTER)

window.mainloop()