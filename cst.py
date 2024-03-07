from tkinter import *
from tkinter import messagebox

import dateutil.utils
from tkcalendar import Calendar
from customtkinter import *
import random, os, tempfile, smtplib
from PIL import Image
from tkinter import filedialog


app = CTk()

set_appearance_mode("dark")
app.geometry("800x400")



if not os.path.exists('name'):
    os.mkdir('name')

def clear():
    name_entry.delete(0,END)
    fname_entry.delete(0,END)
    foccup_entry.delete(0,END)
    std_qualE.delete(0,END)
    std_ageE.delete(0,END)
    std_adde.delete(0,END)
    gen_ent.delete(0,END)
    doj_entry.delete(0,END)
    doj_entry.insert(0, "dd/mm/yyyy")
    img_label.configure(text="",image="")
    img_label1.configure(text="",image="")
    CTkOptionMenu.set(toc_opt,'')
    CTkOptionMenu.set(toc_opt1,'')
def addimage():

     global my_image, filepath,img_label
     filepath = filedialog.askopenfilename(initialdir="D:/Images")
     my_image = CTkImage(light_image=Image.open(filepath),size=(100,100))
     img_label = CTkLabel(master=std_frame1, text="", image=my_image, height=100, width=100)
     img_label.grid(row=5, column=1)


def addimage1():

    global my_image1,filepath1,img_label1
    filepath1 = filedialog.askopenfilename(initialdir="D:/Images1")
    my_image1 = CTkImage(light_image=Image.open(filepath1), size=(100, 100))
    img_label1 = CTkLabel(master=std_frame1, text="", image=my_image1, height=100, width=100)
    img_label1.grid(row=6, column=1)


def view():

    win1 = CTkToplevel(app)
    win1.grab_set()
    win1.geometry("500x350")
    win1.title("Preview")

    def search():
        for i in os.listdir('name/'):
            if i.split('.')[0] == searchent.get():
                f = open(f'name/{i}', 'r')
                detail_txtbox.delete(1.0, END)
                for data in f:
                    detail_txtbox.insert(END, data)
                f.close
                break
        else:
            messagebox.showerror("Error", "invalid name")

    def savingbill():
        result = messagebox.askyesno("confirm", "do  you want to save?")
        if result:
            bill_content = detail_txtbox.get(1.0, END)
            file = open(f'name/{name_entry.get()}.txt', 'w')
            file.write(bill_content)
            file.close()
            messagebox.showinfo("Successs", f'{name_entry.get()} Details saved successfully')
            detail_txtbox.delete(1.0,END)


    std_frame2 = CTkFrame(master=win1, height=500, width=400)
    std_frame2.pack(fill="both", expand="true")

    detail_txtbox = CTkTextbox(master=std_frame2, height=400, width=600, font=("arial", 20, "bold"))
    detail_txtbox.grid(row=0, column=0)
    detail_txtbox.delete(1.0,END)


    detail_txtbox.insert(END, f"\t\t**Welcome Student**\t\t\n\n")
    detail_txtbox.insert(END, f'Stundent_Name\t\t\t{name_entry.get()}\n\n')
    detail_txtbox.insert(END, f'Fathername\t\t\t{fname_entry.get()}\n\n')
    detail_txtbox.insert(END, f'Father Occupation\t\t\t{foccup_entry.get()}\n\n')
    detail_txtbox.insert(END, f'Qualification\t\t\t{std_qualE.get()}\n\n')
    detail_txtbox.insert(END, f'Age\t\t\t{std_ageE.get()}\n\n')
    detail_txtbox.insert(END, f'Address\t\t\t{std_adde.get()}\n\n')
    detail_txtbox.insert(END, f'Gender\t\t\t{gen_ent.get()}\n\n')
    detail_txtbox.insert(END, f'Selected_Course\t\t\t{toc_opt.get()}\n\n')
    detail_txtbox.insert(END, f'Date_of_Join\t\t\t{doj_entry.get()}\n\n')
    detail_txtbox.insert(END, f'Grade\t\t\t{toc_opt1.get()}\n\n')




    searchent = CTkEntry(master=std_frame2, width=400, height=50, font=("arial", 20, "bold"))
    searchent.grid(row=1, column=0, pady=20)

    searchbut = CTkButton(master=std_frame2, text="Search", font=("arial", 40, "bold"),command=search)
    searchbut.grid(row=2, column=0, pady=10,sticky="w")

    savebut = CTkButton(master=std_frame2, text="Save", font=("arial", 40, "bold"), command=savingbill)
    savebut.grid(row=2, column=1, pady=10)

    win1.mainloop()

def getrad():
    if std_var.get() == "Male":
        gen_ent.delete(0,END)
        gen_ent.insert(END,"Male")
    elif std_var.get() == "Female":
        gen_ent.delete(0, END)
        gen_ent.insert(END,"Female")



def pick_date(event):

    global cal,date_window


    date_window = CTkToplevel(app)
    date_window.grab_set()
    date_window.title("Pick a Date")
    date_window.geometry("250x220+550+220")
    cal = Calendar(date_window, selectmode='day', date_pattern="dd/mm/y")
    cal.place(x=0, y=0)

    submit = CTkButton(date_window, text="Submit",command=grab_date)
    submit.place(x=80, y=190)

def grab_date():
    doj_entry.delete(0, END)
    doj_entry.insert(0, cal.get_date())
    date_window.destroy()



