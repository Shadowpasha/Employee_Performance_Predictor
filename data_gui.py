import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar,DateEntry
from data import Performance_Predictor 
import numpy as np
from datetime import datetime

class Data_frame(ttk.Frame):
    def __init__(self, root):
        ttk.Frame.__init__(self, root)
        self.pack()
        self.gender_var = tk.StringVar()
        self.role_var = tk.StringVar()
        self.dep_var = tk.StringVar()
        self.salary_var = tk.IntVar()
        self.salary_var.set(2000)
        self.len_emp_var = tk.IntVar()
        self.len_emp_var.set(12)
        self.contract_end_var = tk.StringVar()
        self.predicted_var = tk.IntVar()
        self.PF = Performance_Predictor()

        self.gender_dict = {"Male":1,"Female":0}
        self.role_dict = {"Director":0,"Manager":2,"Executive":1,"Non-Executive":3}
        self.dep_dict = {"Strategic Communications (SC)":8,"CEO's Office":4,"Finance & Corporate Services (FCS)":6,"Special Projects (SP)":7,"Europe, Middle East & Africa (EMEA)":5,"Asia & Oceania (AO)":2,"Advisory & Ideation (AI)":0,"Americas":1,"Human Resources (HR)":4,"BonusKad Loyalty Sdn Bhd":3}


        # Gender
        label_gender = ttk.Label(self,text="Gender:")
        label_gender.grid(column=0,row=0,pady=30, padx=5)

        list_gender = ttk.Combobox(self,width=10,textvariable=self.gender_var)
        list_gender["values"] = ["Male","Female"]
        list_gender['state'] = 'readonly'
        list_gender.set("Male")
        list_gender.grid(column=1,row=0, padx=5)

        # Role
        label_role = ttk.Label(self,text="Role:")
        label_role.grid(column=4,row=0, padx=5)

        list_role = ttk.Combobox(self,width=16,textvariable=self.role_var)
        list_role["values"] = ['Non-Executive','Executive','Manager','Director']
        list_role['state'] = 'readonly'
        list_role.set('Non-Executive')
        list_role.grid(column=5,row=0, padx=5)

        # Department
        label_dep = ttk.Label(self,text="Department:")
        label_dep.grid(column=2,row=0,  padx=5)

        list_dep = ttk.Combobox(self,width=30,textvariable=self.dep_var)
        list_dep['values'] = ['Strategic Communications (SC)', "CEO's Office", 'Finance & Corporate Services (FCS)','Special Projects (SP)',"Europe, Middle East & Africa (EMEA)","Finance & Corporate Services (FCS)","Asia & Oceania (AO)","Americas","BonusKad Loyalty Sdn Bhd"]
        list_dep['state'] = 'readonly'
        list_dep.set("Strategic Communications (SC)")
        list_dep.grid(column=3,row=0, padx=5)

        # Salary
        label_salary = ttk.Label(self,text="Salary:")
        label_salary.grid(column=0,row=1,pady=30, padx=5)

        entry_salary = ttk.Entry(self, textvariable=self.salary_var, )
        entry_salary.grid(column=1,row=1, padx=5)

        # length Employment
        label_len_emp = ttk.Label(self,text="Employment Duration in Months:")
        label_len_emp.grid(column=2,row=1, padx=5)

        entry_len_emp = ttk.Entry(self,textvariable=self.len_emp_var)
        entry_len_emp.grid(column=3,row=1, padx=5)

        # Contract End
        label_contract_end = ttk.Label(self,text="Contract End (d/m/y)")
        label_contract_end.grid(column=4,row=1, padx=5)

        cal = DateEntry(self,textvariable=self.contract_end_var)
        cal.grid(column=5,row=1, padx=5)

        bt = ttk.Button(root, text = 'Predict',command=self.button_clicked, ) 
        bt.pack()

        frame2 = ttk.Frame(root, height=100,width=200)
        frame2.pack()

        label_predicted_title = ttk.Label(frame2,text="Predicted Perfromance:")
        label_predicted_title.grid(column=0,row=0)

        label_predicted = ttk.Label(frame2,textvariable= self.predicted_var)
        label_predicted.grid(column=1,row=0)


    def button_clicked(self):
        input =  np.array([ self.gender_dict[self.gender_var.get()], self.role_dict[self.role_var.get()], self.dep_dict[self.dep_var.get()],self.salary_var.get(),self.len_emp_var.get(),(datetime.strptime(self.contract_end_var.get(),"%m/%d/%y") - datetime.now()).days]).reshape(1, -1)
        output = self.PF.model_predict(input)
        self.predicted_var.set(str(output[0])+"/5")
    # print(output)
    # print([gender_dict[gender_var.get()],role_dict[role_var.get()],dep_dict[dep_var.get()],salary_var.get(),len_emp_var.get(),(datetime.strptime(contract_end_var.get(),"%m/%d/%y") - datetime.now()).days])

        # Predict
    