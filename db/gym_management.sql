DROP TABLE IF EXISTS lesson_bookings;
DROP TABLE IF EXISTS lessons;
DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS instructors;

CREATE TABLE instructors(
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    email_address VARCHAR(255)
);

CREATE TABLE clients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date_of_birth DATE,
    email_address VARCHAR(255)
);

CREATE TABLE lessons(
    id SERIAL PRIMARY KEY,
    activity VARCHAR(255),
    duration INT,
    lesson_date DATE,
    lesson_time TIME,
    capacity INT,
    instructor_id INT REFERENCES instructors(id)
);

CREATE TABLE lesson_bookings(
    id serial PRIMARY KEY,
    client_id INT REFERENCES clients(id) ON DELETE CASCADE,
    lesson_id INT REFERENCES lessons(id) ON DELETE CASCADE,
    UNIQUE (client_id,lesson_id)
);