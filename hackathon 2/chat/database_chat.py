import sqlite3 as sl

def run_query(query):
    connection = sl.connect("chat.db")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def fetch_query(query):
    connection = sl.connect("chat.db")
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    return results

def signup_server_db(username, ip_address):
    try:
        query = f"INSERT INTO user (username, ip_add) VALUES ('{username}', '{ip_address}')"
        run_query(query)
        return True
    except:
        return False

def signin_server_db(username):
    query = f"SELECT username FROM user WHERE username == '{username}'"
    results = fetch_query(query)
    if results == []:
        return False
    else:
        user = results[0][0]
        return user

def message_server_db(message):
    query = f"INSERT INTO messages (message) VALUES ('{message}')"
    run_query(query)