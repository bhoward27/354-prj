DROP DATABASE IF EXISTS project;
CREATE DATABASE project;
USE project;

CREATE TABLE Item (
    item_ID char(9) NOT NULL,
    price DEC(4, 2),
    quantity TINYINT NOT NULL,
    available TINYINT NOT NULL,
    title VARCHAR(64) NOT NULL,
    publisher VARCHAR(64),
    genre VARCHAR(16),
    picture BLOB,
    language VARCHAR(16),
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