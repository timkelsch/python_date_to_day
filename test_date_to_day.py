import pytest
import date_to_day
from datetime import datetime
from datetime import date
import logging

logger = date_to_day.setup_logging()
logger.disabled = True

MAX_ATTEMPTS = 3

def test_gather_input_valid_date(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '04/12/2004')
    result = date_to_day.gather_input(MAX_ATTEMPTS)
    assert isinstance(result, datetime)
    assert result == datetime(2004, 4, 12)

def test_gather_input_invalid_date_then_valid(monkeypatch):
    inputs = iter(['73/92/3023', '04/12/2004'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = date_to_day.gather_input(MAX_ATTEMPTS)
    assert isinstance(result, datetime)
    assert result == datetime(2004, 4, 12)

def test_gather_input_invalid_format_then_valid(monkeypatch):
    inputs = iter(['2004-04-12', '04/12/2004'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = date_to_day.gather_input(MAX_ATTEMPTS)
    assert isinstance(result, datetime)
    assert result == datetime(2004, 4, 12)

def test_gather_input_two_invalid_then_valid(monkeypatch):
    inputs = iter(['itsadate', '03/26/202', '04/12/2004'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = date_to_day.gather_input(MAX_ATTEMPTS)
    assert isinstance(result, datetime)
    assert result == datetime(2004, 4, 12)

def test_gather_input_three_invalid(monkeypatch):
    inputs = iter(['itsadate', 'badinput', 'justterrible'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(ValueError, match="Max attempts reached"):
        date_to_day.gather_input(MAX_ATTEMPTS)

def test_gather_input_valid_leap_year(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '02/29/2024')
    result = date_to_day.gather_input(MAX_ATTEMPTS)
    assert isinstance(result, datetime)
    assert result == datetime(2024, 2, 29)

def test_gather_input_invalid_leap_year(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '02/29/2023')
    with pytest.raises(ValueError):
        date_to_day.gather_input(MAX_ATTEMPTS)

def test_calculate_day_of_week_valid_date_input():
    date = datetime(2004, 4, 12)
    result = date_to_day.calculate_day_of_week(date)
    assert type(result) == pytest.approx(str)

# def test_calculate_day_of_week_invalid_date_input():
#     date = '01/01/2021'
#     with pytest.raises(AttributeError):
#         _ = date_to_day.calculate_day_of_week(date)

def test_calculate_day_of_week_invalid_string_input():
    date = '01/01/2021'
    with pytest.raises(AttributeError):
        _ = date_to_day.calculate_day_of_week(date)