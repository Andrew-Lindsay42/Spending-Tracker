import datetime

from models.user import User
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction

import repositories.user_repository as user_repo
import repositories.merchant_repository as merchant_repo
import repositories.tag_repository as tag_repo
import repositories.transaction_repository as transaction_repo

# Delete all existing data in tables
user_repo.delete_all()
transaction_repo.delete_all()
merchant_repo.delete_all()
tag_repo.delete_all()

# Add some data to tables
default_user = User('user')
user_with_info = User('info', 100, 12)
user_repo.save(default_user)
user_repo.save(user_with_info)

tesco = Merchant('Tesco', True)
waitrose = Merchant('Waitrose', True, 2)
amazon = Merchant('Amazon', False)
greggs = Merchant('Greggs', True)
merchant_repo.save(tesco)
merchant_repo.save(waitrose)
merchant_repo.save(amazon)
merchant_repo.save(greggs)

groceries = Tag('Groceries', True)
electronics = Tag('Electronics', True, 3)
eating_out = Tag('Eating out', False)
tag_repo.save(groceries)
tag_repo.save(electronics)
tag_repo.save(eating_out)

weekly_shop = Transaction(28.44, datetime.date(2021, 12, 12), 'Weekly shop', tesco, groceries)
lunch = Transaction(2.00, datetime.date(2021, 12, 8), None, greggs)
forgotten_spend = Transaction(7.55, datetime.date(2021, 12, 10))
dinner = Transaction(11.95, datetime.date(2021, 11, 13), 'Dinner', None, eating_out)
transaction_repo.save(weekly_shop)
transaction_repo.save(lunch)
transaction_repo.save(forgotten_spend)
transaction_repo.save(dinner)

# Print the data in tables (will test the select all method)
# Uncomment line 52 - 70 to run
# all_users = user_repo.select_all()
# for user in all_users:
#    print(user.__dict__)
# print('\n')

# all_merchants = merchant_repo.select_all()
# for merchant in all_merchants:
#    print(merchant.__dict__)
# print('\n')

# all_tags = tag_repo.select_all()
# for tag in all_tags:
#    print(tag.__dict__)
# print('\n')

# all_transactions = transaction_repo.select_all()
# for transaction in all_transactions:
#    print(transaction.__dict__)
# print('\n')

# Print a selected row (will test the select method)
# Uncomment line 74 - 84 to run
# print(user_repo.select(default_user.id).__dict__)
# print('\n')

# print(merchant_repo.select(tesco.id).__dict__)
# print('\n')

# print(tag_repo.select(eating_out.id).__dict__)
# print('\n')

# print(transaction_repo.select(lunch.id).__dict__)
# print('\n')

# Delete a specific row in table
user_repo.delete(user_with_info.id)
merchant_repo.delete(greggs.id)
tag_repo.delete(eating_out.id)
transaction_repo.delete(dinner.id)