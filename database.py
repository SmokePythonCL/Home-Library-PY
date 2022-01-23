import sqlite3 as sq

def load():
    try:
        database = ('./database/library.db')
        con = sq.connect(database)
        cur = con.cursor()
        cur.execute('''CREATE TABLE Libros
                    (Título, Autores, Imagen, ISBN)''')

    except sq.OperationalError:
        pass
    
    return cur, con

def save(title, authors, image, cur, con, code):
    keep = input('¿Desea guardar estos datos? [S][N]\n')
    cur.execute(f"INSERT INTO Libros VALUES ( '{title}', '{authors}', '{image}', '{code}')")
    if keep == 'S':
        con.commit()
        print('Se ha guardado la información.')

    elif keep == 'N':
        print('Entonces busquemos otro.')

    else:
        print('Esa opción no existe.')
        save(title, authors, image)

def delete(isbn):
    pass