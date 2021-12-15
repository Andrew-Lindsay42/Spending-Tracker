from db.run_sql import run_sql
from models.user import User
import calendar
import datetime
from repositories import transaction_repository as transaction_repo

def save(user):
    sql = 'INSERT INTO users (name, budget, payday) VALUES (%s, %s, %s) RETURNING *'
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
    sql = 'DELETE FROM users'
    run_sql(sql)

def delete(id):
    sql = 'DELETE FROM users WHERE id = %s'
    values = [id]
    run_sql(sql, values)

def update(user):
    sql = 'UPDATE users SET (name, budget, payday) = (%s, %s, %s) WHERE id = %s'
    values = [user.name, user.budget, user.payday, user.id]
    run_sql(sql, values)

def get_days_till_payday(id):

    sql = 'SELECT * FROM users WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]
    days_to_go = 0
    if result is not None:
        payday = int(result['payday'])
        year = datetime.datetime.today().year
        month = datetime.datetime.today().month
        today = datetime.datetime.today().day

        days_in_month = calendar.monthrange(year, month)[1]
        
        if payday > days_in_month:
            payday = days_in_month

        days_to_go = payday - today

        if days_to_go < 0:
            days_to_go = (days_in_month - today) + payday
    return days_to_go


def get_remaining_budget(id):
    sql = 'SELECT * FROM users WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]
    remaining_budget = 0
    if result is not None:
        payday = int(result['payday'])
        remaining_budget = float(result['budget'])
        year = datetime.datetime.today().year
        month = datetime.datetime.today().month
        today = datetime.datetime.today().day

        days_in_month = calendar.monthrange(year, month)[1]

        if payday > days_in_month:
            payday = days_in_month

        if payday > today:
            end_date = datetime.date(year, month, payday)
            payday = int(result['payday'])
            if month == 1:
                month = 12
                year -= 1
            else:
                month -= 1
                year -= 1
            days_last_month = calendar.monthrange(year, month)[1]
            if payday > days_last_month:
                payday = days_last_month
            start_date = datetime.date(year,month,payday)
        else:
            start_date = datetime.date(year, month, payday)
            payday = int(result['payday'])
            if month == 12:
                month = 1
                year += 1
            else:
                month += 1
                year += 1
            days_next_month = calendar.monthrange(year, month)[1]
            if payday > days_next_month:
                payday = days_next_month
            end_date = datetime.date(year,month,payday)

        transaction_list = transaction_repo.get_custom_date(start_date, end_date)

        for transaction in transaction_list:
            amount = float(transaction.amount)
            remaining_budget -= amount
    remaining_budget = '{:.2f}'.format(remaining_budget)
    return remaining_budget