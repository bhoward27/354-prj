DROP DATABASE IF EXISTS project;
CREATE DATABASE project;
USE project;

CREATE TABLE Member(
    lib_card_num    INT NOT NULL AUTO_INCREMENT,
    address         VARCHAR(100) NOT NULL,
    email           VARCHAR(50) NOT NULL,
    password        VARCHAR(20) NOT NULL,
    fName           VARCHAR(20) NOT NULL,
    mName           VARCHAR(20),
    lName           VARCHAR(20) NOT NULL,
    
    PRIMARY KEY (lib_card_num)
);

CREATE TABLE Item (
    item_id         INT NOT NULL AUTO_INCREMENT,
    bookISBN        CHAR(14) NULL,
    cdISSN          CHAR(12) NULL,
    dvdISSN         CHAR(12) NULL,
    availability    TINYINT NOT NULL DEFAULT 1,

    PRIMARY KEY (item_ID),
    FOREIGN KEY (bookISBN)  REFERENCES Book(ISBN13),
    FOREIGN KEY (cdISSN)    REFERENCES CD(ISSN),
    FOREIGN KEY (dvdISSN)   REFERENCES DVD(ISSN),
    CONSTRAINT FK_Item CHECK (
        (
            (CASE WHEN bookISBN IS NULL THEN 0 ELSE 1 END) +
            (CASE WHEN cdISSN IS NULL THEN 0 ELSE 1 END) +
            (CASE WHEN dvdISSN IS NULL THEN 0 ELSE 1 END)
        ) = 1
    )
);

CREATE TABLE Status (
    -- status is good iff. (fines <= 0 and numOverdueItems == 0).
    lib_card_num        INT NOT NULL,
    fines                DEC(5, 2) DEFAULT 0.0,
    numOverdueItems     INT DEFAULT 0,

    PRIMARY KEY (lib_card_num),
    FOREIGN KEY (lib_card_num)  REFERENCES Member(lib_card_num)
);

CREATE TABLE Book (
    ISBN13      CHAR(14) NOT NULL,
    price       DEC(5, 2) NOT NULL,
    dd_num      VARCHAR(10),
    title       VARCHAR(63) NOT NULL,
    publisher   VARCHAR(63),
    language    VARCHAR(15),
    picture     VARCHAR(255),

    PRIMARY KEY (ISBN13)
);

CREATE TABLE DVD (
    ISSN        CHAR(12) NOT NULL,
    price       DEC(5, 2) NOT NULL,
    dd_num      VARCHAR(10),
    title       VARCHAR(63) NOT NULL,
    publisher   VARCHAR(63),
    language    VARCHAR(15),
    picture     VARCHAR(255),

    PRIMARY KEY (ISSN)
);

CREATE TABLE CD (
    ISSN        CHAR(12) NOT NULL,
    price       DEC(5, 2) NOT NULL,
    dd_num      VARCHAR(10),
    title       VARCHAR(63) NOT NULL,
    publisher   VARCHAR(63),
    language    VARCHAR(15),
    picture     VARCHAR(255),

    PRIMARY KEY (ISSN)
);

CREATE TABLE Reservation(
    item_ID         INT NOT NULL,
    reserveDate     DATE NOT NULL,
    lib_card_num    INT NOT NULL,
    queueNum        TINYINT NOT NULL,

    FOREIGN KEY (item_ID)       REFERENCES Item(item_ID),
    FOREIGN KEY (lib_card_num)  REFERENCES Member(lib_card_num),
    CONSTRAINT PK_Reserve PRIMARY KEY (item_ID, reserveDate, lib_card_num, queueNum)
);

CREATE TABLE LoanedItem(
    lib_card_num    INT NOT NULL,
    item_id         INT NOT NULL,
    timestamp       DATETIME NOT NULL,

    PRIMARY KEY (lib_card_num, item_id),
    FOREIGN KEY (lib_card_num)  REFERENCES Member(lib_card_num),
    FOREIGN KEY (item_id)       REFERENCES Item(item_id)
);

CREATE TABLE Authors(
    author      VARCHAR(100) NOT NULL,
    bookISBN    CHAR(14) NOT NULL,

    FOREIGN KEY (bookISBN) REFERENCES Book(ISBN13),
    CONSTRAINT PK_Author PRIMARY KEY (author, bookISBN)
);

CREATE TABLE DVDActors(
    actor       VARCHAR(100) NOT NULL,
    dvdISSN     CHAR(12) NOT NULL,

    FOREIGN KEY (dvdISSN) REFERENCES DVD(ISSN),
    CONSTRAINT PK_DVDActor PRIMARY KEY (actor, dvdISSN)
);

