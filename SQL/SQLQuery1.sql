CREATE TABLE Department (
    DepartmentId INT PRIMARY KEY,
    DepartmentName VARCHAR(100),
    Acronym VARCHAR(20)
);

CREATE TABLE BatchYear (
    BatchYearId INT PRIMARY KEY,
    YearNumber INT,
    YearInRomanNumber VARCHAR(20)
);

CREATE TABLE Semester (
    SemesterId INT PRIMARY KEY,
    SemesterNumber VARCHAR(20),
    SemesterInRomanNumber VARCHAR(20)
);

CREATE TABLE Course (
    CourseId INT PRIMARY KEY,
    CourseTitle VARCHAR(100),
    CourseCode VARCHAR(50),
    CreditHours INT,
    DepartmentId INT,
    BatchYearId INT,
    SemesterId INT,
    FOREIGN KEY (DepartmentId) REFERENCES Department(DepartmentId),
    FOREIGN KEY (BatchYearId) REFERENCES BatchYear(BatchYearId),
    FOREIGN KEY (SemesterId) REFERENCES Semester(SemesterId)
);

CREATE TABLE Instructor (
    InstructorId INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    AcademicRank VARCHAR(50),
    DepartmentId INT,
    FOREIGN KEY (DepartmentId) REFERENCES Department(DepartmentId)
);

CREATE TABLE Section (
    SectionId INT PRIMARY KEY,
    SectionName VARCHAR(50)
);

CREATE TABLE AcademicYear (
    AcademicYearId INT PRIMARY KEY,
    AcademicYearGC VARCHAR(20),
    AcademicYearEC VARCHAR(20),
    Status BIT
);

CREATE TABLE CourseOffering (
    CourseOfferingId INT PRIMARY KEY,
    AcademicYearId INT,
    CourseId INT,
    InstructorId INT,
    SectionId INT,
    OfferingDate DATETIME,
    FOREIGN KEY (AcademicYearId) REFERENCES AcademicYear(AcademicYearId),
    FOREIGN KEY (CourseId) REFERENCES Course(CourseId),
    FOREIGN KEY (InstructorId) REFERENCES Instructor(InstructorId),
    FOREIGN KEY (SectionId) REFERENCES Section(SectionId)
);


INSERT INTO BatchYear (BatchYearId, YearNumber, YearInRomanNumber)
VALUES
  (1, 2018, 'MMXVIII'),
  (2, 2019,   'MMXIX'),
  (3, 2020,    'MMXX'),
  (4, 2021,   'MMXXI');

  INSERT INTO Department (DepartmentId, DepartmentName, Acronym)
VALUES
  (1, 'Computer Science', 'CSE'),
  (2, 'Mathematics',      'MAT'),
  (3, 'Physics',          'PHY'),
  (4, 'Chemistry',       'CHEM'),
  (5, 'Biology',          'BIO');


  INSERT INTO Course
    (CourseId,
     CourseTitle,
     CourseCode,
     CreditHours,
     DepartmentId,
     BatchYearId)
VALUES
  (1, 'Introduction to Programming',   'CSE101', 3, 1, 1),
  (2, 'Data Structures',               'CSE201', 4, 1, 1),
  (3, 'Calculus I',                    'MAT101', 3, 2, 1),
  (4, 'Linear Algebra',                'MAT202', 3, 2, 2),
  (5, 'General Physics I',             'PHY101', 4, 3, 2),
  (6, 'Classical Mechanics',           'PHY201', 4, 3, 3),
  (7, 'Organic Chemistry',             'CHEM301',3, 4, 3),
  (8, 'Biology of Cells',              'BIO101', 3, 5, 4),
  (9, 'Database Systems',              'CSE301', 3, 1, 2),
  (10,'Software Engineering',          'CSE401', 3, 1, 4);


  INSERT INTO Instructor
    (InstructorId, FirstName, LastName, AcademicRank, DepartmentId)
VALUES
  (1,  'Alice',    'Johnson',    'Assistant Professor', 1),
  (2,  'Benjamin', 'Smith',      'Associate Professor', 1),
  (3,  'Carla',    'Davis',      'Professor',           1),
  (4,  'David',    'Martinez',   'Lecturer',            1),
  (5,  'Emma',     'Lopez',      'Assistant Professor', 2),
  (6,  'Frank',    'Garcia',     'Associate Professor', 2),
  (7,  'Grace',    'Rodriguez',  'Professor',           2),
  (8,  'Henry',    'Wilson',     'Lecturer',            2),
  (9,  'Isabella', 'Anderson',   'Assistant Professor', 3),
  (10, 'Jack',     'Thomas',     'Associate Professor', 3),
  (11, 'Katherine','Taylor',     'Professor',           3),
  (12, 'Liam',     'Moore',      'Lecturer',            3),
  (13, 'Mia',      'Jackson',    'Assistant Professor', 4),
  (14, 'Noah',     'White',      'Associate Professor', 4),
  (15, 'Olivia',   'Harris',     'Professor',           4),
  (16, 'Peter',    'Martin',     'Lecturer',            4),
  (17, 'Quinn',    'Thompson',   'Assistant Professor', 5),
  (18, 'Ryan',     'Garrett',    'Associate Professor', 5),
  (19, 'Sophia',   'Perez',      'Professor',           5),
  (20, 'Thomas',   'Murphy',     'Lecturer',            5);