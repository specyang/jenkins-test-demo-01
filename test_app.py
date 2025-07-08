Python 3.13.5 (v3.13.5:6cb20a219a8, Jun 11 2025, 12:23:45) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
# File: test_app.py
import pytest
... from app import Calculator
... 
... @pytest.fixture
... def calculator_instance():
...     return Calculator()
... 
... def test_add(calculator_instance):
...     print("\nRunning test_add...")
...     assert calculator_instance.add(2, 3) == 5
...     assert calculator_instance.add(-1, 1) == 0
...     assert calculator_instance.add(-2, -3) == -5
... 
... def test_subtract(calculator_instance):
...     print("\nRunning test_subtract...")
...     assert calculator_instance.subtract(3, 2) == 1
...     assert calculator_instance.subtract(0, 2) == -2
... 
... def test_multiply(calculator_instance):
...     print("\nRunning test_multiply...")
...     assert calculator_instance.multiply(2, 3) == 6
...     assert calculator_instance.multiply(5, 0) == 0
...     assert calculator_instance.multiply(2, -3) == -6
... 
... def test_divide(calculator_instance):
...     print("\nRunning test_divide...")
...     assert calculator_instance.divide(6, 3) == 2.0
...     assert calculator_instance.divide(5, 2) == 2.5
... 
... def test_divide_by_zero(calculator_instance):
...     print("\nRunning test_divide_by_zero (expecting exception)...")
...     with pytest.raises(ValueError, match="Cannot divide by zero"):
...         calculator_instance.divide(10, 0)
... 
... # --- 用于面试时演示测试失败的场景 ---
... # 第一次演示时请注释掉此测试，待演示成功后，再取消注释并重新提交，以演示测试失败的报告
... # def test_failing_scenario(calculator_instance):
... #     print("\nRunning a deliberately failing test...")
... #     assert calculator_instance.add(1, 1) == 3 # This line will cause the test to fail
