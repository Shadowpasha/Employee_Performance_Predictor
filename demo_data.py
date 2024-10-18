import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from pickle import dump, load


class Performance_Predictor():
    def __init__(self):
        data = pd.read_excel("./INX_Future_Inc_Employee_Performance_CDS_Project2_Data_V1.8.xls")

        # print(sorted(data["EmpJobRole"].unique()))
        # print(data.columns)

        self.enc = LabelEncoder()
        for i in (1,2,3,4,5):
            data.iloc[:,i] = self.enc.fit_transform(data.iloc[:,i])

        # print(data.head())
        # print(data.corr())

        y = data.PerformanceRating
        X = data.iloc[:,0:12]
        X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=10)
        self.sc = StandardScaler()
        X_train = self.sc.fit_transform(X_train.values)
        X_test = self.sc.transform(X_test.values)
        

        # self.model_mlp = MLPClassifier(hidden_layer_sizes=(60,60,60),learning_rate_init=0.01,max_iter=250,random_state=42)
        # self.model_mlp.fit(X_train,y_train)
        with open("demo_data.pkl", "rb") as f:
            self.model_mlp = load(f)
        y_predict_mlp = self.model_mlp.predict(X_test)

        # with open("demo_data.pkl", "wb") as f:
        #     dump(self.model_mlp, f, protocol=5)
        # print(accuracy_score(y_test,y_predict_mlp))

        # self.rbf_svc = SVC(kernel='rbf', C=100, random_state=10).fit(X_train,y_train)
        # y_predict_svm = self.rbf_svc.predict(X_test)
        # print(accuracy_score(y_test,y_predict_svm))

    def model_predict(self, value_array):
    #  print(value_array)
     value_array = self.sc.transform(value_array)
     y = self.model_mlp.predict(value_array)
    #  print(y)
     return y
# 
# y_predict_mlp = model_mlp.predict(X_test)
# print(accuracy_score(y_test,y_predict_mlp))
# print(classification_report(y_test,y_predict_mlp))