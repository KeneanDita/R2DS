CREATE PROCEDURE numberofInstructor
  @DeptId VARCHAR(20)
AS
BEGIN
  SELECT COUNT(*) FROM Instructor WHERE
DepartmentId = @DeptId 
END

EXEC numberofInstructor 1;


CREATE PROCEDURE allInfo
  @DeptId VARCHAR(20)
AS
BEGIN
  SELECT * FROM Instructor WHERE 
DepartmentId = @DeptId
END

EXEC allInfo 1;


CREATE FUNCTION GetInstructorByDeptId(
  @DeptId VARCHAR(20)
  )
  RETURNS TABLE
AS
RETURN(
  SELECT * FROM Instructor WHERE 
DepartmentId = @DeptId
);

SELECT * FROM dbo.GetInstructorByDeptId(2);


CREATE FUNCTION GetFullInsName(
  @FirstName VARCHAR(50),
  @LastName VARCHAR(50)
)
RETURNS VARCHAR(101)
AS
BEGIN
  RETURN @FirstName + ' ' + @LastName
  
END

SELECT DBO.GetFullInsName(FirstName, LastName)
AS FullName FROM Instructor;

CREATE INDEX idx_