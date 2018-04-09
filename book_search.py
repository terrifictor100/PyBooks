import requests

def find(data):
    results = []
    titles = []
    results = []
    book_data = data.json()
    books = book_data['items']

    for book in books:
        result = {}
        volumeInfo = book.get('volumeInfo')
        result["title"] = volumeInfo.get('title')
        #result["author"] = volumeInfo.get('authors')[0]
        #result["description"] = volumeInfo.get('description')
        results.append(result)


    return results

def search_books (title):
    r = requests.get("https://www.googleapis.com/books/v1/volumes?q={}&key=AIzaSyCbhIgJKBPeTDIhAF4MCY0VXOZoTX3IcAc".format(title))
    book_list = find(r)

    return book_list

print(search_books("harry potter"))



