-- select 
-- origin nb_fans
SELECT origin, sum(fans) as nb_fans
FROM metal_bands
ORDER BY nb_fans DESC;
