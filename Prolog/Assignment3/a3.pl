/*
NAME:           Josiah Norman
DATE:           1/20/2023
COURSE:         330-002
QUARTER:        WINTER
ASSIGNMENT:     3

*/

item(
	name(bread),
	quantity(50),
	price(0.90)
).

item(
	name(milk),
	quantity(30),
	price(2.50)
).

item(
	name(cheese),
	quantity(80),
	price(1.50)
).

item(
	name(chips),
	quantity(50),
	price(1.00)
).

item(
	name(apples),
	quantity(100),
	price(0.30)
).

getPrice(A,B) :- item(name(A),_,price(B)).

getQuantity(A,B) :- item(name(A),quantity(B),_).

lowerPrice(A,B) :- getPrice(A,C),getPrice(B,D),C<D.

computeGross(A,B) :- getPrice(A,C),getQuantity(A,D),B is C*D.

lowerGross(A,B) :- computeGross(A,C),computeGross(B,D),C<D.