import pytest


@pytest.fixture()
def clear_books_database():
    print("[clear_books_database] очищаем БД")


@pytest.fixture()
def fill_book_database():
    print("[fill_book_database] создаем данные в  БД")

@pytest.mark.usefixtures("clear_books_database")
def test_read_books_db():
    pass