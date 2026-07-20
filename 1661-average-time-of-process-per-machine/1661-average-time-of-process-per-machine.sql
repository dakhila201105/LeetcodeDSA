# Write your MySQL query statement below
SELECT machine_id,
       ROUND(AVG(end_time - start_time), 3) AS processing_time
FROM (
    SELECT a1.machine_id,
           a1.process_id,
           MAX(CASE WHEN a1.activity_type = 'start' THEN a1.timestamp END) AS start_time,
           MAX(CASE WHEN a1.activity_type = 'end' THEN a1.timestamp END) AS end_time
    FROM Activity a1
    GROUP BY a1.machine_id, a1.process_id
) t
GROUP BY machine_id;
