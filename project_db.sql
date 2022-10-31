create database project;

create table patients (
    dob DATE,
    iin CHAR(12),
    patientId bigserial PRIMARY KEY,
    full_name VARCHAR(255),
    blood_group VARCHAR(50),
    emergency_contact_number CHAR(12),
    contact_number CHAR(12),
    email VARCHAR(250),
    home_address VARCHAR(250),
    marital_status VARCHAR(250),
    registration_date DATE,
    FOREIGN KEY (doctorId) REFERENCES doctor (doctorId);
    
);
CREATE TABLE doctor (
    dateOfBirth DATE,
    iin BIGINT,
    id PRIMARY KEY,
    patientId FOREIGN KEY,
    fullName VARCHAR(255),
    phoneNumber VARCHAR(50),
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
