from db.run_sql import run_sql
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction

def save(transaction):
    if transaction.merchant is None and transaction.tag is None:
        sql = "INSERT INTO transactions (amount, transaction_date, description) VALUES (%s, %s, %s) RETURNING *"
        values = [transaction.amount, transaction.date, transaction.description]
    elif transaction.merchant is None:
        sql = "INSERT INTO transactions (amount, transaction_date, description, tag) VALUES (%s, %s, %s, %s) RETURNING *"
        values = [transaction.amount, transaction.date, transaction.description, transaction.tag.id]
    elif transaction.tag is None:
        sql = "INSERT INTO transactions (amount, transaction_date, description, merchant) VALUES (%s, %s, %s, %s) RETURNING *"
        values = [transaction.amount, transaction.date, transaction.description, transaction.merchant.id]
    else:
        sql = "INSERT INTO transactions (amount, transaction_date, description, merchant, tag) VALUES (%s, %s, %s, %s, %s) RETURNING *"
        values = [transaction.amount, transaction.date, transaction.description, transaction.merchant.id, transaction.tag.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id
    return transaction

def select_all():
    transaction_list = []
    sql = 'SELECT * FROM transactions'
    result = run_sql(sql)

    for row in result:
        transaction = Transaction(float(row['amount']), row['transaction_date'], row['description'], row['merchant'], row['tag'], row['id'])
        transaction_list.append(transaction)
    return transaction_list

def select(id):
    transaction = None
    sql = 'SELECT * FROM transactions WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        transaction = Transaction(float(result['amount']), result['transaction_date'], result['description'], result['merchant'], result['tag'], result['id'])
    return transaction

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(transaction):
    if transaction.merchant is None and transaction.tag is None:
        sql = "UPDATE transactions SET (amount, transaction_date, description) = (%s, %s, %s) WHERE id = %s"
        values = [transaction.amount, transaction.date, transaction.description, transaction.id]
    elif transaction.merchant is None:
        sql = "UPDATE transactions SET (amount, transaction_date, description, tag) = (%s, %s, %s, %s) WHERE id = %s"
        values = [transaction.amount, transaction.date, transaction.description, transaction.tag.id, transaction.id]
    elif transaction.tag is None:
        sql = "UPDATE transactions SET (amount, transaction_date, description, merchant) = (%s, %s, %s, %s) WHERE id = %s"
        values = [transaction.amount, transaction.date, transaction.description, transaction.merchant.id, transaction.id]
    else:
        sql = "UPDATE transactions SET (amount, transaction_date, description, merchant, tag) = (%s, %s, %s, %s, %s) WHERE id = %s"
        values = [transaction.amount, transaction.date, transaction.description, transaction.merchant.id, transaction.tag.id, transaction.id]
    run_sql(sql, values)