from calculations import Cal
from settings import *
import tkinter as tk
from tkinter.messagebox import showinfo, askyesno
from memory import save, load, delete

#Gui:
class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        #Setup Window
        self.geometry(WINDOW_SIZE)
        self.title(WINDOW_TITLE)
        self.resizable(0, 0)
        self.iconbitmap(ICO_FILE)

        #Setup Rows and Collumns
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        #Buttons
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)

        #Other
        self.RESULT = 0
        self.Opperand = "None"

        #Call Functions
        self.__widgets__()
        self.__buttons__()

    def __widgets__(self):
        Title = tk.Label(self, text=WINDOW_TITLE, font=(0, 15))
        Title.grid(column=0, row=0, sticky=tk.W, padx=PADDING, pady=PADDING)

        Info = tk.Label(self, text="Input Numbers here: ", font=(0, 15))
        Info.grid(column=0, row=1, sticky=tk.W, padx=PADDING, pady=PADDING)

        self.OperandLabel = tk.Label(self, text=f"Current Operand: {self.Opperand}", font=(0, 15))
        self.OperandLabel.grid(column=0, row=2, sticky=tk.W, padx=PADDING, pady=PADDING)

        self.Result = tk.Label(self, text=f"Result: {self.RESULT}", font=(0, 15))
        self.Result.grid(column=1, row=0, sticky=tk.W, padx=PADDING, pady=PADDING)

        self.XEntry = tk.Entry(self)
        self.XEntry.grid(column=1, row=1, sticky=tk.W, padx=PADDING, pady=PADDING)

        self.YEntry = tk.Entry(self)
        self.YEntry.grid(column=1, row=2, sticky=tk.W, padx=PADDING, pady=PADDING)

    def __buttons__(self):
        add = tk.Button(self, text="+", command=lambda: self.__Operand__("+"))
        add.grid(column=2, row=0, sticky=tk.W, padx=PADDING, pady=PADDING)
        sub = tk.Button(self, text="-", command=lambda: self.__Operand__("-"))
        sub.grid(column=2, row=1, sticky=tk.W, padx=PADDING, pady=PADDING)

        multi = tk.Button(self, text="*", command=lambda: self.__Operand__("*"))
        multi.grid(column=3, row=0, sticky=tk.W, padx=PADDING, pady=PADDING)
        div = tk.Button(self, text="/", command=lambda: self.__Operand__("/"))
        div.grid(column=3, row=1, sticky=tk.W, padx=PADDING, pady=PADDING)

        Submit = tk.Button(self, text="Submit",width=16, command=lambda: self.__Handler__())
        Submit.grid(column=1, row=3, sticky=tk.W, padx=PADDING, pady=PADDING)
        
        OpenMen = tk.Button(self, text="History", command=lambda: self.__message__(1))
        OpenMen.grid(column=4, row=0, sticky=tk.W, padx=PADDING, pady=PADDING)

        DeleteMen = tk.Button(self, text="Delete History", command=lambda: self.__message__(2))
        DeleteMen.grid(column=4, row=1, sticky=tk.W, padx=PADDING, pady=PADDING)

    def __confirmdel__(self):
        q = askyesno("confirmation", "Are you sure you wnat to delete your history?")

        if q:
            return True
        else:
            return False

    def __message__(self, type: int):
        if type == 1:
            showinfo("History", load())
        elif type == 2 and self.__confirmdel__():
            showinfo("Deleted", "History has been deleted.")
            delete()
        else:
            raise ValueError("Unknown Type!")

    def __Operand__(self, Oper: str):
        if Oper == "+":
            self.Opperand = "+"
        elif Oper == "-":
            self.Opperand = "-"
        elif Oper == "*":
            self.Opperand = "*"
        elif Oper == "/":
            self.Opperand = "/"

        self.OperandLabel.configure(text=f"Current Operand: {self.Opperand}")
        print(self.Opperand)
    
    def __Handler__(self):
        Unum1 = self.XEntry.get()
        Unum2 = self.YEntry.get()

        if (Unum1 == "") or (Unum2 == ""):
            print("")
        else:
            num1 = float(Unum1)
            num2 = float(Unum2)
            cal = Cal(num1, num2)

        R = "0"

        if self.Opperand == "+":
            R = cal.Add()
        elif self.Opperand == "-":
            R = cal.Sub()
        elif self.Opperand == "*":
            R = cal.Multi()
        elif self.Opperand == "/":
            R = cal.Divide()
        
        self.RESULT = R
        self.Result.configure(text=f"Result: {self.RESULT}")

        FullE = f"{num1} {self.Opperand} {num2} = {R}"

        save(w=FullE)

if __name__ == "__main__":
    app = App()

    app.mainloop()