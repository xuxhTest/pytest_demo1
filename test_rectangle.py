#!/usr/bin/env python3

"""
# @Create    : 2020/8/3   
# @Author  : xuxh
# @Description   :  说明文件功能
# @Modify Time      @Version    @Description
------------      --------    -----------
2020/8/3             1.0         None
"""


from rectangle import Rectangle
import pytest
from time import sleep


@pytest.fixture()
def my_rect():
    rect = Rectangle(30, 15)
    print(rect.length)
    print(rect.width)
    return rect


@pytest.mark.smoke
@pytest.mark.p1
def test_area(my_rect):
    sleep(10)
    assert my_rect.area() == 450


@pytest.mark.regression
@pytest.mark.repeat(5)
def test_perimeter(my_rect):
    sleep(10)
    assert my_rect.perimeter() == 90


@pytest.mark.parametrize(("length", "width", "expected_diff"), [(30, 20, 10), (20, 20, 0)])
def test_diff(length, width, expected_diff):
    sleep(5)
    rect = Rectangle(length, width)
    assert rect.diff() == expected_diff


def test_length(my_rect):
    assert my_rect.length == 30


