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