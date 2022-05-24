# sql_indenter
Is a python software to 'Beautify' and indent an SQL query.
Takes a file in input through a GUI managed by Tkinter and saves a new indented file into indented_sql folder

# Create a new instance, your Instance
## All you need is...

Computer  where to host the python scripts.

python2 intepreter with following modules installed: 
 
- sqlparse
- Tkinter
- os


# Installation  

1. Run a `git clone https://github.com/altair1016/sql_indenter` command or download files from my repo.
2. Pip install sqlparse and Tkinter
3. Run python command `python2 sql_indenter.py`


# Sample of usage  


Before: 

```sql
SELECT a2.ZIP_CODE, COUNT(a1.User_ID) FROM (SELECT User_ID, SUM(Score) FROM User_Score GROUP BY User_ID HAVING SUM(Score) > 200) a1, User_Address a2 WHERE a1.User_ID = a2.User_ID GROUP BY a2.ZIP_CODE;
```

After:

```sql
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
```
