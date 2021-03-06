import datetime
from db.run_sql import run_sql
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction
import repositories.merchant_repository as merchant_repo
import repositories.tag_repository as tag_repo

def save(transaction):
    # Save command needs to be different depending on if the user is passing in a merchant/tag or not 
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
        merchant = merchant_repo.select(row['merchant'])
        tag = tag_repo.select(row['tag'])
        transaction = Transaction(float(row['amount']), row['transaction_date'], row['description'], merchant, tag, row['id'])
        transaction_list.append(transaction)
    return transaction_list

def select(id):
    transaction = None
    sql = 'SELECT * FROM transactions WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        merchant = merchant_repo.select(result['merchant'])
        tag = tag_repo.select(result['tag'])
        transaction = Transaction(result['amount'], result['transaction_date'], result['description'], merchant, tag, result['id'])
    return transaction

def select_for_display(id):
    transaction = None
    sql = 'SELECT * FROM transactions WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        merchant = merchant_repo.select(result['merchant'])
        tag = tag_repo.select(result['tag'])
        transaction = Transaction(result['amount'], datetime.datetime.strftime(result['transaction_date'], '%d %b %Y'), result['description'], merchant, tag, result['id'])
        transaction.update_amount('{:.2f}'.format(transaction.amount))
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
        sql = "UPDATE transactions SET (amount, transaction_date, description, merchant, tag) = (%s, %s, %s, %s, %s) WHERE id = %s"
        values = [transaction.amount, transaction.date, transaction.description, None, None, transaction.id]
    elif transaction.merchant is None:
        sql = "UPDATE transactions SET (amount, transaction_date, description, merchant, tag) = (%s, %s, %s, %s, %s) WHERE id = %s"
        values = [transaction.amount, transaction.date, transaction.description, None, transaction.tag.id, transaction.id]
    elif transaction.tag is None:
        sql = "UPDATE transactions SET (amount, transaction_date, description, merchant, tag) = (%s, %s, %s, %s, %s) WHERE id = %s"
        values = [transaction.amount, transaction.date, transaction.description, transaction.merchant.id, None, transaction.id]
    else:
        sql = "UPDATE transactions SET (amount, transaction_date, description, merchant, tag) = (%s, %s, %s, %s, %s) WHERE id = %s"
        values = [transaction.amount, transaction.date, transaction.description, transaction.merchant.id, transaction.tag.id, transaction.id]
    run_sql(sql, values)

def get_last_week():
    transaction_list = []
    sql = "SELECT * FROM transactions WHERE transaction_date BETWEEN CURRENT_DATE -7 AND CURRENT_DATE"
    result = run_sql(sql)

    for row in result:
        merchant = merchant_repo.select(row['merchant'])
        tag = tag_repo.select(row['tag'])
        transaction = Transaction(row['amount'], row['transaction_date'], row['description'], merchant, tag, row['id'])
        transaction.update_amount('{:.2f}'.format(transaction.amount))
        transaction_list.append(transaction)
    transaction_list.sort(key= lambda transaction : transaction.date)
    for t in transaction_list:
        t.date = datetime.datetime.strftime(t.date, '%d %b %Y')
    return transaction_list

def get_custom_date(start_date, end_date):
    transaction_list = []
    sql = "SELECT * FROM transactions WHERE transaction_date BETWEEN %s AND %s"
    values = [start_date, end_date]
    result = run_sql(sql, values)

    for row in result:
        merchant = merchant_repo.select(row['merchant'])
        tag = tag_repo.select(row['tag'])
        transaction = Transaction(row['amount'], row['transaction_date'], row['description'], merchant, tag, row['id'])
        transaction.update_amount('{:.2f}'.format(transaction.amount))
        transaction_list.append(transaction)
    transaction_list.sort(key= lambda transaction : transaction.date)
    for t in transaction_list:
        t.date = datetime.datetime.strftime(t.date, '%d %b %Y')
    return transaction_list

def filter_by_merchant(merchant, filter_list):
    filtered_list = []
    if merchant == 'All':
        filtered_list = filter_list
    else:
        if merchant is not None:
            for transaction in filter_list:
                if transaction.merchant is not None:
                    if transaction.merchant.id == merchant.id:
                        filtered_list.append(transaction)
        else:
            for transaction in filter_list:
                if transaction.merchant is None:
                    filtered_list.append(transaction)
    return filtered_list

def filter_by_tag(tag, filter_list):
    filtered_list = []
    if tag == 'All':
        filtered_list = filter_list
    else:
        if tag is not None:
            for transaction in filter_list:
                if transaction.tag is not None:
                    if transaction.tag.id == tag.id:
                        filtered_list.append(transaction)
        else:
            for transaction in filter_list:
                if transaction.tag is None:
                    filtered_list.append(transaction)
    return filtered_list

def get_total(transaction_list):
    total = 0
    for transaction in transaction_list:
        total += float(transaction.amount)
    return total