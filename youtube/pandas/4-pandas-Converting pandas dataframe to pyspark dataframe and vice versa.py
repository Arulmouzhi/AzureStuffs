# Databricks notebook source
# DBTITLE 1,Importing Pandas Library & Reading csv file & Storing as pandas DataFrame
import pandas as pd
PATH = "https://raw.githubusercontent.com/rmpbastos/data_sets/main/kaggle_housing/house_df.csv"
df_pandas = pd.read_csv(PATH)

# COMMAND ----------

# DBTITLE 1,checking whether the dataframe is pandas
type(df_pandas)

# COMMAND ----------

# DBTITLE 1,pandas to pyspark
import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('pandasToPysparkDF').getOrCreate()
df_pyspark = spark.createDataFrame(df_pandas)

# COMMAND ----------

# DBTITLE 1,checking whether the dataframe is pyspark
type(df_pyspark)

# COMMAND ----------

# DBTITLE 1,pyspark to pandas
df_pandas_new = df_pyspark.toPandas()

# COMMAND ----------

# DBTITLE 1,checking whether the dataframe is pandas again
type(df_pandas_new)
