from sqlalchemy import Table, Column, Integer, String, MetaData

metadata_obj = MetaData()

#  императивный стиль создания таблиц:
workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("cats_names", String)
)
