# Databricks notebook source
# DBTITLE 1,Importing pandas library 
import numpy as np
import pandas as pd

# COMMAND ----------

# DBTITLE 1,To read file and creating a DataFrame
PATH = "https://raw.githubusercontent.com/rmpbastos/data_sets/main/kaggle_housing/house_df.csv"
df = pd.read_csv(PATH)

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ##Dataset/DataFrame column descriptions
# MAGIC 
# MAGIC * Id — Unique identification for each row (we’ll use it as our index).
# MAGIC 
# MAGIC * LotArea — Lot size in square feet
# MAGIC 
# MAGIC * Street — Type of road access
# MAGIC 
# MAGIC * Neighborhood — Physical location of the house
# MAGIC 
# MAGIC * HouseStyle — Style of residence
# MAGIC 
# MAGIC * YearBuilt — Construction date
# MAGIC 
# MAGIC * CentralAir — Central air conditioning
# MAGIC 
# MAGIC * BedroomAbvGr — Number of bedrooms above basement level
# MAGIC 
# MAGIC * Fireplaces — Number of fireplaces
# MAGIC 
# MAGIC * GarageType — Garage location
# MAGIC 
# MAGIC * GarageYrBlt — Year garage was built
# MAGIC 
# MAGIC * GarageArea — Size of garage in square feet
# MAGIC 
# MAGIC * PoolArea — Pool area in square feet
# MAGIC 
# MAGIC * PoolQC — Pool quality
# MAGIC 
# MAGIC * Fence — Fence quality
# MAGIC 
# MAGIC * SalePrice — House price

# COMMAND ----------

# DBTITLE 1,To display first 1000 rows - use display() function
display(df)

# COMMAND ----------

# DBTITLE 1,To check the type of the DataFrame - use type() function on DataFrame
type(df)

# COMMAND ----------

# DBTITLE 1,To check the type of the column in the DataFrame - use type() function on column of the DataFrame
# In Pandas, a single column can be called Series.
type(df["LotArea"])

# COMMAND ----------

# MAGIC %md
# MAGIC #Examining the DataFrame

# COMMAND ----------

# DBTITLE 1,To check the first n entries on the DataFrame with the function .head(n)
df.head(1)

# COMMAND ----------

# DBTITLE 1,If n is not provided in function .head(n), we’ll see the first 5 rows as default
df.head()

# COMMAND ----------

# DBTITLE 1,To check the first n entries on the DataFrame Column with the function .head(n)
df["Street"].head(2)

# COMMAND ----------

# DBTITLE 1,To check the last n entries on the DataFrame with the function .tail(n)
df.tail(1)

# COMMAND ----------

# DBTITLE 1,If n is not provided in function .tail(n), we’ll see the last 5 rows as default
df.tail()

# COMMAND ----------

# DBTITLE 1,To check the last n entries on the DataFrame Column with the function .tail(n)
df["Street"].tail(2)

# COMMAND ----------

# DBTITLE 1,To check the dimensions of our data using the .shape attribute
df.shape

# COMMAND ----------

# DBTITLE 1,To view a summary of the data set/DataFrame with the function .info()
df.info()

# COMMAND ----------

# DBTITLE 1,To view descriptive statistics about the dataset - use .describe() function
df.describe()

# COMMAND ----------

# DBTITLE 1,To return a Series containing the number of unique values - use .value_counts() function
df["YearBuilt"].value_counts()

# COMMAND ----------

# DBTITLE 1,DataFrame Index
# After checking our data, we noticed that the first column (Id) has a unique value for each row. We can take advantage of it and use this column as our index
df.set_index("Id", inplace=True)
df.index
# When setting the argument inplace as True the DataFrame will be updated in place. Otherwise, using inplace = False, which is the default value, would return a copy of the DataFrame.

# If we know beforehand that we are going to use a column in our data set as the index, we can set it up when reading the file
df = pd.read_csv(PATH, index_col="Id")

# COMMAND ----------

# DBTITLE 1,To check the columns of the dataset/DataFrame, use .columns
df.columns

# COMMAND ----------

# DBTITLE 1,To rename columns, use .rename()
df.rename(columns={"BedroomAbvGr":"Bedroom", "GarageYrBlt":"Garage"}, inplace=True)

# COMMAND ----------

# DBTITLE 1,To create a copy of our DataFrame, use .copy()
df_copy = df.copy()

# COMMAND ----------

# DBTITLE 1,To add a column with default value
df_copy["Sold"] = "N"

# COMMAND ----------

# DBTITLE 1,To add multiple columns with default values
df_copy["column_new_1"], df_copy["column_new_2"], df_copy["column_new_3"] = [np.nan, "dogs", 3]

# COMMAND ----------

# DBTITLE 1,To add n rows in DataFrame, use .append() function
#here adding 2 rows

