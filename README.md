# Spending_Tracker

CodeClan solo project, built over 6 days in December 2021. 
A full stack app to track spending, using Python, Flask and PostgreSQL on the backend, HTML and CSS _*only*_ for frontend - no javascript or other fancy things like Bootstrap allowed, as these were forbidden by the brief.

## Brief:
Build an app that allows a user to track their spending.

### MVP

* The app should allow the user to create and edit merchants, e.g. Tesco, Amazon, ScotRail
* The app should allow the user to create and edit tags for their spending, e.g. groceries, entertainment, transport
* The user should be able to assign tags and merchants to a transaction, as well as an amount spent on each transaction.
* The app should display all the transactions a user has made in a single view, with each transaction's amount, merchant and tag, and a total for all transactions.

### Possible Extensions

* The user should be able to mark Merchants and Tags as deactivated. Users will not be able to choose deactivated merchants/tags when creating a transaction.
* Transactions should have a timestamp, and the user should be able to view transactions sorted by the time they took place.
* The user should be able to supply a budget, and the app should alert the user somehow when when they are nearing this budget or have gone over it.
* The user should be able to filter their view of transactions, for example, to view all transactions in a given month, or view all spending on groceries.

### Things which went well, and things I'd do differently next time
#### Main things I learnt
* The importantance of good planning before getting started
    * In addition to this, how key it is to limit the initial scope of the project to MVP - extensions are extensions for a reason!
* Generated lots of learning of HTML and CSS
* Solidifying Python fundamentals

#### Things I would have done differently and/or wished I'd had time for
* Styling the checkboxes (or rather, implementing a fake checkbox which looks nicer and hiding the real one)
* Finishing off the icon feature for merchants and tags - or removing any mention of it and pretending it never existed!
* After seeing other members of the cohorts presentations and their approaches to similar briefs, there were a few new ways I could have solved some things
    * SQL's ORDER BY keyword might have been better than sorting the returned results with Python - although it may also have been slower!
    * Using Flask's request object for a few different routes could have cut down on some unnecessary repeated function calls
    * Using Jinja's *include* tag could have been an interesting way to reduce the number of html templates used

----

Running instructions -
From the command line, assuming you have all of the aforementioned backend programs installed:

1) cd {wherever the repo has been saved on your machine}
2) createdb spending_tracker
3) psql -d spending_tracker -f db/spending_tracker.sql
4) python3 console.py (this will populate the database with some entries)
5) flask run

Then navigate to the URL flask is running on (by default this is http://127.0.0.1:5000)
