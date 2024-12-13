from solutions.day01 import Day01
from solutions.day02 import Day02
from solutions.day03 import Day03

from utils.file_utils import read_file
import logging
import time

logging.basicConfig(format="%(asctime)s.%(msecs)03d:%(levelname)s:%(name)s:\t%(message)s", 
                    datefmt='%H:%M:%S')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def main():
    day01input = read_file("input/day01/input.txt")
    day01 = Day01(day01input)
    logger.info(f"Day 01, part 1 answer is: {day01.part1_solution()}")
    logger.info(f"Day 01, part 2 answer is: {day01.part2_solution()}")

    day02input = read_file("input/day02/input.txt")
    day02 = Day02(day02input)
    logger.info(f"Day 02, part 1 answer is: {day02.part1_solution()}")
    logger.info(f"Day 02, part 2 answer is: {day02.part2_solution()}")

    day03input = read_file("input/day03/input.txt")
    day03 = Day03(day03input)
    logger.info(f"Day 03, part 1 answer is: {day03.part1_solution()}")
    logger.info(f"Day 03, part 2 answer is: {day03.part2_solution()}")

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    logger.info("Execution time: %0.2fms", (t2 - t1) * 1000)