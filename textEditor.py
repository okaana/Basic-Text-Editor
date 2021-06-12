
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import tkinter.messagebox
import os
from pyautogui import hotkey
import subprocess

cmd = 'python texteditor.py'


def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.grid()


def newfile():
    # os.system('python textEditor.py')
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)


def tellAbout():
    tkinter.messagebox.showinfo("About", "This Editor is created by \nPrafful Chowdhary\n Chaitra Rao")


def openFile():
    name = askopenfilename()
    file_var = open(name, "r+")
    print(file_var.name)
    root.title(file_var.name)
    file_content = file_var.read(1000)
    editorBox.delete('1.0', 'end-1c')
    editorBox.insert('1.0', file_content)
    editor_forname.delete('1.0', 'end-1c')
    editor_forname.insert('1.0', file_var.name)
    file_var.close()


def showtext():
    print(editorBox.get('1.0', 'end-1c'))


def saveFile():
    filename = editor_forname.get('1.0', 'end-1c')
    file_var = open(filename, "w")
    print("Saved")
    content = editorBox.get('1.0', 'end-1c')
    file_var.write(content)
    file_var.close()


def saveAs():
    file_options = options = {}
    options['filetypes'] = [('text files', '.txt'), ('all files', '.*')]
    options['initialfile'] = 'Untitled.txt.txt'
    options['parent'] = root

    savelocation = asksaveasfilename(**file_options)
    file1 = open(savelocation, "w+")
    content = editorBox.get('1.0', 'end-1c')
    file1.write(content)
    file1.close()


def close():
    root.destroy()


def copy():
    hotkey('ctrl', 'c')


def cut():
    hotkey('ctrl', 'x')


def paste():
    hotkey('ctrl', 'v')


def select_all():
    hotkey('ctrl', 'a')


def undo():
    hotkey('ctrl', 'z')


def close_shortcut(event):
    root.destroy()


def save_shortcut(event):
    saveFile()


def open_shortcut(event):
    openFile()


root = Tk()

menubar = Menu(root)
# menu File
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=newfile)
filemenu.add_command(label="Open", command=openFile, accelerator="Ctrl+O")
filemenu.add_command(label="Save", command=saveFile, accelerator="Ctrl+S")
filemenu.add_command(label="Save as...", command=saveAs)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=close, accelerator="Ctrl+Q")
menubar.add_cascade(label="File", menu=filemenu)

# menu Edit
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=undo, accelerator="Ctrl+Z")

editmenu.add_separator()

editmenu.add_command(label="Copy", command=copy, accelerator="Ctrl+C")
editmenu.add_command(label="Cut", command=cut, accelerator="Ctrl+X")
editmenu.add_command(label="Paste", command=paste, accelerator="Ctrl+V")
editmenu.add_command(label="Select All", command=select_all, accelerator="Ctrl+A")

# editmenu.add_command(label="Exit", command=close,accelerator="Ctrl+Q")
menubar.add_cascade(label="Edit", menu=editmenu)
# menu Help
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", command=tellAbout)
menubar.add_cascade(label="Help", menu=helpmenu)

# text and display button
editorBox = Text(root, width=100, height=40)
editorBox.pack(side=TOP, fill=BOTH, expand=YES)
# editorBox.

# to pass the name between functions and name the file
initial_name = "Untitled"
file_name = initial_name + ".txt"
count = 0
while (os.path.isfile(file_name) == True):
    if (os.path.isfile(file_name) != True):
        print("inside if")
        editor_forname = Text(root)
        editor_forname.insert('1.0', file_name)
    else:
        count += 1
        print("inside else")
        file_name = initial_name + str(count) + ".txt"
        print(file_name)
        editor_forname = Text(root)
        editor_forname.insert('1.0', file_name)

root.config(menu=menubar)

root.title(file_name)
root.bind('<Control-q>', close_shortcut)
root.bind('<Control-s>', save_shortcut)
root.bind('<Control-o>', open_shortcut)
root.mainloop()
