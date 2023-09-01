import os
import tkinter as tk
from tkinter import *



root= Tk()
root.title('Logistic Regression ')
root.geometry('400x450')
icon = PhotoImage(file="images/python.png")
root.iconphoto(False,icon)
root.configure()


import numpy as np
import pandas as pd



from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression


data = pd.read_csv('Preprocess_Data_Bankruptcy.csv')


def preprocess_inputs(df):
    df = data

    # Drop single-value column
    df = df.drop('id', axis=1)

    # Split df into X and y
    y = df['class']
    X = df.drop('class', axis=1)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, shuffle=True, random_state=42)

    # Scale X
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = pd.DataFrame(scaler.transform(X_train), index=X_train.index, columns=X_train.columns)
    X_test = pd.DataFrame(scaler.transform(X_test), index=X_test.index, columns=X_test.columns)

    return X_train, X_test, y_train, y_test

X_train, X_test, y_train, y_test = preprocess_inputs(data)

#canvas = tk.Canvas(root, height=200, width=200)
#canvas.pack()

background_image = tk.PhotoImage(file='images/lr.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

#frame = tk.Frame(root, bg='#80c1ff', bd=5)
#frame.place(relx=0.5, rely=0.4, relwidth=0.15, relheight=0.1, anchor='n')


button = tk.Button(root,text='Show Accuracy',font="System",activebackground="black",command=lambda:LR(),activeforeground="blue",bg ="green")
#button = tk.Button(frame, text="Show Accuracy", font="system", command=lambda:LR())
button.place(relx=0.35,rely= 0.3, relheight=0.1, relwidth=0.3)

lower_frame = tk.Frame(root, bd=10)
#lower_frame.place(relx=0.5, rely=0.4, relwidth=0.75, relheight=0.1, anchor='n')
lower_frame.place(relx=0.25, rely=0.6, relwidth=0.5, relheight=0.1)



def LR():
    Model = LogisticRegression(solver='lbfgs', max_iter=1000)
    Model.fit(X_train, y_train,)
    result = Model.score(X_test, y_test)
    #output= tk.Label(' Accuracy of LogisticRegression ' + ": {:.2f}%".format(result * 100))
    label = tk.Label(lower_frame)
    label.place(relwidth=1, relheight=1)
    res ="Accuracy" + "= {:.2f}%".format(result * 100)
    label.configure(text = res,font="system")



label1 = Label(root,text= "Click on Green Button for \n Accuracy of Logistic Regression ",font="System")
label1.place(relx=0.2, rely=0.1,relheight=0.1, relwidth=0.6)
#label = tk.Label(lower_frame)
#label.place(relwidth=1, relheight=1)
#label =tk.Label(lower_frame)
#label.place(relwidth=1, relheight=1)
#Label(root,text= " " font="System").place(x=450, y=300)

root.mainloop()