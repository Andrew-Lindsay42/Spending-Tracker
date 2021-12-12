from db.run_sql import run_sql
from models.merchant import Merchant

def save(merchant):
    pass

def select_all():
    merchant_list = []
    sql = 'SELECT * FROM merchants'
    result = run_sql(sql)

    for row in result:
        merchant = Merchant(row['name'], row['active'], row['icon_num'], row['id'])
        merchant_list.append(merchant)
    return merchant_list

def select(id):
    pass

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(merchant):
    pass