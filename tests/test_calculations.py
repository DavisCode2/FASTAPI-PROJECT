import pytest

from app.calculations import add, subtract, multiply, divide, BankAccount

@pytest.mark.parametrize("num1, num2, expected", [(6, 16, 22), (8, 1, 9), (0, 24, 24)])
def test_add(num1, num2, expected):
    print("testing add function")
    assert add(num1,num2) == expected

def test_subtract():
    assert subtract(9, 4) == 5

def test_multiply():
    assert multiply(2,3) == 6

def test_divide():
    assert divide(5,1) == 5

def test_bank_set_initial_amount():
    bank_account = BankAccount(50)
    assert bank_account.balance == 50