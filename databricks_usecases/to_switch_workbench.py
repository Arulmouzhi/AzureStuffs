# Databricks notebook source
devWorkspaceID =  ['01************']
qaWorkspaceID =   ['02************']
prodWorkspaceID = ['03************']

currentWorkspaceID = spark.conf.get('spark.databricks.clusterUsageTags.clusterOwnerOrgId')

if currentWorkspaceID in devWorkspaceID:
  catalog_table_name_wb = 'dev_wb.comm_schema'
  catalog_table_name_gold = 'dev_gold.comm_schema'
  CommonAdlsPath = 'abfss://container@azyyd1datalakewe.dfs.core.windows.net/layer/'
elif currentWorkspaceID in qaWorkspaceID:
  catalog_table_name_wb = 'qa_wb.comm_schema'
  catalog_table_name_gold = 'qa_gold.comm_schema'
  CommonAdlsPath = 'abfss://container@azyyq1datalakewe.dfs.core.windows.net/layer/'
elif currentWorkspaceID in prodWorkspaceID:
  catalog_table_name_wb = 'prod_wb.comm_schema'
  catalog_table_name_gold = 'prod_gold.comm_schema'
  CommonAdlsPath = 'abfss://container@azyyp1datalakewe.dfs.core.windows.net/layer/'
  
else:
  raise Exception("Environment Mismatch : You are not logged in to the correct databricks workspace")

print(CommonAdlsPath)
print(catalog_table_name_wb)
print(catalog_table_name_gold)
