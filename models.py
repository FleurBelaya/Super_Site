# # # !!!!! декларативный стиль !!!!!!

from database import Base
from sqlalchemy.orm import Mapped, mapped_column

class WorkersOrm(Base):
    __tablename__ = 'workers'
    id: Mapped[int] = mapped_column(primary_key=True)
    cats_names: Mapped[str]


# # # !!!!! императивный стиль создания таблиц: !!!!!!

from sqlalchemy import Table, Column, Integer, String, MetaData

# # # # # # # # # # # #
metadata_obj = MetaData()

workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("cats_names", String)
)
# # # # # # # # # # # #
