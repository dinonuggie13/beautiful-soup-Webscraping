from bs4 import BeautifulSoup
import requests

base_url = "https://books.toscrape.com/catalogue/category/books_1/index.html"
current_page_url = base_url

while True:
    print(f"Scraping page: {current_page_url}")  # Debugging: Print the current page URL
    response = requests.get(current_page_url)
    if response.status_code != 200:
        print(f"Failed to fetch {current_page_url}. Status code: {response.status_code}")
        break

    html_text = response.text
    soup = BeautifulSoup(html_text, 'html.parser')

    # Find all <h3> tags within the appropriate structure for each page
    books = soup.find_all('h3')
    counter = 0

    for book in books:
        book_title = book.a['title']
        print(f'Book title: {book_title}')

        # Extracting the price for each book
        bookprice_tag = book.find_next('p', class_='price_color')
        if bookprice_tag:
            bookprice = bookprice_tag.text.strip()
            counter += 1
        else:
            bookprice = 'N/A'

        print(f'Book price: {bookprice}')
        print(f'Book count: {counter}\n')

    # Find the next page link
    next_link = soup.find('li', class_='next')
    
    if next_link:
        next_page = next_link.find('a')['href']
        current_page_url = base_url.rsplit('/', 1)[0] + '/' + next_page
       
    else:
        print('No more pages available')
        print(next_page)
        break


