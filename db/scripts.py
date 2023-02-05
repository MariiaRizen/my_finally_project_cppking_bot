# import os
# import sqlite3
# from dotenv import load_dotenv
#
# load_dotenv()
#
# con = sqlite3.connect(os.environ['DB_PATH'])
# cur = con.cursor()
#
#
# def create_tables():
#     cur.execute("""CREATE TABLE cooking(
#     id PRIMARY KEY,
#     name VARCHAR(127),
#     section VARCHAR(63),
#     recipe VARCHAR,
#     image VARCHAR(511),
#     video VARCHAR
#
#     )""")
#
#
# def inserts_one():
#     cur.execute("""
#             INSERT INTO cooking_db VALUES()""")
#
#
# def inserts_many():
#     pass

