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

def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = Merchant(result['merchant_name'], result['id'])
        merchant.icon = result['icon']
        merchant.website = result['website']
    return merchant

def select_all():
    merchants = []

    sql = "SELECT * FROM merchants"
    results = run_sql(sql)

    for row in results:
        merchant = Merchant(row['merchant_name'], row['id'])
        merchant.icon = row['icon']
        merchant.website = row['website']
        merchants.append(merchant)
    return merchants