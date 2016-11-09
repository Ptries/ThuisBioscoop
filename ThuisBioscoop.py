"""
Start van het project Thuisbioscoop
Projectgroep 3 klas V1M
"""

import time
import urllib.request
import xmltodict
from tkinter import messagebox, Label, Button, FALSE, Tk, Entry

username = ("Test")
password = ("Temp")

def try_login():
    print("Trying to login...")
    if username_guess.get() == username and password_guess.get() == password:
        messagebox.showinfo("-- COMPLETE --", "You Have Now Logged In.", icon="info")
    else:
        messagebox.showinfo("-- ERROR --", "Please enter valid infomation!", icon="warning")

def try_register():
    print("Trying to register...")
    #Sign-Up
    #Maakt het fram voor aan te melden
    signup_window = Tk()
    signup_window.resizable(width=FALSE, height=FALSE)
    signup_window.title("Registreren")
    signup_window.geometry("250x200")
    #Maakt de username en wachtwoord textboxen voor aan te melden
    username_register_text = Label(signup_window, text="Username:")
    username_register_guess = Entry(signup_window)
    password_register_text = Label(signup_window, text="Password:")
    password_register_guess = Entry(signup_window, show="*")
    #Maakt sign-up button
    attempt_sign_up = Button(signup_window,text="Sign Up")
    #Toont alles in de gui Register
    username_register_text.pack()
    username_register_guess.pack()
    password_register_text.pack()
    password_register_guess.pack()
    attempt_sign_up.pack()

#Login
#Maakt het frame voor in te loggen
login_window = Tk()
login_window.resizable(width=FALSE, height=FALSE)
login_window.title("Log-In")
login_window.geometry("250x160")
#Maakt de username en wachtwoord textboxen en de buttons
username_text = Label(login_window, text="Username:")
username_guess = Entry(login_window)
password_text = Label(login_window, text="Password:")
password_guess = Entry(login_window, show="*")
#Maakt login button
attempt_login = Button(login_window,text="Login", command=try_login)
#Maakt registratie button
attempt_register = Button(login_window,text="Registreer", command=try_register)
#Toont alles in de gui Login
username_text.pack()
username_guess.pack()
password_text.pack()
password_guess.pack()
attempt_login.pack()
attempt_register.pack()

#Main Starter
login_window.mainloop()

def openAPI():
    datumVandaag = time.strftime("%d-%m-%Y")
    APIlink = 'http://api.filmtotaal.nl/filmsoptv.xml?apikey=zky5pqtra4entxe7lk3agqqtk8snjgry&dag=' + str(
        datumVandaag) + '&sorteer=0'
    response = urllib.request.urlopen(APIlink).read()
    xmldictionary = xmltodict.parse(response)
    return xmldictionary

filmsVandaag = openAPI()

print(filmsVandaag)
