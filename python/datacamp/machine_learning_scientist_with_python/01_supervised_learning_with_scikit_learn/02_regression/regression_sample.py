import pandas as pd
import matplotlib.pyplot as plt

diabetes_df = pd.read_csv('diabetes_clean.csv')
print(diabetes_df.head())
print(diabetes_df.info())

X = diabetes_df.drop("glucose", axis=1).values
y = diabetes_df["glucose"].values
print(type(X), type(y))

# trying to predict diabetes with only one variable
X_bmi = X[:, 4]
# print(y.shape, X_bmi.shape)
# we need 2D array for sklearn
X_bmi = X_bmi.reshape(-1, 1)
# print(y.shape, X_bmi.shape)
# see how bmi looks when plotted
# print(y, X_bmi)
plt.scatter(X_bmi, y)
plt.ylabel('Blood Glucose (mg/dl)')
plt.xlabel('Body Mass Index')
plt.show()

from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(X_bmi, y)
predictions = reg.predict(X_bmi)
plt.scatter(X_bmi, y)
plt.scatter(X_bmi, predictions)
plt.ylabel('Blood Glucose (mg/dl)')
plt.xlabel('Body Mass Index')
plt.show()