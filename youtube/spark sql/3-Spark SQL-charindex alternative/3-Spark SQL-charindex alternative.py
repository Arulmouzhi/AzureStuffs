# Databricks notebook source
# MAGIC %sql
# MAGIC select instr('Arulmouzhi','m') as Located_Position

# COMMAND ----------

# MAGIC %sql
# MAGIC select instr('Arulmouzhi','M') as Located_Position

# COMMAND ----------

# MAGIC %sql
# MAGIC select instr('Arulmouzhi',lower('M')) as Located_Position
