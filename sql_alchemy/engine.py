from sql_alchemy import 
from

cp= (
            "host=aws-1-ca-central-1.pooler.supabase.com "
            "dbname=postgres "
            "user=postgres.ydzmjycrlxoypwfgasht "
            "password=defecebcrevbvbebhcvebvuiev "
            "port=5432"
        )
db_credentials={
    "drivername":"postgresql+psycopg",
    "host":"aws-1-ca-central-1.pooler.supabase.com ",
    "username":"postgres.ydzmjycrlxoypwfgasht",
    "password":"defecebcrevbvbebhcvebvuiev ",
    "port":"5432"    

}
DATABASE_URL=URL.create(**db_credentials)

engine=create_engine(DATABASE_URL,echo=True,future=True)

with engine.connect()as conn:
    result=conn.execute(text("SELECT*FROM "))
    rows=result.fetchall()

    fro row
