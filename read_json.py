import json
import os
import json
import re



def read_recipes_file():
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, 'recipes.json')
    with open(file_path, 'r', encoding='utf-8') as file:
        recipes = json.loads(file.read())

        return recipes


read_recipes_file()


