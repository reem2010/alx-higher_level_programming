-- lists all the cities of California
SELECT id, name
FROM cities
where state_id=(select id from states where name='California')
ORDER BY cities.id  ASC;
