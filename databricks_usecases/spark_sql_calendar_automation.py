# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT explode(sequence(DATE'2024-02-27',DATE'2024-03-18',INTERVAL 1 DAY)) as tst;
