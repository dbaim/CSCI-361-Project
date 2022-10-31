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
