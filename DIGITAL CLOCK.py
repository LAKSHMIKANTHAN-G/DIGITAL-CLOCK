from tkinter import*
import time

def digital():
    d=time.strftime("%H:%M:%S")
    clock.config(text=d)
    clock.after(200,digital)
root=Tk()
root.title("DIGITAL CLOCK- LAKSHMIKANTHAN")
clock=Label(root,font=("times",100,"bold"),bg="blue")
clock.grid(rows=2,column=1)
digital()
root.mainloop()