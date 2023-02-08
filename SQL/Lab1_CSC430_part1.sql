-- QUESTION 1

create database lab1_beginning; 

use lab1_beginning;

CREATE TABLE STUDENT ( 
s_id int not null PRIMARY KEY, 
s_name varchar (15), 
s_gpa decimal (2,1), 
s_sizehs int);

CREATE TABLE COLLEGE ( 
c_name varchar(25) not null PRIMARY KEY, 
c_state varchar(2), 
c_enrollment int);

CREATE TABLE Apply (
s_id int,
c_name varchar(25),
a_major varchar(25), 
a_decision varchar(1), 
FOREIGN KEY (s_ID) REFERENCES STUDENT (s_id),
FOREIGN KEY (c_name) REFERENCES COLLEGE (c_name)
);