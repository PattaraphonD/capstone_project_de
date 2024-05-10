SELECT personal_id, psn_age, EXTRACT(YEAR FROM actual_dead_date) AS year, vehicle_name
FROM {{ ref('view_accident_obt')}} 
GROUP BY personal_id, psn_age, year, vehicle_name




