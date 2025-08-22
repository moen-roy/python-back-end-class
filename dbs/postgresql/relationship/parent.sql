CREATE TABLE IF NOT EXISTS parent (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR (250) NOT NULL    
);
CREATE TABLE IF NOT EXISTS parent_address(
    id BIGSERIAL PRIMARY KEY,
    parent_id BIGSERIAL REFERENCES parent(id),
    county_name VARCHAR(100),
    town VARCHAR (250),
    logitude REAL,
    latitude REAL,
    house_number VARCHAR (200)

);

INSERT INTO parent
(name,email)
VALUES 
('moen','roy@gmail.com'),
('miroy','oen@gmail.com');

INSERT INTO parent_address
(parent_id,county_name,town,logitude,latitude,house_number)
VALUES
(1,'Nakuru','naivasha',-023,43,'h23'),
(3,'Kiambu','zambo',009,-004,'j45')


