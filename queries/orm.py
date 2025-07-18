from sqlalchemy import text, insert, inspect, select, cast, Integer, func, and_
from database import engine, session_factory, Base
from models import metadata_obj, WorkersOrm, ResumesOrm, Workload

# def get_123_sync():
#     with engine.connect() as conn:
#         res = conn.execute(text("SELECT 1,2,3 union select 4,5,6"))
#         print(f"{res.first()=}")

class SyncORM:
    @staticmethod
    def create_tables():
        engine.echo = False
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
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
            # parent = Author(name="John")
            # db.add(parent)
            # db.flush()  # Получаем parent.id до коммита !
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

            # session.expire_all()
            # Обнуляет кэш всех объектов в сессии —
            # при следующем доступе к полям произойдёт запрос к БД

            # session.refresh(worker)
            # Перезагружает объект worker из БД,
            # чтобы получить самые актуальные значения

            session.commit()

    @staticmethod
    def insert_resumes():
        with session_factory() as session:
            resume_jack_1 = ResumesOrm(
                title="Python Junior Developer",
                compensation=50000,
                workload=Workload.fulltime,
                worker_id=1
            )
            resume_jack_2 = ResumesOrm(
                title="Python Разработчик",
                compensation=150000,
                workload=Workload.fulltime,
                worker_id=1
            )
            resume_michael_1 = ResumesOrm(
                title="Python Data Engineer",
                compensation=250000,
                workload=Workload.parttime,
                worker_id=2
            )
            resume_michael_2 = ResumesOrm(
                title="Data Scientist",
                compensation=300000,
                workload=Workload.fulltime,
                worker_id=2
            )

            session.add_all([
                resume_jack_1,
                resume_jack_2,
                resume_michael_1,
                resume_michael_2
            ])
            session.commit()

        engine.echo = True

    @staticmethod
    def select_resumes_avg_compensation(like_language: str = "Python"):
        """
        SQL-подобный запрос:
        select workload, avg(compensation)::int as avg_compensation
        from resumes
        where title like '%Python%' and compensation > 40000
        group by workload
        having avg(compensation)::int > 70000
        """
        with session_factory() as session:
            query = (
                select(
                    ResumesOrm.workload,
                    cast(func.avg(ResumesOrm.compensation), Integer).label("avg_compensation")
                )
                .select_from(ResumesOrm)
                .filter(
                    and_(
                        ResumesOrm.title.contains(like_language),
                        ResumesOrm.compensation > 40000
                    )
                )
                .group_by(ResumesOrm.workload)
                .having(cast(func.avg(ResumesOrm.compensation), Integer) > 70000)
            )

            print(query.compile(compile_kwargs={"literal_binds": True}))
            res = session.execute(query)
            result = res.all()
            print(result[0].avg_compensation)
