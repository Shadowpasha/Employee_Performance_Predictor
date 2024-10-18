import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.neural_network import MLPClassifier
from datetime import datetime
import numpy as np
from pickle import dump, load


class Performance_Predictor():
  def __init__(self):
    self.data = pd.read_excel("./investKL Dataset.xls")

    # print(self.data.columns)

    self.enc = LabelEncoder()
    for i in (0,1,2):
        self.data.iloc[:,i] = self.enc.fit_transform(self.data.iloc[:,i])

    # print(self.data.iloc[:,4])

    end_dates = self.data["Contract End"].to_list()
    for i in range(len(end_dates)):
        if type(end_dates[i])  != datetime:
            end_dates[i] = end_dates[i].strip()
            end_dates[i] = datetime.strptime(end_dates[i],"%d/%m/%Y")

    time_difference = []
    for i in range(len(end_dates)):
        time_difference.append((end_dates[i] - datetime.now()).days)
    self.data["Contract End"] = time_difference

    y = self.data["Performance"]
    X = self.data.iloc[:,0:6]
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=10)
    self.sc = StandardScaler()
    X_train = self.sc.fit_transform(X_train.values)
    X_test = self.sc.transform(X_test.values)
    # print(X_test[0])

    # self.model_mlp = MLPClassifier(hidden_layer_sizes=(128,128,128),learning_rate_init=0.01,max_iter=1000,random_state=10)
    # self.model_mlp.fit(X_train,y_train)
    with open("data.pkl", "rb") as f:
      self.model_mlp = load(f)
    y_predict_mlp = self.model_mlp.predict(X_test) 
    # with open("data.pkl", "wb") as f:
    #   dump(self.model_mlp, f, protocol=5)
    # print(accuracy_score(y_test,y_predict_mlp))

  def model_predict(self, value_array):
    #  print(value_array)
     value_array = self.sc.transform(value_array)
     y = self.model_mlp.predict(value_array)
    #  print(y)
     return y


# x = np.array([0,0,0,1000,10,160]).reshape(1, -1)
# y_predict_mlp = model_mlp.predict(x)
# y_predict_mlp = model_mlp.predict(X_test)
# print(y_predict_mlp)
# print(accuracy_score(y_test,y_predict_mlp))
# print(classification_report(y_test,y_predict_mlp))

