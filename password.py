import time
import Tkinter as tk
window = tk.Tk()
#Code for password
def checkPassword ():
    username ="Admin"
    password ="2267922033"
    
    #Code for password
    #Password is password
    enteredUsername = usernameEntry.get()
    enteredPassword = passwordEntry.get()
  
    if username == enteredUsername:
        confirmLabel.config(text="Correct Entry. Logging in as Admin")
    if password == enteredPassword:
        confirmLabel.config(text="Correct Entry")
        time.sleep(1)
        print ("Logged In as Admin")
        u1 = raw_input ("Show peronal information. show/hide:")
        if u1 == "show":
            pA = raw_input ("Enter personal 4-digit pin:")
        if pA == "5790":
            print ("Made in: 3/25/2020 by GoodCoding Studios")
            print ("Head of project: Shayan Saeed")
            print ("Project No. 998709")
            print ("Project Code: 22654387")
            print ("Recovery code:990087")
            print ("No more information availible")
        else:
            rc = raw_input("Incorrect Pin .Try Again by Clicking F5 or Entering Recovery Code:")
            if rc == "990087":
                
                print ("Made in: 3/25/2020 by GoodCoding Studios")
                print ("Head of project: Shayan Saeed")
                print ("Project No. 998709")
                print ("Project Code: 22654387")
                print ("Recovery code:990087")
                print ("No more information availible")
    else:
        confirmLabel.config(text="Incorrect Password or Username. Try again")
        
            
#Username Box
usernameLabel = tk.Label (window, text="Username:")
usernameEntry = tk.Entry (window)
#Password Box
passwordLabel = tk.Label (window, text="Password:")
passwordEntry = tk.Entry(window, show="*")

#File editor
button = tk.Button (window, text="Submit", command=checkPassword)
confirmLabel = tk.Label(window)

usernameLabel.pack()
usernameEntry.pack()
passwordLabel.pack()
passwordEntry.pack()
button.pack()
confirmLabel.pack()

window.mainloop()
    
#Code to run a password program
