-- QUESTION 2

use lab1_beginning;




-- COLLEGE INSERTS
INSERT INTO COLLEGE (c_name, c_state, c_enrollment)
VALUES ('Stanford', 'CA', 15000);

INSERT INTO COLLEGE (c_name, c_state, c_enrollment)
VALUES ('Berkley', 'CA', 36000);

INSERT INTO COLLEGE (c_name, c_state, c_enrollment)
VALUES ('MIT', 'MA', 10000);

INSERT INTO COLLEGE (c_name, c_state, c_enrollment)
VALUES ('Cornell', 'NY', 21000);




-- STUDENT INSERTS
INSERT INTO STUDENT (s_id, s_name, s_gpa, s_sizehs)
VALUES (123, 'Amy', 3.9, 1000);

INSERT INTO STUDENT (s_id, s_name, s_gpa, s_sizehs)
VALUES (234, 'Bob', 3.6, 1500);

INSERT INTO STUDENT (s_id, s_name, s_gpa, s_sizehs)
VALUES (345, 'Craig', 3.5, 500);

INSERT INTO STUDENT (s_id, s_name, s_gpa, s_sizehs)
VALUES (456, 'Doris', 3.9, 1000);

INSERT INTO STUDENT (s_id, s_name, s_gpa, s_sizehs)
VALUES (567, 'Edward', 2.9, 2000);

INSERT INTO STUDENT (s_id, s_name, s_gpa, s_sizehs)
VALUES (678, 'Fay', 3.8, 200);

INSERT INTO STUDENT (s_id, s_name, s_gpa, s_sizehs)
VALUES (789, 'Gary', 3.4, 800);

INSERT INTO STUDENT (s_id, s_name, s_gpa, s_sizehs)
VALUES (987, 'Helen', 3.7, 800);

INSERT INTO STUDENT (s_id, s_name, s_gpa, s_sizehs)
VALUES (876, 'Irene', 3.9, 400);

INSERT INTO STUDENT (s_id, s_name, s_gpa, s_sizehs)
VALUES (765, 'Jay', 2.9, 1500);

INSERT INTO STUDENT (s_id, s_name, s_gpa, s_sizehs)
VALUES (654, 'Amy', 3.9, 1000);

INSERT INTO STUDENT (s_id, s_name, s_gpa, s_sizehs)
VALUES (543, 'Craig', 3.4, 2000);





-- APPLY INSERTS
INSERT INTO APPLY (s_id, c_name, a_major, a_decision)
VALUES (123, 'Stanford', 'CS', 'Y');

INSERT INTO APPLY (s_id, c_name, a_major, a_decision)
VALUES (123, 'Stanford', 'EE', 'N');

INSERT INTO APPLY (s_id, c_name, a_major, a_decision)
VALUES (123, 'Berkley', 'CS', 'Y');

INSERT INTO APPLY (s_id, c_name, a_major, a_decision)
VALUES (123, 'Cornell', 'EE', 'Y');

INSERT INTO APPLY (s_id, c_name, a_major, a_decision)
VALUES (234, 'Berkley', 'Biology', 'N');

INSERT INTO APPLY (s_id, c_name, a_major, a_decision)
VALUES (345, 'MIT', 'Bioengineering', 'Y');

INSERT INTO APPLY (s_id, c_name, a_major, a_decision)
VALUES (345, 'Cornell', 'Bioengineering', 'N');

INSERT INTO APPLY (s_id, c_name, a_major, a_decision)
VALUES (345, 'Cornell', 'Bioengineering', 'Y');

INSERT INTO APPLY (s_id, c_name, a_major, a_decision)
VALUES (345, 'Cornell', 'CS', 'N');

INSERT INTO APPLY (s_id, c_name, a_major, a_decision)
VALUES (678, 'Stanford', 'History', 'Y');

INSERT INTO APPLY (s_id, c_name, a_major, a_decision)
VALUES (987, 'Stanford', 'CS', 'Y');

INSERT INTO APPLY (s_id, c_name, a_major, a_decision)
VALUES (987, 'Berkley', 'CS', 'Y');

INSERT INTO APPLY (s_id, c_name, a_major, a_decision)
VALUES (876, 'Stanford', 'CS', 'N');

INSERT INTO APPLY (s_id, c_name, a_major, a_decision)
VALUES (876, 'MIT', 'Biology', 'Y');

INSERT INTO APPLY (s_id, c_name, a_major, a_decision)
VALUES (876, 'MIT', 'Marine Biology', 'N');

INSERT INTO APPLY (s_id, c_name, a_major, a_decision)
VALUES (765, 'Stanford', 'History', 'Y');

INSERT INTO APPLY (s_id, c_name, a_major, a_decision)
VALUES (765, 'Cornell', 'History', 'N');

INSERT INTO APPLY (s_id, c_name, a_major, a_decision)
VALUES (765, 'Cornell', 'Psychology', 'Y');

INSERT INTO APPLY (s_id, c_name, a_major, a_decision)
VALUES (543, 'MIT', 'CS', 'N');