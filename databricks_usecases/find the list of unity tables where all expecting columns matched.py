# Databricks notebook source
cols = "col1,col2" #mandatory
table_name_pattern = "" # "table_name%", "table_name", "" means optional
catalog = "catalog_name" #mandatory
spark.sql(f"""
WITH values_set AS (
  SELECT explode(split('{cols}', ',')) AS column_name
)
SELECT table_name
FROM {catalog}.information_schema.columns as t1
WHERE ( TRIM('{table_name_pattern}')='' OR table_name LIKE '{table_name_pattern}' )
AND t1.column_name IN (SELECT column_name FROM values_set)
GROUP BY table_name
HAVING COUNT(DISTINCT column_name) = (SELECT COUNT(DISTINCT column_name) FROM values_set);
""").display()
