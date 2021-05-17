#Naeemah Davis
#BMI Calculator
import tkinter as tk
from tkinter import *
from tkinter import INSERT
from tkinter import messagebox

top = tk.Tk()
stvar = StringVar(top)
top.title("Naeemah Davis")
#size of the window on which everything will be displayed
top.geometry("700x700")
#made it non-resizable so the user cannot change the size of the window
top.resizable(width=False, height=True)
top.config(bg= "light blue")
#making a Frame variable called frame
frame = tk.Frame(top)
#setting the width, height and position of frame
frame.place(x=70, y=210, height=250, width=550)
#making a label with the title thats being displaye ont hte window called top
lbl_title = Label(top, text= "Ideal Body Mass Index", font="Arial 23")
#position of title label on window called top
lbl_title.place(x=300, y=50)
lbl = Label(top, text="Calculator", font= "Arial 23")
lbl.place(x=380, y=89)
lbl_sub = Label(top, text="Enter the following", font="Arial 18")
lbl_sub.place(x=100, y=180)
lbl_height = Label(frame, text="Height(cm) :", font="Arial 16")
lbl_height.place(x=50, y=30)
#height of user will be entered and value will be displayed in blue
ent_height = Entry(frame, fg="blue")
ent_height.place(x=300, y=30, height= 25)
ent_height.focus_set()
lbl_weight = Label(frame, text="Weight(kg) :", font="Arial 16")
lbl_weight.place(x=50, y=80)
ent_weight = Entry(frame, fg="blue")
ent_weight.place(x=300, y=80)
lbl_gender = Label(frame, text="Gender :", font="Arial 16")
lbl_gender.place(x=50, y=130)

# Section that if the user is female the AGE entry becomes active and will be taken into consideration
lbl_age = Label(frame, text="Age :", font="Arial 16")
lbl_age.place(x=50, y=180)
ent_age = Entry(frame, fg="blue", state="readonly")
ent_age.place(x=300, y=180, width=50)
def females(item):
    stvar.set(item)
    if item != "Female":
        ent_age.config(state="readonly")
    else:
        ent_age.config(state="normal")

dict_genders= { "Male", "Female"}
stvar.set(["Male"]) # set the default option
gender_menu = tk.OptionMenu(frame, stvar, *dict_genders, command= females)
gender_menu.place(x=300, y=130)


#Section that calculates the BMI of User
def bmi():

    if ent_age['state'] == "normal":
        try:
            weight = float(ent_weight.get())
            height = float(ent_height.get())
            age = int(ent_age.get())
            bmi = weight/(height/float(100))**float(2)
            txt_bmi.configure(state= "normal")
            txt_bmi.insert(INSERT, str(round(bmi,1)))
            ideal_bmi = 0.5*weight/(height/100)**2+0.03*age+11
            txt_ibmi.config(state="normal")
            txt_ibmi.insert(INSERT, str(round(ideal_bmi,1)))

        except ValueError:
            messagebox.showinfo("Error", "Incorrect value entered")
            ent_height.delete(0, END)
            ent_weight.delete(0, END)
            ent_age.delete(0, END)
            txt_bmi.delete(0, END)
            txt_ibmi.delete(0, END)
    else:
        try:
            weight = float(ent_weight.get())
            height = float(ent_height.get())
            bmi = weight/(height/float(100))**float(2)
            txt_bmi.configure(state="normal")
            txt_bmi.insert(INSERT, str(round(bmi, 1)))
            ideal_bmi = 0.5*weight/(height/100)**2+11.5
            txt_ibmi.config(state="normal")
            txt_ibmi.insert(INSERT, str(round(ideal_bmi,1)))
        except ValueError:
            messagebox.showinfo("Error", "Incorrect value entered")
            ent_height.delete(0, END)
            ent_weight.delete(0, END)
            txt_bmi.delete(0, END)
            txt_ibmi.delete(0, END)


btncalculate = Button(top, text="Calculate Your Ideal Body Mass Index", font= "Arial 20", command=bmi)
btncalculate.place(x=100, y=480, width=500)
lbl_bmi = Label(top, text="BMI :", font="Arial 16")
lbl_bmi.place(x=100, y=530)
txt_bmi = Text(top, fg= "blue", state="disabled")
txt_bmi.place(x=200, y=530, height=30, width=100)
lbl_ibmi = Label(top, text= "Ideal BMI", font="Arial 16")
lbl_ibmi.place(x=350, y=530)
txt_ibmi = Text(top, fg= "blue", state= "disabled")
txt_ibmi.place(x=500, y=530, height=30, width=100)

def clear():
    ent_height.delete(0, END)
    ent_weight.delete(0, END)
    ent_age.delete(0, END)
    txt_bmi.delete(1.0, END)
    txt_ibmi.delete(1.0, END)
    txt_bmi.config(state = "disabled")
    txt_ibmi.config(state ="disabled")
    ent_height.focus_set()


btn_clear =Button(top, font="Arial 20", text="Clear", fg="Red", command=clear)
btn_clear.place(x=70, y=600, width=150)

def exit():
    msg =messagebox.askquestion("Exit Application", "Are you sure you want to exit the BMI Calculator?")
    if msg == "yes":
        top.destroy()
    else:
        messagebox.showinfo("Return", "You will now return to the BMI Calculator")
btn_exit =Button(top, font="Arial 20", text="Exit", bg="Red")
btn_exit.place(x=500, y=600, width=150)

# pic = tk.PhotoImage(file="treadmill.jpg")

top.mainloop()