import tkinter as tk
from tkinter.font import Font 
from tkinter import messagebox as tkMsgBox
from tkinter import constants as const
from tkinter import StringVar
import configparser
import math
import os
import sys
from pathlib import Path

from Modules import PyMath as Calc
from Modules.TkMenus.help import HelpMenu
from Modules import FileOperations as FileOp

ConfigPath = Path("Configs/PyCalc.ini")

Config = configparser.ConfigParser()
Config.read(ConfigPath)

def ConfigWrite():
    with open(ConfigPath, "w") as configfile:
        Config.write(configfile)

class TKWindow:
    def __init__(self, SizeXmin =500, SizeYmin=400, SizeXmax = 900, SizeYmax = 800, FontFamily = 'helvetica'):
        """
        Size min inputs set the minimum size that the window can shrink to. 
        Size max inputs set the maximum size that the window can grow to.
        """

        self.Master = tk.Tk(screenName="PyCalc",)
        self.myFont = Font(family=FontFamily, size = 12)
        self.Master.minsize(SizeXmin,SizeYmin)
        self.Master.maxsize(SizeXmax, SizeYmax)

        rows = 0
        while rows < 50:
            self.Master.rowconfigure(rows, weight=1)
            self.Master.columnconfigure(rows,weight=1)
            rows += 1
        del rows

        self.StartingRow = 2
        self.A = []
        self.B = []
        self.DeleteAble = []
        self.IsRemovable = True
        self.InputList = []
        self.InputIndex = 0

        if(Config.getboolean("Booleans", "firsttime") == True):
            tk.messagebox.showwarning("Warning", message ="PyCalc does not function as a standard calculator! This message will not show again.")
            Config.set("Booleans", "firsttime", "False")
            ConfigWrite()
        
        self.List = []

        self.BuildEntry()
    
    #Builds the Main Menu
    def BuildEntry(self):
        for child in self.Master.winfo_children():
            child.destroy()

        self.InputRow = 2
        self.B.clear()
        self.DeleteAble.clear()
        self.InputList.clear()
        self.InputIndex = 0
        
        self.A.clear()
        self.A.append(tk.Button(self.Master, text="Statistics", command= self.BuildStatisticMenu))

        self.A.append(tk.Button(self.Master, text="Permute", command=self.BuildPermMenu))

        self.A.append(tk.Button(self.Master, text="Combonation", command=self.BuildComboMenu))
    
        self.A.append(tk.Button(self.Master, text="Help", command=self.HelpMenu))
        for i in self.A:
            i.pack(side=const.TOP, padx=10, pady=5)

    #Builds the Help Menu
    def HelpMenu(self):
        for child in self.Master.winfo_children():
            child.destroy()
        self.A.clear()

        HelpMenu(self.Master, self)

    #Resets first time bools
    def Reset(self):
        print("I am reseting")
        if Config.getboolean("Booleans", "firsttime") == False:
            Config.set("Booleans", "firsttime", "True")
            ConfigWrite()

    #Builds the Statistics menu
    def BuildStatisticMenu(self):
        for child in self.Master.winfo_children():
            child.destroy()
        self.A.clear()
        self.A.append(tk.Button(self.Master, text = "Return", command= self.BuildEntry))
        self.A[-1].grid(row=0, column=1)

        EntryWidget = (tk.Entry(self.Master))
        EntryWidget.grid(row= 1, column=1)
        EntryWidget.focus_set()

        self.A.append(tk.Button(self.Master, text = "Clear", command = lambda: self.StatClear(EntryWidget)))
        self.A[-1].grid(row = 0, column = 2)

        self.A.append(tk.Button(self.Master, text="Add", command= lambda: self.AddInput(EntryWidget.get(), EntryWidget ,IsRemovable=True)))
        self.A[-1].grid(row=1, column=2)

        self.A.append(tk.Button(self.Master, text = "Calculate", command =lambda: self.CalculateStatistics(EntryWidget)))
        self.A[-1].grid(row = 1, column = 4)

    #Builds the Permutations menu
    def BuildPermMenu(self):
        for child in self.Master.winfo_children():
            child.destroy()
        self.A.clear()
        IsNumber = StringVar()

        self.A.append(tk.Button(self.Master, text = "Return", command= self.BuildEntry))
        self.A[-1].grid(row=0, column=1)

        self.A.append(tk.Checkbutton(self.Master, text = "If you want to permute the digits\n and not the number, Check this box", variable = IsNumber, onvalue="IsString", offvalue = 'IsNumber'))
        self.A[-1].grid(row = 3, column = 1)
        self.A[-1].deselect()
        
        EntryWidget = (tk.Entry(self.Master))
        EntryWidget.grid(row= 1, column=1)
        EntryWidget.focus_set()

        EntryWidgetSpots = tk.Entry(self.Master)
        EntryWidgetSpots.grid(row= 2, column=1)
        EntryWidgetSpots.insert(const.INSERT, 'Spots/Places (Optional)')

        self.A.append(tk.Button(self.Master, text = "Calculate", command = lambda: self.CalculatePerm(EntryWidget.get(), EntryWidgetSpots.get(),  IsNumber.get())))
        self.A[-1].grid(row = 1, column = 2)

    #Builds the Combonation menu
    def BuildComboMenu(self):
        for child in self.Master.winfo_children():
            child.destroy()
        self.A.clear()
        
        self.A.append(tk.Button(self.Master, text = "Return", command= self.BuildEntry))
        self.A[-1].grid(row=0, column=1)

        self.A.append(tk.Label(self.Master, text = "Options"))
        self.A[-1].grid(row = 1, column = 0)

        self.A.append(tk.Label(self.Master, text = "Spots"))
        self.A[-1].grid(row = 2, column = 0)

        EntryInput = tk.Entry(self.Master)
        EntryInput.grid(row = 1, column = 1)


        EntrySpots = tk.Entry(self.Master)
        EntrySpots.grid(row = 2, column = 1)

        self.A.append(tk.Button(self.Master, text = "Calculate", command = lambda: self.CalculateCombo(EntryInput.get(), EntrySpots.get())))
        self.A[-1].grid(row = 1, column = 2)

        self.A.append(tk.Checkbutton(self.Master, text = "If there a limited\nnumber of spots\nCheck this box", onvalue = "Limited", offvalue = "Same"))
        self.A[-1].grid(row = 2, column = 2)
        self.A[-1].select()

    #Adds a User Input label to show what they have inputed, and, if IsRemovable is equal to true, puts a button that allows the uset to remove the input
    def AddInput(self, Input, Entry,IsRemovable = False):
        try:
            self.InputList.append(Input)
        except ValueError:
            print("there is a value error in AddInput")
        try:
            Input = str(Input)
        except ValueError:
            print("all is well")
            
        Entry.delete(0, const.END)

        self.DeleteAble.append(AddInputButton(self.Master, Input, self.InputRow, self.InputIndex, self, self.IsRemovable))
        self.InputIndex += 1
        self.InputRow += 1
    
    def StatClear(self, Entry):
        for i in self.DeleteAble:
            i.DestroySelf()
        Entry.delete(0, "end")
        self.InputList.clear()
        self.InputIndex = 0
        self.InputRow = self.StartingRow

    #Is called by AddInput, and removes the label and button, and sets the entered index to 0
    def RemoveInput(self, IndexNumber):
        self.InputList[IndexNumber] = 0
    
    #Calculates and Builds labels for all of the statistic calculation
    def CalculateStatistics(self, Entry):
        Entry.delete(0, const.END)
        
        if len(self.InputList) == 1:
            self.A.append(tk.messagebox.showerror("Not Enough Inputs", "You did't put enough numbers!\n please return and input more"))
            return
        
        StatInputs = []
        Stats = []
        for i in self.InputList:
            if i != 0:
                StatInputs.append(int(i))

        StatInputs.sort()

        Stats.append("Average: " + str(Calc.Average(StatInputs)))
        Stats.append("Median: " + str(Calc.Median(StatInputs)))
        Stats.append("Standard Deviation: " + str(Calc.StandardDeviation(StatInputs)))
        StatCount = Calc.Count(StatInputs)
        
        self.DeleteAble.append(PrintStatistics(self.Master, Stats, 2, 7, StatCount))

    #Calculates and Builds labels for all of the Permutation Inputs
    def CalculatePerm(self, Input, Spots, IsString):
        if IsString == "IsNumber":
            try:
                Input = int(Input)
            except ValueError:
                temp = [str(Input) + " = " + str(Calc.PermuteString(Input))]
                self.DeleteAble.append(AddOutput(self.Master, temp, self.StartingRow + len(self.B), "Perm"))
                del temp
                return
            try:
                Spots = int(Spots)
            except ValueError:
                if isinstance(Input, int):
                    Spots = Input
                else:
                    Spots = len(Input)
            temp = [str(Input) + " = " + str(Calc.Permute(int(Input), int(Spots)))]
            self.DeleteAble.append(AddOutput(self.Master, temp, self.StartingRow + len(self.B), "Perm"))
        else:
            temp = [str(Input) + " = " + str(Calc.PermuteString(Input))]
            self.DeleteAble.append(AddOutput(self.Master, temp, self.StartingRow + len(self.DeleteAble), "Perm"))
        del temp

    def CalculateCombo(self, Input, Spots):
        ComboOut = Calc.Combination(int(Input), int(Spots))
        combList = []

        combList.append("Combonation Result")
        combList.append(Input + " & "+ Spots + " Spots")
        combList.append(ComboOut)

        self.DeleteAble.append(AddOutput(self.Master, combList, self.StartingRow, "Combo"))

    #is a placeholder command
    def SayHi(self):
        print("hi")

