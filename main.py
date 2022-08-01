"""
Main module.

Interact with this module to run the solution.
"""

# Standard application
import sys

# Local applications
from solution import schedule, settings


def run(data_path):
    """Run full solution."""
    lines = schedule.read_file(data_path)
    timeline = schedule.get_timeline(lines)
    solution = schedule.solve(timeline)
    print(schedule.format_solution(solution))


if __name__ == '__main__':
    args = dict(arg.split('=') for arg in sys.argv[1:])
    data_path = args.get('data_path', settings.DATA_PATH)
    run(data_path)
