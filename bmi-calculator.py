import tkinter as tk

screen = tk.Tk()
screen.minsize(220,260)
screen.title("BMI Calculator")
screen.config(background="#EDF1D6",)

#? BMI Calculator label
first_label = tk.Label(text="BMI Calculator",bg="#EDF1D6",padx=10,pady=5,fg="#40513B",font="Times 16 bold")
first_label.pack()

#? height
height_label = tk.Label(text="Enter height(cm): ",background="#EDF1D6",pady=10)
height_entry = tk.Entry()
height_label.pack()
height_entry.pack()

#? weight
weight_frame = tk.Frame(bg="#EDF1D6",pady=10)
weight_frame.pack()
weight_label = tk.Label(master=weight_frame,text="Enter weight(kg)",background="#EDF1D6",pady=10)
weight_entry = tk.Entry(master=weight_frame)
weight_label.pack()
weight_entry.pack()

#?calculate button
calculate_button = tk.Button(text="Calculate")
calculate_button.pack()

tk.mainloop()
