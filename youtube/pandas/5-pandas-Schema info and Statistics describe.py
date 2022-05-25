# Databricks notebook source
# DBTITLE 1,Importing Pandas Library & Reading csv file & Storing as pandas DataFrame
import pandas as pd
PATH = "https://raw.githubusercontent.com/rmpbastos/data_sets/main/kaggle_housing/house_df.csv"
df_pandas = pd.read_csv(PATH)

# COMMAND ----------

# DBTITLE 1,To Find name of the columns
df_pandas.columns

# COMMAND ----------

# DBTITLE 1,Schema info of the pandas dataframe
df_pandas.info()

# COMMAND ----------

# DBTITLE 1,Statistics describe of the pandas dataframe
df_pandas.describe()
