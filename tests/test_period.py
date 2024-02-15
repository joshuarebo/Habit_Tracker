import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from datetime import datetime, timedelta
from period import Period  # Import the Period class from period.py


# Test period creation
def test_period_creation():
    start_date = datetime(2024, 1, 1)
    periodicity = "daily"
    period = Period(start_date, periodicity)
    assert period.start_date == start_date
    assert period.periodicity == periodicity


# Test checking if a date is within the period
def test_is_within_period():
    start_date = datetime(2024, 1, 1)
    periodicity = "daily"
    period = Period(start_date, periodicity)

    # Test with dates within the period
    assert period.is_within_period(start_date) is True
    assert period.is_within_period(start_date + timedelta(days=1)) is True

    # Test with dates outside the period
    assert period.is_within_period(start_date - timedelta(days=1)) is False
    assert period.is_within_period(start_date + timedelta(days=2)) is False


# Test checking if a date is within the period for weekly periodicity
def test_is_within_period_weekly():
    start_date = datetime(2024, 1, 1)
    periodicity = "weekly"
    period = Period(start_date, periodicity)

    # Test with dates within the period
    assert period.is_within_period(start_date) is True
    assert period.is_within_period(start_date + timedelta(weeks=1)) is True

    # Test with dates outside the period
    assert period.is_within_period(start_date - timedelta(days=1)) is False
    assert period.is_within_period(start_date + timedelta(weeks=2)) is False




# Run pytest
if __name__ == "__main__":
    pytest.main()
