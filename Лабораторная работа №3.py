class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author


    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name=name, author=author)
        self.pages = pages
    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages):

        if not isinstance(pages, int):
            raise TypeError
        if pages <= 0:
            raise ValueError
        self._pages = pages


    def __str__(self):
        return f"Бумажная книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name=name, author=author)
        self.duration = duration
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        if not isinstance(duration, float):
            raise TypeError
        if duration <= 0:
            raise ValueError
        self._duration = duration



    def __str__(self):
        return f"Аудиокнига {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"

book = Book('Война и мир', 'Л.Н. Толстой')
pbook = PaperBook('Война и мир', 'Л.Н. Толстой', 10)
abook = AudioBook('Война и мир', 'Л.Н. Толстой', 3245.6)

print(book, book.__repr__(), sep='\n')
print()
print(pbook, pbook.__repr__(), sep='\n' )
print()
print(abook, abook.__repr__(), sep='\n')
print()

pbook.pages = 12
abook.duration = 1234.1


print('Заменили параметры pages и duration', '\n')

print(pbook.__repr__())
print(abook.__repr__())