class AddOutput:
    def __init__(self, Master, LabelText, StartingRow, Type, Column = 7):
        Row = StartingRow
        self.DestroyList = []
        dL = self.DestroyList

        loopNum = 0

        while loopNum < len(LabelText):
            dL.append(tk.Label(Master, text = LabelText[loopNum]))
            dL[-1].grid(row = Row, column = Column)
            Row += 1
            loopNum += 1

        dL.append(tk.Button(Master, text="Clear Calculation", command = self.DestroySelf))
        dL[-1].grid(row = Row, column = Column)
        Row += 1

        dL.append(tk.Button(Master, text = "Save to txt File", command = lambda: FileOp.SaveToFile(LabelText, Type, 'Time', Config.get("Output", "outputfolder"))))
        dL[-1].grid(row = Row , column = Column)

        self.DestroyList = dL
        
    def DestroySelf(self):
        for i in self.DestroyList:
            i.destroy()

#Builds the label, destroy button, and index, for the associated input
class AddInputButton:
    def __init__(self, Master ,LabelText, InputRow, IndexNum, ParentClass, IsRemovable = False):
        self.IndexNum = IndexNum
        self.ParentClass = ParentClass
        self.DestroyList = []

        self.DestroyList.append(tk.Label(Master, text = LabelText))
        self.DestroyList[-1].grid(row=InputRow, column = 1)

        if IsRemovable == True:
            self.DestroyList.append(tk.Button(Master, text="X", command = lambda: self.DestroySelf()))
            self.DestroyList[-1].grid(row = self.DestroyList[-2].grid(), column = 2)

    def DestroySelf(self):
        for i in self.DestroyList:
            i.destroy()
        self.ParentClass.RemoveInput(self.IndexNum)

