import os
import json
from parsers.klopotenko import klopotenko_parser
from dotenv import load_dotenv


load_dotenv()

outpath = os.path.join(os.environ['KLOPOTENKO_DATA_DIR'], 'categories_list.json')
categories = klopotenko_parser.get_all_categories()

with open(outpath, 'w') as fout:
    fout.write(json.dumps(categories))

