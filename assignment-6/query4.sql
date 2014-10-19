SELECT RTRIM(fares_jan18.station) as station_with_largest_increase
FROM fares_jan18
JOIN fares_feb1 ON fares_jan18.station=fares_feb1.station
GROUP BY fares_jan18.station ORDER BY SUM(fares_feb1.ff) - SUM(fares_jan18.ff) DESC
LIMIT 1;
