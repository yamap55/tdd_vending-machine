import pytest

from vending_machine.money import Money


def test_exists_money():
    for m in Money:
        assert m.amount


def test_error_money():
    with pytest.raises(ValueError) as excinfo:
        Money(11)

    actual = str(excinfo.value)
    expected = "11 is not a valid Money"
    assert actual == expected
