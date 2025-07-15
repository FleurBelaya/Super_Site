from sqlalchemy import text, insert, select, update
from database import engine
from models import metadata_obj, workers_table

# def get_123_sync():
#     with engine.connect() as conn:
#         res = conn.execute(text("SELECT 1,2,3 union select 4,5,6"))
#         print(f"{res.first()=}")


# def create_tables():
#     metadata_obj.drop_all(engine)
#     metadata_obj.create_all(engine)
#     engine.echo = True
#
#
#
# def insert_data():
#     with (engine.connect() as conn):
#         # stmt = """INSERT INTO workers (cats_names) VALUES
#         # ('Honey'),
#         # ('Mura');"""
#         stmt = insert(workers_table).values([
#             {'cats_names': 'Honey'},
#             {'cats_names': 'Muraaa'}
#         ])
#         conn.execute(stmt)
#         conn.commit()


class SyncCore:
    @staticmethod
    def create_tables():
        engine.echo = False
        metadata_obj.drop_all(engine)
        metadata_obj.create_all(engine)
        engine.echo = True

    @staticmethod
    def insert_workers():
        with engine.connect() as conn:
        # stmt = """INSERT INTO workers (username) VALUES
        #  ('name1'),
        #  ('name2');"
            stmt = insert(workers_table).values(
                [{"username": "Candy"},
                {"username": "Honey"},]
            )
            conn.execute(stmt)
            conn.commit()

    @staticmethod
    def select_workers():
        with engine.connect() as conn:
            query = select(workers_table)  # SELECT * FROM WORKERS
            res = conn.execute(query)
            print(f'{res.all()=}')

    @staticmethod
    def update_workers(worker_id: int = 1, new_username: str = 'Mura'):
        with engine.connect() as conn:
            # stmt = text('UPDATE workers SET username=:username WHERE id=:id')
            # stmt = stmt.bindparams(username=new_username, id=worker_id)
            stmt = (
                update(workers_table)
                .values(username=new_username)
                # .where(workers_table.c.id==worker_id)
                .filter_by(id=worker_id)
            )
            conn.execute(stmt)
            conn.commit()
