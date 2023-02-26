import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()

conn = sqlite3.connect(os.environ['DB_PATH'])
conn.row_factory = sqlite3.Row
cur = conn.cursor()


def retreive_query_result(q):
    res = cur.execute(q)
    res = res.fetchone()
    res = res and dict(res)
    return res


def get_first_category_recipy(category: str):
    q = f"""
    select *
    from recipes
    where category = '{category}'
    limit 1
    """
    return retreive_query_result(q)


def get_recipy_by_title(title):
    q = f"""
    select * 
    from recipes
    where title = '{title}'
    """
    return retreive_query_result(q)


def get_neighbour_recipy(recipy_id: int, category, forward_direction: bool):
    sign = '+' if forward_direction else '-'
    q = f"""
    with cte as (select row_number() OVER () as rn, *
    from recipes
    where category = '{category}'
    )
    select * from cte 
    where rn = (
    select (((select rn from cte where id = {recipy_id}) - 1 {sign} 1 + 
        (select count(*) from cte)) % (select count(*) from cte)) + 1)
    """
    return retreive_query_result(q)


if __name__ == '__main__':
    get_first_category_recipy('snidanki')
