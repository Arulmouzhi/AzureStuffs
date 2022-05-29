# Databricks notebook source
# DBTITLE 1,Replacement Approach
# MAGIC %sql
# MAGIC select regexp_replace('0001234ABCD', '^[0]*', '') as Lead_Zero_Removed_String

# COMMAND ----------

# DBTITLE 1,Common Approach
# MAGIC %sql
# MAGIC select replace(ltrim(replace('0001234ABCD','0',' ')),' ','0') as Lead_Zero_Removed_String
