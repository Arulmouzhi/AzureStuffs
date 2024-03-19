# Databricks notebook source
# DBTITLE 1,method_1
#works for openpyxl
import importlib
spec_check = importlib.util.find_spec("openpyxl")
if (spec_check is None):
  %pip install openpyxl
  print("openpyxl installed")
else:
  print("openpyxl already installed")

# COMMAND ----------

# DBTITLE 1,method_2
#works for beautifulsoup4 and openpyxl
import pkg_resources

def package_installed(package_name):
    try:
        dist = pkg_resources.get_distribution(package_name)
        return True
    except pkg_resources.DistributionNotFound:
        return False

if not package_installed("openpyxl"):
    %pip install openpyxl
else:
  print("openpyxl already installed")
