import mysql.connector as mysql

# Create buyn database
db = mysql.connect(
    host = 'localhost',
    user = '',
    passwd = ''
)
c = db.cursor()
c.execute('CREATE DATABASE buyn')

# Create tables
db = mysql.connect(
    host = 'localhost',
    user = '',
    passwd = '',
    database = 'buyn'
)

c = db.cursor()

# Create users table
c.execute('''CREATE TABLE IF NOT EXISTS users (
    user_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    telegram_handle VARCHAR(255), 
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
)''')

# Create retailers table 
c.execute('''CREATE TABLE IF NOT EXISTS retailers (
    retailer_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(255), 
    website VARCHAR(255), 
    free_shipping_amount INT(11), 
    last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
)''')

# Create items table
c.execute('''CREATE TABLE IF NOT EXISTS items (
    item_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,     
    retailer_id INT(11), 
    web_link VARCHAR(255),
    name VARCHAR(255), 
    price INT(11),     
    size VARCHAR(255), 
    color VARCHAR(255),
    quantity VARCHAR(255),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
)''')

# Create bubbles table
c.execute('''CREATE TABLE IF NOT EXISTS bubbles (
    bubble_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(255), retailer_id INT(11), 
    user_id INT(11), 
    cart_amount INT(11), 
    shipping_location VARCHAR(255), 
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    filled_date TIMESTAMP DEFAULT NULL, 
    paid_date TIMESTAMP DEFAULT NULL, 
    ordered_date TIMESTAMP DEFAULT NULL, 
    received_shipment_date TIMESTAMP DEFAULT NULL, 
    delivered_date TIMESTAMP DEFAULT NULL, 
    last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP    
)''')  

# Create orders table
c.execute('''CREATE TABLE IF NOT EXISTS orders (
    order_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    bubble_id INT(11), 
    user_id INT(11), 
    item_id INT(11), 
    transaction_num VARCHAR(255), 
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    paid_date TIMESTAMP DEFAULT NULL  
)''')


