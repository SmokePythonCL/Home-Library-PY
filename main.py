from urllib.request import urlopen
import requests_html
from PIL import Image
from io import BytesIO
import json


def search(session, code, key):

    try:
        page = urlopen('https://www.googleapis.com/books/v1/volumes?q=isbn:{}&key={}'.format(code, key))
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


def save(title, authors, image):
    keep = input('¿Desea guardar estos datos? [S][N]\n')
    if keep == 'S':
        pass
    elif keep == 'N':
        print('Entonces busquemos otro.')
        main()
    else:
        print('Esa opción no existe.')
        save(title, authors, image)


def main():
    try:
        session = requests_html.HTMLSession()
        key = '' #Here's go yours API key.
        code = input('Introduce ISBN: ')
        title, authors, image = search(session, code, key)
        print(title + '\n' + authors)
        image.show()
        save(title, authors, image)
        

    except AttributeError:
        print('Hubo un error, intenta con otro ISBN')
        main()


if __name__ == '__main__':
    main()