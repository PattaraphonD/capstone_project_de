-- acc_by_sex
SELECT
    case_province AS province,
    EXTRACT(YEAR FROM actual_dead_date) AS year,
    COUNT(acc_case_id) AS accident_count
FROM  {{ ref('view_accident_obt')}} 
GROUP BY
    case_province,
    year
ORDER BY
    province
    