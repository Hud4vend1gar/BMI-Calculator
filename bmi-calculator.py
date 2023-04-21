import tkinter as tk

screen = tk.Tk()
screen.minsize(220,260)
screen.maxsize(220,280)
screen.title("BMI Calculator")
screen.config(background="#EDF1D6",)

#? variables
height = 0
weight = 1


#? BMI Calculator label
first_label = tk.Label(text="BMI Calculator",bg="#EDF1D6",padx=10,pady=5,fg="#40513B",font="Times 16 bold")
first_label.pack()

#? height
height_label = tk.Label(text="Enter height(cm): ",background="#EDF1D6",pady=10)
height_entry = tk.Entry(textvariable=height)
height_label.pack()
height_entry.pack()

#? weight
weight_frame = tk.Frame(bg="#EDF1D6",pady=10)
weight_frame.pack()
weight_label = tk.Label(master=weight_frame,text="Enter weight(kg)",background="#EDF1D6",pady=10)
weight_entry = tk.Entry(master=weight_frame,textvariable=weight)
weight_label.pack()
weight_entry.pack()

#? button func
def button_func():
    global weight
    global height
    try:
        weight = int(weight_entry.get())
        height = int(height_entry.get())
        height_bmi = (height * 0.01) ** 2
        weight_bmi = weight
        calculate_result = weight_bmi / height_bmi
        if calculate_result < 18.5:
            weight_range = "Underweight"
        elif calculate_result >= 18.5 and calculate_result <= 24.9:
            weight_range = "Normal"
        elif calculate_result > 24.9 and calculate_result <= 29.9:
            weight_range = "Overweight"
        elif calculate_result > 29.9:
            weight_range = "Obese"

        result_label = tk.Label(text=(weight_range),bg="#EDF1D6",font="Times 14 normal",pady=10)
        result_label.pack()

    except:
        alert_label = tk.Label(text="Just Enter valid number !!!")
        alert_label.pack()
        alert_label.after(5000,alert_label.destroy)



#?calculate button
calculate_button = tk.Button(text="Calculate",command=button_func)
calculate_button.pack()



tk.mainloop()
