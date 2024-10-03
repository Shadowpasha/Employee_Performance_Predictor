import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar,DateEntry
import numpy as np
from datetime import datetime
from demo_data import Performance_Predictor

class Data_frame(ttk.Frame):
    def __init__(self, root):
        ttk.Frame.__init__(self, root)
        self.pack()
        self.age_var = tk.IntVar()
        self.age_var.set(25)
        self.gender_var = tk.StringVar()
        self.role_var = tk.StringVar()
        self.dep_var = tk.StringVar()
        self.edu_var = tk.StringVar()
        self.marital_var = tk.StringVar()

        self.salary_var = tk.IntVar()
        self.salary_var.set(35)
        self.len_emp_var = tk.IntVar()
        self.len_emp_var.set(2)
        self.sats_var = tk.IntVar()
        self.sats_var.set(2)
        self.num_comp_var = tk.IntVar()
        self.num_comp_var.set(1)
        self.work_life_var = tk.IntVar()
        self.work_life_var.set(3)
        self.year_since_var = tk.IntVar()
        self.year_since_var.set(1)
        self.predicted_var = tk.IntVar()
        

        self.PF = Performance_Predictor()

        self.gender_dict = {"Male":1,"Female":0}
        self.edu_dict = {'Human Resources':0, 'Life Sciences':1, 'Marketing':2, 'Medical':3, 'Other':4, 'Technical Degree':5}
        self.role_dict = {'Business Analyst':0, 'Data Scientist':1, 'Delivery Manager':2, 'Developer':3, 'Finance Manager':4,
            'Healthcare Representative':5, 'Human Resources':6, 'Laboratory Technician':7, 'Manager':8, 'Manager R&D':9,
            'Manufacturing Director':10, 'Research Director':11, 'Research Scientist':12, 'Sales Executive':13, 'Sales Representative':14,
            'Senior Developer':15, 'Senior Manager R&D':16, 'Technical Architect':17, 'Technical Lead':18}
        self.dep_dict = {'Data Science':0, 'Development':1, 'Finance':2, 'Human Resources':3, 'Research & Development':4, 'Sales':5}
        self.marital_dict = {'Divorced':0, 'Married':1, 'Single':2}

        #Age
        label_gender = ttk.Label(self,text="Age:")
        label_gender.grid(column=0,row=0,pady=10, padx=5)

        entry_age = ttk.Entry(self, textvariable=self.age_var)
        entry_age.grid(column=1,row=0, padx=5)

        # Gender
        label_gender = ttk.Label(self,text="Gender:")
        label_gender.grid(column=2,row=0,pady=10, padx=5)

        list_gender = ttk.Combobox(self,width=10,textvariable=self.gender_var)
        list_gender["values"] = ["Male","Female"]
        list_gender['state'] = 'readonly'
        list_gender.set("Male")
        list_gender.grid(column=3,row=0, padx=5,pady=10)

        # Edu
        label_edu = ttk.Label(self,text="Education Background:")
        label_edu.grid(column=0,row=1, padx=5,pady=10)

        list_edu = ttk.Combobox(self,width=16,textvariable=self.edu_var)
        list_edu["values"] = ['Marketing', 'Life Sciences', 'Human Resources', 'Medical', 'Other','Technical Degree']
        list_edu['state'] = 'readonly'
        list_edu.set('Marketing')
        list_edu.grid(column=1,row=1, padx=5,pady=10)

        # Marital
        label_martial = ttk.Label(self,text="Marital Status:")
        label_martial.grid(column=2,row=1,  padx=5,pady=10)

        list_martial = ttk.Combobox(self,width=30,textvariable=self.marital_var)
        list_martial['values'] = ['Single', 'Married', 'Divorced']
        list_martial['state'] = 'readonly'
        list_martial.set("Single")
        list_martial.grid(column=3,row=1, padx=5,pady=10)

        # Department
        label_dep = ttk.Label(self,text="Department:")
        label_dep.grid(column=0,row=2,  padx=5,pady=10)

        list_dep = ttk.Combobox(self,width=30,textvariable=self.dep_var)
        list_dep['values'] = ['Sales', 'Human Resources', 'Development', 'Data Science', 'Research & Development', 'Finance']
        list_dep['state'] = 'readonly'
        list_dep.set("Sales")
        list_dep.grid(column=1,row=2, padx=5,pady=10)

        # Role
        label_role = ttk.Label(self,text="Role:")
        label_role.grid(column=2,row=2,  padx=5,pady=10)

        list_role = ttk.Combobox(self,width=30,textvariable=self.role_var)
        list_role['values'] = ['Sales Executive', 'Manager', 'Developer', 'Sales Representative','Human Resources', 'Senior Developer', 'Data Scientist','Senior Manager R&D', 'Laboratory Technician', 'Manufacturing Director','Research Scientist', 'Healthcare Representative', 'Research Director','Manager R&D', 'Finance Manager', 'Technical Architect', 'Business Analyst','Technical Lead', 'Delivery Manager']
        list_role['state'] = 'readonly'
        list_role.set("Sales Executive")
        list_role.grid(column=3,row=2, padx=5,pady=10)

        # Salary
        label_salary = ttk.Label(self,text="Hourly Rate:")
        label_salary.grid(column=0,row=3,pady=10, padx=5)

        entry_salary = ttk.Entry(self, textvariable=self.salary_var)
        entry_salary.grid(column=1,row=3, padx=5,pady=10)

        # Num of Companies
        label_numcom = ttk.Label(self,text="No. Previous Companies")
        label_numcom.grid(column=2,row=3, padx=5,pady=10)

        entry_numcom = ttk.Entry(self, textvariable=self.num_comp_var)
        entry_numcom.grid(column=3,row=3, padx=5,pady=10)

        # Satisfaction
        label_sats = ttk.Label(self,text="Employee Satisfaction(1-5)")
        label_sats.grid(column=0,row=4, padx=5,pady=10)

        entry_sats = ttk.Entry(self, textvariable=self.sats_var)
        entry_sats.grid(column=1,row=4, padx=5,pady=10)

        # life_bal
        label_life_bal = ttk.Label(self,text="Work-Life Balance(1-5)")
        label_life_bal.grid(column=2,row=4, padx=5,pady=10)

        entry_life_bal = ttk.Entry(self, textvariable=self.work_life_var)
        entry_life_bal.grid(column=3,row=4, padx=5,pady=10)

        # prom
        label_prom = ttk.Label(self,text="Years since Last Promotion")
        label_prom.grid(column=0,row=5, padx=5,pady=10)

        entry_prom = ttk.Entry(self, textvariable=self.year_since_var)
        entry_prom.grid(column=1,row=5, padx=5,pady=10)

        # length Employment
        label_len_emp = ttk.Label(self,text="Years of Experience:")
        label_len_emp.grid(column=2,row=5, padx=5,pady=10)

        entry_len_emp = ttk.Entry(self,textvariable=self.len_emp_var)
        entry_len_emp.grid(column=3,row=5, padx=5,pady=10)

        # Predict
        bt = ttk.Button(root, text = 'Predict',command=self.button_clicked, ) 
        bt.pack()

        frame2 = ttk.Frame(root, height=100,width=200)
        frame2.pack()

        label_predicted_title = ttk.Label(frame2,text="Predicted Perfromance:")
        label_predicted_title.grid(column=0,row=0)

        label_predicted = ttk.Label(frame2,textvariable=self.predicted_var)
        label_predicted.grid(column=1,row=0)

    def button_clicked(self):
        global gender_var, role_var, dep_var, salary_var, len_emp_var, contract_end_var
        input =  np.array([self.age_var.get(),self.gender_dict[self.gender_var.get()],self.edu_dict[self.edu_var.get()],self.marital_dict[self.marital_var.get()],self.dep_dict[self.dep_var.get()],self.role_dict[self.role_var.get()],self.salary_var.get(),self.num_comp_var.get(),self.sats_var.get(),self.work_life_var.get(),self.year_since_var.get(),self.len_emp_var.get()]).reshape(1, -1)
        output = self.PF.model_predict(input)
        self.predicted_var.set(str(output[0])+"/5")
    # print(output)
    # print([gender_dict[gender_var.get()],role_dict[role_var.get()],dep_dict[dep_var.get()],salary_var.get(),len_emp_var.get(),(datetime.strptime(contract_end_var.get(),"%m/%d/%y") - datetime.now()).days])


