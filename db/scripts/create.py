import os
import sqlite3
from dotenv import load_dotenv


load_dotenv()


create_script = """
CREATE TABLE recipes(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
description TEXT,
ingredients TEXT,
steps TEXT,
image_path TEXT,
category TEXT
)
"""


conn = sqlite3.connect(os.environ['DB_PATH'])
conn.execute(create_script)
