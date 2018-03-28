from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/search')
def search():
    return render_template('searchResults.html')


@app.route('/')
def home():
    return render_template('homePage.html')

@app.route('/cfgbooks/search/<specific_book>/')
def book(specific_book):
   return render_template('bookDetails.html', specific_book=specific_book)

app.run(debug=True)