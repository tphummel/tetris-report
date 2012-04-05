SELECT p.playerid, 
get_player_name(p.playerid, 'nick') as nm,
get_location_name(m.location, '') as loc,
m.matchid, m.matchdate, p.lines, p.time, p.wrank, p.erank,
get_numplayers_inmatch(m.matchid) as numplyrs
FROM tntmatch m, playermatch p
WHERE p.playerid = 1
and extract(year from m.matchdate) = 2004
and get_numplayers_inmatch(m.matchid) = 3
AND m.matchid = p.matchid
ORDER BY p.playerid, m.matchdate asc, m.matchid asc;

SELECT m.matchid, 
get_location_name(m.location, '') as loc,
m.matchdate, 
get_numplayers_inmatch(m.matchid) as numplyrs
FROM tntmatch m
WHERE location = 2
ORDER BY m.matchdate asc, m.matchid asc;
