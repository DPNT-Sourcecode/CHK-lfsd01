
import pytest
from solutions.HLO import hello_solution


class TestHello():
    def test_sum(self):
        assert hello_solution.hello('iwoka') == 'Hello, iwoka!'

    def test_hello_input(self):
        """Check that the input fulfils requirements"""
        with pytest.raises(TypeError) as exc:
            hello_solution.hello(20)

        assert f"friend_name must be a string, got {type(20)}" == str(exc.value)

        with pytest.raises(TypeError) as exc:
            hello_solution.hello(10.)

        assert f"friend_name must be a string, got {type(10.)}" == str(exc.value)

    def test_hello_output_type(self):
        """Check that the function returns an int."""
        assert isinstance(hello_solution.hello('Marco'), str)
