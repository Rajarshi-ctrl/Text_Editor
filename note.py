from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def new():
    root.title("Untitled - Text_Editor")
    file = None
    txt.delete(1.0, END)

def opn():
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Editor")
        txt.delete(1.0, END)
        f = open(file, "r")
        txt.insert(1.0, f.read())
        f.close()

def save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            f = open(file, "w")
            f.write(txt.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Editor")
            print("File Saved")
    else:
        f = open(file, "w")
        f.write(txt.get(1.0, END))
        f.close()

def cut():
    txt.event_generate(("<<Cut>>"))

def copy():
    txt.event_generate(("<<Copy>>"))

def paste():
    txt.event_generate(("<<Paste>>"))

def hlp():
    showinfo("Text Editor", "For any type of query, Please visit our website www.mytexteditor.com")


root = Tk()
root.geometry("766x484")
root.title("Text Editor")
root.iconphoto(False, PhotoImage(file='txt.png'))

l = Label(root, text="Welcome to this text editor", bg="grey", fg="black", padx=8, pady=2, font=("lucida",20), relief=GROOVE, borderwidth=3)
l.pack(side=TOP, fill=X)

scrl = Scrollbar(root)
scrl.pack(side=RIGHT, fill=Y)
txt = Text(root,yscrollcommand=scrl.set, bg="white",font=(None,16), borderwidth=4)
file = None
txt.pack(fill=BOTH, expand=True)

scrl.config(command=txt.yview)


mn = Menu(root)
m1 = Menu(mn, tearoff=0)
m1.add_command(label="New", command=new)
m1.add_command(label="Open", command=opn)
m1.add_command(label="Save", command=save)
m1.add_separator()
m1.add_command(label="Exit", command=quit)
root.config(menu=mn)
mn.add_cascade(label="File", menu=m1)


m2 = Menu(mn, tearoff=0)
m2.add_command(label="Cut", command=cut)
m2.add_command(label="Copy", command=copy)
m2.add_command(label="Paste", command=paste)
root.config(menu=mn)
mn.add_cascade(label="Edit", menu=m2)


mn.add_command(label="Help", command=hlp)
root.config(menu=mn)



l1 = Label(root, text="Thank you for using this and have a good day !!", bg="grey", fg="black", font=(None,12,"bold"), relief=RIDGE, borderwidth=1)
l1.pack(side=BOTTOM, fill=X)

root.mainloop()
