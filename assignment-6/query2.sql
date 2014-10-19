SELECT RTRIM(fares_jan18.station) as name FROM fares_jan18
JOIN fares_feb1 ON fares_jan18.station=fares_feb1.station
GROUP BY fares_jan18.station HAVING SUM(fares_feb1.ff) - SUM(fares_jan18.ff) < -1000;
