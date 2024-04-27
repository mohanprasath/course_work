# Import KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklear.model_selection import train_test_split

y = churn_df["churn"].values
X = churn_df[["account_length", "customer_service_calls"]].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=21, stratify=y)

# Create a KNN classifier with 6 neighbors
knn = KNeighborsClassifier(n_neighbors=6)

# Fit the classifier to the data
knn.fit(X, y)

# Predict the labels for the X_new
y_pred = knn.predict(X_new)

# Print the predictions
print("Predictions: {}".format(y_pred))