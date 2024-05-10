SELECT 
    *,
    CASE
        WHEN EXTRACT(MONTH FROM actual_dead_date) BETWEEN 2 AND 4 THEN 'ฤดูร้อน'
        WHEN EXTRACT(MONTH FROM actual_dead_date) BETWEEN 5 AND 10 THEN 'ฤดูฝน'
        WHEN EXTRACT(MONTH FROM actual_dead_date) BETWEEN 11 AND 1 THEN 'ฤดูหนาว'
    END AS wheater
FROM {{ ref('view_accident_obt')}} 




