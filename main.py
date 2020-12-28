import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
from config import *


AMAZON_URL = "https://www.amazon.com/New-Apple-Watch-GPS-44mm-Aluminum/dp/B08J5P53JK/ref=sr_1_3?crid=2ORC3T2GCETBB&dchild=1&keywords=apple+watch+series+6&qid=1609129332&sprefix=app%2Caps%2C210&sr=8-3"

url = AMAZON_URL
headers = {
    "Request Line": "GET / HTTP/1.1",
    "Authority": "www.amazon.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
price = float(soup.find(id="price_inside_buybox").getText().split("$")[1])

# price check
if price < 400.00:
    # send email
    server = smtplib.SMTP("smtp.gmail.com",port=587)

    server.starttls()
    server.sendmail(FROM, TO, "test message")


