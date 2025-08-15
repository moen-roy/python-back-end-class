CREATE Table if NOT EXISTS student(
    id SERIAL PRIMARY KEY ,
    name VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    dob DATE,
    phone INTEGER NOT NULL UNIQUE,
    marks REAL CHECK (marks >-1 AND marks < 101),
    is_married BOOLEAN NOT NULL DEFAULT false,
    created_at TIMESTAMP  DEFAULT CURRENT_TIMESTAMP    
);

-- insert into student (name,email,dob,phone, marks,is_married)
-- values ('On','on@gmail.com','2024-1-2',212345678,444.434, false);