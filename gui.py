import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar,DateEntry
from data import Performance_Predictor as PF
from demo_data import Performance_Predictor as PF_demo
from datetime import datetime
import numpy as np
from data_gui import Data_frame as DF
from demo_data_gui import Data_frame as DF_Demo

PF = PF()
PF_demo = PF_demo()

root = tk.Tk()
style = ttk.Style(root)
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "dark")

root.title("Employee Performance Predictor")
root.geometry("950x450")
root.resizable(False,False)

tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Given Data')
tabControl.add(tab2, text='Demo Data')
tabControl.pack(expand=1, fill="both")

df = DF(tab1)
df2 = DF_Demo(tab2)


root.mainloop()