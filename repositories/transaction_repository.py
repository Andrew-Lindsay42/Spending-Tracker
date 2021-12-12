from db.run_sql import run_sql
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction

def save(transaction):
    pass

def select_all():
    pass

def select(id):
    pass

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def delete(id):
    pass

def update(transaction):
    pass