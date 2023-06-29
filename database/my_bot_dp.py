import random
import sqlite3


def sql_create():
    global db, cursor
    db = sqlite3.connect("mybot.db")
    cursor = db.cursor()

    if db:
        print("База данных подключена!")

    db.execute("CREATE TABLE IF NOT EXISTS mentors"
               "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "name VARCHAR (100) NOT NULL,"
               "course VARCHAR (10),"
               "age INTEGER NOT NULL,"
               "group_number TEXT)")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute(
            "INSERT INTO mentors "
            "(name, course, age, group_number) "
            "VALUES (?, ?, ?, ?)",
            tuple(data.values())
        )
        db.commit()


async def sql_command_random():
    names = cursor.execute("SELECT * FROM mentors").fetchall()
    random_name = random.choice(names)
    return random_name


async def sql_command_all():
    return cursor.execute("SELECT * FROM mentors").fetchall()


async def sql_command_all_names():
    return cursor.execute("SELECT name FROM mentors").fetchall()


async def sql_command_delete(mentor_id):
    cursor.execute("DELETE FROM mentors WHERE id = ?", (mentor_id,))
    db.commit()
