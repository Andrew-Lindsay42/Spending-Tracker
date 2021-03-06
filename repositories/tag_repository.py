from db.run_sql import run_sql
from models.tag import Tag

def save(tag):
    sql = 'INSERT INTO tags (name, active, icon_num) VALUES (%s, %s, %s) RETURNING *'
    values = [tag.name, tag.active, tag.icon_num]
    results = run_sql(sql, values)
    id = results[0]['id']
    tag.id = id
    return tag

def select_all():
    tag_list = []
    sql = 'SELECT * FROM tags'
    result = run_sql(sql)

    for row in result:
        tag = Tag(row['name'], row['active'], row['icon_num'], row['id'])
        tag_list.append(tag)
    return tag_list

def select(id):
    tag = None
    if id is not None:
        sql = 'SELECT * FROM tags WHERE id = %s'
        values = [id]
        result = run_sql(sql, values)[0]
        
        if result is not None:
            tag = Tag(result['name'], result['active'], result['icon_num'], result['id'])
    return tag

def delete_all():
    sql = 'DELETE FROM tags'
    run_sql(sql)

def delete(id):
    sql = 'DELETE FROM tags WHERE id = %s'
    values = [id]
    run_sql(sql, values)

def update(tag):
    sql = 'UPDATE tags SET (name, active, icon_num) = (%s, %s, %s) WHERE id = %s'
    values = [tag.name, tag.active, tag.icon_num, tag.id]
    run_sql(sql, values)

def get_active():
    tag_list = []
    sql = 'SELECT * FROM tags WHERE active = True'
    result = run_sql(sql)

    for row in result:
        tag = Tag(row['name'], row['active'], row['icon_num'], row['id'])
        tag_list.append(tag)
    tag_list.sort(key= lambda tag : tag.name)
    return tag_list

def get_inactive():
    tag_list = []
    sql = 'SELECT * FROM tags WHERE active = False'
    result = run_sql(sql)

    for row in result:
        tag = Tag(row['name'], row['active'], row['icon_num'], row['id'])
        tag_list.append(tag)
    tag_list.sort(key= lambda tag : tag.name)
    return tag_list
