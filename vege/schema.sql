/*
Jacob McKenna
UAF CS601
MySQL Vege Database
*/

-- Create Database if it doesn't exist.
CREATE Database IF NOT EXISTS vege;

-- Create table if it doesn't exist.
-- User must belong to a bank.
CREATE TABLE IF NOT EXISTS User (

	id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
	fname VARCHAR(40) NOT NULL,
	lname VARCHAR(40) NOT NULL,
	iz INTEGER UNIQUE NOT NULL,
	izhk INTEGER DEFAULT 100 NOT NULL,
	mothersMaidenName VARCHAR(40)

) AUTO_INCREMENT = 100000000;

CREATE TABLE IF NOT EXISTS VIP_User(

	id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
	password VARCHAR(400) NOT NULL,
	user INTEGER NOT NULL,
	FOREIGN KEY (user) REFERENCES User(iz)

); 

CREATE TABLE IF NOT EXISTS Vegetable (

	id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
	name VARCHAR(40) UNIQUE NOT NULL

);

CREATE TABLE IF NOT EXISTS Bids (

	id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
	bid INTEGER NOT NULL,
	vege VARCHAR(40) NOT NULL,
	bidding_user INTEGER NOT NULL,
	FOREIGN KEY (vege) REFERENCES Vegetable (name),
	FOREIGN KEY (bidding_user) REFERENCES User (iz)
);

ALTER TABLE User ADD COLUMN izhk INTEGER DEFAULT 100;

INSERT INTO User (fname, lname, iz) VALUES ('prime', 'minister', 999999);
INSERT INTO VIP_User (password, user) VALUES ('$5$rounds=535000$WsGEWLTYHMlHyTd7$TFIP0giw7WDWD//2XBxH34GRC9mC/azE6GDvvaUEuhD', 999999);





INSERT INTO Vegetable (name) VALUES ('Potato');
INSERT INTO Vegetable (name) VALUES ('Onion');
INSERT INTO Vegetable (name) VALUES ('Turnip');
INSERT INTO Vegetable (name) VALUES ('Imported Turnip');

INSERT INTO Bids (bid, vege, bidding_user) VALUES (1000, 'Potato', 999999);