CREATE TABLE DVDDirectors(
    director    VARCHAR(100) NOT NULL,
    dvdISSN     CHAR(12) NOT NULL,

    FOREIGN KEY (dvdISSN) REFERENCES DVD(ISSN),
    CONSTRAINT PK_DVDDirector PRIMARY KEY (director, dvdISSN)
);

CREATE TABLE CDArtist(
    artist      VARCHAR(100) NOT NULL,
    cdISSN      CHAR(12) NOT NULL,

    FOREIGN KEY (cdISSN) REFERENCES CD(ISSN),
    CONSTRAINT PK_CDArtist PRIMARY KEY (artist, cdISSN)
);

CREATE TABLE BookGenre(
    genre       VARCHAR(15) NOT NULL,
    bookISBN    CHAR(14) NOT NULL,

    FOREIGN KEY (bookISBN) REFERENCES Book(ISBN13),
    CONSTRAINT PK_BookGenre PRIMARY KEY (genre, bookISBN)
);

CREATE TABLE CDGenre(
    genre       VARCHAR(15) NOT NULL,
    cdISSN      CHAR(12) NOT NULL,

    FOREIGN KEY (cdISSN) REFERENCES CD(ISSN),
    CONSTRAINT PK_BookGenre PRIMARY KEY (genre, cdISSN)
);

CREATE TABLE DVDGenre(
    genre       VARCHAR(15) NOT NULL,
    dvdISSN     CHAR(12) NOT NULL,

    FOREIGN KEY (dvdISSN) REFERENCES DVD(ISSN),
    CONSTRAINT PK_DVDGenre PRIMARY KEY (genre, dvdISSN)
);

CREATE TABLE MemberPhone(
    lib_card_num    INT NOT NULL,
    phone           CHAR(10) NOT NULL,
    FOREIGN KEY (lib_card_num) REFERENCES Member(lib_card_num),
    CONSTRAINT PK_MemberPhone PRIMARY KEY (lib_card_num, phone)
);

INSERT INTO Member (address, email, password, fName, mName, lName) VALUES
('123 Flynn St.', 'cooldude@hotmail.com', '123', 'Dude', NULL, 'Smith'),
('123 Main St.', 'cristian@sfu.ca', '123', 'Cristian', NULL,'John'),
('123 Street Ave.', 'darebear@gmail.com', 'Seinfeld', 'Darren', NULL, 'Bear'),
('8888 University Dr.', 'sfu@sfu.ca', 'sfu', 'Kurt', NULL, 'Fraser'),
('13450 102 Ave.', 'alex@sfu.ca', 'password', 'Alex', NULL, 'Cap');


INSERT INTO Book (ISBN13, price, title, publisher, language) VALUES
('978-0553213119', 6.00, 'Moby Dick', 'PBS', 'English'),
('978-0062073556', 7.00, 'Death on the Nile', 'William Morrow Paperbacks', 'English'),
('978-0316438988', 12.50, 'Blood of Elves', 'Orbit', 'English'),
('978-0316219136', 9.50, 'The Time of Contempt', 'Orbit', 'English'),
('978-0316219181', 12.50, 'Baptism of Fire', 'Orbit', 'English');

INSERT INTO Item (bookISBN) VALUES
('978-0553213119'),
('978-0062073556'),
('978-0316438988'),
('978-0316219136'),
('978-0316219181');


INSERT INTO DVD (ISSN, price, title, publisher, language) VALUES
('667068824421', 13.99, 'Shrek', 'DreamWorks', 'English'),
('678149087321', 5.00, 'Shrek 2', 'DreamWorks', 'English'),
('505118913383', 5.00, 'Shrek the Third', 'DreamWorks', 'English'),
('191329061091', 13.99, 'Shrek Forever After', 'DreamWorks', 'English'L),
('097368523944', 13.99, 'Shrek the Halls', 'DreamWorks', 'English');

INSERT INTO Item (dvdISSN) VALUES
('667068824421'),
('678149087321'),
('505118913383'),
('191329061091'),
('097368523944');


INSERT INTO CD (ISSN, price, title, publisher, language) VALUES
('720616246523', 9.99, 'Queen Greatest Hits', 'Hollywood Records', 'English'),
('602498568279', 9.99, 'Under The Iron Sea', 'Universal Island Records', NULL),
('602498531785', 9.99, 'Eyes Open', 'Universal Music', NULL),
('886970382724', 9.99, 'Grammy Nominees 2007', 'Sony BMG Music', NULL),
('602517581029', 9.99, 'Grammy Nominees 2008', 'Universal Music', NULL);

INSERT INTO Item VALUES
('720616246523'),
('602498568279'),
('602498531785'),
('886970382724'),
('602517581029');

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
