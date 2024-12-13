import pytest

from utils.file_utils import read_file
from solutions.day01 import Day01, Differ, SimilarityScorer

@pytest.fixture
def input_example():
    return read_file("input/day01/test_input.txt")

def test_p1_left_right_sort(input_example):
    day01 = Day01(input_example)

    assert day01.list_left == [1, 2, 3, 3, 3, 4]
    assert day01.list_right == [3, 3, 3, 4, 5, 9]

def test_p1_diff(input_example):
    day01 = Day01(input_example)
    differ = Differ(day01.list_left, day01.list_right)

    assert differ.diff() == 11

def test_p2_scorer(input_example):
    day01 = Day01(input_example)
    scorer = SimilarityScorer(day01.list_right)

    assert scorer.score(3) == 9
    assert scorer.score(4) == 4
    assert scorer.score(2) == 0
    assert scorer.score(1) == 0

# Example solutions
def test_p1_solution(input_example):
    day01 = Day01(input_example)

    assert day01.part1_solution() == 11

def test_p2_solution(input_example):
    day01 = Day01(input_example)

    assert day01.part2_solution() == 31