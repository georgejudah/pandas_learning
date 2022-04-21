import pandas as pd
import matplotlib.pyplot as plt

print(pd.__version__) #prints the version of python

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

#Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
myvar = pd.DataFrame(mydataset) #convert to a DataFrame

#print(myvar)

a = [1, 7, 2]
myvar = pd.Series(a) #A Pandas Series is like a column in a table. It is a one-dimensional array holding data of any type.
#print(myvar)

#With the index argument, you can name your own indexes.
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
#print(df) 

#Reading data from csv files
df = pd.read_csv('data.csv')
# print(df.to_string())
#print(df.head()) #print first 5 rows of the DataFrame
#print(df.tail()) #print last 5 rows of the DataFrame
#print(df.info()) #information about the data, also shows the no of null rows which helps in cleaning the data

#cleaning data
# print(df.duplicated())  #The duplicated() method returns a Boolean values for each row:
#removing duplicates
#df.drop_duplicates(inplace = True)
#(inplace = True) will make sure that the method does NOT return a new DataFrame, but it will remove all duplicates from the original DataFrame.


#Data Correlations

#The corr() method calculates the relationship between each column in your data set.
print(df.corr())
# The Result of the corr() method is a table with a lot of numbers that represents how well the relationship is between two columns.
# 
# The number varies from -1 to 1.
# 
# 1 means that there is a 1 to 1 relationship (a perfect correlation), and for this data set, each time a value went up in the first column, the other one went up as well.
# 
# 0.9 is also a good relationship, and if you increase one value, the other will probably increase as well.
# 
# -0.9 would be just as good relationship as 0.9, but if you increase one value, the other will probably go down.
# 
# 0.2 means NOT a good relationship, meaning that if one value goes up does not mean that the other will.



#Plotting
df.plot()
plt.show()

#scatter plot
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

#histogram
df["Duration"].plot(kind = 'hist')

plt.show()