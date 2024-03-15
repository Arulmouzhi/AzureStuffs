# Databricks notebook source
df = spark.sql(f""" select concat( year(add_months(last_day(current_date()), -1)) ,'-', lpad(month(add_months(last_day(current_date()), -1)),2,'0') , '-01' ) as Reporting_Month """)
Reporting_Month_var = df.select("Reporting_Month").first()[0]
print(Reporting_Month_var)
