import  mysql.connector as mysql


db = mysql.connect(
    host = 'localhost',
    user = '',
    passwd = '',
    database = 'buyn'
)

c = db.cursor()

def add_users(user):
    query = 'INSERT INTO users (telegram_handle) VALUES (%s)'
    values = (user,)
    c.execute(query, values)
    db.commit()

def add_retailers(name, website, free_shipping_amount):
    query = 'INSERT INTO retailers (name, website, free_shipping_amount) VALUES (%s, %s, %s)'
    values = (name, website, free_shipping_amount)
    c.execute(query, values)
    db.commit()

def add_items(retailer_id, web_link, name, price, size, color, quantity):
    query = 'INSERT INTO items (retailer_id, web_link, name, price, size, color, quantity) VALUES (%s, %s, %s, %s, %s, %s, %s)'
    values = (retailer_id, web_link, name, price, size, color, quantity)
    c.execute(query, values)
    db.commit()

def add_bubbles(name, retailer_id, user_id, cart_amount, shipping_location):
    query = 'INSERT INTO bubbles (name, retailer_id, user_id, cart_amount, shipping_location) VALUES (%s, %s, %s, %s, %s)'
    values = (name, retailer_id, user_id, cart_amount, shipping_location)
    c.execute(query, values)
    db.commit()

def add_orders(bubble_id, user_id, item_id, transaction_num):        
    query = 'INSERT INTO orders (bubble_id, user_id, item_id, transaction_num) VALUES (%s, %s, %s, %s)'
    values = (bubble_id, user_id, item_id, transaction_num)
    c.execute(query, values)
    db.commit()
 
# TO DO
'''
2. add relationships to tables
3. add read funtions
4. add update functions
5. add delete functions
6. generate ptn (create check_if_duplicate, if false, use current ptn generated)
'''

# Run functions
add_users('Tim')
add_retailers('zalora', 'www.zalora.com', '60')
add_items('1', 'www.blah.com', 'purple tee', '10', 'EU 34', 'XS', '2')
add_bubbles('ZA0123UT', '1', '1', '100', 'UT')
add_orders('1', '1', '1', 'ZA0123')

