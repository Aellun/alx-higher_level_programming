-- Lists all records(rows without a name value) of the table second_table
-- Ordered in desc order based on score
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
