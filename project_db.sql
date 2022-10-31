create database project;

create table patients (
    DOB date,
    IIN bigint,
    ID bigserial primary key,
    full_name varchar(255),
    blood_group varchar(50),
    emergency_contact_number varchar(50),
    contact_number varchar(50),
    email varchar(250),
    home_address varchar(250),
    marital_status varchar(250),
    registration_date date,
    -- primary key(ID)
);
CREATE TABLE doctor (
    dateOfBirth DATE,
    iin CHAR(12),
    doctorId PRIMARY KEY,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    fullName VARCHAR(255),
    phoneNumber CHAR(12),
    departmentId INT,
    specializationsId VARCHAR(50),
    experience INT,
    category VARCHAR(50),
    price INT,
    scheduleDetails VARCHAR(255),
    education VARCHAR(50),
    rating VARCHAR(2),
    address VARCHAR(50)
);

CREATE TABLE authentification (
    username VARCHAR(50),
    password VARCHAR(50),
    userType VARCHAR(20)
);
