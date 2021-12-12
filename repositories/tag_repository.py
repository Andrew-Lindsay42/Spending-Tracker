from db.run_sql import run_sql
from models.tag import Tag

def save(tag):
    pass

def select_all():
    tag_list = []
    sql = 'SELECT * FROM tags'
    result = run_sql(sql)

    for row in result:
        tag = Tag(row['name'], row['active'], row['icon_num'], row['id'])
        tag_list.append(tag)
    return tag_list

def select(id):
    pass

def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM tags WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(tag):
    pass