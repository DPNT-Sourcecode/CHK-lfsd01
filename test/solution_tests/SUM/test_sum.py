
import pytest
from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_sum_input(self):
        """Check that the function raises a type exception"""
        with pytest.raises(TypeError):
            sum_solution.compute('a', 1)

        with pytest.raises(TypeError):    
            sum_solution.compute(2, 'a')

        with pytest.raises(TypeError):
            sum_solution.compute('a', 'b')

        with pytest.raises(TypeError):
            sum_solution.compute(3.2, 0.8)

        with pytest.raises(ValueError):
            sum_solution.compute(101, 3)

        with pytest.raises(ValueError):
            sum_solution.compute(3, 101)

        with pytest.raises(ValueError):
            sum_solution.compute(-1, 3)

        with pytest.raises(ValueError):
            sum_solution.compute(3, -1)

    def test_sum_output_type(self):
        """Check that the function raises a type exception"""
        assert isinstance(sum_solution.compute(2, 1), int)
        
        


