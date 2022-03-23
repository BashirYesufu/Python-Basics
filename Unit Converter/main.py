import tkinter

window = tkinter.Tk()
window.title("Unit Converter")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="New Label", font=("Arial", 24, "bold"))
my_label.pack()

window.mainloop()
