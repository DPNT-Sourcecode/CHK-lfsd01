
import pytest
from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_sum_input(self):
        """Check that the input fulfils requirements"""
        with pytest.raises(TypeError) as exc:
            sum_solution.compute('a', 1)
        
        assert f"x must be integer, got {type('a')}" == str(exc.value)

        with pytest.raises(TypeError) as exc:   
            sum_solution.compute(2, 'a')
        
        assert f"y must be integer, got {type('a')}" == str(exc.value)

        with pytest.raises(TypeError) as exc:
            sum_solution.compute('a', 'b')

        assert f"x must be integer, got {type('a')}" == str(exc.value)

        with pytest.raises(TypeError) as exc:
            sum_solution.compute(3.2, 2)

        assert f"x must be integer, got {type(3.2)}" == str(exc.value)

        with pytest.raises(ValueError) as exc:
            sum_solution.compute(101, 3)

        assert f"x must be between 0 and 100 (bounds included), got 101" == str(exc.value)

        with pytest.raises(ValueError) as exc:
            sum_solution.compute(3, 101)

        assert f"y must be between 0 and 100 (bounds included), got 101" == str(exc.value)

        with pytest.raises(ValueError) as exc:
            sum_solution.compute(-1, 3)

        assert f"x must be between 0 and 100 (bounds included), got -1" == str(exc.value)

        with pytest.raises(ValueError) as exc:
            sum_solution.compute(3, -1)

        assert f"y must be between 0 and 100 (bounds included), got -1" == str(exc.value)


    def test_sum_output_type(self):
        """Check that the function returns an int."""
        assert isinstance(sum_solution.compute(2, 1), int)
        
        


