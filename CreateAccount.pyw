# Imports #

import tkinter as tk
from tkinter import *
import customtkinter as ct
from customtkinter import *

# CustomTkinter Config #

ct.set_appearance_mode('dark')
ct.set_default_color_theme('dark-blue')

# Window & Config Start #

root = ct.CTk(className='Create Account')
root.geometry("265x400")
root.config(bg='#3c4454')
root.resizable(False, False)
root.title("Create Account")

# Entry Variables #

entry1 = tk.StringVar()
entry2 = tk.StringVar()
entry3 = tk.StringVar()
entry4 = tk.StringVar()
entry5 = tk.StringVar()
entry6 = tk.StringVar()

# Labels #

lbl = ct.CTkLabel(root, text="Create Account", text_font=10)
lbl.pack(anchor=CENTER, pady=10)

# Entrys #

ent1 = ct.CTkEntry(root, placeholder_text="First Name", width=250, text_font=10, textvariable=entry1)
ent1.pack(after=lbl, pady=10) 
ent2 = ct.CTkEntry(root, placeholder_text="Last Name", width=250, text_font=10, textvariable=entry2)
ent2.pack(after=ent1, pady=10) 
ent3 = ct.CTkEntry(root, placeholder_text="Username", width=250, text_font=10, textvariable=entry3)
ent3.pack(after=ent2, pady=10) 
ent4 = ct.CTkEntry(root, placeholder_text="Email", width=250, text_font=10, textvariable=entry4)
ent4.pack(after=ent3, pady=10) 
ent5 = ct.CTkEntry(root, placeholder_text="Password", width=250, text_font=10, textvariable=entry5, show="*")
ent5.pack(after=ent4, pady=10) 
ent6 = ct.CTkEntry(root, placeholder_text="Confirm Password", width=250, text_font=10, textvariable=entry6, show="*")
ent6.pack(after=ent5, pady=10) 

# SubmitAll Definition #

def submitall():
    var1 = ""
    var2 = ""
    var3 = ""
    var4 = ""
    var5 = ""
    var6 = ""
    var1 += entry1.get()
    var2 += entry2.get()
    var3 += entry3.get()
    var4 += entry4.get()
    var5 += entry5.get()
    var6 += entry6.get()
    f = open(file=(str(var1 + var2)+".user"), mode="w")
    [...]
    f.write("First Name: " + var1 + '\n')
    f.write("Last Name: " + var2 + '\n')
    f.write("Username: " + var3 + '\n')
    f.write("Email: " + var4 + '\n')
    f.write("Password: " + var5 + '\n')
    f.write("Confirm: " + var6 + '\n')
    f.write(" " + '\n')
    f.close()

# Buttons #

btn = ct.CTkButton(root, text="Submit", command=submitall, width=300)
btn.pack(side=BOTTOM)

# Window & Config End #

root.mainloop()