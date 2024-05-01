#from django.test import TestCase
import pytest
from . import views

#some simple example tests
def test_print_message():
    assert views.print_message(None)=="test123"
# Create your tests here.

def test_get_today_date_type():#type test
    assert type(views.get_today_date()) == str

def test_get_today_date_value():
    import datetime
    assert views.get_today_date()== str(datetime.datetime.now)

#polindrom tests

from . import functions
@pytest.mark.parametrize(
        ('input','expected_output'),
        (
            (121,True),
            (-121,False),
            (10,False),

        )
)
def test_is_palindrome(input,expected_output):
    assert functions.Solution.is_palindrome(input)==expected_output
    