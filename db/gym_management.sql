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
    duration TIME,
    lesson_date DATE,
    lesson_time TIME,
    instructor_id INT REFERENCES instructors(id)
);