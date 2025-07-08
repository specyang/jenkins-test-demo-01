Python 3.13.5 (v3.13.5:6cb20a219a8, Jun 11 2025, 12:23:45) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> # File: app.py
... class Calculator:
...     def add(self, a, b):
...         return a + b
... 
...     def subtract(self, a, b):
...         return a - b
... 
...     def multiply(self, a, b):
...         return a * b
... 
...     def divide(self, a, b):
...         if b == 0:
...             raise ValueError("Cannot divide by zero")
...         return a / b
