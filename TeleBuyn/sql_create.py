import sqlite3


def create():
    try:
        c.execute("""CREATE TABLE IF NOT EXISTS users
                 (user_id INTEGER PRIMARY KEY,
                 telegram_handle TEXT,
                 created_at TEXT)""")

        c.execute("""CREATE TABLE IF NOT EXISTS retailers
                 (retailer_id INTEGER PRIMARY KEY,
                 name TEXT,
                 website TEXT,
                 free_shipping_amount INTEGER,
                 created_at TEXT)""")

        c.execute("""CREATE TABLE IF NOT EXISTS items
                 (item_id INTEGER PRIMARY KEY,
                 name TEXT,
                 retailer_id INTEGER,
                 size TEXT,
                 price INTEGER,
                 created_at TEXT)""")

        c.execute("""CREATE TABLE IF NOT EXISTS bubbles
                 (bubble_id INTEGER PRIMARY KEY,
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
                 created_at TEXT)""")

        c.execute("""CREATE TABLE IF NOT EXISTS orders
                 (order_id INTEGER PRIMARY KEY,
                 bubble_id INTEGER,
                 user_id INTEGER,
                 item_id INTEGER,
                 transaction_num TEXT,
                 paid INTEGER,
                 created_at TEXT)""")

    except:
        pass


def insert_users(user_id, telegram_handle, created_at):
    c = conn.cursor()
    c.execute("""INSERT OR IGNORE INTO users (user_id, telegram_handle, created_at) VALUES(?,?,?)""",
              (user_id, telegram_handle, created_at))
    conn.commit()
    c.close()


def insert_retailers(retailer_id, name, website, free_shipping_amount, created_at):
    c.execute("""INSERT OR IGNORE INTO retailers 
                (retailer_id, name, website, free_shipping_amount, created_at)
                VALUES(?,?,?,?,?)""", (retailer_id, name, website, free_shipping_amount, created_at))


def insert_items(item_id, name, retailer_id, size, price, created_at):
    c.execute("""INSERT OR IGNORE INTO items 
                (item_id, name, retailer_id, size, price, created_at)
                VALUES(?,?,?,?,?,?)""", (item_id, name, retailer_id, size, price, created_at))


def insert_bubbles(bubble_id, name, retailer_id, user_id, cart_amount,
                   filled, paid, ordered, received_shipment, delivered, shipping_location, created_at):
    c.execute("""INSERT OR IGNORE INTO bubbles 
                (bubble_id, name, retailer_id, user_id, cart_amount, filled, 
                paid, ordered, received_shipment, delivered, shipping_location, created_at)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?)""", (bubble_id, name, retailer_id, user_id, cart_amount,
                                                     filled, paid, ordered, received_shipment, delivered, shipping_location, created_at))


def insert_orders(order_id, bubble_id, user_id, item_id, transaction_num, paid, created_at):
    c.execute("""INSERT OR IGNORE INTO orders 
                (order_id, bubble_id, user_id, item_id, transaction_num, paid, created_at)
                VALUES(?,?,?,?,?,?,?)""", (order_id, bubble_id, user_id, item_id, transaction_num, paid, created_at))


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
insert_users(1, 'johndoe', '2 feb')
insert_retailers(1, 'Zara (ZA)', 'https://www.zara.com/sg/', 100, '1 Feb')
insert_items(1, 'purple tee', 1, 'EU 34', 30, '1 Feb')
insert_bubbles(1, 'ZA0123SH', 1, 1, 100, 1, 0, 0, 0, 0, 'SH', '1 Feb')
insert_orders(1, 1, 1, 1, 'ZA0123', 1, '1 Feb')

# Commit needed to save data to database
conn.commit()
select('users')
select('retailers')
select('items')
select('bubbles')
select('orders')
c.close()
