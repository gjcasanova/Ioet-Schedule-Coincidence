"""
Schedule module.

This module contains the functions to solve the problem.
"""

minutes_per_day = 60 * 24
days = {
    'MO': 0 * minutes_per_day,
    'TU': 1 * minutes_per_day,
    'WE': 2 * minutes_per_day,
    'TH': 3 * minutes_per_day,
    'FR': 4 * minutes_per_day,
    'SA': 5 * minutes_per_day,
    'SU': 6 * minutes_per_day,
}


def read_file(path: str) -> tuple:
    """Read a .txt file and return the data ready to process."""
    pass


def parse_line(line: str) -> tuple:
    """Parse a line from the input file and return the parsed data."""
    pass


def to_minutes(time: str) -> tuple:
    """Analize a string with format DDHH:mm-HH:mm and return the number of minutes elapsed since Monday at 00:00."""
    pass


def solve(data: tuple) -> tuple:
    """Get input data and return the solution."""
    pass


def format_solution(solution: tuple) -> str:
    """Format the solution according to the presentation rules."""
    pass


def run():
    """Run full solution."""
    pass
