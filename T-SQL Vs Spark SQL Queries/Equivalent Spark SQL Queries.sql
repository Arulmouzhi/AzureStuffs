-- Databricks notebook source
----------------------------------- Spark SQL QUERIES -----------------------------------

-- 1. LIMIT n (at last)
SELECT '#1- TOP n (after SELECT) Vs LIMIT n (at last)',* FROM
(
	SELECT	1 AS S_NO, 'ADARSH' AS STUDENT_NAME
	UNION ALL
	SELECT	2 AS S_NO, 'ARUL' AS STUDENT_NAME
) T LIMIT 1;

-- COMMAND ----------

-- 2. CAST
SELECT '#2- TRY_CAST Vs CAST',CAST( '10 D' AS INT ) AS SAMPLES;

-- COMMAND ----------

-- 3. COALESCE
SELECT '#3- ISNULL Vs COALESCE',COALESCE( CAST('10 D' AS INT) ,-1) AS SAMPLES;

-- COMMAND ----------

-- 4. []
SELECT '#4- [] Vs ``','10 D' AS `SAMPLE DAYS`;

-- COMMAND ----------

-- 5. ISDATE() ==> No Equivalent Built-in Function, So Separate UDF we need to create and use it.
SELECT '#5- ISDATE() Vs No Equivalent Built-in Function'; 
--,ISDATE( '2021/02/29' ) AS SAMPLES;

-- COMMAND ----------

-- 6. GETDATE() - DATETIME version
SELECT '#6- GETDATE() - DATETIME version Vs current_timestamp()',current_timestamp() AS SAMPLES;

-- COMMAND ----------

-- 7. GETDATE() - DATE version
SELECT '#7- GETDATE() - DATE version Vs current_date()', current_date() AS SAMPLES;

-- COMMAND ----------

-- 8. FORMAT
SELECT '#8- FORMAT Vs TO_DATE',TO_DATE( current_timestamp(),"yyyyMMdd" ) AS SAMPLES;

-- COMMAND ----------

-- 9. EOMONTH()
SELECT '#9- EOMONTH() Vs LAST_DAY()',LAST_DAY( current_timestamp() ) AS SAMPLES;

-- COMMAND ----------

-- 10. DATEADD - DAY - 3 parameter
SELECT '#10- DATEADD - DAY - 3 parameter Vs DATE_ADD - 2 parameter',current_date() AS TODAY, DATE_ADD( current_date(),2 ) AS SAMPLES;

-- COMMAND ----------

-- 11. DATEADD - MONTH - 3 parameter
SELECT '#11- DATEADD - MONTH - 3 parameter Vs ADD_MONTHS - 2 parameter',current_date() AS TODAY, ADD_MONTHS( current_date(),2 ) AS SAMPLES;
