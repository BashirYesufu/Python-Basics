from tkinter import *

window = Tk()
window.title("Unit Converter")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="New Label", font=("Arial", 24, "bold"))
my_label.pack()
my_label["text"] = "New Text"
my_label.config(text="Convert")


# Button
def button_clicked():
    new_text = input_field.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry

input_field = Entry(width=10)
input_field.pack()


window.mainloop()
