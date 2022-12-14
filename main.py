from flask import Flask, request

app = Flask(__name__)
app.debug = True

books = []
cars = []

class Book(object):
    def __init__(self, title, author, cost):
        self.title, self.author, self.cost = title, author, cost

class Car(object):
    def __init__(self, title, mark, cost):
        self.title, self.mark, self.cost = title, mark, cost

@app.route('/', methods=['GET'])
def index():
    return "Главная страница. Ссылки на другие страницы: Книги: http://localhost:3005/books, машины: http://localhost:3005/cars"

@app.route('/books/', methods=['GET', 'POST'])
def post_and_get_books():
    if request.method == 'GET':
        a = ''
        book = ''
        for i in books:
            book = f"Название книги: {i.title}, автор книги: {i.author}, цена книги: {i.cost}"
            a = a + book
        return a, 200
    if request.method == 'POST':
        rqs = request.get_json()
        title = None
        author = None
        cost = None
        if rqs:
            if 'title' in rqs:
                title = rqs['title']
            else:
                return "Поле с названием книги не найдено. Введите заново"
            if 'author' in rqs:
                author = rqs['author']
            else:
                return "Поле с автором книги не найдено. Введите заново"
            if 'cost' in rqs:
                cost = rqs['cost']
            else:
                return "Поле с ценой книги не найдено. Введите заново"
        else:
            return "Запрос не обнаружен", 403
        if title and author and cost:
            book = Book(title, author, cost)
            books.append(book)
            return "Книга добавлена успешно", 201


@app.route('/books/<int:bookid>', methods=['DELETE', 'PUT'])
def delete_and_put_books(bookid):
    if request.method == 'DELETE':
        books.pop(bookid)
        return "Книга удалена успешно", 200
    if request.method == 'PUT':
        rqs = request.get_json()
        if rqs:
            if 'title' in rqs:
                books[bookid].title = rqs['title']
            if 'author' in rqs:
                books[bookid].author = rqs['author']
            if 'cost' in rqs:
                books[bookid].cost = rqs['cost']
        else:
            return "Запрос не обнаружен", 403
        return "Книга отредактирована успешно", 200

@app.route('/cars/', methods=['GET', 'POST'])
def post_and_get_cars():
    if request.method == 'GET':
        a = ''
        car = ''
        for i in cars:
            car = f"Название машины: {i.title}, марка машины: {i.mark}, цена машины: {i.cost}"
            a = a + car
        return a, 200
    if request.method == 'POST':
        rqs = request.get_json()
        title = None
        mark = None
        cost = None
        if rqs:
            if 'title' in rqs:
                title = rqs['title']
            else:
                return "Поле с названием машины не найдено. Введите заново"
            if 'mark' in rqs:
                mark = rqs['mark']
            else:
                return "Поле с маркой машины не найдено. Введите заново"
            if 'cost' in rqs:
                cost = rqs['cost']
            else:
                return "Поле с ценой машины не найдено. Введите заново"
        else:
            return "Запрос не обнаружен", 403
        if title and mark and cost:
            car = Car(title, mark, cost)
            cars.append(car)
            return "Машина добавлена успешно", 201


@app.route('/cars/<int:carid>', methods=['DELETE', 'PUT'])
def delete_and_put_cars(carid):
    if request.method == 'DELETE':
        cars.pop(carid)
        return "Машина удалена успешно", 200
    if request.method == 'PUT':
        rqs = request.get_json()
        if rqs:
            if 'title' in rqs:
                cars[carid].title = rqs['title']
            if 'author' in rqs:
                cars[carid].author = rqs['author']
            if 'cost' in rqs:
                cars[carid].cost = rqs['cost']
        else:
            return "Запрос не обнаружен", 403
        return "Машина отредактирована успешно", 200



if __name__ == "__main__":
    app.run(host="localhost", port=3005)





