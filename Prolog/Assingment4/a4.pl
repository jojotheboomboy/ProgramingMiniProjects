/*
Name:           Josiah Norman
Date:           1/29/2023
Number/Section: CSC-330-002 
Quarter:        WINTER
Assignment:     #4
*/

% 1
% Base Cases
myfun(1,3).
myfun(2,4).
% Recursive Case
myfun(N,Result) :- integer(N), N >= 3, N1 is N-1, N2 is N-2, myfun(N1,R1), myfun(N2,R2), Result is R1 + 2*R2.

%2 
% Base Case
listmax([],0).
% Recursive Case
listmax([H|T],Result) :- listmax(T,PlaceHolder), Result is max(H,PlaceHolder).

%3
% Base Case
replace([],_,_,[]).
% Recursive Cases
replace([Target|T], Target, Replace,[Replace|Result]) :- replace(T, Target, Replace, Result).
replace([H|T], Target, Replace,[H|Result]) :- H \= Target, replace(T, Target, Replace, Result).