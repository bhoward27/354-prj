DROP DATABASE IF EXISTS project;
CREATE DATABASE project;
USE project;

CREATE TABLE Member(
    lib_card_num CHAR(7) NOT NULL,
    address VARCHAR(127),
    password VARCHAR(25) NOT NULL,
    status BLOB,
    fName VARCHAR(15) NOT NULL,
    mName VARCHAR(15),
    lName VARCHAR(15) NOT NULL,
    email VARCHAR(31),
    PRIMARY KEY (lib_card_num)
);

CREATE TABLE Item (
    item_ID CHAR(9) NOT NULL,
    price DEC(4, 2),
    quantity TINYINT NOT NULL,
    available TINYINT NOT NULL,
    title VARCHAR(63) NOT NULL,
    publisher VARCHAR(63),
    genre VARCHAR(15),
    language VARCHAR(15),
    picture VARCHAR(255),
    lib_card_num CHAR(7) DEFAULT NULL,
    PRIMARY KEY (item_ID),
    FOREIGN KEY (lib_card_num) REFERENCES Member(lib_card_num)
);

CREATE TABLE Book (
    ISBN13 SMALLINT NOT NULL,
    item_ID CHAR(9) NOT NULL,
    FOREIGN KEY (item_ID) REFERENCES Item(item_ID)
);

CREATE TABLE DVD (
    ISSN SMALLINT NOT NULL,
    item_ID CHAR(9) NOT NULL,
    FOREIGN KEY (item_ID) REFERENCES Item(item_ID)
);

CREATE TABLE CD (
    ISSN SMALLINT NOT NULL,
    item_ID CHAR(9) NOT NULL,
    FOREIGN KEY (item_ID) REFERENCES Item(item_ID)
);

CREATE TABLE Reservation(
    item_ID CHAR(9) NOT NULL,
    reserveDate DATE NOT NULL,
    lib_card_num CHAR(7),
    queueNum TINYINT
);

CREATE TABLE LoanedItem(
    lib_card_num CHAR(7) NOT NULL,
    borrow_ID SMALLINT NOT NULL,
    timestame TIME,
    PRIMARY KEY (borrow_ID),
    FOREIGN KEY (lib_card_num) REFERENCES Member(lib_card_num)
);