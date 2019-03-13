import mysql.connector as mysql

# Create buyn database
db = mysql.connect(
    host='localhost',
    user='root',
    passwd='qweqwe12'
)
c = db.cursor()
c.execute('CREATE DATABASE buyn')

# Create tables
db = mysql.connect(
    host='localhost',
    user='root',
    passwd='qweqwe12',
    database='buyn'
)

c = db.cursor()

# Create users table
c.execute('''CREATE TABLE IF NOT EXISTS users (
    user_id INT(11) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    telegram_handle VARCHAR(255) NOT NULL, 
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_update TIMESTAMP DEFAULT NULL,
    UNIQUE (telegram_handle)
)''')

# Create retailers table
c.execute('''CREATE TABLE IF NOT EXISTS retailers (
    retailer_id INT(11) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(255), 
    website VARCHAR(255) NOT NULL, 
    free_shipping_amount DECIMAL(8,2) UNSIGNED NOT NULL, 
    last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (website)
)''')

# Create bubbles table
c.execute('''CREATE TABLE IF NOT EXISTS bubbles (
    bubble_id INT(11) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    ucn VARCHAR(255) NOT NULL, 
    retailer_id INT(11) UNSIGNED, 
    user_id INT(11) UNSIGNED, 
    cart_amount DECIMAL(8,2) UNSIGNED NOT NULL DEFAULT 0, 
    shipping_location VARCHAR(255), 
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    filled_date TIMESTAMP DEFAULT NULL, 
    paid_date TIMESTAMP DEFAULT NULL, 
    ordered_date TIMESTAMP DEFAULT NULL, 
    received_shipment_date TIMESTAMP DEFAULT NULL, 
    delivered_date TIMESTAMP DEFAULT NULL, 
    last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (retailer_id) REFERENCES retailers(retailer_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    unique (ucn)    
)''')

# Create items table
c.execute('''CREATE TABLE IF NOT EXISTS items (
    item_id INT(11) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,     
    retailer_id INT(11) UNSIGNED, 
    web_link VARCHAR(255),
    name VARCHAR(255), 
    unit_price DECIMAL(8,2) UNSIGNED,     
    size VARCHAR(255), 
    color VARCHAR(255),
    quantity SMALLINT UNSIGNED,
    total_price DECIMAL(8,2) UNSIGNED,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (retailer_id) REFERENCES retailers(retailer_id)
)''')

# Create orders table
c.execute('''CREATE TABLE IF NOT EXISTS orders (
    order_id INT(11) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    bubble_id INT(11) UNSIGNED, 
    user_id INT(11) UNSIGNED, 
    item_id INT(11) UNSIGNED, 
    ptn VARCHAR(255), 
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    paid_date TIMESTAMP DEFAULT NULL,
    FOREIGN KEY (bubble_id) REFERENCES bubbles(bubble_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (item_id) REFERENCES items(item_id) ON DELETE CASCADE  
)''')
