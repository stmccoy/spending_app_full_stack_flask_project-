To Run program

Run 'psql -d spending_tracker -f db/spending_tracker.sql'

If database doesn't exist you will need to create it by typing createdb spending_tracker. Then try running 'psql -d spending_tracker -f db/spending_tracker.sql' again.

Next run 'python3 console.py' 

Finally run 'flask run' 

Change user by moving number in session file number between '1', '2' and '3' and refreshing the page