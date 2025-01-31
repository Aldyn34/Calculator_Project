import pytest
from Calculator.calculator import Calculator

@pytest.fixture
def calculator():
    """Создаем экземпляр калькулятора для использования в тестах."""
    return Calculator()

# Тесты для операций
def test_add(calculator):
    assert calculator.add(2, 3) == 5

def test_subtract(calculator):
    assert calculator.subtract(5, 3) == 2

def test_multiply(calculator):
    assert calculator.multiply(2, 3) == 6

def test_divide(calculator):
    assert calculator.divide(6, 3) == 2

def test_divide_by_zero(calculator):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(1, 0)

# Пример использования setup/teardown
class TestCalculator:
    def setup_method(self, method):
        print(f"Setting up: {method.__name__}")

    def teardown_method(self, method):
        print(f"Tearing down: {method.__name__}")

    def test_add(self, calculator):
        assert calculator.add(10, 15) == 25

    def test_multiply(self, calculator):
        assert calculator.multiply(7, 6) == 42