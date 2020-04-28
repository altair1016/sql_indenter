SELECT a2.ZIP_CODE,
       COUNT(a1.User_ID)
FROM
  (SELECT User_ID,
          SUM(Score)
   FROM User_Score
   GROUP BY User_ID
   HAVING SUM(Score) > 200) a1,
     User_Address a2
WHERE a1.User_ID = a2.User_ID
GROUP BY a2.ZIP_CODE;