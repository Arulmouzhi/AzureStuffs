# save multiple o/p df data into multiple sheets of a same excel(without mounting)

df1 = spark.sql("select 1 as a,2 as b")
df2 = spark.sql("select 11 as aa,22 as bb")
 
df1.write.format("com.crealytics.spark.excel") \
    .option("header", "true") \
    .option("dataAddress", "'Sheet1'!A1") \
    .mode("overwrite").option("overwriteSchema","true")\
    .save("abfss://container_name@adls_name.dfs.core.windows.net/path_name/file_name.xlsx")
 
df2.write.format("com.crealytics.spark.excel") \
    .option("header", "true") \
    .option("dataAddress", "'Sheet2'!A1") \
    .mode("append").option("overwriteSchema","true")\
    .save("abfss://container_name@adls_name.dfs.core.windows.net/path_name/file_name.xlsx")