--1. Create Login at server level(dont expose Password for others)
USE MASTER
CREATE LOGIN <login_name> with password='<password>';

--2. Create user at Database level (recommended to keep both user and login names as same, to avoid confusions)
USE <db_name>
CREATE USER <user_name> FOR LOGIN <login_name>;

--3. GRANT REFERENCES ON DATABASE SCOPED CREDENTIAL (create link between DB scoped credential and User) - at Database level
GRANT REFERENCES ON DATABASE SCOPED CREDENTIAL::<db_scoped_credential_name> TO <user_name>;

--4. GRANT SELECT ON SCHEMA,VIEW DEFINITION - at Database level for users
GRANT SELECT,VIEW DEFINITION ON SCHEMA::<schema_name> TO <user_name>; 




