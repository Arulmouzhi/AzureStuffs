# Databricks notebook source
# DBTITLE 1,Importing Pandas Library
import pandas as pd

# COMMAND ----------

# DBTITLE 1,Sample csv file's github url
PATH = "https://raw.githubusercontent.com/rmpbastos/data_sets/main/kaggle_housing/house_df.csv"

# COMMAND ----------

# DBTITLE 1,Reading csv file & Storing as pandas DataFrame
df_pandas = pd.read_csv(PATH)

# COMMAND ----------

# DBTITLE 1,checking the data
df_pandas

# COMMAND ----------

# DBTITLE 1,Checking DataFrame type using type function
type(df_pandas)
