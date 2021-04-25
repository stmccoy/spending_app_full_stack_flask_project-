from db.run_sql import run_sql
from models.extras import Merchant

def save(merchant):
    sql = "INSERT INTO merchants (merchant_name, icon, website) VALUES (%s, %s, %s) RETURNING ID"
    values = [merchant.merchant_name, merchant.icon, merchant.website]
    results = run_sql( sql, values )
    merchant.id = results[0]['id']
    return merchant

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)