from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()



    def test_add_new_book_add_it_again(self):
        collector = BooksCollector()
        collector.add_new_book('Легенда')
        collector.add_new_book('Легенда')
        assert len(collector.books_rating) == 1

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Legend')
        collector.add_book_in_favorites('Legend')
        assert 'Legend' in collector.get_list_of_favorites_books()

    def test_set_book_rating_for_none_element(self):
        collector = BooksCollector()
        collector.set_book_rating('Fox', 7)
        assert collector.get_book_rating('Fox') != 7

    def test_get_books_with_specific_rating_certain_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Freedom')
        collector.add_new_book('Punisher')
        collector.add_new_book('Monster')
        collector.set_book_rating('Freedom', 5)
        collector.set_book_rating('Punisher', 3)
        collector.set_book_rating('Monster', 5)
        books_list = collector.get_books_with_specific_rating(5)
        assert 'Freedom' and 'Monster' in books_list

    def test_get_books_rating(self):
        collector = BooksCollector()
        assert collector.get_books_rating() == collector.books_rating

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Dark')
        collector.delete_book_from_favorites('Dark')
        assert 'Dark' not in collector.favorites

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        book_list = ['Fly', 'Lord', 'Tiger']
        for book_name in book_list:
            collector.add_new_book(book_name)
            collector.add_book_in_favorites(book_name)
        assert collector.favorites == book_list

    def test_set_book_rating_more_than_10(self):
        collector = BooksCollector()
        collector.add_new_book('Harry Potter')
        collector.set_book_rating('Harry Potter', 15)
        assert collector.books_rating['Harry Potter'] != 15

    def test_set_book_rating_less_than_one(self):
        collector = BooksCollector()
        collector.add_new_book('Live')
        collector.set_book_rating('Live', 0)
        assert collector.books_rating['Live'] != 0

