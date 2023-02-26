import os
import json
from parsers.klopotenko import klopotenko_parser
from dotenv import load_dotenv


load_dotenv()

categories_filepath = os.path.join(os.environ['KLOPOTENKO_DATA_DIR'], 'categories_list.json')
outpath = os.path.join(os.environ['KLOPOTENKO_DATA_DIR'], 'categories_links.json')


with open(categories_filepath, 'r') as fin:
    data = fin.read()
    categoris = json.loads(data)

res = dict()
for category in categoris:
    print(f'Now extracting links for category - {category}')
    links = klopotenko_parser.get_all_category_links(category)
    res[category] = links

with open(outpath, 'w') as fout:
    fout.write(json.dumps(res))


print()