# # # !!!!! декларативный стиль !!!!!!

import datetime
from typing import Optional, Annotated
from sqlalchemy import TIMESTAMP, Enum, Table, Column, Integer, String, MetaData, ForeignKey, func, text
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
import enum

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.utcnow,
    )]

class WorkersOrm(Base):
    __table_args__ = {"schema": "public"}
    __tablename__ = 'workers'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]

class Workload(enum.Enum):
    parttime = "parttime"
    fulltime = "fulltime"
    # Это перечисление (enum): означает,
    # что поле workload в резюме может иметь только два значения

class ResumesOrm(Base):
    __tablename__ = "resumes"
    __table_args__ = {"schema": "public"}

    id: Mapped[intpk]
    title: Mapped[str] = mapped_column(String(356))
    compensation: Mapped[Optional[int]]
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey("public.workers.id", ondelete="CASCADE"))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

# class ResumesOrm(Base):
#     __tablename__ = "resumes"
#
#     id: Mapped[intpk]
#     title: Mapped[str_256]
#     compensation: Mapped[Optional[int]]
#     workload: Mapped[Workload]
#     worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id", ondelete="CASCADE"))
#     created_at: Mapped[created_at]
#     updated_at: Mapped[updated_at]


from sqlalchemy import Table, Column, Integer, String, MetaData
import datetime

# # # # # # # # # # # #
metadata_obj = MetaData(schema="public")

workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String),
)

resumes_table = Table(
    "resumes",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("title", String(256)),
    Column("compensation", Integer, nullable=True),
    Column("workload", Enum(Workload)),
    Column("worker_id", ForeignKey("workers.id", ondelete="CASCADE")),
    Column("created_at", TIMESTAMP,server_default=text("TIMEZONE('utc', now())")),
    Column(
        "updated_at",
        TIMESTAMP,
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.now(datetime.timezone.utc)
    )
)
# # # # # # # # # # # #
