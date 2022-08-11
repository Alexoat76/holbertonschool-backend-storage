-- SQL script that creates a stored procedure that computes and store the average
-- Score for a student. An average score can be a decimal.
-- Procedure takes 1 input:
-- user_id, a users.id value
DELIMITER //
CREATE PROCEDURE ComputeOverallScoreForUser
(IN user_id INT) 
BEGIN
   UPDATE users SET overall_score = 
   (SELECT AVG(score) FROM corrections WHERE corrections.user_id=user_id GROUP BY corrections.user_id )
   WHERE id=user_id;
END//
DELIMITER ;
