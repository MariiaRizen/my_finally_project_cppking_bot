import os
import json
from dotenv import load_dotenv
from parsers.klopotenko import klopotenko_parser


load_dotenv()

links_filepath = os.path.join(os.environ['KLOPOTENKO_DATA_DIR'], 'categories_links.json')
outpath = os.path.join(os.environ['KLOPOTENKO_DATA_DIR'], 'recipes.json')

with open(links_filepath, 'r') as fin:
    category_links = json.loads(fin.read())

i = 0
recipes = []
for category, recipes_url in category_links.items():
    for recipy_url in recipes_url:
        try:
            print(f'Now processing url - {recipy_url}')
            recipy = klopotenko_parser.parse_recipy(recipy_url)
            recipy['category'] = category
            recipes.append(recipy)
            i = i + 1
        except Exception as e:
            print(f'error on parsing url - {recipy_url}. Original error - {e}')

        #if i >= 15:
            #i = 0
            #break

        #if i >= 1000:
            #break


with open(outpath, 'w', encoding="utf-8") as fout:
    json.dump(recipes, fout, ensure_ascii=False)

