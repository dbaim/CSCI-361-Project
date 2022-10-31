INSERT INTO authentification(username, password, userType) VALUES
('abcdefg', '§1234', 'patient'), 
('abcdefgag', '§1411', 'patient'), 
('NM3', '§46346', 'patient'),
('doctor_user', '523525', 'doctor');

INSERT INTO patients(dob, iin, patientId, full_name, blood_group, emergency_contact_number, contact_number, email, home_address, marital_status, registration_date, username, doctorID) VALUES
('2020-05-05', '02030601128', 13456, 'nurbek moldakhmetov1', '1 positive', '+77077077777', '+77073866437', 'abcdefg@mail.com', 'kabanbay batyr 53', 'single', '2020-06-05', 'abcdefg', 123456), 
('2020-07-05', '02030601129', 12456, 'nurbek moldakhmetov2', '2 positive', '+77077077777', '+77073866437', 'abcdefg@mail.com', 'kabanbay batyr 53', 'single', '2020-06-05', 'abcdefgag', 123456),
('2020-05-06', '02030601120', 19456, 'nurbek moldakhmetov3', '3 positive', '+77077077777', '+77073866437', 'abcdefg@mail.com', 'kabanbay batyr 53', 'single', '2020-06-05', 'NM3', 123456);

INSERT INTO doctor(dateOfBirth, iin, doctorId, patientId, username, fullName, phoneNumber, departmentId, specializationsId, experience, category, price, scheduleDetails, education, rating, address, email) VALUES
('1980-02-03', '800203550015', 123456, 13456, 'doctor_user', 'Erbolat nurbolat', '+77777777777', 321, 228, 20, 'lor', 2000, 'HZ', 'MSU', 9, 'turan 22', 'doctor21@mail.ru'); 
