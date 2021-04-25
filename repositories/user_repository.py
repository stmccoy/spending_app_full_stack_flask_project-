from db.run_sql import run_sql
from models.user import User

def save(user):
    sql = "INSERT INTO users (first_name, surname, age, budget,dark_mode) VALUES (%s, %s, %s, %s, %s) RETURNING ID"
    values = [user.first_name, user.surname, user.age, user.budget, user.dark_mode]
    results = run_sql( sql, values )
    user.id = results[0]['id']
    return user

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        user = User(result['first_name'], result['surname'], result['age'], result['id'])
        user.budget = result['budget']
        user.dark_mode = result['dark_mode']
    return user

def select_all():
    users = []

    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        user = User(row['first_name'], row['surname'], row['age'], row['id'])
        user.budget = row['budget']
        user.dark_mode = row['dark_mode']
        users.append(user)
    return users
