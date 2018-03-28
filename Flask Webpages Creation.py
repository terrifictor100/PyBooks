from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    params = {
        'api_key': 'AIzaSyCbhIgJKBPeTDIhAF4MCY0VXOZoTX3IcAc',
        'format': 'json'
    }
    r = requests.get(
        "https://www.googleapis.com/books/v1/volumes?q=harrypotter&key=AIzaSyCbhIgJKBPeTDIhAF4MCY0VXOZoTX3IcAc".format(search))
    return render_template('../templates/homePage.html')


@app.route('/cfgbooks/search/')
def results():
    return render_template('searchResults.html')

@app.route('/cfgbooks/search/<specific_book>/')
def book(specific_book):
   return render_template('bookDetails.html', specific_book=specific_book)

app.run(debug=True)