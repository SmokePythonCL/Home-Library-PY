from urllib.request import urlopen
import requests_html
from PIL import Image
from io import BytesIO
import json
from database import load, save, delete


def search(session, code, key):

    try:
        page = urlopen(f'https://www.googleapis.com/books/v1/volumes?q=isbn:{code}&key={key}')
        data_json = json.loads(page.read())
        info = data_json['items'][0]['volumeInfo']
        title = info['title']
        authors = str(info['authors']).replace('[', '').replace(']', '').replace("'", '').replace("'", '')
        front = info['imageLinks']['thumbnail']
        front_download = session.get(front)
        image = Image.open(BytesIO(front_download.content))

        return title, authors, image

    except TypeError:
        print('No reconozco el ISBN')
    
    except KeyError:
        image = ''
        return title, authors, image


def main():
    cur, con = load()
    title, authors, image = '', '', ''
    try:
        session = requests_html.HTMLSession()
        key = '' #Here's go yours API key.
        code = input('Introduce ISBN: ')
        title, authors, image = search(session, code, key)
        print(title + '\n' + authors)

        if image == '':
            save(title, authors, image, cur, con, code)

        else:
            image.show()
            save(title, authors, image, cur, con, code)
            
        

    except AttributeError:
        print('Hubo un error, intenta con otro ISBN')
        main()

    con.close()


if __name__ == '__main__':
    main()