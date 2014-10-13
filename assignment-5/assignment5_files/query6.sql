SELECT trim(stations.name) as stop_f
FROM stations
WHERE stations.lines LIKE "%f%"
ORDER BY stations.name;
