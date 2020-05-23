#!/usr/bin/env python3
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn import metrics

def plant_classification():
    iris=load_iris()
    X = iris.data
    y = iris.target
    # print(X, y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, train_size=0.8)
    model = GaussianNB()
    model.fit(X_train, y_train)
    y_predicted = model.predict(X_test)
    return metrics.accuracy_score(y_test, y_predicted)

def main():
    print(f"Accuracy is {plant_classification()}")

if __name__ == "__main__":
    main()
