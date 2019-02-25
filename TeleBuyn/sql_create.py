import sqlite3
import datetime

def create():
    try:
        c.execute('''CREATE TABLE IF NOT EXISTS users
                 (user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 telegram_handle TEXT,
                 created_at TEXT)''')

        c.execute('''CREATE TABLE IF NOT EXISTS retailers
                 (retailer_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 name TEXT,
                 website TEXT,
                 free_shipping_amount INTEGER,
                 created_at TEXT)''')

        c.execute('''CREATE TABLE IF NOT EXISTS items
                 (item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 retailer_id INTEGER,
                 size TEXT,
                 price INTEGER,
                 created_at TEXT)''')

        c.execute('''CREATE TABLE IF NOT EXISTS bubbles
                 (bubble_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 retailer_id INTEGER,
                 user_id INTEGER,
                 cart_amount INTEGER,
                 filled INTEGER,
                 paid INTEGER,
                 ordered INTEGER,
                 received_shipment INTEGER,
                 delivered INTEGER,
                 shipping_location TEXT,
                 created_at TEXT)''')               
        
        c.execute('''CREATE TABLE IF NOT EXISTS orders
                 (order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 bubble_id INTEGER,
                 user_id INTEGER,
                 item_id INTEGER,
                 transaction_num TEXT,
                 paid INTEGER,
                 created_at TEXT)''')
        
    except:
        pass

def insert_users(user):
        sqlite_file = 'bb_db.sqlite'
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        c.execute('''INSERT OR IGNORE INTO users 
                (telegram_handle, created_at) 
                VALUES (?,?)''', 
                (user, datetime.datetime.now()))
        conn.commit()
        c.close()

def insert_retailers(name, website, free_shipping_amount):
        sqlite_file = 'bb_db.sqlite'
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        c.execute('''INSERT OR IGNORE INTO retailers 
                (name, website, free_shipping_amount, created_at)
                VALUES(?,?,?,?)''', 
                (name, website, free_shipping_amount, datetime.datetime.now()))
        conn.commit()
        c.close()

def insert_items(name, retailer_id, size, price):
        sqlite_file = 'bb_db.sqlite'
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        c.execute('''INSERT OR IGNORE INTO items 
                (name, retailer_id, size, price, created_at)
                VALUES(?,?,?,?,?)''', 
                (name, retailer_id, size, price, datetime.datetime.now()))
        conn.commit()
        c.close()

def insert_bubbles(name, retailer_id, user_id, cart_amount, 
                filled, paid, ordered, received_shipment, delivered, shipping_location):
        sqlite_file = 'bb_db.sqlite'
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        c.execute('''INSERT OR IGNORE INTO bubbles 
                (name, retailer_id, user_id, cart_amount, filled, 
                paid, ordered, received_shipment, delivered, shipping_location, created_at)
                VALUES(?,?,?,?,?,?,?,?,?,?,?)''', 
                (name, retailer_id, user_id, cart_amount, filled, paid, ordered, 
                received_shipment, delivered, shipping_location, datetime.datetime.now()))
        conn.commit()
        c.close()

def insert_orders(bubble_id, user_id, item_id, transaction_num, paid):        
        sqlite_file = 'bb_db.sqlite'
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        c.execute('''INSERT OR IGNORE INTO orders 
                (bubble_id, user_id, item_id, transaction_num, paid, created_at)
                VALUES(?,?,?,?,?,?)''', 
                (bubble_id, user_id, item_id, transaction_num, paid, datetime.datetime.now()))
        conn.commit()
        c.close()    

# Print data in table
def select(table, verbose=True):
    sql = "SELECT * FROM {tb}".format(tb=table)
    recs = c.execute(sql)
    if verbose:
        for row in recs:
            print(row)

# Connect to database
sqlite_file = 'bb_db.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# New changes
create()
insert_users('johndoe')
insert_retailers('Zara (ZA)', 'https://www.zara.com/sg/', 100)
insert_items('purple tee', 1, 'EU 34', 30)
insert_bubbles('ZA0123SH', 1, 1, 100, 1, 0, 0, 0, 0, 'SH')
insert_orders(1, 1, 1, 'ZA0123', 1)

# Commit needed to save data to database
conn.commit() 
select('users')
select('retailers')
select('items')
select('bubbles')
select('orders')
c.close()