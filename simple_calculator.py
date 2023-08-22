import tkinter
from tkinter import *
root=Tk()
root.title("Simple Calculator")
root.geometry("450x450")
root.configure(bg="black")
#root.resizable(0,0)


equation=""
def show(value):
    global equation
    equation += value
    enter_value.config(text=equation)


def clear():
    global equation
    equation=""
    enter_value.config(text=equation)
def delete():
    global equation
    equation = equation[:-1]
    enter_value.config(text=equation)

def calculate():
    global equation
    result=""
    if equation!="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""

    enter_value.config(text=result)



enter_value=tkinter.Label(root,font=("times new roman",27),width=20,height=2,bg="lightcyan")
enter_value.place(x=25,y=35)



tkinter.Button(root,text="C",font=("arial",22,"bold"),width=5,bg="slate grey",fg="white",command=lambda: clear()).place(x=25,y=125)
tkinter.Button(root,text="%",font=("arial",22,"bold"),width=5,bg="slate grey",fg="white",command=lambda: show("%")).place(x=125,y=125)
tkinter.Button(root,text="X",font=("arial",22,"bold"),width=6,bg="slate grey",fg="white",command=lambda:delete()).place(x=225,y=125)
tkinter.Button(root,text="/",font=("arial",22,"bold"),width=5,bg="slate grey",fg="white",command=lambda: show("/")).place(x=330,y=125)
tkinter.Button(root,text="7",font=("arial",22,"bold"),width=5,bg="slate grey",fg="white",command=lambda: show("7")).place(x=25,y=185)
tkinter.Button(root,text="8",font=("arial",22,"bold"),width=5,bg="slate grey",fg="white",command=lambda: show("8")).place(x=125,y=185)
tkinter.Button(root,text="9",font=("arial",22,"bold"),width=6,bg="slate grey",fg="white",command=lambda: show("9")).place(x=225,y=185)
tkinter.Button(root,text="*",font=("arial",22,"bold"),width=5,bg="slate grey",fg="white",command=lambda: show("*")).place(x=330,y=185)
tkinter.Button(root,text="4",font=("arial",22,"bold"),width=5,bg="slate grey",fg="white",command=lambda: show("4")).place(x=25,y=245)
tkinter.Button(root,text="5",font=("arial",22,"bold"),width=5,bg="slate grey",fg="white",command=lambda: show("5")).place(x=125,y=245)
tkinter.Button(root,text="6",font=("arial",22,"bold"),width=6,bg="slate grey",fg="white",command=lambda: show("6")).place(x=225,y=245)
tkinter.Button(root,text="-",font=("arial",22,"bold"),width=5,bg="slate grey",fg="white",command=lambda: show("-")).place(x=330,y=245)
tkinter.Button(root,text="1",font=("arial",22,"bold"),width=5,bg="slate grey",fg="white",command=lambda: show("1")).place(x=25,y=305)
tkinter.Button(root,text="2",font=("arial",22,"bold"),width=5,bg="slate grey",fg="white",command=lambda: show("2")).place(x=125,y=305)
tkinter.Button(root,text="3",font=("arial",22,"bold"),width=6,bg="slate grey",fg="white",command=lambda: show("3")).place(x=225,y=305)
tkinter.Button(root,text="+",font=("arial",22,"bold"),width=5,bg="slate grey",fg="white",command=lambda: show("+")).place(x=330,y=305)
tkinter.Button(root,text="00",font=("arial",22,"bold"),width=5,bg="slate grey",fg="white",command=lambda: show("00")).place(x=25,y=365)
tkinter.Button(root,text="0",font=("arial",22,"bold"),width=5,bg="slate grey",fg="white",command=lambda: show("0")).place(x=125,y=365)
tkinter.Button(root,text=".",font=("arial",22,"bold"),width=6,bg="slate grey",fg="white",command=lambda: show(".")).place(x=225,y=365)
tkinter.Button(root,text="=",font=("arial",22,"bold"),width=5,bg="slate grey",fg="white",command=lambda:calculate()).place(x=330,y=365)












root.mainloop()

