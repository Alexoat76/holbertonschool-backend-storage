-- Show and compute average score
/* SET FOREIGN_KEY_CHECKS=0; -- to disable them
drop table users;
SET FOREIGN_KEY_CHECKS=1; -- to re-enable the */
SELECT * FROM users;
SELECT * FROM corrections;

SELECT "--";
CALL ComputeAverageScoreForUser((SELECT id FROM users WHERE name = "Jeanne"));

SELECT "--";
SELECT * FROM users;
