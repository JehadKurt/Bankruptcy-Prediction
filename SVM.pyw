
import os
import tkinter as tk
from tkinter import *
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import  SVC

root= Tk()
root.title('Support Vector Machine Classifier ')
root.geometry('400x450')
icon = PhotoImage(file="images/python.png")
root.iconphoto(False,icon)



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

background_image = tk.PhotoImage(file='images/svc1.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

#rame = tk.Frame(root, bg='#80c1ff', bd=5)
#rame.place(relx=0.5, rely=0.15, relwidth=0.75, relheight=0.3, anchor='n')

# = tk.Entry(frame, font=40)
#entry.place(relwidth=0.65, relheight=1)

button = tk.Button(root,text='Show Accuracy',font="System",activebackground="black",command=lambda:SVM(),activeforeground="blue",bg ="blue")
#utton = tk.Button(frame, text="Show Accuracy", font="system", command=lambda:SVM())
button.place(relx=0.35,rely= 0.3, relheight=0.1, relwidth=0.3)

lower_frame = tk.Frame(root, bd=10)
#lower_frame.place(relx=0.5, rely=0.4, relwidth=0.75, relheight=0.1, anchor='n')
lower_frame.place(relx=0.25, rely=0.6, relwidth=0.5, relheight=0.1)

def SVM():
    Model = SVC()
    Model.fit(X_train, y_train)
    result = Model.score(X_test, y_test)
    #print(' Accuracy of Support Vector Machine ' + ": {:.2f}%".format(result * 100))
    label = tk.Label(lower_frame)
    label.place(relwidth=1, relheight=1)
    res ="Accuracy" + "= {:.2f}%".format(result * 100)
    label.configure(text = res,font="system")



label1 = Label(root,text= "Click on Blue Button for\n Accuracy of Support Vector Machine ",font="System")
label1.place(relx=0.15, rely=0.1,relheight=0.1, relwidth=0.7)
root.mainloop()