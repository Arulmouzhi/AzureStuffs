--Convert from 0001234ABCD to 1234ABCD
select trim(substring('0001234ABCD', patindex('%[^0]%','0001234ABCD'), 100)) as Lead_Zero_Removed_String

--Trick/Approach/Query that would work in both sql as well as Spark SQL 
select replace(ltrim(replace('0001234ABCD','0',' ')),' ','0') as Lead_Zero_Removed_String
select replace(ltrim(replace('00012034ABCD','0',' ')),' ','0') as Lead_Zero_Removed_String
