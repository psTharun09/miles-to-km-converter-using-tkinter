from tkinter import *

VALUE = 0
def calculation():
    num = float(miles_input.get())
    VALUE = int(num) * 1.609
    ans_label.config(text=VALUE)

window = Tk()
window.title("Mile to Km Converter")
#window.minsize(width=400,height=200)
window.config(padx=20,pady=20)

miles_input=Entry(width=7)
miles_input.grid(column=1,row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0,row=1)


ans_label = Label(text=VALUE)
ans_label.grid(column=1,row=1)


km_label = Label(text="Km")
km_label.grid(column=2,row=1)


calculate = Button(text="Calculate",command=calculation)
calculate.grid(column=1,row=2)



window.mainloop()