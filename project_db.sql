create database project;

create table patients (
    dob DATE,
    iin CHAR(12),
    patientId INT PRIMARY KEY,
    full_name VARCHAR(255),
    blood_group VARCHAR(50),
    emergency_contact_number CHAR(12),
    contact_number CHAR(12),
    email VARCHAR(250),
    home_address VARCHAR(250),
    marital_status VARCHAR(250),
    registration_date DATE,
    username VARCHAR(50),
    doctorId INT
);
CREATE TABLE doctor (
    dateOfBirth DATE,
    iin CHAR(12),
    doctorId INT PRIMARY KEY ,
    patientID INT,
    username VARCHAR(50),
    
    fullName VARCHAR(255),
    phoneNumber CHAR(12),
    departmentId INT,
    specializationsId INT,
    experience INT,
    category VARCHAR(50),
    price INT,
    scheduleDetails VARCHAR(255),
    education VARCHAR(50),
    rating INT,
    address VARCHAR(50),
    email VARCHAR(250)
);

CREATE TABLE authentification (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(50),
    userType VARCHAR(20)
);
