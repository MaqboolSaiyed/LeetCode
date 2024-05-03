DELETE t1
FROM Person t1
INNER JOIN (
    SELECT MIN(id) as id, email
    FROM Person
    GROUP BY email
    HAVING COUNT(*) > 1
) t2 ON t1.email = t2.email AND t1.id > t2.id;