# # # !!!!! декларативный стиль !!!!!!

from database import Base
from sqlalchemy.orm import Mapped, mapped_column

class WorkersOrm(Base):
    _table_args_ = {"schema": "public"}
    __tablename__ = 'workers'

    id: Mapped[int] = mapped_column(primary_key=True)
    cats_names: Mapped[str]

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


# # # !!!!! императивный стиль создания таблиц: !!!!!!

from sqlalchemy import Table, Column, Integer, String, MetaData

# # # # # # # # # # # #
metadata_obj = MetaData()

workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String)
)
# # # # # # # # # # # #
