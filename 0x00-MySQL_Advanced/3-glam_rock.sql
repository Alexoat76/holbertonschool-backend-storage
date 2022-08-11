-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity
-- Requirements:
-- Column names must be: band_name and lifespan (in years)
-- Use attributes formed and split for computing the lifespan

SELECT band_name, IFNULL(split, 2020)-IFNULL(formed, 0) AS lifespan
FROM metal_bands LIKE '%Glam rock%' ORDER BY lifespan DESC;