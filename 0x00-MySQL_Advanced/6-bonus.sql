-- SQL script that creates a stored procedure that adds a new correction for a student.
-- Procedure takes 3 inputs (in this order):
-- user_id, a users.id value
-- project_name, a new or already exists projects
-- score, the score value for the correction
DELIMITER //
CREATE PROCEDURE AddBonus(IN user_id INTEGER, IN project_name VARCHAR(255), IN score FLOAT)
BEGIN
    INSERT INTO projects (name)
    SELECT project_name from DUAL
    WHERE NOT EXISTS (SELECT * FROM projects WHERE name=project_name LIMIT 1);

    INSERT INTO corrections (user_id, project_id, score)
    VALUES(user_id, (SELECT id from projects WHERE name=project_name), score);
END//
DELIMITER;
