from db.run_sql import run_sql
from models.merchant import Merchant

def save(merchant):
    pass

def select_all():
    pass

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