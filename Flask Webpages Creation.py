from flask import Flask, render_template

app = Flask(__name__)


@app.route('/cfgbooks/')
def content():
    return render_template('homePage.html')


@app.route('/cfgbooks/search/')
def results():
    return render_template('searchResults.html')

@app.route('/cfgbooks/search/<specific_book>/')
def book(specific_book):
   return render_template('bookDetails.html', specific_book=specific_book)

app.run(debug=True)