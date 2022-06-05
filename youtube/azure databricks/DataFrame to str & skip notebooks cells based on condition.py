# Databricks notebook source
# MAGIC %md
# MAGIC ### Condition check scenario on String typed Variable Level

# COMMAND ----------

name_df=spark.sql(f"select 'Arul' as name ");
display(name_df)
type(name_df)

# COMMAND ----------

# DBTITLE 1,Failure condition check scenario
if name_df=='Arul':
  pass
  print('passed')
else:
  dbutils.notebook.exit('skip below code')

# COMMAND ----------

# MAGIC %md
# MAGIC ##### convert from pyspark.sql.dataframe.DataFrame to str

# COMMAND ----------

for row in name_df.rdd.toLocalIterator():
  name_str=row['name']

# COMMAND ----------

name_str

# COMMAND ----------

type(name_str)

# COMMAND ----------

# DBTITLE 1,Success condition check scenario
if name_str=='Arul':
  pass
  print('passed')
else:
  dbutils.notebook.exit('skip below code')

# COMMAND ----------

# MAGIC %md
# MAGIC ### Condition check scenario on Dataframe Level

# COMMAND ----------

# DBTITLE 1,Success condition check scenario
# MAGIC %sql
# MAGIC create or replace temporary view sample_tv as
# MAGIC select 'Arul' as name;

# COMMAND ----------

count_df=spark.sql(f"select 1 from sample_tv");

# COMMAND ----------

if count_df.count()==1:
  pass
  print('passed')
else:
  dbutils.notebook.exit('skip below code')

# COMMAND ----------

# DBTITLE 1,Failure condition check scenario
count_df=spark.sql(f"select 1 from sample_tv where 1==0 ");

# COMMAND ----------

if count_df.count()==1:
  pass
  print('passed')
else:
  dbutils.notebook.exit('skip below code')
