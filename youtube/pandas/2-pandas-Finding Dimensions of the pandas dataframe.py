# Databricks notebook source
# DBTITLE 1,Importing Pandas Library & Reading csv file & Storing as pandas DataFrame
import pandas as pd
PATH = "https://raw.githubusercontent.com/rmpbastos/data_sets/main/kaggle_housing/house_df.csv"
df_pandas = pd.read_csv(PATH)

# COMMAND ----------

# DBTITLE 1,Checking the Dimensions of the DataFrame
df_pandas.shape

# COMMAND ----------

# DBTITLE 1,Checking the number of rows of the DataFrame
df_pandas.shape[0]

# COMMAND ----------

# DBTITLE 1,Checking the number of columns of the DataFrame
df_pandas.shape[1]

# COMMAND ----------

# DBTITLE 1,Checking the name of columns of the DataFrame
df_pandas.columns
