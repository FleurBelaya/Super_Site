from sqlalchemy import text, insert
from database import engine
from models import metadata_obj, workers_table

# def get_123_sync():
#     with engine.connect() as conn:
#         res = conn.execute(text("SELECT 1,2,3 union select 4,5,6"))
#         print(f"{res.first()=}")


def create_tables():
    metadata_obj.drop_all(engine)
    metadata_obj.create_all(engine)
    engine.echo = True



def insert_data():
    with (engine.connect() as conn):
        # stmt = """INSERT INTO workers (cats_names) VALUES
        # ('Honey'),
        # ('Mura');"""
        stmt = insert(workers_table).values([
            {'cats_names': 'Honey'},
            {'cats_names': 'Muraaa'}
        ])
        conn.execute(stmt)
        conn.commit()

