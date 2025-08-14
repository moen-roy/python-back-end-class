CREATE Table if NOT EXISTS student(
    id SERIAL PRIMARY KEY ,
    name TEXT,
    email TEXT,
    dob DATE,
    phone INTEGER,
    marks REAL,
    is_married BOOLEAN,
    created_at TIMESTAMP  DEFAULT CURRENT_TIMESTAMP    
);

insert into student (name,email,dob,phone, marks,is_married)
values ('On','on@gmail.com','2024-1-2',212345678,444.434, false);