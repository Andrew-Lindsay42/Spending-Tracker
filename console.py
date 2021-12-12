import datetime
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction

import repositories.merchant_repository as merchant_repo
import repositories.tag_repository as tag_repo
import repositories.transaction_repository as transaction_repo
import repositories.user_repository as user_repo

# Delete all existing data in tables
user_repo.delete_all()
transaction_repo.delete_all()
merchant_repo.delete_all()
tag_repo.delete_all()