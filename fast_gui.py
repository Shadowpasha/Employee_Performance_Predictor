from fasthtml.common import *
from data import Performance_Predictor
from demo_data import Performance_Predictor as Performance_Predictor_demo
from datetime import datetime
import numpy as np

gender_dict = {"Male":1,"Female":0}
role_dict = {"Director":0,"Manager":2,"Executive":1,"Non-Executive":3}
dep_dict = {"Strategic Communications (SC)":8,"CEO's Office":4,"Finance & Corporate Services (FCS)":6,"Special Projects (SP)":7,"Europe, Middle East & Africa (EMEA)":5,"Asia & Oceania (AO)":2,"Advisory & Ideation (AI)":0,"Americas":1,"Human Resources (HR)":4,"BonusKad Loyalty Sdn Bhd":3}
edu_dict = {'Human Resources':0, 'Life Sciences':1, 'Marketing':2, 'Medical':3, 'Other':4, 'Technical Degree':5}
role_dict_demo = {'Business Analyst':0, 'Data Scientist':1, 'Delivery Manager':2, 'Developer':3, 'Finance Manager':4,
    'Healthcare Representative':5, 'Human Resources':6, 'Laboratory Technician':7, 'Manager':8, 'Manager R&D':9,
    'Manufacturing Director':10, 'Research Director':11, 'Research Scientist':12, 'Sales Executive':13, 'Sales Representative':14,
    'Senior Developer':15, 'Senior Manager R&D':16, 'Technical Architect':17, 'Technical Lead':18}
dep_dict_demo = {'Data Science':0, 'Development':1, 'Finance':2, 'Human Resources':3, 'Research & Development':4, 'Sales':5}
marital_dict = {'Divorced':0, 'Married':1, 'Single':2}
PF = Performance_Predictor()
PF_demo = Performance_Predictor_demo()

app,rt = fast_app()

def mk_opts(nm, cs):
    return (
        map(Option, cs))


@app.post('/submit_given')
def submit_given(d:dict):
    global gender_dict,role_dict,dep_dict, PF
    gender = gender_dict[d["gender"]]
    role = role_dict[d["role"]]
    dep = dep_dict[d["dep"]]
    num_days = (datetime.strptime(d["contact_end"],"%Y-%M-%d") - datetime.now()).days
    input = np.array([gender, role, dep,int(d["salary"]),int(d["len"]),num_days]).reshape(1, -1)
    output = PF.model_predict(input)
    return Div(H4("Predicted Performance: " + str(output[0])),id='progress_bar')

@app.post('/submit_demo')
def submit_demo(d:dict):
    global gender_dict,role_dict_demo,dep_dict_demo,marital_dict, edu_dict, PF_demo
    gender = gender_dict[d["gender"]]
    role = role_dict_demo[d["role"]]
    dep = dep_dict_demo[d["dep"]]
    edu = edu_dict[d["edu"]]
    marital = marital_dict[d["marital"]]
    input =  np.array([d["age"],gender,edu,marital,dep,role,d["salary"],d["numofcomp"],d["satisfaction"],d["work_life"],d["prom"],d["len"]]).reshape(1, -1)
    output = PF_demo.model_predict(input)
    return Div(H4("Predicted Performance: " + str(output[0])),id='progress_bar')

@rt('/demo_data')
def get(): return Title("Performance Predictor"),Div(
    Group(Titled(A("Given Data",href="/")),Titled(P('Demo Data'))),
    Form(
    Group( P("Age",style={"width":"400px"}),P("Marital Status",style={"width":"400px"})) ,
    Group(Input(name="age", type="number",id="age", value="30"),
    Select(*mk_opts('Marital', ['Single', 'Married', 'Divorced']),name='marital',id="marital")),
    Group( Label("Gender",style={"width":"400px"}),Label("Role",style={"width":"400px"})) ,
    Group(Select(*mk_opts('Gender', ["Male","Female"]),name='gender',id="gender"),
    Select(*mk_opts('Role',['Sales Executive', 'Manager', 'Developer', 'Sales Representative','Human Resources', 'Senior Developer', 'Data Scientist','Senior Manager R&D', 'Laboratory Technician', 'Manufacturing Director','Research Scientist', 'Healthcare Representative', 'Research Director','Manager R&D', 'Finance Manager', 'Technical Architect', 'Business Analyst','Technical Lead', 'Delivery Manager']),name='role',id="role")),
    Group(Label("Department",style={"width":"400px"}),Label("Education:")),
    Group(Select(*mk_opts('Department', ['Sales', 'Human Resources', 'Development', 'Data Science', 'Research & Development', 'Finance']),name='dep',id="dep"),
          Select(*mk_opts('Education', ['Marketing', 'Life Sciences', 'Human Resources', 'Medical', 'Other','Technical Degree']),name='edu',id="edu")),
    Group(Label("Hourly Rate",style={"width":"400px"}), Label("No. of Previous Companies",style={"width":"400px"})),
    Group(Input(name="salary", type="number", id="salary",value="20"),
    Input(name="numofcomp", type="number",id="numofcomp", value="3")),
    Group(Label("Years of Experience:",style={"width":"400px"}),Label("Years Since Last Promotion",style={"width":"400px"})),
    Group(Input( type="number",id="len",name="len", value="5"),
          Input(id="prom",name="prom", type="number",value="1")),
    Group(Label("Satisfaction (1-5)",style={"width":"400px"}),Label("Work Life Balance (1-5)",style={"width":"400px"})),
    Group(Input(id="satisfaction",name="satisfaction", type="number", value="3"),
          Input(id="work_life",name="work_life", type="number",value="2")),
    Button("Predict Performance",type="submit")
    ,post="submit_demo",hx_target="#progress_bar"),
    Div(H4("Predicted Performance:"),id='progress_bar')
    ,style={"width":"800px","margin-left":"auto","margin-right":"auto"})

@rt('/')
def get(): return Title("Performance Predictor"),Div(
    Group(Titled(P('Given Data')),
    Titled(A("Demo Data",href="/demo_data"))),
    Form(
    Group( Label("Gender"),Label("Role")) ,
    Group(Select(*mk_opts('Gender', ["Male","Female"]),name='gender',id="gender"),
    Select(*mk_opts('Role', ['Non-Executive','Executive','Manager','Director']),name='role',id="role")),
    Label("Department"),
    Select(*mk_opts('Department', ['Strategic Communications (SC)', "CEO's Office", 'Finance & Corporate Services (FCS)','Special Projects (SP)',"Europe, Middle East & Africa (EMEA)","Finance & Corporate Services (FCS)","Asia & Oceania (AO)","Americas","BonusKad Loyalty Sdn Bhd"]),name='dep',id="dep"),
    Label("Salary"),
    Input(name="salary", type="number", value = "5000",id="salary"),
    Label("Length of Employement in Months"),
    Input( type="number", value = "40",id="len",name="len"),
    Label("Contract End Date"),
    Input(type="date",id="contact_end",name="contact_end",value="2025-04-08"),
    Button("Predict Performance",type="submit")
    ,post="submit_given",hx_target="#progress_bar"),
    Div(H4("Predicted Performance:"),id='progress_bar')
    ,style={"width":"800px","margin-left":"auto","margin-right":"auto"})

serve()