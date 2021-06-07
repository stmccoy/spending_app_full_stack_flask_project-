Created a full stack spending tracker app using postgresql and flask, with html and css on the views. Overall was happy with how it turned out, I managed to use inheritance for the transaction types and I managed to implement 'ON DELETE SET NULL' to the tags and merchants, which meant they could be deleted without deleting the transactions associated with them. However, I was unable to make it so that you could leave fields blank when submitting form data. This meant that I had to set everything to required in the html which felt a bit lazy, if I was to refactor this I would look into making all fields optional. I would also look to improve the CSS for the sidebar as that was rushed as I was running out of time. 

UPDATE

Have made form data optional
Have finished dark mode feature
Have improved sidebar CSS



To Run program

1. If never run before you need to create the database by typing createdb spending_tracker

2. Run 'psql -d spending_tracker -f db/spending_tracker.sql', any errors check you have database and if not run command before

3. Next run 'python3 console.py' 

4. Finally run 'flask run' 

Change user by moving number in session file number between '1', '2' and '3' and refreshing the page