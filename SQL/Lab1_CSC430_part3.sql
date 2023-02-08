-- QUESTION 3

create database lab1_ending; 

use lab1_ending;

CREATE TABLE BRANCH ( 
branchID int not null PRIMARY KEY, 
BranchName varchar (40) not null, 
BranchAddress varchar (40) not null
);

CREATE TABLE ACCOUNT_TYPE ( 
AccTypeID int not null PRIMARY KEY, 
AccountType varchar (30) not null
);

CREATE TABLE CUSTOMER ( 
SSN int not null PRIMARY KEY, 
name varchar (30) not null, 
Phone varchar (20),
Address varchar (40) not null
);

CREATE TABLE ACCOUNT ( 
AccNo int not null PRIMARY KEY, 
AccTypeID int not null, 
Branch int not null,
SSN int not null, 
Balance decimal(15,2) not null,
FOREIGN KEY (Branch) REFERENCES BRANCH (branchID),
FOREIGN KEY (SSN) REFERENCES CUSTOMER (SSN)
);
