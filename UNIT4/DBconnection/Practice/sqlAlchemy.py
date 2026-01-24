import sqlalchemy as db

from UNIT1.el2.p18 import result

engine = db.create_engine(
    "postgresql://postgres:kishikishore@localhost:54321/mydb"
)

with engine.connect() as conn:
    result = conn.execute(db.text("select * from strudent;"))
    print(result.fetchall())
