class Day01:
    def __init__(self, input):
        self.list_left = []
        self.list_right = []
        self.__parse_input(input)

    def part1_solution(self):
        return Differ(self.list_left, self.list_right).diff()

    def part2_solution(self):
        scorer = SimilarityScorer(self.list_right)

        total_score = 0
        for id in self.list_left:
            total_score += scorer.score(id)

        return total_score
    
    def __parse_input(self, location_lists):
        list_lines = str.splitlines(location_lists)

        for line in list_lines:
            ids = [int(x) for x in line.split("   ")]
            self.list_left.append(int(ids[0]))
            self.list_right.append(int(ids[1]))

        self.__sort()

    def __sort(self):
        self.list_left.sort()
        self.list_right.sort()

class Differ:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def diff(self):
        diff = 0

        for i in range(len(self.left)):
            diff += abs(self.left[i] - self.right[i])

        return diff

class SimilarityScorer:
    def __init__(self, list):
        self.list = list

    def score(self, num):
        return self.__count_right_occurrences(num) * num

    def __count_right_occurrences(self, num):
        return self.list.count(num)
