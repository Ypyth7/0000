from PyQt5.QtWidgets import QApplication,QInputDialog,QLineEdit
import keyboard
from time import sleep
app = QApplication([])
password,ok = QInputDialog.getText(None,'password','your password',QLineEdit.Password)
import module
w = module.visual("yaroslav",8)
w.hello()
w.print_password(password)
e = []
def add():
    add = input("add element: ")
    e.append(add)
    print(e)
def delite():
    del1 = input("element name: ")
    e.remove(del1)
def print_all():
    print(e)
def keya():    
    keyboard.press("a")
    keyboard.write("hello")
    keyboard.release("a")
while True:
    con = input("[~Users~Креайтивика~Desktop] >")
    keya()
    if con == "add":
        add()
    elif con == "del":
        delite()    
    elif con == "print_all":
        print_all()
    else:
        print("error! command " + con + " is not defined")
        
'''
x = 1
if x == 1:
    print("hello")'''