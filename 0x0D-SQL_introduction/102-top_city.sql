-- script that displays the top 3 of cities temperature 
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month IN ('July', 'August')
ORDER BY avg_temp
DESC
LIMIT 3;
