import tkinter as tk
from tkinter.constants import RAISED

window = tk.Tk()
window.title("multiplication calculator")
window.geometry("500x20")

entry1 = tk.Entry(window,text="entry", borderwidth=3,relief=RAISED)
label1 = tk.Label(window,text="X")
entry2 = tk.Entry(window,text="entry",borderwidth = 3,relief = RAISED) 
button1 = tk.Button(window,text = "=")
entry3 = tk.Entry(window,text = "here is the answer",borderwidth = 3,relief = RAISED)

entry1.grid(row = 1,column = 1)
label1.grid(row = 1, column = 2)
entry2.grid(row = 1, column = 3)
button1.grid(row = 1, column = 4)
entry3.grid(row = 1, column = 5)

window.mainloop()
exit()