# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def general():
#     return 'general'
#
# if __name__ == '__main__':
#     app.run(debug=True)

import os
import sys
sys.path.insert(1, os.path.join(sys.path[0],'..'))

# from queries.core import create_tables, insert_data
# from queries.orm import create_tables, insert_data

# create_tables()
# insert_data()

from queries.core import SyncCore # AsyncCore
from queries.orm import SyncORM # AsyncORM

# SyncCore.create_tables()
# SyncCore.insert_workers()
# SyncCore.update_workers()
# SyncCore.select_workers()

SyncORM.create_tables()
SyncORM.update_workers()
# SyncORM.insert_workers()
SyncORM.select_workers()

