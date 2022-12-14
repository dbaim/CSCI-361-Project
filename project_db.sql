DROP TABLE IF EXISTS authentification CASCADE;
DROP TABLE IF EXISTS doctor CASCADE;
DROP TABLE IF EXISTS patients CASCADE;
DROP TABLE IF EXISTS appointment CASCADE;

CREATE TABLE authentification (
    username VARCHAR(50) UNIQUE PRIMARY KEY,
    password VARCHAR(50) NOT NULL,
    userType VARCHAR(20) NOT NULL
);

CREATE TABLE patients (
    dob DATE,
    iin CHAR(12) UNIQUE NOT NULL,
    patientId INT PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    blood_group VARCHAR(50),
    emergency_contact_number CHAR(12),
    contact_number CHAR(12) UNIQUE NOT NULL,
    email VARCHAR(250) UNIQUE NOT NULL,
    home_address VARCHAR(250),
    marital_status VARCHAR(250),
    registration_date DATE NOT NULL,
    username VARCHAR(50) REFERENCES authentification(username) NOT NULL,
    doctorId INT
);

CREATE TABLE doctor (
    dateOfBirth DATE,
    iin CHAR(12) UNIQUE NOT NULL,
    doctorId INT UNIQUE,
    patientID INT UNIQUE NOT NULL,
    username VARCHAR(50) REFERENCES authentification(username) NOT NULL,    
    fullName VARCHAR(255) UNIQUE NOT NULL,
    phoneNumber CHAR(12) UNIQUE NOT NULL,
    departmentId INT NOT NULL,
    specializationsId INT,
    experience INT,
    category VARCHAR(50),
    price INT,
    scheduleDetails VARCHAR(255),
    education VARCHAR(50),
    rating INT,
    address VARCHAR(50) NOT NULL,
    email VARCHAR(250) UNIQUE NOT NULL,
	CONSTRAINT doc_key PRIMARY KEY (doctorid, fullname)
);

CREATE TABLE appointment (
    type VARCHAR(50) NOT NULL,
    description VARCHAR(100),
    date DATE UNIQUE NOT NULL,
    doctor INT REFERENCES doctor(doctorId) NOT NULL,
    patient INT REFERENCES patients(patientId) NOT NULL,
	doc_name VARCHAR(255) REFERENCES doctor(fullname) NOT NULL,
    available BOOLEAN NOT NULL,
    CONSTRAINT app_key PRIMARY KEY (date, doctor)
);
