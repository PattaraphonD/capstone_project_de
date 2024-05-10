-- acc_by_Age
SELECT 
    CASE
        WHEN psn_age BETWEEN 10 AND 14 THEN '10-14 ปี'
        WHEN psn_age BETWEEN 15 AND 18 THEN '15-18 ปี'
        WHEN psn_age BETWEEN 19 AND 24 THEN '19-24 ปี'
        WHEN psn_age BETWEEN 25 AND 35 THEN '25-35 ปี'
        WHEN psn_age BETWEEN 36 AND 60 THEN '36-60 ปี'
        ELSE '60 ปีขึ้นไป'
    END AS age_group,
    COUNT(*) AS total_cases,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM {{ ref('view_accident_obt')}} ), 2) AS percentage_dead
FROM  {{ ref('view_accident_obt')}} 
WHERE actual_dead_date IS NOT NULL
GROUP BY age_group
ORDER BY age_group