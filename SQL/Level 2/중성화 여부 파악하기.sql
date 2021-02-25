SELECT ANIMAL_ID,NAME,REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(SEX_UPON_INTAKE,' Male',''),' Female',''),'Neutered','O'),'Spayed','O'),'Intact','X') from ANIMAL_INS order by ANIMAL_ID ASC

/* SELECT  ANIMAL_ID,
        NAME,
        IF(SEX_UPON_INTAKE REGEXP 'Neutered|Spayed', 'O' , 'X') AS 중성화
FROM    ANIMAL_INS

로도 가능
*/ 