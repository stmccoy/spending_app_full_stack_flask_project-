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

