16.1:
SELECT *
FROM wrpracti_bookinfo. employees
ORDER BY FIRST_NAME;

16.2:
SELECT FIRST_NAME, LAST_NAME, SALARY, SALARY *0.15 AS TAX
FROM wrpracti_bookinfo. employees;

16.3:
SELECT SUM(SALARY)
FROM wrpracti_bookinfo. employees;

16.4:
SELECT MAX(SALARY), min(SALARY)
FROM wrpracti_bookinfo. employees;

16.5:

SELECT avg(SALARY), count(*)
FROM wrpracti_bookinfo. employees;