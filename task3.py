import tkinter as tk
from tkinter.constants import LEFT, RIGHT

window = tk.Tk()
window.title("example")

dog = tk.PhotoImage(file="dog.png")
labeldog = tk.Label(window, image = dog)
label1 = tk.Label(window,text="pochacco")
label2 = tk.Label(window,text="a cuddly little puppy! This is from the same \ncreators who brouht you Keropi and Kero Kero", bg="#ADD8E6")

labeldog.grid(row = 1,column=1 )
label1.grid(row = 1,column=2 )
label2.grid(row = 2,column= 1, columnspan= 2)

window.mainloop()
exit()