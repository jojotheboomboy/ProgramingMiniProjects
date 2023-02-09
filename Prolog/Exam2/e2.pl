/*
NAME: Josiah Norman
DATE: 2/1/2023
COURSE: CSC-330
QUARTER: Winter
ASSIGNMENT: Exam 2

*/

course(acct101, instructor(adams), days(mwf), time(1100,1215)).
course(biol102, instructor(barker), days(mwf), time(800,915)).
course(csci103, instructor(collins), days(mwf), time(1400,1515)).
course(econ104, instructor(davidson), days(mwf), time(800,915)).
course(engr105, instructor(evans), days(mwf), time(930,1045)).
course(geol106, instructor(gray), days(tr), time(1000,1150)).
course(kine107, instructor(kelly), days(tr), time(1400,1550)).
course(math111, instructor(murray), days(mwf), time(800,915)).
course(nurs112, instructor(nelson), days(tr), time(800,950)).
course(phys113, instructor(parker), days(tr), time(1000,1150)).
course(stat114, instructor(silver), days(tr), time(1200,1350)).

/* Add your predicates below here */

/* gets the name of the instructor via database, using course. */
getCourseByInstructor(Instructor, Course) :-
course(Course, instructor(Instructor), _,_).

/* gets the time of a class via database, using course */
getCourseByTime(Time, Course) :- 
course(Course, _, _, time(Begin, End)), Begin =< Time, Time =< End.  

/* gets the time of a class via database, using course, 
then uses write to print to the terminal */
printTime(Course) :- 
course(Course, _, _, time(Begin, End)), write(Course), write(' is offered '),
    write(Begin), write(' to '), write(End).