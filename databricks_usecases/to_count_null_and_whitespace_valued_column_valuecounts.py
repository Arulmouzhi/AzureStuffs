# Databricks notebook source
"""
^ indicates the beginning of the string (inverter)
whitespace character ==> spaces, tabs, and newlines etc.,
\s stands for "whitespace character" , it includes [ \t\n\x0B\f\r] --> \s --> a space( ) or a tab(\t) or a line(\n) break or a vertical tab(\x0B sometimes referred as \v) or a form feed(\f) or a carriage return(\r) 
\\s* stands for "zero or more occurrence of whitespace characters"
^\\s* stands for "matching anything except whitespace"
* means "any number of this"
$ indicates the end of the string 
"""

# COMMAND ----------

df = spark.sql("SELECT null as a, 1 as b, '' as c, ' 'as d, 0 as e")
 
from pyspark.sql.functions import col, count
columns_counts = []
 
for column in df.columns:
    null_count = df.filter(col(column).isNull()).count()
    whitespace_count = df.filter(col(column).rlike("^\\s*$")).count()
   
    columns_counts.append((column, (null_count+whitespace_count)))
 
columns_counts_df = spark.createDataFrame(columns_counts, ["Column", "Cnt"])
 
columns_counts_df.display()
