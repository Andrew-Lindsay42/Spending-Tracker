# Spending_Tracker

CodeClan solo project. Full stack app to track spending, using Python, Flask and PostgreSQL on the backend, with HTML and CSS *only* for frontend

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Running instructions -
From the command line, assuming you have all of the aforementioned backend programs installed:

1) cd {wherever the repo has been saved on your machine}
2) createdb spending_tracker
3) psql -d spending_tracker -f db/spending_tracker.sql
4) python3 console.py (this will populate the database with some entries)
5) flask run

Then navigate to the URL flask is running on (by default this is http://127.0.0.1:5000)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Brief:
Build an app that allows a user to track their spending.

MVP

    The app should allow the user to create and edit merchants, e.g. Tesco, Amazon, ScotRail
    The app should allow the user to create and edit tags for their spending, e.g. groceries, entertainment, transport
    The user should be able to assign tags and merchants to a transaction, as well as an amount spent on each transaction.
    The app should display all the transactions a user has made in a single view, with each transaction's amount, merchant and tag, and a total for all transactions.

Possible Extensions

    The user should be able to mark Merchants and Tags as deactivated. Users will not be able to choose deactivated merchants/tags when creating a transaction.
    Transactions should have a timestamp, and the user should be able to view transactions sorted by the time they took place.
    The user should be able to supply a budget, and the app should alert the user somehow when when they are nearing this budget or have gone over it.
    The user should be able to filter their view of transactions, for example, to view all transactions in a given month, or view all spending on groceries.
