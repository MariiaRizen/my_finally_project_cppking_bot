import json
import os
import json




def read_recipes_file():
    # current_dir = os.getcwd()
    # file_path = os.path.join(current_dir, 'recipes.json')
    file_path = 'C:\\Users\\Admin\\PycharmProjects\\my_finally_project_cppking_bot\\recipes.json'
    with open(file_path, 'r', encoding='utf-8') as file:
        recipes = json.load(file)

        return recipes


read_recipes_file()



