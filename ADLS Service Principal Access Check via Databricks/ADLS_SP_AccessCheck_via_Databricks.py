# Databricks notebook source
# DBTITLE 1,Setup variables
ContainerName = "<Container-Name>"
StorageAccountName = "<Storage-Account-Name>"
StoragePath = "abfss://"+ ContainerName +"@"+ StorageAccountName + ".dfs.core.windows.net/"
Folder = "<Folder> /" 

ScopeName = "<Scope-Name>"  #the name of the scope provided in azure databricks while linking Key Vault
ServicePrincipalID = "<Service-Principal-ID>"
ServicePrincipalKey = "<Service-Principal-Key>"
TenantID = "<Tenant-ID>"

# COMMAND ----------

# DBTITLE 1,Building connections and accesses based on above Setup variables
KV_ServicePrincipalID = dbutils.secrets.get( ScopeName, ServicePrincipalID )
KV_ServicePrincipalKey = dbutils.secrets.get( ScopeName, ServicePrincipalKey )
KV_TenantID = dbutils.secrets.get( ScopeName, TenantID )

Directory = "https://login.microsoftonline.com/" + KV_TenantID + "/oauth2/token"

spark.conf.set("fs.azure.account.auth.type." + StorageAccountName + ".dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type." + StorageAccountName + ".dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id." + StorageAccountName + ".dfs.core.windows.net", KV_ServicePrincipalID )
spark.conf.set("fs.azure.account.oauth2.client.secret." + StorageAccountName + ".dfs.core.windows.net", KV_ServicePrincipalKey )
spark.conf.set("fs.azure.account.oauth2.client.endpoint." + StorageAccountName + ".dfs.core.windows.net", Directory)

# COMMAND ----------

# DBTITLE 1,To view the files and directories in filesystem path
dbutils.fs.ls(StoragePath)

# COMMAND ----------

# MAGIC %md
# MAGIC #Checking Service principal Access at Folder level

# COMMAND ----------

# DBTITLE 1,write, copy, read, create directory, move, remove - re Runnable code
#1. Write
dbutils.fs.put(StoragePath + Folder + "check1.csv", "name,dept,email")
#2. Copy
dbutils.fs.cp(StoragePath + Folder + "check1.csv", StoragePath + Folder + "check2.csv")
#3. Read
dbutils.fs.head(StoragePath + Folder + "check1.csv")
#4. Create Directory
dbutils.fs.mkdirs(StoragePath + Folder + "subfolder")
#5. Move
dbutils.fs.mv(StoragePath + Folder + "check2.csv",StoragePath + Folder + "subfolder/")
#6. Remove
dbutils.fs.rm(StoragePath + Folder + "check1.csv")
