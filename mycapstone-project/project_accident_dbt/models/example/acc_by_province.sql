SELECT case_province, case_district, COUNT(acc_case_id) AS num_accidents, EXTRACT(YEAR FROM actual_dead_date) AS year
FROM {{ ref('view_accident_obt')}} 
GROUP BY case_province, year, case_district