# BMI Calculator
import tkinter as kinter
from tkinter import messagebox
# Formula  for BMI: Body weight(kg) / height(m**2) 

# BMI Index : Below 18.5 = underweight , 18.5 - 24.9  = Healthy range, 25.0 - 29.9 = Overweight, >/=30.0  = Obese
def bmi_calculator():
    
    
    
  try:
        underWeight = 18.5 
        
        weight = float(weight_spinbox.get())
        
        height = float(height_spinbox.get())
        
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
  except:
      messagebox.showerror('Sorry the answer:', result,'is not valid, please try using numbers')
      
      overweight_color = "#FF9800"
      normalweight_color = "#4CAF50"
      
        
#   set_default_color_theme('blue')      
# Main window tkinter
root = kinter.Tk()
root.title("The BMI Calculator")

root.configure(bg='#428df5')

# The widget
kinter.Label(root, text="Please fill in the following information").grid(row=0, column=0)
kinter.Label(root, text=" Below 18.5 = underweight").grid(row=1, column=0)
kinter.Label(root, text=" 18.5 - 24.9  = Healthy range",bg="green").grid(row=2, column=0)
kinter.Label(root, text=" 25.0 - 29.9 = Overweight", bg="orange").grid(row=3, column=0)




kinter.Label(root, text="Weight (In Kg):", bg='#428df5', fg='white').grid(row=1, column=1)
weight_spinbox = kinter.Spinbox(root, from_=30.0, to=300.0, increment=1, width=10, bg="black")
weight_spinbox.grid(row=1, column=2)

kinter.Label(root, text="Height (In Metres):",  bg='#428df5', fg='white').grid(row=2, column=1)
height_spinbox = kinter.Spinbox(root, from_=1.0, to=2.5, increment=0.01, width=10, bg="black")
height_spinbox.grid(row=2, column=2)

submit = kinter.Button(root, text="Calculate", command=bmi_calculator, bg='red', fg='black')
submit.grid(row=5, columnspan=5)

BMI_label = kinter.Label(root, text="Your BMI is:" , bg='#428df5')
BMI_label.grid(row=4, columnspan=3)

result = kinter.Label(root, text="", bg='#428df5')
result.grid(row=7, columnspan=3)

root.mainloop()


    
    
    



