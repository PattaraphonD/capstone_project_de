SELECT
    psn_sex,
    COUNT(acc_case_id) AS death_count
FROM {{ ref('view_accident_obt')}} 
GROUP BY
    psn_sex



    