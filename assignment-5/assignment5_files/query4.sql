SELECT trim(fares_jan18.station) AS name, SUM(fares_feb1.ff - fares_jan18.ff) AS diff_feb1_jan18
FROM fares_jan18
INNER JOIN fares_feb1 ON fares_jan18.station=fares_feb1.station AND fares_jan18.remote=fares_feb1.remote
INNER JOIN stations ON fares_jan18.station=stations.name
WHERE stations.line='Broadway'
GROUP BY stations.name;
