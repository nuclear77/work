SELECT Students.student_name, Courses.course_name
FROM Students
LEFT JOIN Courses ON Students.student_id = Courses.course_id;
