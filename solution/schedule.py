"""
Schedule module.

This module contains the functions to solve the problem.
"""

# Standard library
from datetime import datetime, timedelta

date_formats = {
    'MO': '1990-01-01 {}',
    'TU': '1990-01-02 {}',
    'WE': '1990-01-03 {}',
    'TH': '1990-01-04 {}',
    'FR': '1990-01-05 {}',
    'SA': '1990-01-06 {}',
    'SU': '1990-01-07 {}'
}


def read_file(path: str) -> list:
    """Read a .txt file and return a list with its lines."""
    try:
        file = open(path)
        lines = file.readlines()
        return lines
    except Exception:
        raise ValueError('The file is not valid.')


def get_timeline(lines: list) -> list:
    """Return a timeline with the events in the office (people arriving and leaving)."""
    events = []
    try:
        for line in lines:
            name, times = parse_line(line)
            for ingoing, outgoing in times:
                events.append((ingoing, False, name))  # False if is coming.
                events.append((outgoing, True, name))  # True if is leaving.
        events.sort()
        return events
    except Exception:
        raise ValueError('The format of the lines in file is not valid.')


def parse_line(line: str) -> tuple:
    """Parse a line from the input file and return the parsed data."""
    try:
        name, frames = line.strip().split('=')
        times = []
        for frame in frames.split(','):
            time = parse_time(frame)
            times.append(time)
        return name, times
    except Exception:
        raise ValueError('The value of `line` must have the format name=ddHH:mm-HH:mm,ddHH:mm-HH:mm...')


def parse_time(time: str) -> tuple:
    """Analize a string with format ddHH:mm-HH:mm and return arriving and leaving times."""
    try:
        time_a, time_b = time[2:].split('-')
        base_format = date_formats[time[:2]]
        time_arrive = datetime.strptime(base_format.format(time_a), '%Y-%m-%d %H:%M')
        time_leave = datetime.strptime(base_format.format(time_b), '%Y-%m-%d %H:%M') - timedelta(seconds=1)
        return time_arrive, time_leave

    except Exception:
        raise ValueError('The value of `time` must have the format ddHH:mm-HH:mm.')


def solve(timeline: list) -> list:
    """Get a timeline and return the solution."""
    people_in = []
    result = {}
    for _, is_outgoing, name in timeline:
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
