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

val sampleset = spark.sql("""
SELECT 1 as a union all select 2 union all select 3
""")

sampleset.write
     .mode(SaveMode.Overwrite) // <--- Overwrite the existing table
     .jdbc(jdbcUrl, "sampletable", connectionProperties)