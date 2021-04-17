DROP DATABASE IF EXISTS project;
CREATE DATABASE project;
USE project;

CREATE TABLE Member(
    lib_card_num CHAR(10) NOT NULL,
    address VARCHAR(100) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(20) NOT NULL,
    status TINYINT NOT NULL,
    fines DEC(5, 2) NOT NULL,
    fName VARCHAR(20) NOT NULL,
    mName VARCHAR(20),
    lName VARCHAR(20) NOT NULL,
    PRIMARY KEY (lib_card_num)
);

CREATE TABLE Item (
    item_ID     CHAR(10) NOT NULL,
    bookISBN    CHAR(14) NULL,
    cdISSN      CHAR(12) NULL,
    dvdISSN     CHAR(12) NULL,
    quantity TINYINT NOT NULL,
    availability TINYINT NOT NULL,

    PRIMARY KEY (item_ID),
    FOREIGN KEY (bookISBN) REFERENCES Book(ISBN13),
    FOREIGN KEY (cdISSN) REFERENCES CD(ISSN),
    FOREIGN KEY (dvdISSN) REFERENCES DVD(ISSN),
    CONSTRAINT ItemFKs CHECK (
        (
            (CASE WHEN bookISBN IS NULL THEN 0 ELSE 1 END) +
            (CASE WHEN cdISSN IS NULL THEN 0 ELSE 1 END) +
            (CASE WHEN dvdISSN IS NULL THEN 0 ELSE 1 END)
        ) = 1
    )
);

CREATE TABLE Book (
    ISBN13 CHAR(14) NOT NULL,
    price DEC(5, 2) NOT NULL,
    dd_num VARCHAR(10),
    title VARCHAR(63) NOT NULL,
    publisher VARCHAR(63),
    language VARCHAR(15),
    picture VARCHAR(255),
    PRIMARY KEY (ISBN13)
);

CREATE TABLE DVD (
    ISSN CHAR(12) NOT NULL,
    price DEC(5, 2) NOT NULL,
    dd_num VARCHAR(10),
    title VARCHAR(63) NOT NULL,
    publisher VARCHAR(63),
    language VARCHAR(15),
    picture VARCHAR(255),
    PRIMARY KEY (ISSN)
);

