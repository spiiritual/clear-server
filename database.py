import sqlite3
import uuid
import models

def create_user(username : str, password : str):
    connection = sqlite3.connect('clear_database.db')
    cursor = connection.cursor()
    user_id = uuid.uuid4()

    try:
        with connection:
            cursor.execute("INSERT INTO User VALUES(?, ?, ?)", (user_id, username, password)).fetchone()
    except Exception as e:
        return e
    else:
        return True 
    
def create_post(content : str, visibility : str, owner_id : str, anonymous : bool, color : str, title : str = None):
    connection = sqlite3.connect('clear_database.db')
    cursor = connection.cursor()
    post_id = uuid.uuid4()

    try:
        with connection:
            cursor.execute("INSERT INTO Post VALUES(?, ?, ?, CURRENT_TIMESTAMP, ?, ?, ?, ?)", (post_id, title, content, visibility, owner_id, int(anonymous), color))
    except Exception as e:
        return e
    else:
        return True
        
    
def get_post(post_id : str):
    connection = sqlite3.connect('clear_database.db')
    cursor = connection.cursor()

    with connection:
        data = cursor.execute("SELECT * FROM Entry WHERE post_id = ?", (post_id,)).fetchone()
        username = cursor.execute("SELECT username FROM User WHERE user_id = ?", (data[5],)).fetchone()
    
    if data is not None:
        return models.EntryInternal(title=data[1], content=data[2], timestamp=data[3], visibility=data[4], owner_username=username, owner_id=data[5], anonymous=bool(data[6]), color=data[7])
    else:
        return None
    

    







