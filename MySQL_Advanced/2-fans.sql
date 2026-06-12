-- select 
-- origin nb_fans
SELECT origin, count(fans) as nb_fans
FROM metal_bands
ORDER BY nb_fans DESC;
