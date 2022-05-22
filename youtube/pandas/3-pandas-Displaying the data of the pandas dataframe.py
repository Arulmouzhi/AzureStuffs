# Databricks notebook source
# DBTITLE 1,Importing Pandas Library & Reading csv file & Storing as pandas DataFrame
import pandas as pd
PATH = "https://raw.githubusercontent.com/rmpbastos/data_sets/main/kaggle_housing/house_df.csv"
df_pandas = pd.read_csv(PATH)

# COMMAND ----------

# DBTITLE 1,display to show first 1000 records - default
display(df_pandas)

# COMMAND ----------

# DBTITLE 1,head to show first 5 records - default
df_pandas.head()

# COMMAND ----------

# DBTITLE 1,head to show first 3 records - user defined
df_pandas.head(3)

# COMMAND ----------

# DBTITLE 1,head to show first 3 records - user defined with a specific column like Neighborhood
df_pandas[["Neighborhood"]].head(3)

# COMMAND ----------

# DBTITLE 1,head to show first 3 records - user defined with the specific columns like Neighborhood, YearBuilt
df_pandas[["Neighborhood","YearBuilt"]].head(3)

# COMMAND ----------

# DBTITLE 1,tail to show last 5 records - default
df_pandas.tail()

# COMMAND ----------

# DBTITLE 1,tail to show last 2 records - user defined
df_pandas.tail(2)

# COMMAND ----------

# DBTITLE 1,tail to show last 2 records - user defined with a specific column like Neighborhood
df_pandas[["Neighborhood"]].tail(2)

# COMMAND ----------

# DBTITLE 1,tail to show last 2 records - user defined with the specific columns like Neighborhood, YearBuilt
df_pandas[["Neighborhood","YearBuilt"]].tail(2)
