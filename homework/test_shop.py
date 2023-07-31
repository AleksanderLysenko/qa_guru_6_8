"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1)
        assert product.check_quantity(1000)
        assert not product.check_quantity(100000)
        assert product.check_quantity(500)
        assert product.check_quantity(0)
        assert not product.check_quantity(-1)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(1)
        assert product.quantity == 999

        product.buy(0)
        assert product.quantity == 999

        product.buy(599)
        assert product.quantity == 400

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии

        with pytest.raises(ValueError):
            product.buy(10000)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_cart_add_product(self, cart, product):
        cart.add_product(product)
        assert product in cart.products
        assert cart.products[product] == 1

        cart.add_product(product, buy_count=20)
        assert cart.products[product] == 21

    def test_cart_remove_product(self, cart, product):
        cart.add_product(product, 10)
        cart.remove_product(product)
        assert product not in cart.products

        cart.add_product(product, 10)
        cart.remove_product(product, remove_count=10)
        assert product not in cart.products

        cart.add_product(product, 10)
        cart.remove_product(product, remove_count=5)
        assert cart.products[product] == 5

        cart.add_product(product, 10)
        cart.remove_product(product, remove_count=20)
        assert product not in cart.products

    def test_cart_clear(self, cart, product):
        cart.add_product(product, 10)
        cart.clear()
        assert product not in cart.products

    def test_cart_total_price(self, cart, product):
        cart.add_product(product, 10)
        assert cart.get_total_price() == 1000

        cart.remove_product(product, remove_count=5)
        assert cart.get_total_price() == 500

    def test_cart_buy(self, cart, product):
        cart.add_product(product, 100)
        cart.buy()
        assert product.quantity == 900

