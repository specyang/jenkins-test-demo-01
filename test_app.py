import pytest # <-- 确保这一行是文件的第一行
from app import Calculator

@pytest.fixture
def calculator_instance():
    return Calculator()

def test_add(calculator_instance):
    print("\nRunning test_add...")
    assert calculator_instance.add(2, 3) == 5
    assert calculator_instance.add(-1, 1) == 0
    assert calculator_instance.add(-2, -3) == -5

def test_subtract(calculator_instance):
    print("\nRunning test_subtract...")
    assert calculator_instance.subtract(3, 2) == 1
    assert calculator_instance.subtract(0, 2) == -2

def test_multiply(calculator_instance):
    print("\nRunning test_multiply...")
    assert calculator_instance.multiply(2, 3) == 6
    assert calculator_instance.multiply(5, 0) == 0
    assert calculator_instance.multiply(2, -3) == -6

def test_divide(calculator_instance):
    print("\nRunning test_divide...")
    assert calculator_instance.divide(6, 3) == 2.0
    assert calculator_instance.divide(5, 2) == 2.5

def test_divide_by_zero(calculator_instance):
    print("\nRunning test_divide_by_zero (expecting exception)...")
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator_instance.divide(10, 0)

