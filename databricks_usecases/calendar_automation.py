# Databricks notebook source
import pandas as pd
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

start_date = "2024-02-16"
end_date = pd.to_datetime("today").strftime("%Y-%m-%d")

date_range = pd.date_range(start=start_date, end=end_date, freq='D')

date_range_df = spark.createDataFrame(date_range.to_frame(), ["date"])
date_range_df.createOrReplaceTempView("test_vw")
