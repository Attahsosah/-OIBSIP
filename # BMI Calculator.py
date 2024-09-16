# BMI Calculator
import tkinter as tk
from tkinter import messagebox
# Formula  for BMI: Body weight(kg) / height(m**2) 

# BMI Index : Below 18.5 = underweight , 18.5 - 24.9  = Healthy range, 25.0 - 29.9 = Overweight, >/=30.0  = Obese
def bmi_calculator():
    underWeight = 18.5 
    # healthyRange = range (float(18.5), float(24.9))
    # overWeight  = range(25.0, 29.9 )
    weight =  float(weight_in.get())
    
    height =  float(height_in.get())
    BMI = weight / (height**2)
    
    BMI_label.config(text = f"Your BMI is: {BMI:.2f}")
    
    
    if BMI < underWeight:
        result.config(text="According to your BMI, you are underweight")
        
    elif 18.5 <= BMI <= 24.9 :
        result.config(text="You are within normal weight parameters")
    
    elif 25.0 <= BMI <= 29.9 :
        result.config(text="You are overweight")
        
    else: 
        result.config(text="According to your BMI, you are obese")
        
#   set_default_color_theme('blue')      
# Main window tkinter
root = tk.Tk()
root.title=("BMI Calculator")

root.configure(bg='#00008B')

# The widget
tk.Label(root, text="Weight (In Kg):", bg='#00008B', fg='white').grid(row=0, column=0)
weight_in = tk.Entry(root)
weight_in.grid(row=0, column=1)

tk.Label(root, text="Height (In Metres):",  bg='#00008B', fg='white').grid(row=1, column=0)
height_in = tk.Entry(root)
height_in.grid(row=1, column=1)

submit = tk.Button(root, text="Calculate", command=bmi_calculator, bg='red', fg='red')
submit.grid(row=2, columnspan=2)

BMI_label = tk.Label(root, text="Your BMI is:" , bg='#00008B')
BMI_label.grid(row=3, columnspan=2)

result = tk.Label(root, text="", bg='#00008B')
result.grid(row=4, columnspan=2)

root.mainloop()


    
    
    



