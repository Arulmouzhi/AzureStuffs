# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT sequence(1, 5) AS Number_Sequence;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT sequence(DATE'2022-05-29',DATE'2022-05-31',INTERVAL 1 DAY) as Date_Sequence;
