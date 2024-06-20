import tkinter as tk
from tkinter import font,Button, Entry, Label, Tk, messagebox
from tkinter.font import Font
class BMI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("BMI CALCULATOR")
        self.root.geometry("600x300+300+200")
        fstyle= font.Font(family="Arial", size=15)
        f1 = ("arial", 15, 'bold')
        f2 = ("calibre", 14)

        self.label = tk.Label(self.root, text="BMI CALCULATOR",font=f1,fg='red')
        self.label.pack()

        # Creating labels and entry fields for height, and weight

        self.label_height = tk.Label(self.root, text="HEIGHT (CM):",font=f1)
        self.label_height.pack()
        self.entry_height = tk.Entry(self.root,font=f2)
        self.entry_height.pack()

        self.label_weight = tk.Label(self.root, text="WEIGHT (KG):",font=f1)
        self.label_weight.pack()
        self.entry_weight = tk.Entry(self.root,font=f2)
        self.entry_weight.pack()

        self.button = tk.Button(self.root, text="CALCULATE",font=f1,fg='red' ,command=self.calculate_bmi)
        self.button.pack()

        self.label_result =tk.Label(self.root, text="BMI RESULT:",font=f1)
        self.label_result.pack()
        self.entry_result=tk.Label(self.root,text="- - - -",font=f2,fg='blue')
        self.entry_result.pack()
        
        self.label_cat=tk.Label(self.root,text="CATEGORY:",font=f1)
        self.label_cat.pack()
        self.entry_cat=tk.Label(self.root,text="- - - -",font=f2,fg='blue')
        self.entry_cat.pack()

    def calculate_bmi(self):
        height = int(self.entry_height.get())
        weight = int(self.entry_weight.get())

        # Calculate BMI
        height_in_meters = height / 100
        bmi = weight / (height_in_meters ** 2)

        # Display BMI categoryformat(value, ".2f")
        if bmi <= 18.5:
            self.entry_result.config(text=format(bmi,".2f"))
            self.entry_cat.config(text="UNDERWEIGHT")
        elif 18.5 < bmi <= 25:
            self.entry_result.config(text=format(bmi,".2f"))
            self.entry_cat.config(text="NORMAL")
        elif 25 < bmi <= 30:
            self.entry_result.config(text=format(bmi,".2f"))
            self.entry_cat.config(text="OVERWEIGHT")
        else:
            self.entry_result.config(text=format(bmi,".2f"))
            self.entry_cat.config(text="OBESITY")
    def run(self):
        self.root.mainloop()

game = BMI()
game.run()