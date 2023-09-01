

import numpy as np
import pandas as pd



from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#from sklearn.linear_model import LogisticRegression
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

def LR():
    Model = LogisticRegression(solver='lbfgs', max_iter=1000)
    Model.fit(X_train, y_train,)
    result = Model.score(X_test, y_test)
    print(' Accuracy of LogisticRegression ' + ": {:.2f}%".format(result * 100))


LR()