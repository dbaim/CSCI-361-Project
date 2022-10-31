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
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(50),
    username VARCHAR(50),
    sex CHAR(1),
    address VARCHAR(50),
    phoneNumber varchar(50),
    email VARCHAR(250)
);