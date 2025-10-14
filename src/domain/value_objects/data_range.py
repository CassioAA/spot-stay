from datetime import date

class DataRange:
    def __init__(self, start_date: date, end_date: date) -> None:
        self.__validate_date_range(start_date, end_date)
        self.start_date = start_date
        self.end_date = end_date

    @staticmethod
    def __validate_date_range(start_date: date, end_date: date) -> None:
        if start_date == end_date:
            raise ValueError("Start date and end date cannot be the same")
        if start_date > end_date:
            raise ValueError("Start date must be before end date")

    def get_start_date(self) -> date:
        return self.start_date

    def get_end_date(self) -> date:
        return self.end_date

    def get_total_days(self) -> int:
        diff_time = self.end_date - self.start_date
        return diff_time.days

    def overlaps(self, other: "DataRange") -> bool:
        return (
            self.start_date < other.end_date and
            other.get_start_date() < self.end_date
        )