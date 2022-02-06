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

# Add a user who has a budget of £500
default_user = User('user', 500)
user_repo.save(default_user)

# Add some merchants
amazon = Merchant('Amazon', False)
greggs = Merchant('Greggs', True)
scotrail = Merchant('ScotRail', False)
tesco = Merchant('Tesco', True)
vue = Merchant('Vue', True)
waitrose = Merchant('Waitrose', True)
merchant_repo.save(amazon)
merchant_repo.save(greggs)
merchant_repo.save(scotrail)
merchant_repo.save(tesco)
merchant_repo.save(vue)
merchant_repo.save(waitrose)

# Add some tags
eating_out = Tag('Eating out', True)
electronics = Tag('Electronics', True)
entertainment = Tag('Entertainment', True)
groceries = Tag('Groceries', True)
transport = Tag('Transport', False)
tag_repo.save(eating_out)
tag_repo.save(electronics)
tag_repo.save(entertainment)
tag_repo.save(groceries)
tag_repo.save(transport)


# Add some transactions for the past 2 weeks
today = datetime.date.today()

today_shop = Transaction(9.30, today, 'Odds and ends', waitrose, groceries)
yesterday_shop = Transaction(0.89, today - datetime.timedelta(days = 1), 'Milk', tesco, groceries)
transaction_repo.save(today_shop)
transaction_repo.save(yesterday_shop)

weekly_shop = Transaction(38.44, today - datetime.timedelta(days = 4), 'Weekly shop', tesco, groceries)
dinner = Transaction(19.95, today - datetime.timedelta(days = 3), 'Takeaway', None, eating_out)
transaction_repo.save(weekly_shop)
transaction_repo.save(dinner)

cinema = Transaction(4.99, today - datetime.timedelta(days = 5), 'Move night!', vue, entertainment)
transaction_repo.save(cinema)

headphones = Transaction(44.99, today - datetime.timedelta(days = 8), 'New headphones', amazon, electronics)
transaction_repo.save(headphones)

train = Transaction(27.60, today - datetime.timedelta(days = 11), 'Train to Glasgow', scotrail, transport)
transaction_repo.save(train)

# Excessive greggs habit
for i in range(1, 13):
    lunch = Transaction(2.00, today - datetime.timedelta(days = i), 'Two sausage rolls', greggs, eating_out)
    transaction_repo.save(lunch)