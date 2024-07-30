from database import connect_db


def add_transaction(amount, category_name, date, description):
    from categories import get_category_id_by_name
    category_id = get_category_id_by_name(category_name)
    if not category_id:
        raise ValueError("Category not found.")

    db = connect_db()
    cursor = db.cursor()
    sql = "INSERT INTO transactions (amount, category_id, date, description) VALUES (%s, %s, %s, %s)"
    val = (amount, category_id, date, description)
    cursor.execute(sql, val)
    db.commit()
    db.close()


def view_transactions():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT t.id, t.amount, c.name, t.date, t.description FROM transactions t JOIN categories c ON t.category_id = c.id")
    transactions = cursor.fetchall()
    db.close()
    return transactions


def edit_transaction(transaction_id, amount, category_name, date, description):
    from categories import get_category_id_by_name
    category_id = get_category_id_by_name(category_name)
    if not category_id:
        raise ValueError("Category not found.")

    db = connect_db()
    cursor = db.cursor()
    sql = "UPDATE transactions SET amount = %s, category_id = %s, date = %s, description = %s WHERE id = %s"
    val = (amount, category_id, date, description, transaction_id)
    cursor.execute(sql, val)
    db.commit()
    db.close()


def delete_transaction(transaction_id):
    db = connect_db()
    cursor = db.cursor()
    sql = "DELETE FROM transactions WHERE id = %s"
    val = (transaction_id,)
    cursor.execute(sql, val)
    db.commit()
    db.close()
