import requests

def find(data):
    book_data = r.json()
    print(book_data['items'])
    book = book_data['items']

    for books in book:
        volumeInfo = books.get('volumeInfo')
        print(volumeInfo.get('title'))
        print(volumeInfo.get('authors'))
        print(volumeInfo.get('description'))

title_or_auth = input('title or author or both? ')

if title_or_auth == 'title':
    search = input('which title would you like to find?: ')
    r = requests.get("https://www.googleapis.com/books/v1/volumes?q={}&key=AIzaSyCbhIgJKBPeTDIhAF4MCY0VXOZoTX3IcAc".format(search))
    find(r)
elif title_or_auth == 'author':
    search = input('which author would you like to find?: ')
    r = requests.get("https://www.googleapis.com/books/v1/volumes?q=inauthor:{}&key=AIzaSyCbhIgJKBPeTDIhAF4MCY0VXOZoTX3IcAc".format(search))
    find(r)
else:
    title_search = input('which title would you like to find?: ')
    author_search = input('which author would you like to find?: ')
    r = requests.get("https://www.googleapis.com/books/v1/volumes?q={}+inauthor:{}&key=AIzaSyCbhIgJKBPeTDIhAF4MCY0VXOZoTX3IcAc".format(title_search, author_search))
    find(r)




