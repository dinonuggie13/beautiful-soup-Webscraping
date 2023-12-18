from bs4 import BeautifulSoup
import requests

url = "https://books.toscrape.com/catalogue/category/books_1/index.html"
response = requests.get(url)
html_text = response.text
soup = BeautifulSoup(html_text, 'html.parser')

# Find all <h3> tags within the appropriate structure
books = soup.find_all('h3')

for book in books:
    book_title = book.a['title']
    print(f'book title: {book_title}')

    # Extract the price for each book
    bookprice_tag = book.find_next('p', class_='price_color')
    if bookprice_tag:
        bookprice = bookprice_tag.text.strip()
    else:
        bookprice = 'N/A'

    print(f'book price: {bookprice}\n')


