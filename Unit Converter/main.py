from tkinter import *

window = Tk()
window.title("Unit Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="New Label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="Convert")
my_label.grid(column=0, row=0)


# Button
def button_clicked():
    new_text = input_field.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=0)

# Entry

input_field = Entry(width=10)
input_field.grid(column=2, row=2)


window.mainloop()
