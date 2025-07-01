import pytest
from _pytest.fixtures import SubRequest


#############################################################################################
#                               Базовая параметризация
#############################################################################################

@pytest.mark.parametrize('number', [1, 2, 3, - 1])
def test_number(number: int):
    print(f"Число {number}")
    assert number > 0, f"{number} не больше 0"


#############################################################################################
#                         Базовая параметризация с несколькими параметрами
#############################################################################################

@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 6)])
def test_several_numbers(number: int, expected: int):
    assert number ** expected


#############################################################################################
#                         Матрица параметров(перемножение)
#############################################################################################

@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"])  # Параметризируем по операционной системе
@pytest.mark.parametrize("browser", ["chromium", "webkit", "firefox"])  # Параметризируем по браузеру
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0  # Проверка указана для примера


#############################################################################################
#                         Параметризация через test_pytest.param
#############################################################################################

@pytest.mark.parametrize("x, y, expected",
                         [pytest.param(1, 2, 3, id="simple_case"),
                          pytest.param(2, 2, 5, marks=pytest.mark.skip(reason="bug"), id="xfail_case")])
def test_add(x, y, expected):
    assert x + y == expected


#############################################################################################
#                         Параметризация с помощью словаря(dict)
#############################################################################################

@pytest.mark.parametrize("data", [
    {"username": "user1", "password": "pass1"},
    {"username": "user2", "password": "pass2"},
    {"username": "admin", "password": "admin123"},
])
def test_login(data):
    print(data["username"], data["password"])
    assert login(data["username"], data["password"]) == "Success"


#############################################################################################
#                         Параметризация фикстуры
#############################################################################################

@pytest.fixture(params=["chrome", "firefox", "safari"])
def browser(request: SubRequest) -> str:
    return request.param


def test_browser(browser):
    assert browser in ["chrome", "firefox", "safari"]


#############################################################################################
#                         Параметризация классов
#############################################################################################

@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperations:
    @pytest.mark.parametrize("account", ["Credit card", "Debit card"])
    def test_user_with_operations(self, user: str, account: str):
        print(f"User with operations: {user}")

    def test_user_without_operations(self, user: str):
        print(f"User without operations: {user}")


#############################################################################################
#                         Именование параметризованных тестов(ids)
#############################################################################################
@pytest.mark.parametrize(
    "phone_number",
    ["+70000000011", "+70000000022", "+70000000033"],
    ids=[
        "User with money on bank account",
        "User without money on bank account",
        "User with operations on bank account"
    ]
)
def test_identifiers_01(phone_number: str):
    pass


#############################################################################################
#                          Динамические идентификаторы в параметризации
#############################################################################################

users = {
    "+70000000011": "User with money on bank account",
    "+70000000022": "User without money on bank account",
    "+70000000033": "User with operations on bank account"
}


@pytest.mark.parametrize(
    "phone_number",
    users.keys(),  # Передаем список номеров телефонов
    ids=lambda phone_number: f"{phone_number}: {users[phone_number]}"  # Генерируем идентификаторы динамически
)
def test_identifiers_02(phone_number: str):
    pass


#############################################################################################
#                          Параметризация через indirect
#                    параметр передается в фикстуру, а не напрямую в функцию
#############################################################################################
@pytest.fixture
def user(request: SubRequest):
    return f"user_{request.param}"


@pytest.mark.parametrize("user", ["alice", "bob", "anton"], indirect=True)
def test_user(user):
    assert user.startswith("user_")
