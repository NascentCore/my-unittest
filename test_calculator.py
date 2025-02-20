import pytest
from calculator import add_numbers, multiply_numbers

def test_add_numbers():
    # 测试正数相加
    assert add_numbers(1, 2) == 3
    
    # 测试负数相加
    assert add_numbers(-1, -1) == -2
    
    # 测试零的相加
    assert add_numbers(0, 0) == 0
    
    # 测试小数相加
    assert add_numbers(0.1, 0.2) == pytest.approx(0.3)

def test_multiply_numbers():
    # 测试正数相乘
    assert multiply_numbers(2, 3) == 6
    
    # 测试负数相乘
    assert multiply_numbers(-2, 3) == -6
    
    # 测试零相乘
    assert multiply_numbers(0, 5) == 0
    
    # 测试小数相乘
    assert multiply_numbers(0.1, 0.1) == pytest.approx(0.01) 