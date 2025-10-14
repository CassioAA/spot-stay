import pytest
import data_range
from datetime import date

def test_should_raise_error_if_end_and_start_dates_are_equal() -> None:
    start_date = date(2020, 1, 5)
    end_date = date(2020, 1, 5)

    with pytest.raises(ValueError,
                       match="Start date and end date cannot be the same"):
        data_range.DataRange(start_date, end_date)

def test_should_raise_error_if_end_date_is_before_start_date() -> None:
    start_date = date(2020, 1, 5)
    end_date = date(2020, 1, 1)

    with pytest.raises(ValueError,
                       match="Start date must be before end date"):
        data_range.DataRange(start_date, end_date)

def test_should_return_end_and_start_dates_passed_to_constructor() -> None:
    start_date = date(2020, 1, 20)
    end_date = date(2020, 1, 25)
    stay_range = data_range.DataRange(start_date, end_date)

    assert stay_range.get_start_date() == start_date
    assert stay_range.get_end_date() == end_date

def test_should_calculate_total_days_correctly() -> None:
    start_date = date(2020, 1, 10)
    end_date = date(2020, 1, 15)
    stay_range = data_range.DataRange(start_date, end_date)

    assert stay_range.get_total_days() == (end_date - start_date).days

    start_date = date(2020, 1, 1)
    end_date = date(2020, 1, 15)
    stay_range = data_range.DataRange(start_date, end_date)

    assert stay_range.get_total_days() == (end_date - start_date).days

def test_should_report_overlap() -> None:
    # beginning overlying
    start_date_1 = date(2026, 4, 10)
    end_date_1 = date(2026, 4, 20)
    stay_range_1 = data_range.DataRange(start_date_1, end_date_1)
    start_date_2 = date(2026, 4, 15)
    end_date_2 = date(2026, 4, 25)
    stay_range_2 = data_range.DataRange(start_date_2, end_date_2)

    assert stay_range_1.overlaps(stay_range_2) is True

    # ending overlying
    start_date_1 = date(2026, 4, 10)
    end_date_1 = date(2026, 4, 20)
    stay_range_1 = data_range.DataRange(start_date_1, end_date_1)
    start_date_2 = date(2026, 4, 5)
    end_date_2 = date(2026, 4, 15)
    stay_range_2 = data_range.DataRange(start_date_2, end_date_2)

    assert stay_range_1.overlaps(stay_range_2) is True

    # beginning and ending overlying
    start_date_1 = date(2026, 4, 10)
    end_date_1 = date(2026, 4, 20)
    stay_range_1 = data_range.DataRange(start_date_1, end_date_1)
    start_date_2 = date(2026, 4, 11)
    end_date_2 = date(2026, 4, 19)
    stay_range_2 = data_range.DataRange(start_date_2, end_date_2)

    assert stay_range_1.overlaps(stay_range_2) is True