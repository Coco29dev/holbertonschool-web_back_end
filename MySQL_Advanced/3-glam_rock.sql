-- select
-- band_name lifespan
SELECT band_name, (IFNULL(split, 2024) - formed) as lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
