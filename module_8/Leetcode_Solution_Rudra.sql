-- 1978. Employees Whose Manager Left the Company

SELECT e.employee_id
FROM Employees e
LEFT JOIN Employees m ON e.manager_id = m.employee_id
WHERE m.employee_id IS NULL 
AND e.manager_id IS NOT NULL
AND e.salary < 30000
ORDER BY e.employee_id;


-- SELECT e.employee_id
-- From Employees e
-- WHERE e.manager_id NOT IN (SELECT employee_id FROM Employees) AND e.manager_id IS NOT NULL
-- AND e.salary < 30000
-- ORDER BY e.employee_id;

-- 626. Exchange Seats
SELECT
    CASE
        WHEN id % 2 = 1 AND id + 1 <= (SELECT MAX(id) FROM Seat) THEN id + 1
        WHEN id % 2 = 0 THEN id - 1
        ELSE id
    END AS id,
    student
FROM Seat
ORDER BY id;


-- 1341. Movie Rating

-- (SELECT u.name AS results
-- FROM Users u
-- JOIN MovieRating m
-- ON u.user_id = m.user_id
-- GROUP BY u.user_id
-- ORDER BY COUNT(movie_id) DESC, name
-- LIMIT 1)

-- UNION ALL

-- (SELECT m.title FROM Movies m
-- JOIN MovieRating mr ON m.movie_id = mr.movie_id
-- WHERE DATE_FORMAT(created_at, '%Y-%m') = '2020-02'
-- GROUP BY m.movie_id
-- ORDER BY AVG(mr.rating) DESC, m.title
-- LIMIT 1)

(SELECT u.name AS results
 FROM Users u
 JOIN MovieRating m ON u.user_id = m.user_id
 GROUP BY u.user_id, u.name
 ORDER BY COUNT(m.movie_id) DESC, u.name
 LIMIT 1)

UNION ALL

(SELECT m.title
 FROM Movies m
 JOIN MovieRating mr ON m.movie_id = mr.movie_id
 WHERE mr.created_at >= '2020-02-01' AND mr.created_at < '2020-03-01'
 GROUP BY m.movie_id, m.title
 ORDER BY AVG(mr.rating) DESC, m.title
 LIMIT 1);