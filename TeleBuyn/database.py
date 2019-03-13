import mysql.connector as mysql
import random
import string

db = mysql.connect(
    host='localhost',
    user='root',
    passwd='qweqwe12',
    database='buyn'
)

c = db.cursor()


def add_user(user):
    # Check if user exists
    c.execute(
        "SELECT user_id FROM users WHERE telegram_handle = %s LIMIT 1", (user,))
    try:
        # User exist
        user_id = c.fetchone()[0]
        print('user exists')
    except:
        # User does not exist, add into users table
        query = 'INSERT INTO users (telegram_handle) VALUES (%s)'
        values = (user,)
        c.execute(query, values)
        db.commit()
        user_id = c.lastrowid
        print('user added')

    return user_id


def add_retailer(name, website, free_shipping_amount):
    # Check if retailer exists
    c.execute(
        "SELECT retailer_id FROM retailers WHERE website = %s LIMIT 1", (website,))
    try:
        # Retailer exist
        retailer_id = c.fetchone()[0]
        print('retailer exists')
    except:
        # Retailer does not exist, add into retailers table
        query = 'INSERT INTO retailers (name, website, free_shipping_amount) VALUES (%s, %s, %s)'
        values = (name, website, free_shipping_amount)
        c.execute(query, values)
        db.commit()
        retailer_id = c.lastrowid
        print('retailer added')

    return retailer_id


def add_bubble(retailer_id, user_id, shipping_location):
    try:
        # Check if retailer and user id exists
        c.execute(
            "SELECT retailer_id FROM retailers WHERE retailer_id = %s LIMIT 1", (retailer_id,))
        c.fetchone()[0]
        c.execute(
            "SELECT user_id FROM users WHERE user_id = %s LIMIT 1", (user_id,))
        c.fetchone()[0]

        # generate UCN and add row
        ucn = ''.join(
            [random.choice(string.ascii_letters + string.digits) for n in range(4)])
        ucn += shipping_location
        query = 'INSERT INTO bubbles (ucn, retailer_id, user_id, shipping_location) VALUES (%s, %s, %s, %s)'
        values = (ucn, retailer_id, user_id, shipping_location)
        c.execute(query, values)
        db.commit()
        bubble_id = c.lastrowid
        print('bubble added')

        return bubble_id, ucn
    except:
        return 'error: the id does not exist'


def add_item(retailer_id, web_link, name, unit_price, size, color, quantity):
    try:
        # Add item into items table
        query = 'INSERT INTO items (retailer_id, web_link, name, unit_price, size, color, quantity, total_price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
        values = (retailer_id, web_link, name, unit_price,
                  size, color, quantity, unit_price*quantity)
        c.execute(query, values)
        db.commit()
        item_id = c.lastrowid
        print('item added')

        return item_id
    except:
        return 'error'


def add_order(bubble_id, user_id, item_id):
    try:
        # Check if bubble, user and item id exists
        c.execute(
            "SELECT bubble_id FROM bubbles WHERE bubble_id = %s LIMIT 1", (bubble_id,))
        c.fetchone()[0]
        c.execute(
            "SELECT user_id FROM users WHERE user_id = %s LIMIT 1", (user_id,))
        c.fetchone()[0]
        c.execute(
            "SELECT item_id FROM items WHERE item_id = %s LIMIT 1", (item_id,))
        c.fetchone()[0]

        # generate PTN and add row
        ptn = ''.join(
            [random.choice(string.ascii_letters + string.digits) for n in range(4)])
        query = 'INSERT INTO orders (bubble_id, user_id, item_id, ptn) VALUES (%s, %s, %s, %s)'
        values = (bubble_id, user_id, item_id, ptn)
        c.execute(query, values)
        db.commit()
        print('order added')

        return ptn
    except:
        return 0  # error: the id does not exist


def replace_ptn(ptn, bubble_id, user_id):
    try:
        c.execute('UPDATE orders SET ptn = %s WHERE bubble_id = %s AND user_id = %s',
                  (ptn, bubble_id, user_id))
        db.commit()

        return True  # replace successful
    except:
        return False  # replace unsuccessful


def retrieve_bubble(ucn):
    c.execute(
        'SELECT bubble_id, retailer_id FROM bubbles WHERE ucn = %s LIMIT 1', (ucn,))
    bubble_id, retailer_id = c.fetchone()

    return bubble_id, retailer_id


def edit_get_item(ptn):
    item_list = []
    c.execute('SELECT item_id FROM orders WHERE ptn = %s', (ptn,))
    item_ids = c.fetchall()
    for item in item_ids:
        item_id = item[0]
        c.execute('SELECT name FROM items WHERE item_id = %s', (item_id,))
        item_name = c.fetchone()[0]
        item_list.append([item_id, item_name])
    return item_list


def edit_item(item_id, column_to_change, value_to_change):
    try:
        # Check if item_id exists
        c.execute(
            "SELECT item_id FROM items WHERE item_id = %s LIMIT 1", (item_id,))
        c.fetchone()[0]

        # Edit column value based on column specified
        if column_to_change == 'size':
            c.execute('UPDATE items SET size = %s WHERE item_id = %s',
                      (value_to_change, item_id))
        elif column_to_change == 'color':
            c.execute('UPDATE items SET color = %s WHERE item_id = %s',
                      (value_to_change, item_id))
        elif column_to_change == 'quantity':
            c.execute('UPDATE items SET quantity = %s WHERE item_id = %s',
                      (value_to_change, item_id))
            # Update total price
            # c.execute('UPDATE items SET total_price = %s WHERE item_id = %s', (??,item_id))
        elif column_to_change == 'delete':
            c.execute('DELETE FROM items WHERE item_id = %s', (item_id,))
        db.commit()

        return True  # edit successful
    except:
        return False  # edit unsuccessful


# TO DO
'''
1. TIMESTAMP no default value allowed in server? no more than 2 CURRENT TIME
'''

# Run functions
print(add_user('tommy'))

print(add_retailer('zalora', 'www.zalora.com', 60))

#print(add_bubble(1, 1, 'UT'))

#print(add_item(1, 'www.blah4.com', 'purple tee', 20.25, 'EU 34', 'purple', 2))

#print(add_order(1, 3, 2))

# print(retrieve_bubble('6PR8UT'))

# print(edit_get_item('b50A'))

print(edit_item(3, 'size', 'XS'))

#print(replace_ptn('atRF', 10, 1))
