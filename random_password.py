from tkinter import *
import tkinter as tk
import tkinter.messagebox
import random
import string

root=Tk()
root.title("Random Password Generator")
root.geometry('450x350')
root.configure(bg="teal")


def generate_password():
        len= int(e2.get())
        name=str(e1.get())
        if len>0 and name!="":
            my_password=""
            for x in range(len):
                my_password += chr(random.randint(33,126))
            label_result.config(text=my_password)
        else:
            tk.messagebox.showwarning(title="Warning!", message="You must enter a task. ")

def accept():
   return exit()
def reset():
    if e1.get()!='' and e2.get()!='' :
        e1.delete(0, END)
        e2.delete(0, END)
        label_result.config(text='')
    else :
        tkinter.messagebox.showwarning(title="Warning!", message="Username or Length of Password is missing.")


frame1 = tk.Frame(root,bg="teal")
frame1.place(x=20, y=70)
tk.Label(root,text="Password Generator",font=('Times New Roman',18),bg="teal").place(x=150, y=20)
tk.Label(frame1, text="Enter user name       :",bg="teal",font=("times new roman",16)).grid(row=0)
tk.Label(frame1,text="Length of the password:",bg="teal",font=("times new roman",16)).grid(row=1)
tk.Label(frame1,text="Generate Password      :",bg="teal",font=("times new roman",16)).grid(row=2)



e1=tk.Entry(frame1,bg="floralwhite",width=25,font=("times new roman", 12))
e2=tk.Entry(frame1,bg="floralwhite",width=25,font=("times new roman", 12))
label_result=Label(frame1, text="", font=("times new roman", 11), bg='floralwhite',width=25)


e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
label_result.grid(row=2,column=1)


tk.Button(root,text="Generate password",command=generate_password,borderwidth=1, relief="solid",background="skyblue",font=("times new roman",16)).place(x=133, y=180)
tk.Button(root,text="Accept",command=accept,borderwidth=1, relief="solid",background="green",font=("times new roman",16)).place(x=180,y=225)
tk.Button(root,text="Reset",command=reset,borderwidth=1, relief="solid",bg="orangered",font=("times new roman",16)).place(x=185,y=272)


root.mainloop()
