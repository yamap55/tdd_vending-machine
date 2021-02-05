from vending_machine.money import Money


def test_exists_money():

    money = Money(100)
    assert money
    assert money.amount == 100
