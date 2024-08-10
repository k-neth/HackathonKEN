
SELECT * FROM Users
WHERE CreateDate >= DATEADD(DAY, -30, GETDATE());


SELECT COUNT(*) AS TotalUsers
FROM Users
WHERE Email LIKE '%@example.com';

UPDATE Users
SET Email = 'newemail@example.com'
WHERE UserId = 123;


given a database table 'Users' with columns 'UserId','Username','Password','Email', and 'CreateDate', write SQL queries to 
-Retrieve all users who registered within the last 30 days
-find total number of users with a specific domain in their email(e.g., all users with emails ending in @example.comp)
-update the email of a user with a specific 'UserId'