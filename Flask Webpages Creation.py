from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/search')
def search():
    def find(data):
        results = []
        book_data = data.json()
        books = book_data['items']

        for book in books:
            result = {}
            volumeInfo = book.get('volumeInfo')
            result["title"] = volumeInfo.get('title')
            result["author"] = volumeInfo.get('authors')[0]
            result["description"] = volumeInfo.get('description')
            results.append(result)

        return results

    def search_books(title):
        r = requests.get(
            "https://www.googleapis.com/books/v1/volumes?q={}&key=AIzaSyCbhIgJKBPeTDIhAF4MCY0VXOZoTX3IcAc".format(
                title))
        book_list = find(r)

        return book_list

    print(search_books("harry potter"))

    return render_template('searchResults.html', results=book_list)

@app.route('/')
def home():
    return render_template('homePage.html')

@app.route('/cfgbooks/search/<specific_book>/')
def book(specific_book):
   return render_template('bookDetails.html', specific_book=specific_book)

app.run(debug=True)