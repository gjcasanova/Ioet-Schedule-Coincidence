"""Solution tests."""

# Standard library
from datetime import datetime

# Third party
import pytest

# Local application
from . import schedule, settings


def test_read_file():
    """Check the format of data returned is correct when a file is read."""
    data = schedule.read_file(settings.DATA_PATH)
    assert type(data).__name__ == 'list'
    for row in data:
        assert type(row).__name__ == 'str'


def test_read_file_exception():
    """Check the function `read_file` raises an exception when the function tries to read an invalid path."""
    with pytest.raises(ValueError):
        schedule.read_file('')


def test_get_timeline():
    """Check the events of the timeline are generated property."""
    lines = ['ASTRID=MO10:00-12:00,SU20:00-21:00',
             'ANDRES=TH12:00-14:00']

    expected = [
        (datetime(year=1990, month=1, day=1, hour=10, minute=0), False, 'ASTRID'),
        (datetime(year=1990, month=1, day=1, hour=11, minute=59, second=59), True, 'ASTRID'),
        (datetime(year=1990, month=1, day=4, hour=12, minute=0), False, 'ANDRES'),
        (datetime(year=1990, month=1, day=4, hour=13, minute=59, second=59), True, 'ANDRES'),
        (datetime(year=1990, month=1, day=7, hour=20, minute=0), False, 'ASTRID'),
        (datetime(year=1990, month=1, day=7, hour=20, minute=59, second=59), True, 'ASTRID'),
    ]

    assert schedule.get_timeline(lines) == expected


def test_get_timeline_exception():
    """Check the function `get_timeline` raises an exception when the function tries to parse invalid lines."""
    with pytest.raises(ValueError):
        schedule.get_timeline(['', ''])


def test_parse_line():
    """Check the data returned by the function `parse_line` was parsed properly for each line."""
    assert schedule.parse_line('RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00') == \
        ('RENE', [(datetime(year=1990, month=1, day=1, hour=10, minute=0),
                   datetime(year=1990, month=1, day=1, hour=11, minute=59, second=59)),
                  (datetime(year=1990, month=1, day=2, hour=10, minute=0),
                   datetime(year=1990, month=1, day=2, hour=11, minute=59, second=59)),
                  (datetime(year=1990, month=1, day=4, hour=1, minute=0),
                   datetime(year=1990, month=1, day=4, hour=2, minute=59, second=59)),
                  (datetime(year=1990, month=1, day=6, hour=14, minute=0),
                   datetime(year=1990, month=1, day=6, hour=17, minute=59, second=59)),
                  (datetime(year=1990, month=1, day=7, hour=20, minute=0),
                  datetime(year=1990, month=1, day=7, hour=20, minute=59, second=59))])

    assert schedule.parse_line('ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00') == \
        ('ASTRID', [(datetime(year=1990, month=1, day=1, hour=10, minute=0),
                     datetime(year=1990, month=1, day=1, hour=11, minute=59, second=59)),
                    (datetime(year=1990, month=1, day=4, hour=12, minute=0),
                    datetime(year=1990, month=1, day=4, hour=13, minute=59, second=59)),
                    (datetime(year=1990, month=1, day=7, hour=20, minute=0),
                    datetime(year=1990, month=1, day=7, hour=20, minute=59, second=59))])


def test_parse_line_exception():
    """Check the function `parse_line` raises an exception when the line has not the correct format."""
    with pytest.raises(ValueError):
        schedule.parse_line('RENEMO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00')


def test_parse_time():
    """Check the function `parse_time` calculates properly the elapsed minutes since Monday at 00:00."""
    assert schedule.parse_time('MO10:00-12:00') == (datetime(year=1990, month=1, day=1, hour=10, minute=0),
                                                    datetime(year=1990, month=1, day=1, hour=11, minute=59, second=59))
    assert schedule.parse_time('SU20:15-21:00') == (datetime(year=1990, month=1, day=7, hour=20, minute=15),
                                                    datetime(year=1990, month=1, day=7, hour=20, minute=59, second=59))
    assert schedule.parse_time('TH12:00-14:15') == (datetime(year=1990, month=1, day=4, hour=12, minute=0),
                                                    datetime(year=1990, month=1, day=4, hour=14, minute=14, second=59))


def test_parse_time_exception():
    """Check the function `parse_time` raises an exception when the format is not correct."""
    with pytest.raises(ValueError):
        schedule.parse_time('MO10:0012:00')


def test_solve_example_1():
    """Check if `solve` function can solve the first example given by the exercise."""
    lines = ['RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00',
             'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00',
             'ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00']

    timeline = schedule.get_timeline(lines)

    expected = [
        (('ANDRES', 'RENE'), 2),
        (('ASTRID', 'RENE'), 2),
        (('ANDRES', 'ASTRID'), 3)
    ]

    assert schedule.solve(timeline) == expected


def test_solve_example_2():
    """Check if `solve` function can solve the second example given by the exercise."""
    lines = ['RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00',
             'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00']

    timeline = schedule.get_timeline(lines)

    expected = [
        (('ASTRID', 'RENE'), 3)
    ]

    assert schedule.solve(timeline) == expected


def test_format_solution():
    """Check the `format_solution` function comply with the output presentation rules."""
    solution = [
        (('ASTRID', 'RENE'), 2),
        (('ANDRES', 'ASTRID'), 3),
        (('ANDRES', 'RENE'), 2)
    ]

    expected = ('ASTRID-RENE: 2\n'
                'ANDRES-ASTRID: 3\n'
                'ANDRES-RENE: 2')

    assert schedule.format_solution(solution) == expected
