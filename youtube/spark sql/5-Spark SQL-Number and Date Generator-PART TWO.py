# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT sequence(1, 5) AS Number_Sequence;

# COMMAND ----------

# MAGIC %md 
# MAGIC ## explode()

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT explode(sequence(1, 5)) AS Number_Sequence;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT explode(sequence(date'2022-05-29',date'2022-05-31',interval 1 day)) as Date_Sequence;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT explode(sequence(date'2022-05-29',date'2023-03-31',interval 1 month)) as Date_Sequence;
