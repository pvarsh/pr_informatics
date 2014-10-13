SELECT stations.lat, stations.lng, SUM(fares_jan18.ff) as ff
FROM fares_jan18
INNER JOIN stations ON fares_jan18.station=stations.name
WHERE stations.line LIKE 'Broadway'
GROUP BY stations.name
ORDER BY ff DESC;
