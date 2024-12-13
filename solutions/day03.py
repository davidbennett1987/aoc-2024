import math
import re

class Day03:
    def __init__(self, input):
        self.memory_parser = MemoryParser(input)

    def part1_solution(self):
        muls = self.memory_parser.findMuls()

        return sum([x.calculate() for x in muls])

    def part2_solution(self):
        muls = self.memory_parser.findMulsWithInstructions()

        return sum([x.calculate() for x in muls])

class MemoryParser:
    def __init__(self, memory):
        self.memory = memory
        self.mul_matcher = re.compile("mul\((\d{1,3},\d{1,3})\)")

    def findMuls(self):
        matches = self.mul_matcher.findall(self.memory)

        return [Mul(x) for x in matches]

    def findMulsWithInstructions(self):
        do_blocks = self.memory.split("do()")
        enabled_memory = [x.split("don't()")[0] for x in do_blocks]

        matches = []
        for block in enabled_memory:
            matches.extend(self.mul_matcher.findall(block))

        return [Mul(x) for x in matches]

class Mul:
    def __init__(self, input):
        self.input = input
        self.factors = [int(x) for x in input.split(",")]

    def calculate(self):
        return math.prod(self.factors)
