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