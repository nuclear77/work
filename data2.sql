CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(255)
);

INSERT INTO Students (student_id, student_name) VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Charlie');

CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(255)
);

INSERT INTO Courses (course_id, course_name) VALUES
(1, 'Math'),
(2, 'Physics'),
(3, 'Chemistry');
