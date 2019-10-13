# Datacamp R Programming Series
# Course 1 Introduction to R

# numeric computation
# without variables
print(3 + 4)
print(2 - 1)
print(9 * 3)
print(9 / 3)
print(9 %% 3)
# with variables
x = 3 + 4 # assignment style 1
print(x)
x <- 3 + 4 # assignment style 2
print(x)

# Vectors
y = c(3, 5, 6, 7)
names(y) = c('column_1', 'column_2', 'column_3', 'column_4') # assigning column names for each variables in the vector
print(y) 
print(sum(y)) # sum of all the values in the vector
print(y["column_3"]) # accessing a single column value
print(y[1]) # index starts from 1 
print(y[c(1, 2)]) # selecting multiple elements 
print(y[1:4]) # selecting using range 
# NOTE: Range includes the ending element as well
print(mean(y))
print(y[y >= 6])

# Matrix