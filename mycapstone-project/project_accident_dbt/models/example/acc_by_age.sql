SELECT
    CASE
        WHEN psn_age BETWEEN 0 AND 10 THEN '0-10'
        WHEN psn_age BETWEEN 11 AND 20 THEN '11-20'
        WHEN psn_age BETWEEN 21 AND 30 THEN '21-30'
        WHEN psn_age BETWEEN 31 AND 40 THEN '31-40'
        WHEN psn_age BETWEEN 41 AND 50 THEN '41-50'
        WHEN psn_age BETWEEN 51 AND 60 THEN '51-60'
        ELSE '61+'
    END AS age_range,
    COUNT(acc_case_id) AS death_count
FROM {{ ref('view_accident_obt')}} 
GROUP BY
    age_range
ORDER BY
    MIN(psn_age)







    