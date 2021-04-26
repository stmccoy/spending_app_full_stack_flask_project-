# from db.run_sql import run_sql
# from models.transaction_category import TransactionCategory
# import repositories.transaction_repository as transaction_repository
# import repositories.direct_debit_repository as direct_debit_repository
# import repositories.debt_repository as debt_repository
# import repositories.tag_repository as tag_repository

# def save(transaction_category):
#     sql = "INSERT INTO transaction_categories (transaction_id, direct_debit_id, debt_id, tag_id) VALUES (%s, %s, %s, %s) RETURNING ID"
#     if transaction_category.transaction != None:
#         values = [transaction_category.transaction.id, transaction_category.direct_debit, transaction_category.debt, transaction_category.tag.id]
#     elif transaction_category.direct_debit != None:
#         values = [transaction_category.transaction, transaction_category.direct_debit.id, transaction_category.debt, transaction_category.tag.id]
#     elif transaction_category.debt != None:
#         values = [transaction_category.transaction, transaction_category.direct_debit, transaction_category.debt.id, transaction_category.tag.id]
#     results = run_sql( sql, values )
#     transaction_category.id = results[0]['id']
#     return transaction_category

# def delete_all():
#     sql = "DELETE FROM transaction_categories"
#     run_sql(sql)

# def delete(id):
#     sql = "DELETE FROM transaction_categories WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)

# def select(id):
#     transaction_category = None
#     sql = "SELECT * FROM transaction_categories WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]

#     if result is not None:
#         tag = tag_repository.select(result['tag_id'])
#         transaction_category = TransactionCategory(tag, result['id'])   
#         if result['debt_id'] != None:
#             debt = debt_repository.select(result['debt_id'])
#             transaction_category.debt = debt
#         elif result['transaction_id'] != None:
#             transaction = transaction_repository.select(result['transaction_id'])
#             transaction_category.transaction = transaction
#         elif result['direct_debit_id'] != None:
#             direct_debit = direct_debit_repository.select(result['direct_debit_id'])  
#             transaction_category.direct_debit = direct_debit
#     return transaction_category

# def select_all():
#     transaction_categories = []

#     sql = "SELECT * FROM transaction_categories"
#     results = run_sql(sql)

#     for row in results:
#         tag = tag_repository.select(row['tag_id'])
#         transaction_category = TransactionCategory(tag, row['id'])   
#         if row['debt_id'] != None:
#             debt = debt_repository.select(row['debt_id'])
#             transaction_category.debt = debt
#         elif row['transaction_id'] != None:
#             transaction = transaction_repository.select(row['transaction_id'])
#             transaction_category.transaction = transaction
#         elif row['direct_debit_id'] != None:
#             direct_debit = direct_debit_repository.select(row['direct_debit_id'])  
#             transaction_category.direct_debit = direct_debit
#         transaction_categories.append(transaction_category)
#     return transaction_categories

# def select_transaction_by_user_and_transaction_id(user_id, transaction_id):
#     transaction_categories = []

#     sql = "SELECT * FROM transaction_categories INNER JOIN tags ON tags.id = transaction_categories.tag_id INNER JOIN transactions ON transactions.id = transaction_categories.transaction_id WHERE transactions.user_id = %s and transactions.id = %s"
#     values = [user_id, transaction_id]
#     result = run_sql(sql, values)

#     for row in results:
#         tag = tag_repository.select(row['tag_id'])
#         transaction_category = TransactionCategory(tag, row['id'])   
#         if row['debt_id'] != None:
#             debt = debt_repository.select(row['debt_id'])
#             transaction_category.debt = debt
#         elif row['transaction_id'] != None:
#             transaction = transaction_repository.select(row['transaction_id'])
#             transaction_category.transaction = transaction
#         elif row['direct_debit_id'] != None:
#             direct_debit = direct_debit_repository.select(row['direct_debit_id'])  
#             transaction_category.direct_debit = direct_debit
#         transaction_categories.append(transaction_category)
#     return transaction_categories