SELECT INS.NAME,INS.DATETIME from ANIMAL_INS as INS
LEFT JOIN ANIMAL_OUTS as OUTS on INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE OUTS.ANIMAL_ID IS NULL
ORDER BY INS.DATETIME ASC
LIMIT 3