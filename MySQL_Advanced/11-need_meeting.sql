-- Creates a view need_meeting listing students with score < 80
-- and no last_meeting or last_meeting older than 1 month
CREATE VIEW need_meeting AS
    SELECT name
    FROM students
    WHERE score < 80
      AND (last_meeting IS NULL
           OR last_meeting < ADDDATE(CURDATE(), INTERVAL -1 MONTH));
