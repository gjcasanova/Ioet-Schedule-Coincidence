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


def read_file(path: str) -> list:
    """Read a .txt file and return the data ready to process."""
    events = []
    try:
        with open(path) as file:
            lines = file.readlines()
            for line in lines:
                name, times = parse_line(line)
                for ingoing, outgoing in times:
                    events.append((ingoing, True, name))
                    events.append((outgoing, False, name))
        events.sort()
        return events
    except Exception:
        raise ValueError('The file is not valid.')


def parse_line(line: str) -> tuple:
    """Parse a line from the input file and return the parsed data."""
    try:
        name, frames = line.split('=')
        times = []
        for frame in frames.split(','):
            time = to_minutes(frame)
            times.append(time)
        return name, times
    except Exception:
        raise ValueError('The value of `line` must have the format name=DDHH:mm-HH:mm,DDHH:mm-HH:mm...')


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
