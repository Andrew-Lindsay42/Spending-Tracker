from db.run_sql import run_sql
from models.tag import Tag

def save(tag):
    pass

def select_all():
    pass

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