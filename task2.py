import tkinter as tk

window = tk.Tk()
window.title("Veterinary Clinic")
window.geometry("500x200")

dog = tk.PhotoImage(file="dog.png")
labeldog = tk.Label(window, image = dog)
label1 = tk.Label(window,text="Name")
label2 = tk.Label(window,text="client database")
label3 = tk.Label(window,text="Type")
entry1 = tk.Entry(window,width = 15)
entry2 = tk.Entry(window,width = 15)
button1 = tk.Button(window,text="< previous")
button2 = tk.Button(window,text="next >")
button3 = tk.Button(window,text="save entry")

label4 = tk.Label(window,text="Breed")
entry3 = tk.Entry(window,width = 15)

label5 = tk.Label(window,text="Owner")
entry4 = tk.Entry(window,width = 15)

label6 = tk.Label(window,text="Birthdate")
entry5 = tk.Entry(window,width = 15)

button4 = tk.Button(window,text="search by name")
entry6 = tk.Entry(window,width = 15)


labeldog.grid(row = 1, column = 1)
label1.grid(row = 2, column = 1)
label2.grid(row = 1, column = 3)
label4.grid(row = 2, column = 3)
entry3.grid(row = 3, column = 3)
label3.grid(row = 2, column = 2)
entry1.grid(row = 3, column = 1)
entry2.grid(row = 3, column = 2)
label5.grid(row = 2, column = 4)
entry4.grid(row = 3, column = 4)
label6.grid(row = 2, column = 5)
entry5.grid(row = 3, column = 5)
button1.place(x = 0, y = 170)
button2.place(x = 455, y = 170)
button3.place(x = 230, y = 170)
button4.grid(row = 1, column = 4)
entry6.grid(row = 1, column = 5)

window.mainloop()
exit()