// Databricks notebook source - scala script

// Connection Strings for source

val containerName = "<container_name>"
val storageAccountName = "<storage_account_name>"
val sas = "<sas_token>"

val url = "wasbs://" + containerName + "@" + storageAccountName + ".blob.core.windows.net/"
var config = "fs.azure.sas." + containerName + "." + storageAccountName + ".blob.core.windows.net"



// mounted file into Databricks

dbutils.fs.mount(
  source = url,
  mountPoint = "/mnt/covidmount",
  extraConfigs = Map(config -> sas))



// changed as dataframe

val df = spark.read.csv("/mnt/covidmount/countries-aggregated.csv")
display(df)



// made necessary column name changes

val specificColumnsDf = df.withColumnRenamed("_c0","date").withColumnRenamed("_c1","country").withColumnRenamed("_c2","confirmed").withColumnRenamed("_c3","recovered").withColumnRenamed("_c4","deaths")
display(specificColumnsDf)



//  then changed as temp view-sql

specificColumnsDf.createOrReplaceTempView("coviddatasqltable")



// MAGIC COMMAND - applied normal sql group by query with aggregating counts

%sql
SELECT country,sum(confirmed) as confirmedcount,sum(recovered) as recoveredcount,sum(deaths) as deathscount
FROM coviddatasqltable
GROUP BY country



// Created Connection Strings for destination

// Declare the values for your Azure SQL database
val jdbcUsername = "<user_name>"
val jdbcPassword = "<password>"
val jdbcHostname = "<server_name>"
val jdbcPort     = 1433
val jdbcDatabase ="<database_name>"

// Created JDBC URL without passing in the user and password parameters.
val jdbcUrl = s"jdbc:sqlserver://${jdbcHostname}:${jdbcPort};database=${jdbcDatabase}"

// Build JDBC URL to hold the parameter/ secret
import java.util.Properties

val jdbc_url = s"jdbc:sqlserver://${jdbcHostname}:${jdbcPort};database=${jdbcDatabase};encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.database.windows.net;loginTimeout=60;"
val connectionProperties = new Properties()
connectionProperties.put("user", s"${jdbcUsername}")
connectionProperties.put("password", s"${jdbcPassword}")



// Load data as table in destination DB

import org.apache.spark.sql.SaveMode

val Covidcountrywise = spark.sql("""
SELECT country,sum(confirmed) as confirmedcount,sum(recovered) as recoveredcount,sum(deaths) as deathscount
FROM coviddatasqltable
GROUP BY country
""")

Covidcountrywise.write
     .mode(SaveMode.Overwrite) // <--- Overwrite the existing table
     .jdbc(jdbcUrl, "Covidcountrywisetable", connectionProperties)