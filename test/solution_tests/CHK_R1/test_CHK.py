
import pytest
from solutions.CHK import checkout_solution


class TestHello():
    """pytest class for testing the CHK solution"""

    def test_sum(self):
        assert checkout_solution.checkout('AA') == 100
        assert checkout_solution.checkout('AAA') == 130
        assert checkout_solution.checkout('B') == 30
        assert checkout_solution.checkout('BB') == 45
        assert checkout_solution.checkout('AAAA') == 180
        assert checkout_solution.checkout('BBB') == 75
        assert checkout_solution.checkout('BBCD') == 80

    def test_hello_input(self):
        """Check that the input fulfils requirements"""
        with pytest.raises(TypeError) as exc:
            checkout_solution.checkout(20)

        assert f"skus must be a string, got {type(20)}" == str(exc.value)

        with pytest.raises(TypeError) as exc:
            checkout_solution.checkout(10.)

        assert f"skus must be a string, got {type(10.)}" == str(exc.value)

    def test_hello_output_type(self):
        """Check that the function returns an int."""
        assert isinstance(checkout_solution.checkout('BBCD'), int)
