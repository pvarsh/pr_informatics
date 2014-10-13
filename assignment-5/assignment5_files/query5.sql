SELECT stations.name,
SUM(fares_feb1.7d - fares_jan18.7d) AS diff_7d,
SUM(fares_feb1.30d - fares_jan18.30d) AS diff_30d
FROM fares_feb1
INNER JOIN fares_jan18 ON fares_feb1.station=fares_jan18.station AND fares_feb1.remote = fares_jan18.remote
INNER JOIN stations ON fares_feb1.station=stations.name
WHERE stations.line='Broadway'
GROUP BY stations.name;
