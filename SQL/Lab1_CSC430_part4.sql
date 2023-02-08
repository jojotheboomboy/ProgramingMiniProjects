-- QUESTION 4

INSERT INTO BRANCH (branchID, BranchName, BranchAddress)
VALUES (101, 'Tree', '432 Maple Street.');

INSERT INTO BRANCH (branchID, BranchName, BranchAddress)
VALUES (202, 'Egg', '1001 Bacon Blvd');

INSERT INTO BRANCH (branchID, BranchName, BranchAddress)
VALUES (303, 'SML', '4218 Functional Way');

INSERT INTO BRANCH (branchID, BranchName, BranchAddress)
VALUES (430, 'PHP', '1232 Bad-Lang Blvd');

INSERT INTO CUSTOMER (SSN, name, Phone, Address)
VALUES (123456789, 'Sam Fry', null, '1819 Green street');

INSERT INTO CUSTOMER (SSN, name, Phone, Address)
VALUES (987654321, 'Bob Smith', '318-985-4532', '1819 Green street');

INSERT INTO ACCOUNT (AccNo, AccTypeID, Branch, SSN, Balance)
VALUES (121, 1, 101, 123456789, 1.00);

INSERT INTO ACCOUNT (AccNo, AccTypeID, Branch, SSN, Balance)
VALUES (122, 2, 101, 123456789, 10.00);

INSERT INTO ACCOUNT (AccNo, AccTypeID, Branch, SSN, Balance)
VALUES (123, 3, 101, 123456789, 100.00);

INSERT INTO ACCOUNT (AccNo, AccTypeID, Branch, SSN, Balance)
VALUES (124, 4, 101, 123456789, 1000.00);

INSERT INTO ACCOUNT (AccNo, AccTypeID, Branch, SSN, Balance)
VALUES (125, 4, 202, 123456789, 10000.00);

INSERT INTO ACCOUNT_TYPE (AccTypeID, AccountType)
VALUES(1, 'Checking');

INSERT INTO ACCOUNT_TYPE ( AccTypeID, AccountType)
VALUES(2, 'Savings');

INSERT INTO ACCOUNT_TYPE ( AccTypeID, AccountType)
VALUES(3, 'Credit Card');

INSERT INTO ACCOUNT_TYPE ( AccTypeID, AccountType)
VALUES(4, 'Mortgage');

