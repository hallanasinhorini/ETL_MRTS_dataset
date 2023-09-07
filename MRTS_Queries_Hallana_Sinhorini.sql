

-- This query will return the TOTAL for each month (January through December) and the year for the NAICS_Code values 44811(Men's clothing stores) and 
-- 44812 (Women's clothing stores). The results will be sorted by year.

SELECT Year, NAICS_Code,  Business_kind,
  Jan AS "January", 
  Feb AS "February", 
  Mar AS "March", 
  Apr AS "April", 
  May AS "May", 
  Jun AS "June", 
  Jul AS "July", 
  Aug AS "August", 
  Sep AS "September", 
  Oct AS "October", 
  Nov AS "November", 
  Decm AS "December", 
  TOTAL
FROM MRTS_Business
WHERE NAICS_Code IN (44811, 44812)
ORDER BY Year;

-- This query will return the average TOTAL for each Business_kind in the MRTS_Business table. 
SELECT Business_kind, AVG(TOTAL) FROM MRTS_Business GROUP BY Business_kind;

-- This query will return the total TOTAL for each NAICS_Code in the MRTS_Business table.
SELECT NAICS_Code, SUM(TOTAL) FROM MRTS_Business GROUP BY NAICS_Code;

SELECT Year, NAICS_Code, Business_kind, 
  Jan AS "January", 
  Feb AS "February", 
  Mar AS "March", 
  Apr AS "April", 
  May AS "May", 
  Jun AS "June", 
  Jul AS "July", 
  Aug AS "August", 
  Sep AS "September", 
  Oct AS "October", 
  Nov AS "November", 
  Decm AS "December", 
  TOTAL
FROM MRTS_Business
WHERE NAICS_Code IN (44811, 44812)
ORDER BY Year;

-- This query that will retrieve the sales or revenues for 2010 for bookstores (NAICS_Code 451211), sporting goods stores (NAICS_Code 45111), and hobbies, toys, and games stores
-- (NAICS_Code 45112) using data from the Monthly Retail Trade Survey (MRTS), for the year 2010.

SELECT NAICS_Code, 
  SUM(Jan) AS "January", 
  SUM(Feb) AS "February", 
  SUM(Mar) AS "March", 
  SUM(Apr) AS "April", 
  SUM(May) AS "May", 
  SUM(Jun) AS "June", 
  SUM(Jul) AS "July", 
  SUM(Aug) AS "August", 
  SUM(Sep) AS "September", 
  SUM(Oct) AS "October", 
  SUM(Nov) AS "November", 
  SUM(Decm) AS "December", 
  SUM(TOTAL) AS "Total Sales"
FROM MRTS_Business
WHERE NAICS_Code IN (451211, 45111, 45112)
AND Year = 2010
GROUP BY NAICS_Code
ORDER BY NAICS_Code;



    SELECT NAICS_Code, 
        SUM(Jan) AS "January", 
        SUM(Feb) AS "February", 
        SUM(Mar) AS "March", 
        SUM(Apr) AS "April", 
        SUM(May) AS "May", 
        SUM(Jun) AS "June", 
        SUM(Jul) AS "July", 
        SUM(Aug) AS "August", 
        SUM(Sep) AS "September", 
        SUM(Oct) AS "October", 
        SUM(Nov) AS "November", 
        SUM(Decm) AS "December", 
        SUM(TOTAL) AS "Total Sales"
        FROM MRTS_Business
        WHERE NAICS_Code IN (451211, 45111, 45112)
        AND Year = 2010
        GROUP BY NAICS_Code
        ORDER BY NAICS_Code;
        
        
        
SELECT Year, NAICS_Code, 
  SUM(Jan) AS "January", 
  SUM(Feb) AS "February", 
  SUM(Mar) AS "March", 
  SUM(Apr) AS "April", 
  SUM(May) AS "May", 
  SUM(Jun) AS "June", 
  SUM(Jul) AS "July", 
  SUM(Aug) AS "August", 
  SUM(Sep) AS "September", 
  SUM(Oct) AS "October", 
  SUM(Nov) AS "November", 
  SUM(Decm) AS "December", 
  SUM(TOTAL) AS "Total Sales"
FROM MRTS_Business
WHERE NAICS_Code IN (451211, 45111, 45112)
AND Year BETWEEN 2010 AND 2015
GROUP BY Year, NAICS_Code
ORDER BY Year, NAICS_Code