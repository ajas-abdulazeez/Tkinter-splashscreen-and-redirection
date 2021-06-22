from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
from tkinter import filedialog
from typing import TextIO
from PIL import ImageTk,Image
import numpy as np
from os.path import isfile, join


company_name="ABCDEF COMPNAY"
main_window = Tk()

# setting up our main windwo alignment
app_width = 1060
app_height = 600
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

#finding the center of the screen
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2 ) - (app_height / 2)
#aligning window in the center
main_window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
main_window.title(company_name+"  billing software")
# Hide the title bar
#main_window.overrideredirect(True)

#calling our homescreen
def call_homescreen():
	print("called loginscreen screen successfully!")
	splash_section.destroy()
	loginscreen()




    

#loginscreen
def loginscreen():

    login_section = Frame(main_window,padx=30, pady=30,background="#6285E2")
    login_section.pack(fill="both", expand=True)
    label_company_name = Label(login_section,
                                    text = company_name,
                                    fg = "black").pack()
    label_login_tag = Label(login_section,
                                    text = "Please log in here!",
                                    fg = "black",height=2 ).pack()
    #admin login section here
    admin_login_section = Frame(login_section,padx=10, pady=10,highlightbackground="#6285E2",highlightthickness=3)
    admin_login_section.pack(side=LEFT,fill="both",padx=25,pady=50,expand=True)
    label_admin_login_tag = Label(admin_login_section,
                                    text = "ADMIN",
                                    fg = "black",height=2 ).pack()
    #textbox=.pack()
    button_admin_login = Button(admin_login_section,
                                text = "Browse Files",bd=8,
                                bg="black",
                                fg="green",
                                activeforeground="Orange",
                                activebackground="green",
                                font="Andalus",
                                highlightcolor="purple",
                                justify="right",
                                padx=50,
                                relief="groove", command =call_homescreen).pack(side=RIGHT)
    #staff login section here
    staff_login_section = Frame(login_section,padx=15, pady=10,highlightbackground="#6285E2",highlightthickness=3)
    staff_login_section.pack(side=RIGHT,fill="both",pady=50,padx=25, expand=True)
    label_staff_login_tag = Label(staff_login_section,
                                    text = "STAFF",
                                    fg = "black",height=2 ).pack()


    button_staff_login = Button(staff_login_section,
                                text = "Login",bd=8,
                                bg="black",
                                fg="green",
                                activeforeground="Orange",
                                activebackground="green",
                                font="Andalus",
                                highlightcolor="purple",
                                justify="right",
                                padx=50,
                                relief="groove", command =call_homescreen)

    button_staff_login.pack(side=RIGHT)









print("Now,you are at splash screen!")
splash_section = Frame(main_window,padx=10, pady=10,background="#6285E2")
splash_section.pack(fill="both", expand=True)
label_image_opened_data = Label(splash_section,
                                    text = "SPLASH SCREEN",
                                    fg = "black",height=2 ).pack(padx=100,pady=50)
label_developedby= Label(splash_section,
                                    text = "Developed by CYBARZ PRODUCTIONS",
                                    fg = "black",height=2 ).pack(side=BOTTOM,padx=100,pady=50)


# Splash Screen Timer
main_window.after(2500, call_homescreen)
main_window.mainloop()








