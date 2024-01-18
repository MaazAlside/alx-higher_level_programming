-- script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT AVG(value) AS avg_temp
FROM temperatures
WHERE BY city DESC;

