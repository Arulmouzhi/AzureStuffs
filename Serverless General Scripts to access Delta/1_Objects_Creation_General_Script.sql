--Step 1 - Create database at your respective serverless synapse server
CREATE DATABASE <db_name>;

--Step 2 - Use the database that is created in above step
USE <db_name>;

--Step 3 - create schema under the database
CREATE SCHEMA <schema_name>;

--Step 4 - Create Master key in the Database
CREATE MASTER KEY;

--Step 5 - Database Scope credential (dont expose credentials like app-client-id,secret_key and tenant id); --below is spn way
CREATE DATABASE SCOPED CREDENTIAL <db_scoped_credential_name> WITH
IDENTITY = '<app-client-id>@https://login.microsoftonline.com/<tenant_id>/oauth2/token', 
SECRET = '<secret_key>'; 

--Step 6 - CREATE EXTERNAL FILE FORMAT for Delta and Parquet Files. (we can also use DELIMITEDTEXT as FORMAT_TYPE for CSV)
CREATE EXTERNAL FILE FORMAT <delta_ext_f_format> WITH (  FORMAT_TYPE = DELTA );
CREATE EXTERNAL FILE FORMAT <parquet_ext_f_format> WITH ( FORMAT_TYPE = PARQUET );

--Step 7 - Create external datasource(data source can be created at parent directory level and subdirectory can be specified in while creating view or table)
CREATE EXTERNAL DATA SOURCE <ext_data_source_name>
WITH (    
    LOCATION   = 'https://<adls_name>.blob.core.windows.net/<container_name>/',
    CREDENTIAL = <db_scoped_credential_name>
);

--Step 8 -> check using open rowset command to access adls data(delta/parquet etc.,)
SELECT 
 cast([COL_name1] as float) as [col name1]
,col_name2
FROM
    OPENROWSET(
        BULK 'gold/folder_main/folder_sub/xxxyyyzzz',
        DATA_SOURCE='<ext_data_source_name>',
        FORMAT = 'DELTA'
    ) 
WITH(
    COL_name1 nvarchar(500), --float
    col_name2 nvarchar(500)
) AS [result];

--Step 9 --> View Creation
--DROP VIEW <schema_name>.<view_name>
CREATE OR ALTER VIEW <schema_name>.<view_name>
AS
SELECT 
 cast([COL_name1] as float) as [col name1]
,col_name2
FROM
    OPENROWSET(
        BULK 'gold/folder_main/folder_sub/xxxyyyzzz',
        DATA_SOURCE='<ext_data_source_name>',
        FORMAT = 'DELTA'
    ) 
WITH(
    COL_name1 nvarchar(500), --float
    col_name2 nvarchar(500)
) AS [result];

--testing
SELECT * FROM <schema_name>.<view_name>;

--Step 10 --> external table creation (mainly to write data into adls)
--DROP EXTERNAL TABLE <schema_name>.<ext_table_name>
-- CREATE EXTERNAL TABLE <schema_name>.<ext_table_name>
-- (
--   COL_name1 nvarchar(500),
--   col_name2 nvarchar(500)
-- )  
-- WITH (
--         LOCATION = 'silver/testfolder/',
--         DATA_SOURCE = '<ext_data_source_name>',
--         FILE_FORMAT = <parquet_ext_f_format>
--)
--AS
--SELECT * FROM <schema_name>.<view_name>;

--SELECT * FROM <schema_name>.<ext_table_name>;



--SPN RENEW CASE- PLEASE FOLLOW BELOW STEPS, SO THAT WE CAN ACCESS SERVERLESS AGAIN EASILY
--STEP 0 - REVOKE REFERENCES TO USER
--STEP 1 - EXTERNAL TABLE [EXISTING DROP]
--STEP 2 - EXTERNAL DATA SOURCE [EXISTING DROP]
--STEP 3 - DATABASE SCOPED CREDENTIAL [EXISTING DROP]
--STEP 4 - CREATE DATABASE SCOPED CREDENTIAL AGAIN
--STEP 5 - CREATE EXTERNAL DATA SOURCE AGAIN
--STEP 6 - CREATE EXTERNAL TABLE AGAIN
--STEP 7 - GRANT AGAIN THE REFERENCES TO USER

--0
REVOKE REFERENCES ON DATABASE SCOPED CREDENTIAL::<db_scoped_credential_name> TO <user_name>;
--1 
DROP EXTERNAL TABLE <schema_name>.<ext_table_name>;
--2
DROP EXTERNAL DATA SOURCE <ext_data_source_name>;
--3 
DROP DATABASE SCOPED CREDENTIAL <db_scoped_credential_name>;
--4
CREATE DATABASE SCOPED CREDENTIAL <db_scoped_credential_name> WITH
IDENTITY = '<app-client-id>@https://login.microsoftonline.com/<tenant_id>/oauth2/token', 
SECRET = '<NEW_secret_key>'; 
--5
CREATE EXTERNAL DATA SOURCE <ext_data_source_name>
WITH (    
    LOCATION   = 'https://<adls_name>.blob.core.windows.net/<container_name>/',
    CREDENTIAL = <db_scoped_credential_name>
);
--6 
-- CREATE EXTERNAL TABLE <schema_name>.<ext_table_name>
-- (
--   COL_name1 nvarchar(500),
--   col_name2 nvarchar(500)
-- )  
-- WITH (
--         LOCATION = 'silver/testfolder/',
--         DATA_SOURCE = '<ext_data_source_name>',
--         FILE_FORMAT = <parquet_ext_f_format>
--)
--AS
--SELECT * FROM <schema_name>.<view_name>;
--7
GRANT REFERENCES ON DATABASE SCOPED CREDENTIAL::<db_scoped_credential_name> TO <user_name>;

