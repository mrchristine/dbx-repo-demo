# Databricks notebook source
df = spark.range(1e6)
df.count()

# COMMAND ----------

df.collect()

# COMMAND ----------


