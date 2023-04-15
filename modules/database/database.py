import sqlite3

def create_connection():
    conn = sqlite3.connect('main', check_same_thread=False)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS main.users;")
    c.execute("CREATE TABLE IF NOT EXISTS main.users (id INTEGER PRIMARY KEY,name TEXT NOT NULL,age INTEGER NOT NULL,salary INTEGER NOT NULL);")
    c.execute("INSERT INTO main.users (name,age,salary) VALUES('user1',20,20000),('user2',22,22000),('user3',25,25000),('user4',28,28000),('user5',30,30000),('user6',33,33000),('user7',35,35000),('user8',37,37000),('user9',40,40000),('user10',45,45000);")
    conn.commit()
    return conn
