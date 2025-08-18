-- gets all the data i the student table columns
    -- SELECT * FROM student;

-- getting specified data from the table columns
    -- SELECT id, name,email,phone,marks,created_at FROM student;\

--FILTERING THE DATA
    -- SELECT * FROM student
    -- WHERE pocket_money > 500
    -- AND
    -- marks >= 50

-- ARRANGING DATA IN DESENDNG FORMAT
    -- SELECT * FROM student
    -- ORDER BY  marks DESC

-- ARRANGING DATA IN ASCENDING FORMAT
    --  SELECT * FROM student
    -- ORDER BY marks ASC

--ADDING A LIMIT TO DATA RETRIVAL
    SELECT * FROM student
    ORDER BY  marks DESC
    limit 3