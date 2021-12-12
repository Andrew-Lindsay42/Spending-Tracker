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
    user = None
    sql = 'SELECT * FROM users WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        user = User(result['name'], result['budget'], result['payday'], result['id'])
    return user

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(user):
    pass