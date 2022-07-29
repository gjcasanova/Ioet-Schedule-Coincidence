"""
Schedule module.

This module contains the functions to solve the problem.
"""

# Local application
from solution import settings

minutes_per_day = 60 * 24
base_minutes_per_day = {
    'MO': 0 * minutes_per_day,
    'TU': 1 * minutes_per_day,
    'WE': 2 * minutes_per_day,
    'TH': 3 * minutes_per_day,
    'FR': 4 * minutes_per_day,
    'SA': 5 * minutes_per_day,
    'SU': 6 * minutes_per_day
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
                    events.append((ingoing, False, name))  # False if is coming.
                    events.append((outgoing, True, name))  # True if is leaving.
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
        return name, times  # ('RENE', [(600, 719), (2040, 2159), (4380, 4499), (8040, 8279), (9840, 9899)])
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
        return base_minutes + time_a, base_minutes + time_b - 1  # (420, 719)

    except Exception:
        raise ValueError('The value of `time` must have the format DDHH:mm-HH:mm.')


def solve(data: list) -> list:
    """Get input data and return the solution."""
    people_in = []
    result = {}
    for _, is_outgoing, name in data:
        if is_outgoing:
            people_in.remove(name)
        else:
            for person in people_in:
                key = (person, name) if person < name else (name, person)
                result[key] = result.get(key, 0) + 1
            people_in.append(name)
    return sorted(result.items(), key=lambda x: (x[1], x[0]))  # [(('ANDRES', 'RENE'), 2)]


def format_solution(solution: list) -> str:
    """Format the solution according to the presentation rules."""
    return '\n'.join([f'{a}-{b}: {result}' for (a, b), result in solution])


def run():
    """Run full solution."""
    data = read_file(settings.DATA_PATH)
    solution = solve(data)
    print(format_solution(solution))
