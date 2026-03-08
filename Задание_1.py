BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

class Book:
    """Класс, книга."""

    def __init__(self, id: int, name: str, pages: int):
        """
        Инициализирует экземпляр книга.

        :param id: id книги
        :param name: название книги
        :param pages: кол-во страниц
        """
        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """Возвращает строковое представление."""
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """Возвращает строку Python для воссоздания экземпляра."""
        return f"Book(id={self.id}, name={repr(self.name)}, pages={self.pages})"


if __name__ == "__main__":
    # инициализируем список книг
    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"])
        for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__
    print(list_books)  # проверяем метод __repr__