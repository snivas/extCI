import calc


class TestCalc:

    def test_addition(self):
        assert 4 == calc.add(2, 2)

    def test_subtraction(self):
        assert 2 == calc.subtract(4, 2)
