use StudentdbW23;

-- 1
-- Using aliasing, select the names and grades 
-- of students with Grade greater than 3.0
SELECT S.Name, T.grade
FROM STUDENT S, TAKE T
WHERE S.Sid = T.Sid and T.grade>3.0;

-- 2
-- For each student compute the average between their grade and 
-- their ProfessorEval and sort the result in ascending order
SELECT S.Name, T.Grade, T.ProfessorEval
FROM STUDENT S, TAKE T
WHERE S.Sid = T.Sid
order by (T.grade+T.ProfessorEval)/2 asc;

-- 3
-- Use a subquery in the FROM clause to find those students belonging 
-- to the ‘Education Department’ who have taken course numbered 101.
-- NOTE: USED 'Education' instead of 'Education Department', the ladder would yield a Name table with 0 instances.
SELECT S.Name
FROM STUDENT S, (SELECT * FROM Take) T
WHERE S.Sid = T.Sid AND T.DeptName = 'Education' AND T.courseNum = '101';


-- 4
-- Find those courses that were taken by student that do not
-- have any perquisites
SELECT C.CourseName
FROM COURSE C, PreReq PR, STUDENT S, Take T
WHERE T.Sid = S.Sid AND T.CourseNum = PR.CourseNum AND PR.PreReqNumber = null;

-- 5
-- List all the courses that have prerequisites (using EXISTS)
SELECT C.CourseName
FROM COURSE C
WHERE EXISTS 
			(SELECT	* 
			FROM	PreReq P 
			WHERE 	P.coursenum = C.coursenum);