from sqlalchemy import text, insert
from database import engine, session_factory
from models import metadata_obj, WorkersOrm

# def get_123_sync():
#     with engine.connect() as conn:
#         res = conn.execute(text("SELECT 1,2,3 union select 4,5,6"))
#         print(f"{res.first()=}")

class SyncORM:
    @staticmethod
    def create_tables():
        metadata_obj.drop_all(engine)
        metadata_obj.create_all(engine)
        engine.echo = True

    @staticmethod
    #  ещё есть асинхронный вариант, но это синхронный
    def insert_data():
        with session_factory() as session:
            worker_sandy = WorkersOrm(cats_names='Sandy')
            worker_candy = WorkersOrm(cats_names='Candy')
            session.add_all([worker_sandy, worker_candy])
            session.commit()

    @staticmethod
    def select_workers():
        with session_factory() as session:
            worker_id = 1
            worker = session.get(WorkersOrm, worker_id)

    @staticmethod
    def update_workers(worker_id: int = 1, new_username: str = 'Mura'):
        with engine.connect() as conn:
            pass