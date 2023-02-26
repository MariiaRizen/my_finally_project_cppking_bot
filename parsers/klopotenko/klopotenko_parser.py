import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup


load_dotenv()

images_path = os.environ['KLOPOTENKO_IMGS_DIR']
start_page = 'https://klopotenko.com/reczepti/'
get_recipes_links_url = 'https://klopotenko.com/wp-admin/admin-ajax.php'
payload_get_recipes = {
    'action': 'loadmore',
    'page': 0,
}
query_payload_unf = '"page":0,"posts_per_page":1000,"ranna_recipe_category":"{category}","term":"{category}","error":"","m":"","p":0,"post_parent":"","subpost":"","subpost_id":"","attachment":"","attachment_id":0,"name":"","pagename":"","page_id":0,"second":"","minute":"","hour":"","day":0,"monthnum":0,"year":0,"w":0,"category_name":"","tag":"","cat":"","tag_id":"","author":"","author_name":"","feed":"","tb":"","paged":0,"meta_key":"","meta_value":"","preview":"","s":"","sentence":"","title":"","fields":"","menu_order":"","embed":"","category__in":[],"category__not_in":[],"category__and":[],"post__in":[],"post__not_in":[],"post_name__in":[],"tag__in":[],"tag__not_in":[],"tag__and":[],"tag_slug__in":[],"tag_slug__and":[],"post_parent__in":[],"post_parent__not_in":[],"author__in":[],"author__not_in":[],"ignore_sticky_posts":false,"suppress_filters":false,"cache_results":true,"update_post_term_cache":true,"update_menu_item_cache":false,"lazy_load_term_meta":true,"update_post_meta_cache":true,"post_type":"","nopaging":false,"comments_per_page":"50","no_found_rows":false,"taxonomy":"ranna_recipe_category","order":"DESC"'


def _get_category_post_payload(category):
    payload = payload_get_recipes.copy()
    payload['query'] = '{' + query_payload_unf.format(category=category) + '}'
    return payload


def get_all_categories():
    r = requests.get(start_page, verify=False)
    soup = BeautifulSoup(r.text)
    categories_soup = soup.find('ul', {"class": "sub-menu"})
    categories = categories_soup.find_all('li')
    categories = [x.a['href'].split('/')[-2] for x in categories]
    return categories


def get_all_category_links(category):
    payload_category = _get_category_post_payload(category)
    r = requests.post(get_recipes_links_url, verify=False, data=payload_category)
    soup = BeautifulSoup(r.text)
    titles_html = soup.find_all('h3', {'class': "item-title"})
    links = [x.a['href'].strip() for x in titles_html]
    return links


def save_image(image_url):
    image_name = image_url.split('?')[0].split('/')[-1]
    outpath = os.path.join(os.environ['KLOPOTENKO_IMGS_DIR'], image_name)
    ir = requests.get(image_url, verify=False)
    with open(outpath, 'wb') as fout:
        fout.write(ir.content)
    rel_outpath = os.path.relpath(outpath, os.environ['DATA_DIR'])
    return rel_outpath


def parse_recipy(recipy_url):
    r = requests.get(recipy_url, verify=False)
    soup = BeautifulSoup(r.text)

    res = dict()

    res['title'] = soup.find('h1', {'class': 'item-title'}).text.strip()

    description_html = soup.find('div', {"class": "item-description"})
    res['description'] = '\n'.join([x.text for x in description_html.find_all('p')])

    ingredients = soup.find('div', {'class': "ingredient-list"})
    ingredients = [x.text.strip() for x in ingredients.find_all('label')]
    res['ingredients'] = '\n'.join(ingredients)

    steps = soup.find('div', {'class': 'direction-wrap-layout1'})
    steps = [x.text.strip() for x in steps.find_all('p')[:-1]]

    new_steps = []
    for step_number, step_description in enumerate(steps):
        new_step = f'Крок {step_number + 1}: {step_description}'
        new_steps.append(new_step)

    res['steps'] = '\n'.join(new_steps)
    img_url = soup.find('div', {'class': "item-figure lazy-no"}).img['data-src']
    img_path = save_image(img_url)
    res['image_path'] = img_path

    return res

