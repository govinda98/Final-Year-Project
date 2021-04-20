mport tkinter as tk
from tkinter import ttk
 
 
window = tk.Tk()
 
window.title("ALS Comms")
window.minsize(600,400)
 
def clickMe():
    label.configure(text= name.get())
 
label1 = ttk.Label(//path to generated text file) ) //Govinda's path >>osf_examples>dataset>absolute>cachly>hello.txt
label1.grid(column = 0, row = 0)
 
label = ttk.Label(window, text = " ")
label.grid(column = 0, row = 30) 
 
 
name = tk.StringVar()
nameEntered = ttk.Entry(window, width = 15, textvariable = name)
nameEntered.grid(column = 0, row = 1)
 
 
button = ttk.Button(window, text = "Reply", command = clickMe)
button.grid(column= 0, row = 5)
 
window.mainloop()