SELECT AVG(broadway_ff_avg_diff) AS broadway_ff_avg_diff FROM (
SELECT SUM(fares_feb1.ff) - SUM(fares_jan18.ff) AS broadway_ff_avg_diff
FROM fares_feb1, fares_jan18, stations
WHERE fares_feb1.remote = fares_jan18.remote
  AND fares_feb1.station = stations.name
  AND stations.line LIKE 'Broadway'
GROUP BY fares_feb1.station) as tmp
;
