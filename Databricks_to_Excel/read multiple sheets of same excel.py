# Databricks notebook source
df = spark.read.format('com.crealytics.spark.excel').options(header='true').option('inferSchema', 'true').option("dataAddress", "'Sheet1'!A1").load("abfss://container_name@adls_name.dfs.core.windows.net/path_name/file_name.xlsx")
df.display()
