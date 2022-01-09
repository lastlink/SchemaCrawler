CREATE DATABASE SCHEMA_A_A;
CREATE DATABASE SCHEMA_A_B;

CREATE TABLE SCHEMA_A_A.A_A_TABLE1
(
  Id INT PRIMARY KEY NOT NULL,
  Name VARCHAR(40) NOT NULL
);

CREATE TABLE SCHEMA_A_A.A_A_TABLE2
(
  Id INT PRIMARY KEY NOT NULL,
  Name VARCHAR(40) NOT NULL,
  FK_COL_TO_A_A INT NOT NULL,
  CONSTRAINT FK_A_A_TO_A_A FOREIGN KEY (FK_COL_TO_A_A) REFERENCES SCHEMA_A_A.A_A_TABLE1 (Id)
);

CREATE TABLE SCHEMA_A_B.A_B_TABLE2
(
  Id INT PRIMARY KEY NOT NULL,
  Name VARCHAR(40) NOT NULL,
  FK_COL_TO_A_A INT NOT NULL,
  CONSTRAINT FK_A_B_TO_A_A FOREIGN KEY (FK_COL_TO_A_A) REFERENCES SCHEMA_A_A.A_A_TABLE1 (Id)
);

CREATE VIEW SCHEMA_A_B.A_B_VIEW1
AS
  SELECT * FROM SCHEMA_A_A.A_A_TABLE2
;
