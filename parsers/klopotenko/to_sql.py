import os
import json
import sqlite3
from dotenv import load_dotenv
from enums.sections import category_mapper

load_dotenv()


inpath = os.path.join(os.environ['KLOPOTENKO_DATA_DIR'], 'recipes.json')

with open(inpath, 'r', encoding="utf8") as fin:
    js_recipes = json.loads(fin.read())


insert_query = """
INSERT INTO recipes (title, description, ingredients, steps, image_path, category)
VALUES (?, ?, ?, ?, ?, ?)
"""

conn = sqlite3.connect(os.environ['DB_PATH'])
cur = conn.cursor()

for js in js_recipes:
    try:
        if len(js['description'] + js['ingredients'] + js['steps']) > 4095:
            continue
        new_category = category_mapper[js['category']]
        row = (js['title'], js['description'], js['ingredients'],
               js['steps'], js['image_path'], new_category)
        cur.execute(insert_query, row)
        conn.commit()
    except Exception as e:
        if str(e).startswith('UNIQUE constraint failed:'):
            continue
        print(f'Unexpected error occurred. Skipping it. Error message - {e}')

print(13)
