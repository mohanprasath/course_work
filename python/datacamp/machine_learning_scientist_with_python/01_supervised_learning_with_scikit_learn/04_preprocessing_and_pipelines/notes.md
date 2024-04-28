# Notes

- Dealing with category values
- dummy variables - ex: genre from rows to columns
- OneHotEncoder() from sklearn or from pandas get_dummies()
- music dataset

## missing values

- removing missing values is a long shot approach
- fill the missing values by mean or median or mode
- data leakage - 
- from sklearn.impute import SimpleImputer
- imputers are transformers
- Pipeline shortens the process here

## data

- check if the data is varying ie for knn check the distance between data points
- scale or center the data ie standardize the data
  - subtract the mean and divide by variance
  - from sklearn.preprocessing import StandardScalar
  - 