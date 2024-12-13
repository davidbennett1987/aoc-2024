import pytest

from utils.file_utils import read_file
from solutions.day02 import Day02, Report, ReportParser

@pytest.fixture
def input_example():
    return read_file("input/day02/test_input.txt")

def test_p1_parse_reports(input_example):
    report_parser = ReportParser(input_example)

    assert len(report_parser.reports) == 6
    assert all(isinstance(report, Report) for report in report_parser.reports) == True
    assert all(len(report.levels) > 0 for report in report_parser.reports) == True

def test_p1_report_is_safe(input_example):
    report1 = Report("7 6 4 2 1")
    report2 = Report("1 2 7 8 9")
    report3 = Report("9 7 6 2 1")
    report4 = Report("1 3 2 4 5")
    report5 = Report("8 6 4 4 1")
    report6 = Report("1 3 6 7 9")

    assert report1.is_safe() == True
    assert report2.is_safe() == False
    assert report3.is_safe() == False
    assert report4.is_safe() == False
    assert report5.is_safe() == False
    assert report6.is_safe() == True

def test_p1_report_is_safe_with_dampener(input_example):
    report1 = Report("7 6 4 2 1")
    report2 = Report("1 2 7 8 9")
    report3 = Report("9 7 6 2 1")
    report4 = Report("1 3 2 4 5")
    report5 = Report("8 6 4 4 1")
    report6 = Report("1 3 6 7 9")

    assert report1.is_safe(True) == True
    assert report2.is_safe(True) == False
    assert report3.is_safe(True) == False
    assert report4.is_safe(True) == True
    assert report5.is_safe(True) == True
    assert report6.is_safe(True) == True

# Example solutions
def test_p1_solution(input_example):
    day02 = Day02(input_example)

    assert day02.part1_solution() == 2

def test_p2_solution(input_example):
    day02 = Day02(input_example)

    assert day02.part2_solution() == 4