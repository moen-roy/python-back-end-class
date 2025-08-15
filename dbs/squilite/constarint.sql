CREATE Table if NOT EXISTS student(
    id INTEGER PRIMARY KEY autoincrement,
    name TEXT,
    email TEXT,
    dob TEXT,
    phone INTEGER,
    marks REAL    
);

insert into student (name,email,dob,phone, marks)
values ('Roy','roy@gmail.com','100-9939-93',12345678,344.433)