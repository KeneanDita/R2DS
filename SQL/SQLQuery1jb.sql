CREATE FUNCTION GetFullInstName
(
@FirstName VARCHAR(50),
@LastName VARCHAR(50)
)
RETURNS VARCHAR(101)
AS
BEGIN
RETURN @FirstName + ' ' + @LastName;
END

EXEC numberofInstructor 2;

CREATE FUNCTION GetFullInstName
(
@FirstName VARCHAR(50),
@LastName VARCHAR(50)
)
RETURNS VARCHAR(101)
AS
BEGIN
RETURN @FirstName + ' ' + @LastName;
END

SELECT dbo.GetFullInstName(FirstName, LastName) 
AS FullName FROM Instructor;

CREATE INDEX idx_FirstName ON
Instructor (FirstName);

SELECT * FROM Instructor WHERE FirstName = 'Carla';