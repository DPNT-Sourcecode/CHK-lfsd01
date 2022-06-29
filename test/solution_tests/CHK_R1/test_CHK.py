
import pytest
from solutions.CHK import checkout_solution


class TestHello():
    """pytest class for testing the CHK solution"""

    def test_sum(self):
        # assert checkout_solution.checkout('AA') == 100
        # assert checkout_solution.checkout('AAA') == 130
        # assert checkout_solution.checkout('B') == 30
        # assert checkout_solution.checkout('BB') == 45
        # assert checkout_solution.checkout('AAAA') == 180
        # assert checkout_solution.checkout('BBB') == 75
        # assert checkout_solution.checkout('BBCD') == 80

        # # CHK R2
        # assert checkout_solution.checkout('AAA') == 130
        # assert checkout_solution.checkout('AAAAAAAAAAAAA') == 400 + 130
        # assert checkout_solution.checkout('AAAAAAAAAAAA') == 400 + 100
        # assert checkout_solution.checkout('EE') == 80
        # assert checkout_solution.checkout('EEB') == 80
        # assert checkout_solution.checkout('EEEB') == 120

        # assert checkout_solution.checkout('BBCDE') == 45 + 20 + 15 + 40
        # assert checkout_solution.checkout('BBBBCDE') == 90 + 20 + 15 + 40
        # assert checkout_solution.checkout('BBBCDEEE') == 75 + 20 + 15 + 120 - 30
        # assert checkout_solution.checkout('BBBCDEEEE') == 30 + 20 + 15 + 160

        # # CHK R3
        # assert checkout_solution.checkout('FF') == 20
        # assert checkout_solution.checkout('FFF') == 20
        # assert checkout_solution.checkout('FFFFF') == 40
        # assert checkout_solution.checkout('FFFFFF') == 40
        # assert checkout_solution.checkout('PPPPQRUVPQRUVPQRUVSU') == 740

        # # CHK R4
        # assert checkout_solution.checkout('UUU') == 120

        # CHK R5
        assert checkout_solution.checkout('AASTXZXBBEE') == 1222

    def test_hello_input(self):
        """Check that the input fulfils requirements"""
        assert checkout_solution.checkout(10) == -1
        assert checkout_solution.checkout(20.) == -1
        # assert checkout_solution.checkout('AAAAX') == -1
        # assert checkout_solution.checkout('ABOAAX') == -1
        assert checkout_solution.checkout(10) == -1
        assert checkout_solution.checkout(10) == -1

    def test_hello_output_type(self):
        """Check that the function returns an int."""
        assert isinstance(checkout_solution.checkout('BBCD'), int)