data_to_append = {"LotArea": [9500, 15000],
                  "Street": ["Pave", "Gravel"],
                  "Neighborhood": ["Downtown", "Downtown"],
                  "HouseStyle": ["2Story", "1Story"],
                  "YearBuilt": [2021, 2019],
                  "CentralAir": ["Y", "N"],
                  "Bedroom": [5, 4],
                  "Fireplaces": [1, 0],     
                  "GarageType": ["Attchd", "Attchd"],  
                  "Garage": [2021, 2019],
                  "GarageArea": [300, 250],
                  "PoolArea": [0, 0],
                  "PoolQC": ["G", "G"],
                  "Fence": ["G", "G"], 
                  "SalePrice": [250000, 195000]}

# changing normal dict (key-value pairs) as DataFrame
df_to_append = pd.DataFrame(data_to_append)

df_copy = df.copy()

# appending 2 dataframes using .append() function
df_copy = df_copy.append(df_to_append, ignore_index=True)

df_copy.tail(3)

# COMMAND ----------

# DBTITLE 1,To remove the rows, use .drop() function where axis=0 means row
df_copy.drop(labels=[1460,1461], axis=0, inplace=True)

# COMMAND ----------

# DBTITLE 1,To remove the columns, use .drop() function where axis=1 means column
df_copy.drop(labels=["Fence","PoolQC"], axis=1, inplace=True)

# COMMAND ----------

# MAGIC %md
# MAGIC ## .loc method

# COMMAND ----------

# DBTITLE 1,To Select data with .loc method, to bring all columns
df_copy = df.copy()
#index starts from 0 in python
df_copy.loc[1459]

# COMMAND ----------

# DBTITLE 1,To Select data with .loc method, to bring selected columns
df_copy.loc[1459,["Neighborhood","SalePrice"]]

# COMMAND ----------

# DBTITLE 1,To Select data with .loc method, to apply filter condition + bring selected columns(optional)
df_copy.loc[df["SalePrice"] >= 600000, ["Neighborhood","SalePrice"] ]
# where ,["Neighborhood","SalePrice"] --> second parameter is optional. if not mentioned, then it will bring all columns.

# COMMAND ----------

# MAGIC %md
# MAGIC ## .iloc method

# COMMAND ----------

# DBTITLE 1,To select the data contained in the first row and the first column
df.iloc[0,0]

# COMMAND ----------

# DBTITLE 1,To select the data contained in an entire row
df.iloc[10,:]

# COMMAND ----------

# DBTITLE 1,To select the data contained in the last column
df.iloc[:,-1]

# COMMAND ----------

# DBTITLE 1,To select multiple rows and columns
df.iloc[8:12, 2:5]

# COMMAND ----------

# MAGIC %md
# MAGIC #Handling missing values

# COMMAND ----------

# DBTITLE 1,To Detect missing values using .isnull() function
df.isnull()

# COMMAND ----------

# DBTITLE 1,To Detect the number of missing values under each column, using .isnull() function
df.isnull().sum()
# True=1 and False=0

# COMMAND ----------

# DBTITLE 1,To get the number of rows or/and columns of the dataset/DataFrame
df.shape[0], df.shape[1]

# COMMAND ----------

# DBTITLE 1,To check the proportion of missing values for each column
(df.isnull().sum() / df.shape[0])*100

# COMMAND ----------

# DBTITLE 1,To get only the columns with missing values and display the percentage of values that are missing
for column in df.columns:
    if df[column].isnull().sum() > 0:
        print(column, ': {:.2%}'.format(df[column].isnull().sum() /
                                               df[column].shape[0]))

# COMMAND ----------

# DBTITLE 1,To Remove missing values
df_toremove = df.copy()
df_toremove.dropna(subset=["GarageType"], axis=0, inplace=True)
df_toremove.shape[0]

# COMMAND ----------

# DBTITLE 1,To Fill the missing values with default value
df_tofill = df.copy()
df_tofill["Fence"].value_counts()
df_tofill["Fence"].fillna(value="NoFence", inplace=True)
df_tofill["Fence"].value_counts()

# COMMAND ----------

# DBTITLE 1,To Fill the missing values with median value
garage_median = df_tofill["Garage"].median()
df_tofill.fillna({"GarageYrBlt": garage_median}, inplace=True)

# COMMAND ----------

# MAGIC %md
# MAGIC #Visualizing data
# MAGIC 
# MAGIC 2 other Python libraries
# MAGIC 
# MAGIC * ###Matplotlib
# MAGIC 
# MAGIC * ###seaborn

# COMMAND ----------

# DBTITLE 1,Histograms - to display the distribution of data
df["SalePrice"].plot(kind="hist")

# COMMAND ----------

# DBTITLE 1,Scatter plots - to visualize the relationship between two variables
df.plot(x="SalePrice", y="YearBuilt", kind="scatter")

# COMMAND ----------

# DBTITLE 1,To save our DataFrame as a file
df.to_csv("My_DataFrame.csv")
