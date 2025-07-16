from sqlalchemy import text, insert, inspect, select
from database import engine, session_factory
from models import metadata_obj, WorkersOrm

# def get_123_sync():
#     with engine.connect() as conn:
#         res = conn.execute(text("SELECT 1,2,3 union select 4,5,6"))
#         print(f"{res.first()=}")

class SyncORM:
    @staticmethod
    def create_tables():
        engine.echo = False
        metadata_obj.drop_all(engine)
        metadata_obj.create_all(engine)
        engine.echo = True

    @staticmethod
    #  ещё есть асинхронный вариант, но это синхронный
    def insert_workers():
        with session_factory() as session:
            worker_sandy = WorkersOrm(username='Sandy')
            worker_candy = WorkersOrm(username='Candy')
            session.add_all([worker_sandy, worker_candy])
            session.flush()
            # flush()
            # Сохраняет изменения в базу в рамках текущей транзакции
            # Не завершает транзакцию (commit() это делает)
            # Позволяет получить, например, сгенерированный id у объекта до commit
            # Пример!
            # new_post = Post(title="Hello", user_id=new_user.id)
            # db.add(new_post)
            # db.flush()  # ! Теперь new_post.id уже есть !
            session.commit()

    @staticmethod
    def select_workers():
        with session_factory() as session:
            # worker_id = 1
            # worker = session.get(WorkersOrm, worker_id)
            # print(worker)
            query = select(WorkersOrm)  # SELECT * FROM WORKERS
            res = session.execute(query)
            print(f'{res.all()=}')

    @staticmethod
    def update_workers(worker_id: int = 1, new_username: str = 'Queen Mura'):
        with session_factory() as session:
            worker = session.get(WorkersOrm, worker_id)
            worker.username = new_username
            session.commit()
