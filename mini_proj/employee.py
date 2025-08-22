from db import PG

class Employee():
    def __init__(self):
        pg= PG()
        self.pg=pg
        query="""
            CREATE TABLE IF NOT EXISTS employee(
              id BIGSERIAL PRIMARY KEY,
              name TEXT NOT NULL,
              email TEXT NOT NULL UNIQUE
              )
        """
        pg.pg_query(query=query)
        
    def add (self,name,email):
        pg= PG()
        query= """
                INSERT INTO employee
                (name,email)
                VALUES (%s,%s)
        """
        pg.pg_query(query=query,params= (name,email))

    def all(self):
        pg=PG()
        query="""
         SELECT * FROM Employee
        """
        results=pg.pg_query(query=query)
         #print(results)
        for employee in results:
            print(employee)
        return
emp1=Employee()
emp1.add("oen","oy@gmail.com")
emp1.all()