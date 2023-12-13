-- select from two tables
SELECT c.id, c.name
FROM cities AS c, states AS s
WHERE c.id = s.id
ORDER BY c.id ASC;