head_label = CTkLabel(master=app, text="RAJU INSTITUDE", font=("arial", 40, "bold"))
head_label.pack(pady=6)


std_frame = CTkFrame(master=app, height=500, width=400)
std_frame.pack(side="left", fill="both", expand="true")

name_label = CTkLabel(master=std_frame, text="Name", font=("arial", 40, "bold"))
name_label.grid(row=0, column=0, sticky="w", pady=15)

name_entry = CTkEntry(master=std_frame, font=("arial", 30, "bold"),width=300)
name_entry.grid(row=0, column=1, pady=15, padx=15)

fname_label = CTkLabel(master=std_frame, text="Father_Name", font=("arial", 40, "bold"))
fname_label.grid(row=1, column=0, sticky="w", pady=15)

fname_entry = CTkEntry(master=std_frame, font=("arial", 30, "bold"),width=300)
fname_entry.grid(row=1, column=1, pady=15, padx=15)

foccup_label = CTkLabel(master=std_frame, text="Father_Occupation", font=("arial", 40, "bold"))
foccup_label.grid(row=2, column=0, sticky="w", pady=15)

foccup_entry = CTkEntry(master=std_frame, font=("arial", 30, "bold"),width=300)
foccup_entry.grid(row=2, column=1, pady=15, padx=15)

std_qual = CTkLabel(master=std_frame, text="Qualification", font=("arial", 40, "bold"))
std_qual.grid(row=3, column=0, sticky="w", pady=15)

std_qualE = CTkEntry(master=std_frame, font=("arial", 30, "bold"),width=300)
std_qualE.grid(row=3, column=1, pady=15, padx=15)

std_age = CTkLabel(master=std_frame, text="Age", font=("arial", 40, "bold"))
std_age.grid(row=4, column=0, sticky="w", pady=15)

std_ageE = CTkEntry(master=std_frame, font=("arial", 30, "bold"),width=300)
std_ageE.grid(row=4, column=1, pady=15, padx=15)

std_add = CTkLabel(master=std_frame, text="ADDRESS", font=("arial", 40, "bold"))
std_add.grid(row=5, column=0, sticky="w", pady=15)

std_adde = CTkEntry(master=std_frame, font=("arial", 30, "bold"),width=300)
std_adde.grid(row=5, column=1, pady=15, padx=15)



view_button = CTkButton(master=std_frame, text="View",font=("arial", 40, "bold"),command=view)
view_button.grid(row=6, column=0, pady=20)

clear_button = CTkButton(master=std_frame, text="Clear",font=("arial", 40, "bold"),command=clear)
clear_button.grid(row=6, column=1, pady=20)



std_frame1 = CTkFrame(master=app, height=500, width=400)
std_frame1.pack(side="left", fill="both", expand="true")

std_var = StringVar(value="other")

gen_label = CTkLabel(master=std_frame1, text="Gender",font=("arial", 40, "bold"))
gen_label.grid(row=0, column=0, sticky="w", pady=15)

gen_rad1 = CTkRadioButton(master=std_frame1,text="Male",variable=std_var, value="Male",font=("arial", 40, "bold"),command=getrad)
gen_rad1.grid(row=1, column=0, sticky="W",pady=15)

gen_rad2 = CTkRadioButton(master=std_frame1,text="Female", variable=std_var, value="Female",font=("arial", 40, "bold"), command=getrad)
gen_rad2.grid(row=1, column=1,pady=15,sticky="w")

gen_ent = CTkEntry(master=std_frame1, font=("arial", 30, "bold"),width=300)
gen_ent.grid(row=0, column=1, pady=15, padx=15)



toc_label = CTkLabel(master=std_frame1, text="Type_Of_Course", font=("arial", 40, "bold"))
toc_label.grid(row=2, column=0,pady=15)

datas = ['','TWTamil','TWEnglish','SHTamil','SHEnglish','COA','TALLY','HindiTeach']

toc_opt = CTkOptionMenu(master=std_frame1, values=datas, font=("arial", 40, "bold"),width=300)
toc_opt.grid(row=2, column=1, padx=10)


doj_label = CTkLabel(master=std_frame1, text="Date of join", font=("arial", 40, "bold"))
doj_label.grid(row=3, column=0, sticky="w", pady=15)

doj_entry = CTkEntry(master=std_frame1, font=("arial", 40, "bold"), width=300)
doj_entry.grid(row=3, column=1, pady=15, padx=15)
doj_entry.insert(0, "dd/mm/yyyy")
doj_entry.bind("<1>", pick_date)


grad_label = CTkLabel(master=std_frame1, text="Grade", font=("arial", 40, "bold"))
grad_label.grid(row=4, column=0, sticky="w", pady=15)

datas = ['','Junior','Senior']

toc_opt1 = CTkOptionMenu(master=std_frame1, values=datas, font=("arial", 40, "bold"),width=300)
toc_opt1.grid(row=4, column=1, padx=10)


img_button = CTkButton(master=std_frame1, text="SelectImage",font=("arial", 10, "bold"),command=addimage)
img_button.grid(row=5, column=0, pady=20)

img1_button = CTkButton(master=std_frame1, text="SelectSign",font=("arial", 10, "bold"),command=addimage1)
img1_button.grid(row=6, column=0, pady=20)






app.mainloop()