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
from queries.core import create_tables, insert_data

create_tables()
insert_data()

