--computes the score average of all records in the table second_table
--in the column name average

USE hbtn_0c_0;

SELECT AVG('score') AS 'average'
FROM 'second_table';
