"""
Schedule module.

This module contains the functions to solve the problem.
"""

minutes_per_day = 60 * 24
base_minutes_per_day = {
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
    def parse_time(time: str) -> int:
        """Calculate the minutes elapsed since the beginning of the day."""
        hh, mm = map(int, time.split(':'))
        return 60*hh + mm

    try:
        day = time[:2]
        base_minutes = base_minutes_per_day[day]
        time_a, time_b = map(parse_time, time[2:].split('-'))
        return base_minutes + time_a, base_minutes + time_b

    except Exception:
        raise ValueError('The value of `time` must have the format DDHH:mm-HH:mm.')


def solve(data: tuple) -> tuple:
    """Get input data and return the solution."""
    pass


def format_solution(solution: tuple) -> str:
    """Format the solution according to the presentation rules."""
    pass


def run():
    """Run full solution."""
    pass