CREATE TABLE CD (
    ISSN CHAR(12) NOT NULL,
    price DEC(5, 2) NOT NULL,
    dd_num VARCHAR(10),
    title VARCHAR(63) NOT NULL,
    publisher VARCHAR(63),
    language VARCHAR(15),
    picture VARCHAR(255),
    PRIMARY KEY (ISSN)
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
    borrow_ID BIGINT NOT NULL,
    timestamp DATETIME NOT NULL,
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

INSERT INTO member VALUES
('1234567890', '123 Flynn St.', 'cooldude@hotmail.com', '123', 1, 0, 'Dude', NULL, 'Smith'),
('1234567891', '123 Main St.', 'cristian@sfu.ca', '123', 1, 0, 'Cristian', NULL,'John'),
('1234567892', '123 Street Ave.', 'darebear@gmail.com', 'Seinfeld', 1, 0, 'Darren', NULL, 'Bear'),
('1234567893', '8888 University Dr.', 'sfu@sfu.ca', 'sfu', 1, 0, 'Kurt', NULL, 'Fraser'),
('1234567894', '13450 102 Ave.', 'alex@sfu.ca', 'password', 1, 0, 'Alex', NULL, 'Cap');

INSERT INTO Item VALUES
('0000000001', 6.00, 1, 1, NULL, 'Moby-Dick', 'PBS', NULL, NULL, NULL),
('0000000002', 7.00, 1, 1, NULL, 'Death on the Nile', 'William Morrow Paperbacks', NULL, NULL, NULL),
('0000000003', 12.50, 1, 1, NULL, 'Blood of Elves', 'Orbit', NULL, NULL, NULL),
('0000000004', 9.50, 1, 1, NULL, 'The Time of Contempt', 'Orbit', NULL, NULL, NULL),
('0000000005', 12.50, 1, 1, NULL, 'Baptism of Fire', 'Orbit', NULL, NULL, NULL);

INSERT INTO Book VALUES
('978-0553213119', '0000000001'),
('978-0062073556', '0000000002'),
('978-0316438988', '0000000003'),
('978-0316219136', '0000000004'),
('978-0316219181', '0000000005');

INSERT INTO Item VALUES
('0000000006', 13.99, 1, 1, NULL, 'Shrek', 'DreamWorks', NULL, NULL, NULL),
('0000000007', 5.00, 1, 1, NULL, 'Shrek 2', 'DreamWorks', NULL, NULL, NULL),
('0000000008', 5.00, 1, 1, NULL, 'Shrek the Third', 'DreamWorks', NULL, NULL, NULL),
('0000000009', 13.99, 1, 1, NULL, 'Shrek Forever After', 'DreamWorks', NULL, NULL, NULL),
('0000000010', 13.99, 1, 1, NULL, 'Shrek the Halls', 'DreamWorks', NULL, NULL, NULL);

INSERT INTO DVD VALUES
('667068824421', '0000000006'),
('678149087321', '0000000007'),
('505118913383', '0000000008'),
('191329061091', '0000000009'),
('097368523944', '0000000010');

INSERT INTO Item VALUES
('0000000011', 9.99, 1, 1, NULL, 'Queen Greatest Hits', 'Hollywood Records', NULL, NULL, NULL),
('0000000012', 9.99, 1, 1, NULL, 'Under The Iron Sea', 'Universal Island Records', NULL, NULL, NULL),
('0000000013', 9.99, 1, 1, NULL, 'Eyes Open', 'Universal Music', NULL, NULL, NULL),
('0000000014', 9.99, 1, 1, NULL, 'Grammy Nominees 2007', 'Sony BMG Music', NULL, NULL, NULL),
('0000000015', 9.99, 1, 1, NULL, 'Grammy Nominees 2008', 'Universal Music', NULL, NULL, NULL);

INSERT INTO CD VALUES
('720616246523', '0000000011'),
('602498568279', '0000000012'),
('602498531785', '0000000013'),
('886970382724', '0000000014'),
('602517581029', '0000000015');

INSERT INTO Reservation VALUES
('0000000001', '2021-01-01', '1234567890', 1),
('0000000002', '2021-02-02', '1234567890', 1),
('0000000006', '2021-03-03', '1234567890', 1),
('0000000007', '2021-03-03', '1234567890', 1),
('0000000011', '2021-03-03', '1234567890', 1);

INSERT INTO LoanedItem VALUES
('1234567891', 1, '2021-03-04 10:00:00'),
('1234567891', 2, '2021-03-04 10:00:00'),
('1234567891', 3, '2021-03-04 10:00:00'),
('1234567891', 4, '2021-03-04 10:00:00'),
('1234567891', 5, '2021-03-04 10:00:00');

INSERT INTO Authors VALUES
('Herman Melville', '0000000001'),
('Agatha Christie', '0000000002'),
('Andrzej Sapkowski', '0000000003'),
('Andrzej Sapkowski', '0000000004'),
('Andrzej Sapkowski', '0000000005');

INSERT INTO DVDActors VALUES
('Mike Myers', '0000000006'),
('Eddie Murphy', '0000000006'),
('Cameron Diaz', '0000000006'),
('John Lithgow', '0000000006'),
('Vincent Cassel', '0000000006');

INSERT INTO DVDDirectors VALUES
('Andrew Adamson', '0000000006'),
('Vicky Jenson', '0000000006'),
('Kelly Asbury', '0000000007'),
('Conrad Vernon', '0000000007'),
('Chris Miller', '0000000008'),
('Raman Hui', '0000000008');

INSERT INTO CDArtist VALUES
('Queen', '0000000011'),
('Keane', '0000000012'),
('Snow Patrol', '0000000013'),
('Varius Artists', '0000000014'),
('Varius Artists', '0000000015');

INSERT INTO ItemGenre VALUES
('Comedy', '0000000006'),
('Comedy', '0000000007'),
('Comedy', '0000000008'),
('Comedy', '0000000009'),
('Comedy', '0000000010');

INSERT INTO MemberPhone VALUES
('1234567890', '6045551212'),
('1234567891', '6045551213'),
('1234567892', '6045551214'),
('1234567893', '6045551215'),
('1234567894', '6045551216');
