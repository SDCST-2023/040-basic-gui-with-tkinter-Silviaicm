import tkinter as tk
from tkinter.constants import LEFT, RIGHT

window = tk.Tk()
window.title("example")

dog = tk.PhotoImage(file="dog.png")
labeldog = tk.Label(window, image = dog)
label1 = tk.Label(window,text="pochacco")
label2 = tk.Label(window,text="a cuddly little puppy! This is from the same \ncreators who brouht you Keropi and Kero Kero", bg="#ADD8E6")

labeldog.place(side = LEFT )
label1.place(side= RIGHT )
label2.place()

window.mainloop()
exit()