DROP DATABASE IF EXISTS project;
CREATE DATABASE project;
USE project;

CREATE TABLE Item (
    item_ID char(9) NOT NULL,
    price DEC(4, 2),
    quantity TINYINT NOT NULL,
    available TINYINT NOT NULL,
    title VARCHAR(63) NOT NULL,
    publisher VARCHAR(63),
    genre VARCHAR(15),
    picture VARCHAR(255),
    language VARCHAR(15),
    PRIMARY KEY (item_ID)
);

CREATE TABLE Book (
    ISBN13 SMALLINT NOT NULL,
    item_ID char(9) NOT NULL,
    FOREIGN KEY (item_ID) REFERENCES Item(item_ID)
);

CREATE TABLE DVD (
    ISSN SMALLINT NOT NULL,
    item_ID char(9) NOT NULL,
    FOREIGN KEY (item_ID) REFERENCES Item(item_ID)
);

CREATE TABLE CD (
    ISSN SMALLINT NOT NULL,
    item_ID char(9) NOT NULL,
    FOREIGN KEY (item_ID) REFERENCES Item(item_ID)
);

CREATE TABLE Member(
    lib_card_num CHAR(7) NOT NULL,
    address VARCHAR(127),
    password VARCHAR(25) NOT NULL,
    status BLOB,
    fName VARCHAR(15) NOT NULL,
    mName VARCHAR(15),
    lName VARCHAR(15),
    email VARCHAR(31),
    PRIMARY KEY (lib_card_num)
);