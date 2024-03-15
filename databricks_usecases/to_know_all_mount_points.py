# Databricks notebook source
mounts = dbutils.fs.mounts()
for mount in mounts:
  mount_point = mount.mountPoint
  print(mount_point)
