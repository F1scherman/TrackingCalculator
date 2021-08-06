import calculator
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
from ttkthemes import ThemedStyle
import calculatorAdsDataBase
import advertising
from PIL import Image
from PIL import ImageTk
class guiCalculator(calculator.calculator):
    def trigSwitch(self):
        if self._defaultTrig == False:
            self._defaultTrig = True
            self.trigSetting.set("Degrees")
        else:
            self._defaultTrig = False
            self.trigSetting.set("Radians")
    def on_closing(self):
        del self.__dbObject
        self.window.destroy()
    def isInteger(self,n):
        try:
            int(n)
        except ValueError:
            return False
        else:
            return True
    def solve(self,string):
        expression = string
        #this section converts pi and e to useable approximations
        while expression.partition('π')[1] != '':
            expression = expression.partition('π')[0] + '3.14159265358979323846' + expression.partition('π')[2]
            self.__dbObject.update('pi')
        
        while expression.partition('e')[1] != '':
            expression = expression.partition('e')[0] + '2.71828182845904523536' + expression.partition('e')[2]
            self.__dbObject.update('e')
        #Parentheses
        #this finds each instance of a parenthese, cuts out the part of the string within the parentheses, and then solves those and plugs it back in
        while expression.partition("(")[1] != '':
            expression = expression.partition("(")[0] + self.solve(expression.partition("(")[2].partition(")")[0]) + expression.partition("(")[2].partition(")")[2]
        #these lines will cut out any remaining right parentheses
        while expression.find(")") != -1:
            expression = expression.rstrip(")")

        while expression.find("abs") != -1:
            expression = expression.partition("abs")[0] + 'a' + expression.partition("abs")[2]
            exponentIndex = expression.find("a")
            integerIndex = 0
            powerIndex = -1
            for i in range(exponentIndex - 1, -1, -1):
                if self.isInteger(expression[i]) or expression[i] == ('.' or '-'):
                    continue
                integerIndex = i + 1
            for i in range(exponentIndex + 1, len(expression), 1):
                if self.isInteger(expression[i]) or expression[i] == '.':
                    continue
                powerIndex = i
            expression = expression[0:integerIndex] + str(self.absolute(float(expression[exponentIndex+1:powerIndex]+expression[powerIndex]))) + expression[powerIndex:-1]

        #Exponents/Logs/Trig/Roots
        while expression.find("^") != -1:
            exponentIndex = expression.find("^")
            integerIndex = 0
            powerIndex = -1
            for i in range(exponentIndex - 1, -1, -1):
                if self.isInteger(expression[i]) or expression[i] == '.':
                    continue
                integerIndex = i + 1
            for i in range(exponentIndex + 1, len(expression), 1):
                if self.isInteger(expression[i]) or expression[i] == '.':
                    continue
                powerIndex = i
            expression = expression[0:integerIndex] + str(self.power(float(expression[integerIndex:exponentIndex]),float(expression[exponentIndex+1:powerIndex]+expression[powerIndex]))) + expression[powerIndex:-1]
        while expression.find("sqrt") != -1:
            expression = expression.partition("sqrt")[0] + 'a' + expression.partition("sqrt")[2]
            exponentIndex = expression.find("a")
            integerIndex = 0
            powerIndex = -1
            for i in range(exponentIndex - 1, -1, -1):
                if self.isInteger(expression[i]) or expression[i] == '.':
                    continue
                integerIndex = i + 1
            for i in range(exponentIndex + 1, len(expression), 1):
                if self.isInteger(expression[i]) or expression[i] == '.':
                    continue
                powerIndex = i
            expression = expression[0:integerIndex] + str(self.power(float(expression[exponentIndex+1:powerIndex]+expression[powerIndex]),1/2)) + expression[powerIndex:-1]
            self.__dbObject.update('roots')
        while expression.find("ln") != -1:
            expression = expression.partition("ln")[0] + 'a' + expression.partition("ln")[2]
            exponentIndex = expression.find("a")
            integerIndex = 0
            powerIndex = -1
            for i in range(exponentIndex - 1, -1, -1):
                if self.isInteger(expression[i]) or expression[i] == '.':
                    continue
                integerIndex = i + 1
            for i in range(exponentIndex + 1, len(expression), 1):
                if self.isInteger(expression[i]) or expression[i] == '.':
                    continue
                powerIndex = i
            expression = expression[0:integerIndex] + str(self.logarithm('ln',float(expression[exponentIndex+1:powerIndex]+expression[powerIndex]))) + expression[powerIndex:-1]
            self.__dbObject.update('ln')
        while expression.find("log") != -1:
            expression = expression.partition("log")[0] + 'a' + expression.partition("log")[2]
            exponentIndex = expression.find("a")
            integerIndex = 0
            powerIndex = -1
            for i in range(exponentIndex - 1, -1, -1):
                if self.isInteger(expression[i]) or expression[i] == '.':
                    continue
                integerIndex = i + 1
            for i in range(exponentIndex + 1, len(expression), 1):
                if self.isInteger(expression[i]) or expression[i] == '.':
                    continue
                powerIndex = i
            expression = expression[0:integerIndex] + str(self.logarithm("log",float(expression[exponentIndex+1:powerIndex]+expression[powerIndex]))) + expression[powerIndex:-1]
            self.__dbObject.update('log')
        while expression.find("arcsin") != -1:
            expression = expression.partition("arcsin")[0] + 'a' + expression.partition("arcsin")[2]
            exponentIndex = expression.find("a")
            integerIndex = 0
            powerIndex = -1
            for i in range(exponentIndex - 1, -1, -1):
                if self.isInteger(expression[i]) or expression[i] == '.':
                    continue
                integerIndex = i + 1
            for i in range(exponentIndex + 1, len(expression), 1):
                if self.isInteger(expression[i]) or expression[i] == '.':
                    continue
                powerIndex = i
            expression = expression[0:integerIndex] + str(self.invTrig('arcsin',float(expression[exponentIndex+1:powerIndex]+expression[powerIndex]))) + expression[powerIndex:-1]
        while expression.find("arccos") != -1:
            expression = expression.partition("arccos")[0] + 'a' + expression.partition("arccos")[2]
            exponentIndex = expression.find("a")
            integerIndex = 0
            powerIndex = -1
            for i in range(exponentIndex - 1, -1, -1):
                if self.isInteger(expression[i]) or expression[i] == '.':
                    continue
                integerIndex = i + 1
            for i in range(exponentIndex + 1, len(expression), 1):
                if self.isInteger(expression[i]) or expression[i] == '.':
                    continue
                powerIndex = i
            expression = expression[0:integerIndex] + str(self.invTrig('arccos',float(expression[exponentIndex+1:powerIndex]+expression[powerIndex]))) + expression[powerIndex:-1]
        while expression.find("arctan") != -1:
            expression = expression.partition("arctan")[0] + 'a' + expression.partition("arctan")[2]
            exponentIndex = expression.find("a")
            integerIndex = 0
            powerIndex = -1
            for i in range(exponentIndex - 1, -1, -1):
                if self.isInteger(expression[i]) or expression[i] == '.':
                    continue
                integerIndex = i + 1
            for i in range(exponentIndex + 1, len(expression), 1):
                if self.isInteger(expression[i]) or expression[i] == '.':
                    continue
                powerIndex = i
            expression = expression[0:integerIndex] + str(self.invTrig('arctan',float(expression[exponentIndex+1:powerIndex]+expression[powerIndex]))) + expression[powerIndex:-1]
        while expression.find("sin") != -1:
            expression = expression.partition("sin")[0] + 'a' + expression.partition("sin")[2]
            exponentIndex = expression.find("a")
            integerIndex = 0
            powerIndex = -1
            for i in range(exponentIndex - 1, -1, -1):
                if self.isInteger(expression[i]) or expression[i] == '.':
                    continue
                integerIndex = i + 1
            for i in range(exponentIndex + 1, len(expression), 1):
                if self.isInteger(expression[i]) or expression[i] == '.':
                    continue
                powerIndex = i
            expression = expression[0:integerIndex] + str(self.trig('sin',float(expression[exponentIndex+1:powerIndex]+expression[powerIndex]))) + expression[powerIndex:-1]
            self.__dbObject.update('sin')
        while expression.find("cos") != -1:
            expression = expression.partition("cos")[0] + 'a' + expression.partition("cos")[2]
            exponentIndex = expression.find("a")
            integerIndex = 0
            powerIndex = -1
            for i in range(exponentIndex - 1, -1, -1):
                if self.isInteger(expression[i]) or expression[i] == '.':
                    continue
                integerIndex = i + 1
            for i in range(exponentIndex + 1, len(expression), 1):
                if self.isInteger(expression[i]) or expression[i] == '.':
                    continue
                powerIndex = i
            expression = expression[0:integerIndex] + str(self.trig('cos',float(expression[exponentIndex+1:powerIndex]+expression[powerIndex]))) + expression[powerIndex:-1]
        while expression.find("tan") != -1:
            expression = expression.partition("tan")[0] + 'a' + expression.partition("tan")[2]
            exponentIndex = expression.find("a")
            integerIndex = 0
            powerIndex = -1
            for i in range(exponentIndex - 1, -1, -1):
                if self.isInteger(expression[i]) or expression[i] == '.':
                    continue
                integerIndex = i + 1
            for i in range(exponentIndex + 1, len(expression), 1):
                if self.isInteger(expression[i]) or expression[i] == '.':
                    continue
                powerIndex = i
            expression = expression[0:integerIndex] + str(self.trig('tan',float(expression[exponentIndex+1:powerIndex]+expression[powerIndex]))) + expression[powerIndex:-1]
            self.__dbObject.update('tan')
        while expression.find("*") != -1:
            exponentIndex = expression.find("*")
            integerIndex = 0
            powerIndex = -1
            for i in range(exponentIndex - 1, -1, -1):
                if self.isInteger(expression[i]) or expression[i] == '.':
                    continue
                integerIndex = i + 1
            for i in range(exponentIndex + 1, len(expression), 1):
                if self.isInteger(expression[i]) or expression[i] == '.':
                    continue
                powerIndex = i
            expression = expression[0:integerIndex] + str(self.product([float(expression[integerIndex:exponentIndex]),float(expression[exponentIndex+1:powerIndex]+expression[powerIndex])])) + expression[powerIndex:-1]
        while expression.find("/") != -1:
            exponentIndex = expression.find("/")
            integerIndex = 0
            powerIndex = -1
            for i in range(exponentIndex - 1, -1, -1):
                if self.isInteger(expression[i]) or expression[i] == '.':
                    continue
                integerIndex = i + 1
            for i in range(exponentIndex + 1, len(expression), 1):
                if self.isInteger(expression[i]) or expression[i] == '.':
                    continue
                else:
                    powerIndex = i
                    break
            expression = expression[0:integerIndex] + str(self.divide(float(expression[integerIndex:exponentIndex]),float(expression[exponentIndex+1:powerIndex]+expression[powerIndex]))) + expression[powerIndex:-1]
        while expression.find("+") != -1:
            exponentIndex = expression.find("+")
            integerIndex = 0
            powerIndex = -1
            for i in range(exponentIndex - 1, -1, -1):
                if self.isInteger(expression[i]) or expression[i] == '.':
                    continue
                integerIndex = i + 1
            for i in range(exponentIndex + 1, len(expression), 1):
                if self.isInteger(expression[i]) or expression[i] == '.':
                    continue
                powerIndex = i
            expression = expression[0:integerIndex] + str(self.sum([float(expression[integerIndex:exponentIndex]),float(expression[exponentIndex+1:powerIndex]+expression[powerIndex])])) + expression[powerIndex:-1]
        while expression.find("-") != -1:
            exponentIndex = expression.find("-")
            integerIndex = 0
            powerIndex = -1
            for i in range(exponentIndex - 1, -1, -1):
                if self.isInteger(expression[i]) or expression[i] == '.':
                    continue
                integerIndex = i + 1
            for i in range(exponentIndex + 1, len(expression), 1):
                if self.isInteger(expression[i]) or expression[i] == '.':
                    continue
                powerIndex = i
            expression = expression[0:integerIndex] + str(self.sum([float(expression[integerIndex:exponentIndex]),-1 * float(expression[exponentIndex+1:powerIndex]+expression[powerIndex])])) + expression[powerIndex:-1]

        expression = round(float(expression),10)
        self.img = ImageTk.PhotoImage(Image.open(self.__adsObject.refresh(self.__dbObject)))
        self.canvas.create_image(600,200, image = self.img)
        return str(expression)
    def __init__(self,dbObject,adsObject,defaultTrig = False):
        self._defaultTrig = defaultTrig
        self.__dbObject = dbObject
        self.__adsObject = adsObject

        self.window = tk.Tk()
        self.window.title("Calculator.py")
        self.window.geometry("1500x1000")

        self.s = ThemedStyle(self.window)
        self.s.theme_use('equilux')
        self.window.config(bg='#464646')
        
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Overpass',15))
        self.style.configure('TLabel', font=('Overpass',20))

        self.mainLine = tk.StringVar()
        self.lineDisplay = ttk.Label(self.window,textvariable = self.mainLine).grid(row=0,column=4,columnspan=4,ipady=30)

        self.plus = ttk.Button(self.window,text='+',command= lambda: self.mainLine.set(self.mainLine.get()+'+')).grid(row=4,column=8,ipady=22,ipadx=8)
        self.minus = ttk.Button(self.window,text='-',command= lambda: self.mainLine.set(self.mainLine.get()+'-')).grid(row=3,column=8,ipady=22,ipadx=8)
        self.times = ttk.Button(self.window,text='*',command= lambda: self.mainLine.set(self.mainLine.get()+'*')).grid(row=2,column=8,ipady=22,ipadx=8)
        self.division = ttk.Button(self.window,text='/',command= lambda: self.mainLine.set(self.mainLine.get()+'/')).grid(row=1,column=8,ipady=22,ipadx=8)

        self.one = ttk.Button(self.window,text='1',command= lambda:self.mainLine.set(self.mainLine.get()+'1')).grid(row=3,column=5,ipady=22,ipadx=8)
        self.two = ttk.Button(self.window,text='2',command= lambda:self.mainLine.set(self.mainLine.get()+'2')).grid(row=3,column=6,ipady=22,ipadx=8)
        self.three = ttk.Button(self.window,text='3',command= lambda:self.mainLine.set(self.mainLine.get()+'3')).grid(row=3,column=7,ipady=22,ipadx=8)
        self.four = ttk.Button(self.window,text='4',command= lambda:self.mainLine.set(self.mainLine.get()+'4')).grid(row=2,column=5,ipady=22,ipadx=8)
        self.five = ttk.Button(self.window,text='5',command= lambda:self.mainLine.set(self.mainLine.get()+'5')).grid(row=2,column=6,ipady=22,ipadx=8)
        self.six = ttk.Button(self.window,text='6',command= lambda:self.mainLine.set(self.mainLine.get()+'6')).grid(row=2,column=7,ipady=22,ipadx=8)
        self.seven = ttk.Button(self.window,text='7',command= lambda:self.mainLine.set(self.mainLine.get()+'7')).grid(row=1,column=5,ipady=22,ipadx=8)
        self.eight = ttk.Button(self.window,text='8',command= lambda:self.mainLine.set(self.mainLine.get()+'8')).grid(row=1,column=6,ipady=22,ipadx=8)
        self.nine = ttk.Button(self.window,text='9',command= lambda:self.mainLine.set(self.mainLine.get()+'9')).grid(row=1,column=7,ipady=22,ipadx=8)
        self.zero = ttk.Button(self.window,text='0',command= lambda:self.mainLine.set(self.mainLine.get()+'0')).grid(row=4,column=5,ipady=22,ipadx=8)
        self.dot = ttk.Button(self.window,text='.',command= lambda:self.mainLine.set(self.mainLine.get()+'.')).grid(row=4,column=6,ipady=22,ipadx=8)

        self.ln = ttk.Button(self.window,text='ln',command= lambda:self.mainLine.set(self.mainLine.get()+'ln(')).grid(row=1,column=0,ipady=22,ipadx=8)
        self.log = ttk.Button(self.window,text='log',command= lambda:self.mainLine.set(self.mainLine.get()+'log(')).grid(row=1,column=1,ipady=22,ipadx=8)
        self.square = ttk.Button(self.window,text='^2',command= lambda:self.mainLine.set(self.mainLine.get()+'^2')).grid(row=1,column=2,ipady=22,ipadx=8)
        self.exponent = ttk.Button(self.window,text='^',command= lambda:self.mainLine.set(self.mainLine.get()+'^')).grid(row=1,column=3,ipady=22,ipadx=8)

        self.leftParen = ttk.Button(self.window,text='(',command= lambda:self.mainLine.set(self.mainLine.get()+'(')).grid(row=2,column=0,ipady=22,ipadx=8)
        self.rightParen = ttk.Button(self.window,text=')',command= lambda:self.mainLine.set(self.mainLine.get()+')')).grid(row=2,column=1,ipady=22,ipadx=8)
        self.sqrt = ttk.Button(self.window,text='sqrt',command= lambda:self.mainLine.set(self.mainLine.get()+'sqrt(')).grid(row=2,column=2,ipady=22,ipadx=8)
        self.abs = ttk.Button(self.window,text='abs',command= lambda:self.mainLine.set(self.mainLine.get()+'abs(')).grid(row=2,column=3,ipady=22,ipadx=8)

        self.sin = ttk.Button(self.window,text='sin',command= lambda:self.mainLine.set(self.mainLine.get()+'sin(')).grid(row=3,column=0,ipady=22,ipadx=8)
        self.cos = ttk.Button(self.window,text='cos',command= lambda:self.mainLine.set(self.mainLine.get()+'cos(')).grid(row=3,column=1,ipady=22,ipadx=8)
        self.tan = ttk.Button(self.window,text='tan',command= lambda:self.mainLine.set(self.mainLine.get()+'tan(')).grid(row=3,column=2,ipady=22,ipadx=8)
        self.e = ttk.Button(self.window,text='e',command= lambda:self.mainLine.set(self.mainLine.get()+'e')).grid(row=3,column=3,ipady=22,ipadx=8)

        self.csc = ttk.Button(self.window,text='arcsin',command= lambda:self.mainLine.set(self.mainLine.get()+'arcsin(')).grid(row=4,column=0,ipady=22,ipadx=8)
        self.sec = ttk.Button(self.window,text='arccos',command= lambda:self.mainLine.set(self.mainLine.get()+'arccos(')).grid(row=4,column=1,ipady=22,ipadx=8)
        self.cot = ttk.Button(self.window,text='arctan',command= lambda:self.mainLine.set(self.mainLine.get()+'arctan(')).grid(row=4,column=2,ipady=22,ipadx=8)
        self.pi = ttk.Button(self.window,text='π',command= lambda:self.mainLine.set(self.mainLine.get()+'π')).grid(row=4,column=3,ipady=22,ipadx=8)

        self.spacer = ttk.Label(self.window,textvariable = '',width=5).grid(row=1,column=4)

        self.backspace = ttk.Button(self.window,text='⌫',command= lambda: self.mainLine.set(self.mainLine.get().rstrip(self.mainLine.get()[-1]))).grid(row=3,column=9,columnspan=2,ipady=22,ipadx=16)
        self.equals = ttk.Button(self.window,text='Enter',command= lambda: self.mainLine.set(self.solve(self.mainLine.get()))).grid(row=4,column=9,columnspan=2,ipady=22,ipadx=16)
        self.clear = ttk.Button(self.window,text='CLEAR',command= lambda: self.mainLine.set('')).grid(row=1,column=9,columnspan=2,ipady=22,ipadx=16)

        self.trigSetting = tk.StringVar()
        self.trigSwitch()
        self.trigSwitch()
        self.trigButton = ttk.Button(self.window,textvariable=self.trigSetting,command= self.trigSwitch).grid(row=2,column=9,columnspan=2,ipady=22,ipadx=16)

        self.canvas = tk.Canvas(self.window,width=1200,height=400,bg='#464646')
        self.canvas.grid(row=5,column=0,columnspan=10)
        self.img = ImageTk.PhotoImage(Image.open(self.__adsObject.refresh(self.__dbObject)))
        self.canvas.create_image(600,200, image = self.img)

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()