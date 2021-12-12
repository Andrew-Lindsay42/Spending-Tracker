from db.run_sql import run_sql
from models.user import User

def save(user):
    pass

def select_all():
    user_list = []
    sql = 'SELECT * FROM users'
    result = run_sql(sql)

    for row in result:
        user = User(row['name'], row['budget'], row['payday'], row['id'])
        user_list.append(user)
    return user_list

def select(id):
    pass

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(user):
    pass