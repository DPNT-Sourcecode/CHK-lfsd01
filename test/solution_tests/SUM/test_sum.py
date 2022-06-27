from typing import Type
import pytest

from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_sum_input_type(self):
        with pytest.raises(TypeError):
            sum_solution.compute('a', 1)
            sum_solution.compute(2, 'a')
            sum_solution.compute('a', 'b')

