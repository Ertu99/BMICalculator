from tkinter import *

window = Tk()
window.title("BMI")
window.config(padx=30,pady=30)

def button_clicked():
    height = entry_height.get()
    weight = entry_weight.get()

    if entry_weight == "" or entry_height == "":
        result_label.config(text="enter weight and height!")
    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="enter a valid number")



def write_result(bmi):
    result_string = f"Your bmi is {bmi}. You are  "
    if bmi <=16:
        result_string += "Severe Thinness"
    elif 16 < bmi >= 17:
        result_string += "Moderate Thinness	"
    elif 17 < bmi >= 18.5:
        result_string += "Mild Thinness"
    elif 18.5 < bmi >= 25:
        result_string += "normal"
    elif 25 < bmi >= 30:
        result_string += "overweight"
    elif 30 < bmi >= 35:
        result_string += "obese class I"
    elif 35 < bmi >= 40:
        result_string += "obese class II"
    else:
        result_string += "obese class III"
    return result_string


label_height = Label(text="Your height (cm) ")
label_height.pack()

entry_height = Entry()
entry_height.pack()

label_weight = Label(text="Your Weight (kg) ")
label_weight.pack()

entry_weight = Entry()
entry_weight.pack()

button = Button(text="Calculate",command=button_clicked)
button.pack()

result_label = Label()
result_label.pack()


window.mainloop()


