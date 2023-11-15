-- displays the max temperature of each state (ordered by State name).
SELECT `state`, MAX(`value`) AS `Max_Temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
