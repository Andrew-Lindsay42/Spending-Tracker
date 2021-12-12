from db.run_sql import run_sql
from models.user import User

def save(user):
    sql = "INSERT INTO users (name, budget, payday) VALUES (%s, %s, %s) RETURNING *"
    values = [user.name, user.budget, user.payday]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return user

def select_all():
    user_list = []
    sql = 'SELECT * FROM users'
    result = run_sql(sql)

    for row in result:
        user = User(row['name'], float(row['budget']), row['payday'], row['id'])
        user_list.append(user)
    return user_list

def select(id):
    user = None
    sql = 'SELECT * FROM users WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        user = User(result['name'], float(result['budget']), result['payday'], result['id'])
    return user

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(user):
    sql = "UPDATE users SET (name, budget, payday) = (%s, %s, %s) WHERE id = %s"
    values = [user.name, user.budget, user.payday, user.id]
    run_sql(sql, values)