import pytest
from unittest import mock
import builtins
from quiz import run_quiz, questions


def test_run_quiz_with_no_answers():
    input_values = iter(['', '', ''])

    def mock_input():
        return next(input_values)

    with pytest.raises(TypeError):
        with mock.patch.object(builtins, 'input', mock_input):
            run_quiz(questions)


def test_run_quiz_with_correct_answers():
    input_values = iter(['c', 'a', 'b'])

    def mock_input(s):
        return next(input_values)

    with mock.patch.object(builtins, 'input', mock_input):
        assert run_quiz(questions) == "You got 3 out of 3 correct."


def test_run_quiz_with_incorrect_answers():
    input_values = iter(['b', 'c', 'a'])

    def mock_input(s):
        return next(input_values)

    with mock.patch.object(builtins, 'input', mock_input):
        assert run_quiz(questions) == "You got 0 out of 3 correct."


def test_run_quiz_with_incorrect_input():
    input_values = iter(['y', 'x', 'z'])

    def mock_input():
        return next(input_values)

    with pytest.raises(TypeError):
        with mock.patch.object(builtins, 'input', mock_input):
            run_quiz(questions)
