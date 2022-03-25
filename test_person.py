import pytest
from person import Person

def test_petr():
    name = 'Petr'
    sex = 'Male'
    petr = Person(sex, name)
    assert str(petr) == 'Petr, Male'

def test_lena():
    name = 'Lena'
    sex = 'Male'
    lena = Person(sex, name)
    assert str(lena) == 'Lena, Male'

def test_can_marry_petr_lena():
    petr = Person('Male', 'Petr')
    lena = Person('Female', 'Lena')
    assert petr._can_marry(lena) == True

def test_marry_petr_lena():
    petr = Person('Male', 'Petr')
    lena = Person('Female', 'Lena')
    petr.marry(lena)
    assert petr.spouse == lena and lena.spouse == petr

def test_cant_marry_petr_john():
    petr = Person('Male', 'Petr')
    john = Person('Male', 'John')
    with pytest.raises(AttributeError):
        petr._can_marry(john)


def test_divorce():
    petr = Person('Male', 'Petr')
    lena = Person('Female', 'Lena')
    petr.marry(lena)
    petr.divorce()
    assert petr.spouse == None and lena.spouse == None