#Is called to build removable labels for all of the statistic outputs
class PrintStatistics:
    def __init__(self, Master, LabelText, StartingRow, Column, StatisticOutput = []):
        self.LabelList = []
        """
        Takes LabelText and makes a label with the string contained in each index.\n
        It then takes a two-dimensional list, StatisticOutput, and prints its memberes side by side. 
        """
        Row=StartingRow
        LoopNum = 0

        while LoopNum < len(LabelText):
            self.LabelList.append(tk.Label(Master, text = LabelText[LoopNum]))
            self.LabelList[-1].grid(row=Row, column=Column)
            Row += 1
            LoopNum +=1

        if len(StatisticOutput) > 0  :
            self.LabelList.append(tk.Label(Master, text = " x:y means that x appeared y times"))
            self.LabelList[-1].grid(row = Row, column = Column)
            Row +=1
            LoopNum = 0
            while LoopNum < len(StatisticOutput[0]):
                a = StatisticOutput[0][LoopNum]
                b = StatisticOutput[1][LoopNum]
                self.LabelList.append(tk.Label(Master, text = str(a) + ":" + str(b)))
                self.LabelList[-1].grid(row = Row, column = Column)
                Row += 1
                del a, b
                LoopNum +=1

        self.LabelList.append(tk.Button(Master, text="Clear Calculation", command = self.DestroySelf))
        self.LabelList[-1].grid(row = Row, column = Column)
        Row += 1

        self.LabelList.append(tk.Button(Master, text = "Save to txt File", command = lambda: FileOp.SaveToFile(LabelText, "Stat")))
        self.LabelList[-1].grid(row = Row , column = Column)

    def DestroySelf(self):
        for i in self.LabelList:
            i.destroy()

#Is called by permMenu to print the removable labels that display the input and the permutation.
class AddResult:
    def __init__(self, Master, LabelText, StartingRow, Column, LabelInput = False, InputString = ''):
        self.LabelList = []
        """
        Takes the inputs, and makes a label that displays 'LabelText' and has a remove function.
        """

        self.LabelList.append(tk.Label(Master, text = LabelText))
        self.LabelList[-1].grid(row = StartingRow, column = Column)

        self.LabelList.append(tk.Button(Master, text = "Clear", command = self.Destroy))
        self.LabelList[-1].grid(row = StartingRow, column = Column + 1)

        if LabelInput == True:
            self.LabelList.append(tk.Label(Master, text = InputString))
            self.LabelList[-1].grid(row = StartingRow, column = Column - 1)

    def Destroy(self):
        for i in self.LabelList:
            i.destroy()

Window = TKWindow()

Window.Master.mainloop()
