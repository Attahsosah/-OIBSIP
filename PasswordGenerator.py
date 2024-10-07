# Python program to generate random
# password using Tkinter module
import random
import pyperclip
from tkinter import *
from tkinter.ttk import *

# Function for calculation of password
def pas():
    # This ensures that the input field is empty to start with . 
    entry.delete(0,END)
    # Collecting the length of the password given
    leng = vari.get()
    # We have the type of  characters to use
    
    # In the lowercase, we only have characters that are lowercase
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    # Uppercase has characters that are uppercase and the addition of lowercase characters
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    # This has the lowercase and uppercase characters. Then I added the numbers and characters
    numbers =  "!@#$%^&*()~ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`'  "
    password = ""
    
    # Here we have defined what will happen when a particular strength is selected . Either Low, Medium or High
    
    if var.get() == 1: 
        for i in range(0, leng):
            password = password + random.choice(lowercase)

        return password
    elif var.get() == 2:
        for i in range(0,leng):
            password = password + random.choice(uppercase)
        return password
    elif var.get() == 3:
        for i in range(0, leng):
            password = password + random.choice(numbers)
        return password
    else:
        print("Please choose one of the options in the radio buttons")
    
    
def create():
        code = pas()
        entry.insert(10, code)
        
    # The function that we will use to copy the password to the clipboard
def clip():
    rand_pass = entry.get()
    # pyperclip is what we use to copy the password
    pyperclip.copy(rand_pass)
    
    







# Main Function

# create GUI window
root = Tk()
var = IntVar()
vari = IntVar()

# Title of your GUI window
root.title("Random Password Generator")

# create label and entry to show
# password generated
rand_pass = Label(root, text="Password")
rand_pass.grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)



# create label for length of password
c_label = Label(root, text="Length")
c_label.grid(row=1)

# create Buttons Copy which will copy
# password to clipboard and Generate
# which will generate the password
copy_button = Button(root, text="Copy", command=clip)
copy_button.grid(row=0, column=2)
generate_button = Button(root, text="Create", command=create)
generate_button.grid(row=0, column=3)

# Radio Buttons for deciding the
# strength of password
# Default strength is Medium
radio_low = Radiobutton(root, text="Low", variable=var, value=1  )
radio_low.grid(row=1, column=2, sticky='E')
radio_middle = Radiobutton(root, text="Medium", variable=var, value=2)
radio_middle.grid(row=1, column=3, sticky='E')
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3 )
radio_strong.grid(row=1, column=4, sticky='E')
combo = Combobox(root, textvariable=vari)

length_slider = Scale(root, from_=8, to_=32, orient=HORIZONTAL, variable=vari)
length_slider.grid(row=1, column=1)


# start the GUI
root.mainloop()
