from flask import Flask, render_template, request
import requests


app = Flask("PyBooks")


@app.route('/search', methods=["POST"])
def search_books():
    form_data = request.form
    search_term = form_data["text"]
    return search_term




    # r = requests.get("https://www.googleapis.com/books/v1/volumes?q=harrypotter&key=AIzaSyCbhIgJKBPeTDIhAF4MCY0VXOZoTX3IcAc")
    # book_list = search(r)
    # return book_list
    # return render_template('searchResults.html', results=book_list)


#def search(data):
    #results = []
    #book_data = data.json()
    #books = book_data['items']

    #for book in books:
    #result = {}
    #volumeInfo = book.get('volumeInfo')
    # result["title"] = volumeInfo.get('title')
    #   result["author"] = volumeInfo.get('authors')[0]
    #   result["description"] = volumeInfo.get('description')
#   results.append(result)


@app.route('/')
def home():
    return render_template('homePage.html')

app.run(debug=True)