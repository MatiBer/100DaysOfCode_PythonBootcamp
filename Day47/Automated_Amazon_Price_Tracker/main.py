import requests
from bs4 import BeautifulSoup
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Amazon product URL
url = "https://www.amazon.com/Google-Pixel-Unlocked-Smartphone-Advanced/dp/B0CGTKM9WC/ref=sr_1_2?crid=SH121WWGSTUI"

# Set your user agent to a browser user agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61",
    "Accept-Language": "pl,en;q=0.9,en-GB;q=0.8,en-US;q=0.7"
}

# Create or connect to the SQLite database
conn = sqlite3.connect('price_tracker.db')
c = conn.cursor()

# Create a table to store price history
c.execute('''
    CREATE TABLE IF NOT EXISTS price_history (
        id INTEGER PRIMARY KEY,
        product_url TEXT,
        price REAL
    )
''')


# Send email function
def send_email(subject, message):
    sender_email = ""
    sender_password = ""
    recipient_email = ""

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()

# Function to get the current price
def get_price():
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    price_element = soup.find(class_="a-offscreen")

    if price_element:
        price_str = price_element.get_text()
        # Extract the price as a float, removing '$' and converting to float
        price = float(price_str.replace('$', '').replace(',', ''))
        return price
    else:
        return None

# Function to track the price
def track_price():
    price = get_price()

    if price:
        print(f"Current Price: ${price}")

        # Check if the price has changed
        c.execute('SELECT price FROM price_history WHERE product_url = ?', (url,))
        last_price = c.fetchone()

        if last_price is None or last_price[0] != price:
            # Price has changed, insert into the database and send an email notification
            c.execute('INSERT INTO price_history (product_url, price) VALUES (?, ?)', (url, price))
            conn.commit()

            subject = "Price Alert: Amazon Product Price Changed!"
            message = f"The price of the product at {url} has changed to ${price}."
            send_email(subject, message)
        else:
            print("Price has not changed.")
    else:
        print("Price not found. Check the URL or website structure.")

# Execute the tracking function
track_price()

# Close the database connection
conn.close()
