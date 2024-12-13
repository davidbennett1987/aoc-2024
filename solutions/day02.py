class Day02:
    def __init__(self, input):
        self.reports = ReportParser(input).reports

    def part1_solution(self):
        return len([report for report in self.reports if report.is_safe()])

    def part2_solution(self):
        return len([report for report in self.reports if report.is_safe(True)])

class ReportParser:
    def __init__(self, input):
        self.reports = self.__parse(input)

    def __parse(self, input):
        reports_lines = str.splitlines(input)

        reports = []
        for report_line in reports_lines:
            reports.append(Report(report_line))

        return reports

class Report:
    def __init__(self, report_line):
        self.levels = [int(x) for x in report_line.split(" ")]

    def is_safe(self, dampener = False):
        if (self.__levels_safe(self.levels)):
            return True

        if (dampener):
            safe = self.__levels_safe(self.levels)
            if (safe):
                return True

            # Test by omitting a level one-by-one
            for i in range(len(self.levels)):
                safe = self.__levels_safe([x for idx, x in enumerate(self.levels) if idx != i])
                if (safe):
                    break

            return safe

        return False

    def __levels_safe(self, levels):
        asc = list(sorted(levels)) 
        desc = list(reversed(asc))

        # Exit early if the levels are neither all increasing or decreasing
        if (not(levels == asc or levels == desc)):
            return False

        safe = True
        for i in range(len(asc) - 1):
            diff = abs(asc[i] - asc[i + 1])
            if (diff < 1 or diff > 3):
                safe = False
                break

        return safe