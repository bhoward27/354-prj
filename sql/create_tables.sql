DROP DATABASE IF EXISTS project;
CREATE DATABASE project;
USE project;

CREATE TABLE Member(
    lib_card_num CHAR(10) NOT NULL,
    address VARCHAR(100) NOT NULL,
    password VARCHAR(25) NOT NULL,
    availability TINYINT NOT NULL,
    dd_num VARCHAR(10),
    fines DEC(5, 2),
    fName VARCHAR(20) NOT NULL,
    mName VARCHAR(20),
    lName VARCHAR(20) NOT NULL,
    email VARCHAR(50) NOT NULL,
    PRIMARY KEY (lib_card_num)
);

CREATE TABLE Item (
    item_ID CHAR(10) NOT NULL,
    price DEC(5, 2),
    quantity TINYINT NOT NULL,
    available TINYINT NOT NULL,
    title VARCHAR(63) NOT NULL,
    publisher VARCHAR(63),
    genre VARCHAR(15),
    language VARCHAR(15),
    picture VARCHAR(255),
    lib_card_num CHAR(10),
    FOREIGN KEY (lib_card_num) REFERENCES Member(lib_card_num),
    PRIMARY KEY (item_ID)
);

CREATE TABLE Book (
    ISBN13 SMALLINT NOT NULL,
    item_ID CHAR(10) NOT NULL,
    FOREIGN KEY (item_ID) REFERENCES Item(item_ID),
    PRIMARY KEY (item_ID)
);

CREATE TABLE DVD (
    ISSN SMALLINT NOT NULL,
    item_ID CHAR(10) NOT NULL,
    FOREIGN KEY (item_ID) REFERENCES Item(item_ID),
    PRIMARY KEY (item_ID)
);

CREATE TABLE CD (
    ISSN SMALLINT NOT NULL,
    item_ID CHAR(10) NOT NULL,
    FOREIGN KEY (item_ID) REFERENCES Item(item_ID),
    PRIMARY KEY (item_ID)
);

CREATE TABLE Reservation(
    item_ID CHAR(10) NOT NULL,
    reserveDate DATE NOT NULL,
    lib_card_num CHAR(10) NOT NULL,
    queueNum TINYINT NOT NULL,
    FOREIGN KEY (item_ID) REFERENCES Item(item_ID),
    FOREIGN KEY (lib_card_num) REFERENCES Member(lib_card_num),
    CONSTRAINT PK_Reserve PRIMARY KEY (item_ID, reserveDate, lib_card_num, queueNum)
);

CREATE TABLE LoanedItem(
    lib_card_num CHAR(10) NOT NULL,
    borrow_ID INT NOT NULL,
    timestame TIME,
    FOREIGN KEY (lib_card_num) REFERENCES Member(lib_card_num),
    PRIMARY KEY (lib_card_num, borrow_ID)
);

CREATE TABLE Authors(
    author VARCHAR(100) NOT NULL,
    item_ID CHAR(10) NOT NULL,
    FOREIGN KEY (item_ID) REFERENCES Item(item_ID),
    CONSTRAINT PK_Author PRIMARY KEY (author, item_ID)
);

CREATE TABLE DVDActors(
    actor VARCHAR(100) NOT NULL,
    item_ID CHAR(10) NOT NULL,
    FOREIGN KEY (item_ID) REFERENCES Item(item_ID),
    CONSTRAINT PK_DVDActor PRIMARY KEY (actor, item_ID)
);

CREATE TABLE DVDDirectors(
    director VARCHAR(100) NOT NULL,
    item_ID CHAR(10) NOT NULL,
    FOREIGN KEY (item_ID) REFERENCES Item(item_ID),
    CONSTRAINT PK_DVDDirector PRIMARY KEY (director, item_ID)
);

CREATE TABLE CDArtist(
    artist VARCHAR(100) NOT NULL,
    item_ID CHAR(10) NOT NULL,
    FOREIGN KEY (item_ID) REFERENCES Item(item_ID),
    CONSTRAINT PK_CDArtist PRIMARY KEY (artist, item_ID)
);

CREATE TABLE ItemGenre(
    genre VARCHAR(15) NOT NULL,
    item_ID CHAR(10) NOT NULL,
    FOREIGN KEY (item_ID) REFERENCES Item(item_ID),
    CONSTRAINT PK_ItemGenre PRIMARY KEY (genre, item_ID)
);

CREATE TABLE MemberPhone(
    lib_card_num CHAR(10) NOT NULL,
    phone CHAR(10) NOT NULL,
    FOREIGN KEY (lib_card_num) REFERENCES Member(lib_card_num),
    CONSTRAINT PK_MemberPhone PRIMARY KEY (lib_card_num, phone)
);
