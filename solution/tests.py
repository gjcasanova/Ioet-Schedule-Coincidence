"""Solution tests."""

# Third party
import pytest

# Local application
from . import schedule, settings


def test_read_file():
    """Check the format of data returned is correct when a file is read."""
    data = schedule.read_file(settings.DATA_PATH)
    before = -1
    for row in data:
        # Check the structure.
        assert type(data).__name__ == 'list'
        minute, is_ingoing, name = row
        assert type(minute).__name__ == 'int'
        assert type(is_ingoing).__name__ == 'bool'
        assert type(name).__name__ == 'str'
        # Check the order.
        assert minute >= before
        before = minute


def test_read_file_exception():
    """Check the function `read_file` raises an exception when the function tries to read an invalid path."""
    with pytest.raises(ValueError):
        schedule.read_file('')


def test_parse_line():
    """Check the data returned by the function `parse_line` was parsed properly for each line."""
    assert schedule.parse_line('RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00') == \
        ('RENE', [(600, 720), (2040, 2160), (4380, 4500), (8040, 8280), (9840, 9900)])
    assert schedule.parse_line('ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00') == \
        ('ASTRID', [(600, 720), (5040, 5160), (9840, 9900)])


def test_parse_line_exception():
    """Check the function `parse_line` raises an exception when the line has not the correct format."""
    with pytest.raises(ValueError):
        schedule.parse_line('RENEMO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00')


def test_to_minutes():
    """Check the function `to_minutes` calculates properly the elapsed minutes since Monday at 00:00."""
    assert schedule.to_minutes('MO10:00-12:00') == (600, 720)
    assert schedule.to_minutes('SU20:15-21:00') == (9855, 9900)
    assert schedule.to_minutes('TH12:00-14:15') == (5040, 5175)


def test_to_minutes_exception():
    """Check the function `to_minutes` raises an exception when the format is not correct."""
    with pytest.raises(ValueError):
        schedule.to_minutes('MO10:0012:00')


def test_solve():
    """Check the result of the solution got by `solve` function is correct."""
    data = [(600, False, 'ANDRES'), (600, False, 'ASTRID'), (600, False, 'RENE'), (720, True, 'ANDRES'),
            (720, True, 'ASTRID'), (720, True, 'RENE'), (2040, False, 'RENE'), (2160, True, 'RENE'),
            (4380, False, 'RENE'), (4500, True, 'RENE'), (5040, False, 'ANDRES'), (5040, False, 'ASTRID'),
            (5160, True, 'ANDRES'), (5160, True, 'ASTRID'), (8040, False, 'RENE'), (8280, True, 'RENE'),
            (9840, False, 'ANDRES'), (9840, False, 'ASTRID'), (9840, False, 'RENE'), (9900, True, 'ANDRES'),
            (9900, True, 'ASTRID'), (9900, True, 'RENE')]

    expected = [
        (('ANDRES', 'RENE'), 2),
        (('ASTRID', 'RENE'), 2),
        (('ANDRES', 'ASTRID'), 3)
    ]

    assert schedule.solve(data) == expected


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
