from db.run_sql import run_sql
from models.extras import Tag

def save(tag):
    sql = "INSERT INTO tags (tag_name, adult_rating) VALUES (%s, %s) RETURNING ID"
    values = [tag.tag_name, tag.adult_rating]
    results = run_sql( sql, values )
    tag.id = results[0]['id']
    return tag

def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM tags WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select(id):
    tag = None
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        tag = Tag(result['tag_name'], result['adult_rating'], result['id'])
    return tag

def select_all():
    tags = []

    sql = "SELECT * FROM tags"
    results = run_sql(sql)

    for row in results:
        tag = Tag(row['tag_name'], row['adult_rating'], row['id'])
        tags.append(tag)
    return tags

def select_all_by_user(user_id):
    tags = []

    sql = "SELECT * FROM tags INNER JOIN transactions ON transactions.tag_id = tags.id WHERE transactions.user_id = %s"
    values = [user_id]
    results = run_sql(sql, values)

    for row in results:
        tag = Tag(row['tag_name'], row['adult_rating'], row['id'])
        tags.append(tag)
    return tags

def select_all_by_user_direct_debit(user_id):
    tags = []

    sql = "SELECT * FROM tags INNER JOIN direct_debits ON direct_debits.tag_id = tags.id WHERE direct_debits.user_id = %s"
    values = [user_id]
    results = run_sql(sql, values)

    for row in results:
        tag = Tag(row['tag_name'], row['adult_rating'], row['id'])
        tags.append(tag)
    return tags

def select_all_by_user_debt(user_id):
    tags = []

    sql = "SELECT * FROM tags INNER JOIN debts ON debts.tag_id = tags.id WHERE debts.user_id = %s"
    values = [user_id]
    results = run_sql(sql, values)

    for row in results:
        tag = Tag(row['tag_name'], row['adult_rating'], row['id'])
        tags.append(tag)
    return tags