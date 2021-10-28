# Databricks notebook source
# DBTITLE 1,Create Mount Point - re-runnable
# Python re-runnable code to mount and access ADLS Gen2 Storage Account to Azure Databricks with Service Principal and OAuth

# Variables defined for creating connection strings

adlsContainerName = "testcontainer"
adlsStorageAccountName = "testsan20210725"
adlsFolderName = "testsubcontainer"
MountPointMain = "/mnt/testworkingblob"
StoragePointMain = "abfss://" + adlsContainerName + "@" + adlsStorageAccountName + ".dfs.core.windows.net/" + adlsFolderName

# Application (Client) ID = ServicePrincipalID
ServicePrincipalID = dbutils.secrets.get(scope="CSVProjectKeyVault",key="ClientId")
# Application (Client) Secret Key = ServicePrincipalKey
ServicePrincipalKey = dbutils.secrets.get(scope="CSVProjectKeyVault",key="ClientSecret")
# Directory (Tenant) ID
TenantID = dbutils.secrets.get(scope="CSVProjectKeyVault",key="TenantId")

endpoint = "https://login.microsoftonline.com/" + TenantID + "/oauth2/token"

# Connecting using Service Principal secrets and OAuth
configs = {"fs.azure.account.auth.type": "OAuth",
       "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
       "fs.azure.account.oauth2.client.id":  ServicePrincipalID,
       "fs.azure.account.oauth2.client.secret": ServicePrincipalKey,
       "fs.azure.account.oauth2.client.endpoint": endpoint,
       "fs.azure.createRemoteFileSystemDuringInitialization": "true"}

MountInfo = ""
listMountPoints  = dbutils.fs.mounts()
MountInfo = [iMountPoints for iMountPoints in listMountPoints if MountPointMain in iMountPoints]

if not MountInfo:
  dbutils.fs.mount(
    source = StoragePointMain,
    mount_point = MountPointMain,
    extra_configs = configs)
  print(MountPointMain+" has been mounted" + "\n\n")
else:  
  print(MountPointMain+" has already been mounted" + "\n\n")

# COMMAND ----------

# DBTITLE 1,To test access and to show files inside the folder
# MAGIC %fs ls "/mnt/testworkingblob"

# COMMAND ----------

# DBTITLE 1,Testing by displaying csv file stored in ADLS Gen2
dF = spark.read.options(header='True', inferSchema='True', delimiter=',') \
  .csv("/mnt/testworkingblob/Book1.csv")
display(dF)

# COMMAND ----------

# DBTITLE 1,Unmount Mount Point- re-runnable
lMountPoints  = dbutils.fs.mounts()
sMountInfo = [iMountPoints for iMountPoints in lMountPoints if MountPointMain in iMountPoints]

if not sMountInfo:
  print(MountPointMain+" has already been unmounted" + "\n\n")
else:
  print("Unmounting - " + MountPointMain + "\n\n")
  dbutils.fs.unmount(MountPointMain) 
